# Gestion des Produits - Application Flask

Une application web Flask pour la gestion des produits, convertie depuis un formulaire Windows Forms VB.NET.

## Fonctionnalités

### Gestion des Produits
- **Création/Modification/Suppression** de produits
- **Recherche avancée** par numéro, description ou code-barres
- **Gestion des images** de produits
- **Pagination** pour les listes importantes
- **Validation complète** des données

### Informations Produit
- Informations générales (numéro, groupe, format, substitut)
- Descriptions multilingues (français/anglais)
- Mots-clés et catégorisation
- Code-barres et identification

### Gestion Avancée
- **Taxes** (TVP, TVF avec taux personnalisé)
- **Postes comptables** (vente/achat CAN/US)
- **Gestion des stocks** (point de commande, min/max)
- **Coûts et prix** (référence, TVF, prix de revient)
- **Noyau/Redevance** avec calculs automatiques

### Interface Utilisateur
- Design moderne et responsive avec Bootstrap 5
- Navigation intuitive avec barre d'outils
- Formulaires avec validation en temps réel
- Prévisualisation des images
- Raccourcis clavier (Ctrl+S, Ctrl+N, Échap)

## Installation

1. **Cloner ou créer le projet** dans le répertoire `f:\SEILite`

2. **Installer Python 3.8+** si ce n'est pas déjà fait

