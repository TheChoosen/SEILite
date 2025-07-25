"""
Module de gestion des documents commerciaux pour SEILite (Version Simplifiée)
Routes pour les vraies tables MySQL existantes (COTETE, COMMA, LIGNE, QOMMA)
"""

from flask import Blueprint, render_template, request, jsonify, redirect, url_for, flash, current_app
from datetime import datetime, date, timedelta
from sqlalchemy import func, desc, asc, or_, text
import json

# Import des modèles simplifiés
from documents_models_simple import init_simple_documents_models

# Variables globales pour les modèles (initialisées dans register_documents_routes)
MODELS = {}

# Création du blueprint pour le module documents
documents_bp = Blueprint('documents', __name__, url_prefix='/documents')

# Configuration simplifiée pour les données existantes
MODULES_CONFIG = {
    'PI': {
        'label': 'Commandes/Factures',
        'icon': 'fas fa-file-invoice-dollar',
        'types': {
            'COM': {'label': 'Commandes', 'icon': 'fas fa-shopping-cart'},
            'FAC': {'label': 'Factures', 'icon': 'fas fa-file-invoice'}
        }
    }
}

STATUTS_CONFIG = {
    'O': {'label': 'Ouvert', 'color': 'warning'},
    'F': {'label': 'Fermé', 'color': 'success'},
    'A': {'label': 'Annulé', 'color': 'danger'},
    'P': {'label': 'En cours', 'color': 'info'},
    'L': {'label': 'Livré', 'color': 'primary'}
}

# Utilitaires pour la conversion de données
def safe_float(value, default=0.0):
    """Convertit une valeur en float de manière sécurisée"""
    if not value:
        return default
    try:
        return float(str(value).replace(',', '.'))
    except:
        return default

def parse_mysql_date(date_str):
    """Parse une date MySQL au format varchar vers datetime"""
    if not date_str:
        return datetime.now()
    
    try:
        # Formats possibles : YYYY-MM-DD, DD/MM/YYYY, YYYY/MM/DD
        if '-' in date_str:
            return datetime.strptime(date_str, '%Y-%m-%d')
        elif '/' in date_str:
            # Essayer DD/MM/YYYY puis YYYY/MM/DD
            try:
                return datetime.strptime(date_str, '%d/%m/%Y')
            except:
                return datetime.strptime(date_str, '%Y/%m/%d')
        else:
            return datetime.now()
    except:
        return datetime.now()

def format_commande_for_ui(commande, lignes):
    """Convertit une commande MySQL vers le format UI"""
    return {
        'id': commande.id,
        'numero': commande.NOCOM or f'COM-{commande.id}',
        'module': 'PI',
        'type_document': 'COM',
        'client_nom': commande.NOM or '',
        'client_code': commande.NOCLI or '',
        'client_email': '',
        'date_creation': parse_mysql_date(commande.DATEC),
        'date_document': parse_mysql_date(commande.DATEC).date() if commande.DATEC else date.today(),
        'date_echeance': parse_mysql_date(commande.DATEL).date() if commande.DATEL else None,
        'statut': commande.STAT or 'O',
        'total_ht': safe_float(commande.TOTAL),
        'total_ttc': safe_float(commande.TOTAL) + safe_float(commande.TAXE) + safe_float(commande.TAXEF),
        'description': commande.REMD or '',
        'vendeur': commande.VENDEUR or '',
        'depot': commande.DEPOT or '',
        'lignes': [format_ligne_commande_for_ui(ligne, i+1) for i, ligne in enumerate(lignes)]
    }

def format_ligne_commande_for_ui(ligne, numero):
    """Convertit une ligne de commande MySQL vers le format UI"""
    return {
        'id': ligne.id,
        'numero_ligne': numero,
        'code_produit': ligne.CODE or '',
        'designation': ligne.DESC or '',
        'quantite': safe_float(ligne.QUANT),
        'unite': ligne.UNIT or 'pcs',
        'prix_unitaire': safe_float(ligne.TAUX),
        'remise_pourcentage': safe_float(ligne.ESC),
        'total_ligne': safe_float(ligne.MONTANT)
    }

