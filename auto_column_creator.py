"""
Utilitaire pour synchroniser automatiquement les colonnes de base de données
Crée les colonnes manquantes détectées lors des erreurs "Unknown column"
"""

from sqlalchemy import text, inspect
from flask import current_app
import logging

def auto_create_missing_columns(db, error_message, table_name, model_class):
    """
    Détecte et crée automatiquement les colonnes manquantes
    
    Args:
        db: Instance SQLAlchemy
        error_message: Message d'erreur MySQL
        table_name: Nom de la table
        model_class: Classe du modèle SQLAlchemy
    """
    try:
        # Extraire le nom de la colonne manquante du message d'erreur
        missing_column = extract_missing_column_name(error_message)
        if not missing_column:
            return False
            
        current_app.logger.info(f"Détection colonne manquante: {missing_column} dans {table_name}")
        
        # Vérifier si la colonne existe vraiment
        if column_exists(db, table_name, missing_column):
            current_app.logger.info(f"La colonne {missing_column} existe déjà dans {table_name}")
            return True
            
        # Obtenir le type de colonne depuis le modèle
        column_definition = get_column_definition_from_model(model_class, missing_column)
        if not column_definition:
            current_app.logger.warning(f"Impossible de déterminer le type pour {missing_column}")
            return False
            
        # Créer la colonne
        success = create_column(db, table_name, missing_column, column_definition)
        if success:
            current_app.logger.info(f"✅ Colonne {missing_column} créée dans {table_name}")
            return True
        else:
            current_app.logger.error(f"❌ Échec création colonne {missing_column} dans {table_name}")
            return False
            
    except Exception as e:
        current_app.logger.error(f"Erreur auto_create_missing_columns: {e}")
        return False

def extract_missing_column_name(error_message):
    """Extrait le nom de la colonne manquante du message d'erreur MySQL"""
    try:
        # Formats possibles:
        # "Unknown column 'NOSOUM' in 'field list'"
        # "(1054, \"Unknown column 'NOSOUM' in 'field list'\")"
        
        if "Unknown column" in error_message:
            # Chercher le pattern 'nom_colonne'
            import re
            match = re.search(r"Unknown column '([^']+)'", error_message)
            if match:
                return match.group(1)
                
        return None
    except Exception:
        return None

def column_exists(db, table_name, column_name):
    """Vérifie si une colonne existe dans une table"""
    try:
        inspector = inspect(db.engine)
        columns = inspector.get_columns(table_name)
        column_names = [col['name'] for col in columns]
        return column_name in column_names
    except Exception:
        return False

def get_column_definition_from_model(model_class, column_name):
    """Obtient la définition d'une colonne depuis le modèle SQLAlchemy"""
    try:
        if not hasattr(model_class, '__table__'):
            return None
            
        # Chercher dans les colonnes du modèle
        for column in model_class.__table__.columns:
            if column.name == column_name:
                return column
                
        # Chercher dans les classes parentes (héritage)
        for base in model_class.__mro__:
            if hasattr(base, '__table__') and base.__table__ is not None:
                for column in base.__table__.columns:
                    if column.name == column_name:
                        return column
                        
        return None
    except Exception:
        return None

def create_column(db, table_name, column_name, column_definition):
    """Crée une colonne dans la table"""
    try:
        # Construire la définition SQL
        sql_type = get_mysql_type_from_sqlalchemy(column_definition)
        if not sql_type:
            return False
            
        # Construire la requête ALTER TABLE
        sql = f"ALTER TABLE `{table_name}` ADD COLUMN `{column_name}` {sql_type}"
        
        # Ajouter les contraintes
        if not column_definition.nullable:
            sql += " NOT NULL"
        
        if column_definition.default is not None:
            default_value = column_definition.default.arg
            if isinstance(default_value, str):
                sql += f" DEFAULT '{default_value}'"
            else:
                sql += f" DEFAULT {default_value}"
        
        current_app.logger.info(f"Exécution SQL: {sql}")
        
        # Exécuter la requête
        db.session.execute(text(sql))
        db.session.commit()
        
        return True
        
    except Exception as e:
        current_app.logger.error(f"Erreur création colonne: {e}")
        db.session.rollback()
        return False