3. **Créer un environnement virtuel** (recommandé) :
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   ```

4. **Installer les dépendances** :
   ```bash
   pip install -r requirements.txt
   ```

5. **Créer les répertoires nécessaires** :
   ```bash
   mkdir static\uploads
   ```

## Configuration

L'application utilise SQLite par défaut. La base de données sera créée automatiquement au premier lancement.

### Variables d'environnement (optionnel)
Créer un fichier `.env` :
```
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///produits.db
UPLOAD_FOLDER=static/uploads
```

## Utilisation

### Démarrer l'application
```bash
python app.py
```

L'application sera accessible à l'adresse : http://localhost:5000

### Fonctionnalités principales

#### Gestion des Produits
1. **Liste des produits** : `/produits`
   - Recherche par numéro, description ou code-barres
   - Pagination automatique
   - Actions rapides (voir, modifier, supprimer)

2. **Nouveau produit** : `/produits/nouveau`
   - Formulaire complet avec tous les champs
   - Validation en temps réel
   - Upload d'image

3. **Modifier un produit** : `/produits/{id}/modifier`
   - Pré-remplissage des données existantes
   - Calculs automatiques (coûts, marge)
   - Historique des modifications

4. **Détail d'un produit** : `/produits/{id}`
   - Vue d'ensemble complète
   - Informations organisées par sections

#### Champs Principaux

**Informations de base** :
- Numéro de produit (obligatoire, unique)
- Groupe et famille
- Format et substitut
- Descriptions français/anglais

**Gestion** :
- Statut (actif/inactif, discontinué)
- Inventorié, escomptable, étiquettes
- Gestion série/lot

**Taxes et comptabilité** :
- TVP (Taxe de Vente Provinciale)
- TVF (Taxe de Vente Fédérale) avec taux personnalisé
- Postes comptables CAN/US

**Coûts et stocks** :
- Coût de référence
- Prix de revient (calculé automatiquement)
- Point de commande, min/max inventaire

**Noyau/Redevance** :
- Produit noyau associé
- Valeurs et escalades
- Marge calculée automatiquement

#### Calculs Automatiques

L'application effectue plusieurs calculs automatiques :

1. **Coût TVF** = Coût référence × (1 + Taux TVF%)
2. **Prix de revient** = Coût TVF
3. **Marge** = Valeur Core + Escalade Core

### Raccourcis Clavier
- **Ctrl+S** : Sauvegarder le formulaire
- **Ctrl+N** : Nouveau produit
- **Échap** : Retour à la liste

### Recherche Avancée
- **Par numéro** : Recherche exacte ou partielle
- **Par description** : Recherche dans les descriptions FR/EN
- **Par code-barres** : Recherche exacte

## Structure du Projet

```
f:\SEILite\
├── app.py                      # Application Flask principale
├── requirements.txt            # Dépendances Python
├── README.md                   # Cette documentation
├── static\                     # Fichiers statiques
│   ├── css\
│   │   └── style.css          # Styles CSS personnalisés
│   ├── js\
│   │   └── app.js             # JavaScript de l'application
│   └── uploads\               # Images des produits
├── templates\                  # Templates Jinja2
│   ├── base.html              # Template de base
│   └── produits\
│       ├── liste.html         # Liste des produits
│       ├── formulaire.html    # Formulaire création/modification
│       └── detail.html        # Vue détaillée d'un produit
└── produits.db               # Base de données SQLite (créée auto)
```

## Modèle de Données

### Table Produit
- **Identification** : id (PK), numero_produit (unique), groupe, format, substitut
- **Descriptions** : description_fr, description_en, motclef1, motclef2
- **Catégorisation** : type_produit, categorie, remarques1, remarques2
- **Codes** : barcode
- **Gestion** : inventorie, actif, discontinue, escomptable, etiquettes
- **Série/Lot** : gestion_serie, gestion_lot
- **Taxes** : tvp, tvf, taux_taxe_fed
- **Comptabilité** : poste_vente_can, poste_vente_us, poste_achat_can, poste_achat_us
- **Localisation** : localisation, famille
- **Coûts** : cout_reference, cout_tvf, prix_revient
- **Stocks** : point_commande, minimum_commander, maximum_inventaire
- **Calculs** : mode_calcul, formule, maj_auto
- **Core** : produit_core, groupe_core, g_core, core_valeur, core_escalade, marge
- **Divers** : evaluation, image_path
- **Système** : date_creation, date_modification

## Sécurité

- Validation côté serveur pour tous les champs
- Upload d'images sécurisé avec vérification des extensions
- Protection contre l'injection SQL (SQLAlchemy ORM)
- Gestion des sessions sécurisée

## Personnalisation

### Ajouter des Champs
1. Modifier le modèle `Produit` dans `app.py`
2. Ajouter les champs dans les templates
3. Mettre à jour la validation JavaScript

### Modifier l'Apparence
- Éditer `static/css/style.css` pour les styles
- Modifier `templates/base.html` pour la structure générale

### Ajouter des Fonctionnalités
- Créer de nouvelles routes dans `app.py`
- Ajouter les templates correspondants
- Mettre à jour le JavaScript si nécessaire

## Déploiement

Pour un déploiement en production :

1. Utiliser un serveur web comme **Gunicorn**
2. Configurer un **reverse proxy** (Nginx)
3. Utiliser une base de données plus robuste (**PostgreSQL**)
4. Activer le **HTTPS**
5. Configurer les **logs**

Exemple avec Gunicorn :
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```

## Migration depuis Windows Forms

Cette application Flask reproduit fidèlement les fonctionnalités du formulaire Windows Forms original :

### Correspondances des Contrôles
- **TextBox** → `<input type="text">`
- **ComboBox** → `<select>`
- **CheckBox/RadioButton** → `<select>` avec Oui/Non
- **DataGridView** → Table HTML avec pagination
- **PictureBox** → `<img>` avec upload
- **Button** → `<button>` ou `<a class="btn">`
- **ToolStrip** → Navigation Bootstrap

### Fonctionnalités Équivalentes
- **Navigation d'enregistrements** → Pagination web
- **Recherche** → Formulaire de recherche
- **Validation** → Validation HTML5 + JavaScript
- **Calculs automatiques** → JavaScript temps réel
- **Gestion d'images** → Upload HTML5
- **États des contrôles** → Classes CSS Bootstrap

## Support et Maintenance

Cette application est conçue pour être facile à maintenir et à étendre. La structure modulaire permet d'ajouter facilement de nouvelles fonctionnalités sans impacter l'existant.

Pour toute question ou amélioration, référez-vous au code source qui est largement documenté.