def format_facture_for_ui(facture_data, lignes):
    """Convertit des données de facture vers le format UI"""
    # Les factures sont stockées dans la table LIGNE avec NOFACT
    # Grouper par NOFACT pour reconstituer la facture
    if not lignes:
        return None
        
    # Utiliser la première ligne pour les infos de base
    first_ligne = lignes[0]
    
    # Calculer les totaux
    total_ht = sum(safe_float(ligne.MONTANT) for ligne in lignes)
    total_taxes = sum(safe_float(ligne.TAXEPR) + safe_float(ligne.TAXEFE) for ligne in lignes)
    
    return {
        'id': f"FAC-{first_ligne.NOFACT}",
        'numero': first_ligne.NOFACT or f'FAC-{first_ligne.id}',
        'module': 'PI',
        'type_document': 'FAC',
        'client_nom': '',  # Pas directement disponible dans LIGNE
        'client_code': first_ligne.NOCLI or '',
        'client_email': '',
        'date_creation': parse_mysql_date(first_ligne.DATEC),
        'date_document': parse_mysql_date(first_ligne.DATEC).date() if first_ligne.DATEC else date.today(),
        'date_echeance': parse_mysql_date(first_ligne.DATEL).date() if first_ligne.DATEL else None,
        'statut': 'F',  # Assumé facturé
        'total_ht': total_ht,
        'total_ttc': total_ht + total_taxes,
        'description': f'Facture {first_ligne.NOFACT}',
        'vendeur': first_ligne.VENDEUR or '',
        'depot': '',
        'lignes': [format_ligne_facture_for_ui(ligne, i+1) for i, ligne in enumerate(lignes)]
    }

def format_ligne_facture_for_ui(ligne, numero):
    """Convertit une ligne de facture MySQL vers le format UI"""
    return {
        'id': ligne.id,
        'numero_ligne': numero,
        'code_produit': ligne.CODE or '',
        'designation': ligne.DESC or '',
        'quantite': safe_float(ligne.QUANT),
        'unite': ligne.UNIT or 'pcs',
        'prix_unitaire': safe_float(ligne.TAUX),
        'remise_pourcentage': safe_float(ligne.ESC),
        'total_ligne': safe_float(ligne.MONTANT)
    }

# ================================
# ROUTES PRINCIPALES
# ================================

@documents_bp.route('/')
def liste():
    """Page principale - Liste des documents"""
    return render_template('documents/liste.html',
                         modules_config=MODULES_CONFIG,
                         statuts_config=STATUTS_CONFIG)

@documents_bp.route('/detail/<document_id>')
def detail(document_id):
    """Page de détail d'un document"""
    try:
        from app import db
        document = None
        
        # Essayer commande d'abord
        if document_id.startswith('COM-') or document_id.isdigit():
            doc_id = int(document_id.replace('COM-', ''))
            commande = db.session.query(MODELS['Cotete']).filter(MODELS['Cotete'].id == doc_id).first()
            if commande:
                lignes = db.session.query(MODELS['Comma']).filter(MODELS['Comma'].NOCOM == commande.NOCOM).all()
                document = format_commande_for_ui(commande, lignes)
        
        # Essayer facture
        elif document_id.startswith('FAC-'):
            nofact = document_id.replace('FAC-', '')
            lignes = db.session.query(MODELS['Ligne']).filter(MODELS['Ligne'].NOFACT == nofact).all()
            if lignes:
                document = format_facture_for_ui(None, lignes)
        
        if not document:
            flash('Document non trouvé', 'error')
            return redirect(url_for('documents.liste'))
        
        return render_template('documents/detail.html',
                             document=document,
                             modules_config=MODULES_CONFIG,
                             statuts_config=STATUTS_CONFIG)
    
    except Exception as e:
        current_app.logger.error(f"Erreur detail document {document_id}: {e}")
        flash('Erreur lors de la récupération du document', 'error')
        return redirect(url_for('documents.liste'))

@documents_bp.route('/formulaire')
@documents_bp.route('/formulaire/<document_id>')
def formulaire(document_id=None):
    """Page de formulaire pour créer/modifier un document"""
    document = None
    
    if document_id:
        # Mode édition - récupérer le document existant
        try:
            from app import db
            
            # Essayer commande d'abord
            if document_id.startswith('COM-') or document_id.isdigit():
                doc_id = int(document_id.replace('COM-', ''))
                commande = db.session.query(MODELS['Cotete']).filter(MODELS['Cotete'].id == doc_id).first()
                if commande:
                    lignes = db.session.query(MODELS['Comma']).filter(MODELS['Comma'].NOCOM == commande.NOCOM).all()
                    document = format_commande_for_ui(commande, lignes)
            
            # Essayer facture
            elif document_id.startswith('FAC-'):
                nofact = document_id.replace('FAC-', '')
                lignes = db.session.query(MODELS['Ligne']).filter(MODELS['Ligne'].NOFACT == nofact).all()
                if lignes:
                    document = format_facture_for_ui(None, lignes)
                    
            if not document:
                flash('Document non trouvé', 'error')
                return redirect(url_for('documents.liste'))
                
        except Exception as e:
            current_app.logger.error(f"Erreur récupération document {document_id}: {e}")
            flash('Erreur lors de la récupération du document', 'error')
            return redirect(url_for('documents.liste'))
    
    return render_template('documents/formulaire.html',
                         document=document,
                         modules_config=MODULES_CONFIG,
                         statuts_config=STATUTS_CONFIG)