def get_mysql_type_from_sqlalchemy(column_definition):
    """Convertit un type SQLAlchemy vers un type MySQL"""
    try:
        sql_type = str(column_definition.type)
        
        # Mapping des types courants
        type_mapping = {
            'INTEGER': 'INT',
            'VARCHAR': lambda: f"VARCHAR({column_definition.type.length or 255})",
            'TEXT': 'TEXT',
            'DECIMAL': lambda: f"DECIMAL({getattr(column_definition.type, 'precision', 10)},{getattr(column_definition.type, 'scale', 2)})",
            'DATETIME': 'DATETIME',
            'DATE': 'DATE',
            'BOOLEAN': 'TINYINT(1)',
            'FLOAT': 'FLOAT',
            'DOUBLE': 'DOUBLE'
        }
        
        # Extraire le type de base
        base_type = sql_type.split('(')[0].upper()
        
        if base_type in type_mapping:
            mapper = type_mapping[base_type]
            if callable(mapper):
                return mapper()
            else:
                return mapper
        elif 'VARCHAR' in sql_type:
            return sql_type.replace('VARCHAR', 'VARCHAR')
        else:
            # Par défaut, utiliser VARCHAR(255)
            return 'VARCHAR(255)'
            
    except Exception:
        return 'VARCHAR(255)'

def safe_query_with_auto_column_creation(db, model_class, query_func, *args, **kwargs):
    """
    Exécute une requête avec création automatique des colonnes manquantes
    
    Args:
        db: Instance SQLAlchemy
        model_class: Classe du modèle
        query_func: Fonction qui exécute la requête
        *args, **kwargs: Arguments pour query_func
    """
    max_retries = 3
    retry_count = 0
    
    while retry_count < max_retries:
        try:
            # Tenter d'exécuter la requête
            return query_func(*args, **kwargs)
            
        except Exception as e:
            error_message = str(e)
            
            # Vérifier si c'est une erreur de colonne manquante
            if "Unknown column" in error_message and retry_count < max_retries - 1:
                current_app.logger.warning(f"Tentative {retry_count + 1}: {error_message}")
                
                # Tenter de créer la colonne manquante
                table_name = model_class.__tablename__
                success = auto_create_missing_columns(db, error_message, table_name, model_class)
                
                if success:
                    retry_count += 1
                    current_app.logger.info(f"Nouvelle tentative après création de colonne...")
                    continue
                else:
                    # Impossible de créer la colonne, abandonner
                    raise e
            else:
                # Autre type d'erreur ou nombre max de tentatives atteint
                raise e
    
    # Si on arrive ici, on a épuisé les tentatives
    raise Exception(f"Impossible d'exécuter la requête après {max_retries} tentatives")

def initialize_missing_columns_for_model(db, model_class):
    """
    Vérifie et crée toutes les colonnes manquantes pour un modèle donné
    """
    try:
        table_name = model_class.__tablename__
        current_app.logger.info(f"Vérification colonnes pour {table_name}")
        
        # Obtenir les colonnes existantes
        inspector = inspect(db.engine)
        existing_columns = [col['name'] for col in inspector.get_columns(table_name)]
        
        # Obtenir les colonnes définies dans le modèle
        model_columns = []
        for column in model_class.__table__.columns:
            model_columns.append(column.name)
        
        # Trouver les colonnes manquantes
        missing_columns = set(model_columns) - set(existing_columns)
        
        if missing_columns:
            current_app.logger.info(f"Colonnes manquantes dans {table_name}: {missing_columns}")
            
            for column_name in missing_columns:
                column_definition = get_column_definition_from_model(model_class, column_name)
                if column_definition:
                    success = create_column(db, table_name, column_name, column_definition)
                    if success:
                        current_app.logger.info(f"✅ Créé colonne {column_name} dans {table_name}")
                    else:
                        current_app.logger.error(f"❌ Échec création {column_name} dans {table_name}")
        else:
            current_app.logger.info(f"✅ Toutes les colonnes existent pour {table_name}")
            
    except Exception as e:
        current_app.logger.error(f"Erreur initialize_missing_columns_for_model: {e}")