# ================================
# API ENDPOINTS
# ================================

@documents_bp.route('/api/documents')
def api_documents():
    """API pour récupérer la liste des documents avec filtres"""
    try:
        from app import db
        
        # Paramètres de la requête
        type_filter = request.args.get('type', 'COM')  # Default to commandes
        status_filter = request.args.get('status')
        search_query = request.args.get('search', '').strip()
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 20))
        
        documents = []
        
        if type_filter == 'COM' or not type_filter:
            # Récupérer les commandes
            query = db.session.query(MODELS['Cotete'])
            
            # Filtres
            if status_filter:
                query = query.filter(MODELS['Cotete'].STAT == status_filter)
            
            if search_query:
                search_filter = or_(
                    MODELS['Cotete'].NOM.ilike(f'%{search_query}%'),
                    MODELS['Cotete'].NOCOM.ilike(f'%{search_query}%'),
                    MODELS['Cotete'].NOCLI.ilike(f'%{search_query}%')
                )
                query = query.filter(search_filter)
            
            # Pagination et tri
            query = query.order_by(desc(MODELS['Cotete'].DATEC))
            commandes = query.limit(per_page).offset((page-1)*per_page).all()
            
            for commande in commandes:
                lignes = db.session.query(MODELS['Comma']).filter(MODELS['Comma'].NOCOM == commande.NOCOM).all()
                document = format_commande_for_ui(commande, lignes)
                documents.append(document)
        
        if type_filter == 'FAC' or not type_filter:
            # Récupérer les factures (groupées par NOFACT)
            query = db.session.query(MODELS['Ligne'].NOFACT).distinct()
            
            if search_query:
                query = query.filter(
                    or_(
                        MODELS['Ligne'].NOFACT.ilike(f'%{search_query}%'),
                        MODELS['Ligne'].NOCLI.ilike(f'%{search_query}%')
                    )
                )
            
            # Pagination
            nofacts = query.limit(per_page).offset((page-1)*per_page).all()
            
            for (nofact,) in nofacts:
                if nofact:
                    lignes = db.session.query(MODELS['Ligne']).filter(MODELS['Ligne'].NOFACT == nofact).all()
                    document = format_facture_for_ui(None, lignes)
                    if document:
                        documents.append(document)
        
        # Calculer les statistiques
        stats = {'O': 0, 'F': 0, 'A': 0, 'P': 0, 'L': 0}
        for doc in documents:
            statut = doc.get('statut', 'O')
            if statut in stats:
                stats[statut] += 1
        
        # Conversion des dates pour JSON
        for doc in documents:
            if isinstance(doc.get('date_creation'), datetime):
                doc['date_creation'] = doc['date_creation'].isoformat()
            if isinstance(doc.get('date_document'), date):
                doc['date_document'] = doc['date_document'].isoformat()
            if doc.get('date_echeance') and isinstance(doc['date_echeance'], date):
                doc['date_echeance'] = doc['date_echeance'].isoformat()
        
        return jsonify({
            'success': True,
            'documents': documents,
            'stats': stats,
            'pagination': {
                'page': page,
                'per_page': per_page,
                'total': len(documents),
                'has_next': len(documents) == per_page,
                'has_prev': page > 1
            }
        })
    
    except Exception as e:
        current_app.logger.error(f"Erreur API documents: {e}")
        return jsonify({'success': False, 'message': str(e)}), 500

@documents_bp.route('/api/clients/search')
def api_search_clients():
    """API pour rechercher des clients"""
    try:
        from app import db
        
        query = request.args.get('q', '').strip()
        if len(query) < 2:
            return jsonify({'clients': []})
        
        # Rechercher dans les commandes
        clients = db.session.query(
            MODELS['Cotete'].NOCLI,
            MODELS['Cotete'].NOM,
            MODELS['Cotete'].ADR1,
            MODELS['Cotete'].VILLE,
            MODELS['Cotete'].TELCON
        ).filter(
            or_(
                MODELS['Cotete'].NOM.ilike(f'%{query}%'),
                MODELS['Cotete'].NOCLI.ilike(f'%{query}%')
            )
        ).distinct().limit(10).all()
        
        results = []
        for client in clients:
            if client.NOCLI and client.NOM:
                results.append({
                    'code': client.NOCLI,
                    'nom': client.NOM,
                    'adresse': client.ADR1 or '',
                    'ville': client.VILLE or '',
                    'telephone': client.TELCON or ''
                })
        
        return jsonify({'clients': results})
    
    except Exception as e:
        current_app.logger.error(f"Erreur recherche clients: {e}")
        return jsonify({'clients': []})

@documents_bp.route('/api/produits/search')
def api_search_produits():
    """API pour rechercher des produits"""
    try:
        from app import db
        
        query = request.args.get('q', '').strip()
        if len(query) < 2:
            return jsonify({'produits': []})
        
        # Rechercher dans les lignes de commandes
        produits = db.session.query(
            MODELS['Comma'].CODE,
            MODELS['Comma'].DESC,
            MODELS['Comma'].UNIT,
            MODELS['Comma'].TAUX
        ).filter(
            or_(
                MODELS['Comma'].CODE.ilike(f'%{query}%'),
                MODELS['Comma'].DESC.ilike(f'%{query}%')
            )
        ).distinct().limit(10).all()
        
        results = []
        for produit in produits:
            if produit.CODE and produit.DESC:
                results.append({
                    'code': produit.CODE,
                    'designation': produit.DESC,
                    'unite': produit.UNIT or 'pcs',
                    'prix': safe_float(produit.TAUX)
                })
        
        return jsonify({'produits': results})
    
    except Exception as e:
        current_app.logger.error(f"Erreur recherche produits: {e}")
        return jsonify({'produits': []})

@documents_bp.route('/api/documents/<document_id>')
def api_document_detail(document_id):
    """API pour récupérer le détail d'un document"""
    try:
        from app import db
        document = None
        
        # Essayer commande d'abord
        if document_id.startswith('COM-') or document_id.isdigit():
            doc_id = int(document_id.replace('COM-', ''))
            commande = db.session.query(MODELS['Cotete']).filter(MODELS['Cotete'].id == doc_id).first()
            if commande:
                lignes = db.session.query(MODELS['Comma']).filter(MODELS['Comma'].NOCOM == commande.NOCOM).all()
                document = format_commande_for_ui(commande, lignes)
        
        # Essayer facture
        elif document_id.startswith('FAC-'):
            nofact = document_id.replace('FAC-', '')
            lignes = db.session.query(MODELS['Ligne']).filter(MODELS['Ligne'].NOFACT == nofact).all()
            if lignes:
                document = format_facture_for_ui(None, lignes)
        
        if not document:
            return jsonify({'success': False, 'message': 'Document non trouvé'}), 404
        
        # Conversion des dates pour JSON
        if isinstance(document.get('date_creation'), datetime):
            document['date_creation'] = document['date_creation'].isoformat()
        if isinstance(document.get('date_document'), date):
            document['date_document'] = document['date_document'].isoformat()
        if document.get('date_echeance') and isinstance(document['date_echeance'], date):
            document['date_echeance'] = document['date_echeance'].isoformat()
        
        return jsonify({'success': True, 'document': document})
    
    except Exception as e:
        current_app.logger.error(f"Erreur API detail document {document_id}: {e}")
        return jsonify({'success': False, 'message': str(e)}), 500

# Fonctions pour les actions document (simplifiées)
@documents_bp.route('/dupliquer/<document_id>', methods=['POST'])
def dupliquer(document_id):
    """Duplication d'un document"""
    try:
        flash('Fonctionnalité de duplication en cours de développement', 'info')
        return jsonify({'success': True, 'message': 'Document dupliqué'})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

@documents_bp.route('/convertir/<document_id>', methods=['POST'])
def convertir(document_id):
    """Conversion d'un document"""
    try:
        flash('Fonctionnalité de conversion en cours de développement', 'info')
        return jsonify({'success': True, 'message': 'Document converti'})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

@documents_bp.route('/imprimer/<document_id>')
def imprimer(document_id):
    """Impression d'un document"""
    try:
        flash('Fonctionnalité d\'impression en cours de développement', 'info')
        return redirect(url_for('documents.detail', document_id=document_id))
    except Exception as e:
        flash('Erreur lors de l\'impression', 'error')
        return redirect(url_for('documents.liste'))

# ================================
# INITIALISATION DU MODULE
# ================================

def register_documents_routes(app):
    """Enregistre le module documents dans l'application Flask"""
    global MODELS
    
    # Initialiser les modèles simplifiés avec la base de données
    from app import db
    MODELS = init_simple_documents_models(db)
    
    # Enregistrer le blueprint
    app.register_blueprint(documents_bp)
    
    return True
