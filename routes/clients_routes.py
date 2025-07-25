# ========================================
# Module Gestion des Clients - SEI Lite
# ========================================
# 
# Blueprint Flask pour la gestion complète des clients
# Conforme au PRD dans clients.md
# 
# Fonctionnalités :
# - CRUD complet (Create, Read, Update, Delete)
# - Recherche et filtres dynamiques  
# - Navigation inter-modules
# - API REST
# - Statistiques et rapports
# - Duplication de clients
# - Désactivation/archivage
# - Modal AJAX pour création rapide
# 

from flask import Blueprint, render_template, request, jsonify, redirect, url_for, flash
from sqlalchemy import func, desc, and_, or_
from datetime import datetime, timedelta
import json

# Blueprint pour le module clients
clients_bp = Blueprint('clients', __name__, url_prefix='/clients')

# Variable globale pour le modèle Client (sera initialisé par init_clients_models)
Client = None
db = None

def init_clients_models(database):
    """
    Initialise le modèle Client avec la base de données
    Retourne la classe Client pour utilisation dans d'autres modules
    """
    global Client, db
    db = database
    
    class Client(db.Model):
        __tablename__ = 'client'
        
        # 🆔 Identification principale
        id = db.Column('client_index', db.Integer, primary_key=True, autoincrement=True)
        client_id = db.Column('CLIENT', db.String(30), unique=True, nullable=False, index=True)
        nom = db.Column('NOM', db.String(60))
        prenom = db.Column('PRENOM', db.String(60))
        compagnie = db.Column('COMPAGNY', db.String(60))
        loyalid = db.Column('LOYALID', db.String(30))
        
        # 📞 Coordonnées principales
        adresse1 = db.Column('ADR1', db.String(60))
        adresse2 = db.Column('ADR2', db.String(60))
        ville = db.Column('VILLE', db.String(30))
        code_postal = db.Column('CP1', db.String(15))
        province = db.Column('PROV', db.String(30))
        pays = db.Column('PAYS', db.String(30), default='CANADA')
        telephone = db.Column('TPHONE', db.String(30))
        cellulaire = db.Column('TELCEL', db.String(30))
        email = db.Column('EMAIL', db.String(100))
        
        # 📞 Contacts secondaires
        contact = db.Column('CONTACT', db.String(60))
        tel_contact = db.Column('TELCON', db.String(30))
        fax = db.Column('FAX', db.String(30))
        
        # 🔍 Statuts et catégories
        actif = db.Column('ACTIF', db.String(1), default='O')
        arret = db.Column('ARRET', db.String(1), default='N')
        statut = db.Column('STAT', db.String(15))
        categorie = db.Column('CAT', db.String(15))
        type_client = db.Column('TYPE', db.String(15))
        type_extended = db.Column('TYPEE', db.String(15))
        langue = db.Column('LANGUE', db.String(10), default='FR')
        vendeur = db.Column('VENDEUR', db.String(30))
        groupe = db.Column('GROUPE', db.String(15))
        
        # 💰 Données fiscales et financières
        no_taxe_federale = db.Column('NOTAXFED', db.String(1), default='N')
        no_taxe_provinciale = db.Column('NOTAXPRO', db.String(1), default='N')
        taux_taxe = db.Column('TAUX', db.String(10))
        termes = db.Column('TERMES', db.String(15))
        limite_credit = db.Column('LIMCRE', db.String(15))
        depot = db.Column('DEPOT', db.String(15))
        transport = db.Column('TRANS', db.String(15))
        monnaie = db.Column('MON', db.String(10), default='CAD')
        
        # 🧠 CRM et remarques
        motcle1 = db.Column('MOTCLE1', db.String(30))
        motcle2 = db.Column('MOTCLE2', db.String(30))
        commentaire = db.Column('COMMENT', db.Text)
        commentaire2 = db.Column('COMMENT2', db.Text)
        remarque1 = db.Column('REM1', db.String(100))
        remarque2 = db.Column('REM2', db.String(100))
        
        # 🔐 Sécurité et fichiers
        rep_envoi = db.Column('REPENVOIE', db.String(100))
        rep_sortie = db.Column('REPSORTIE', db.String(100))
        ftp = db.Column('FTP', db.String(100))
        mot_passe = db.Column('MOTPASSE', db.String(30))
        permis = db.Column('PERMIS', db.String(30))
        carte = db.Column('CARTE', db.String(30))
        
        # 📅 Dates importantes
        date_creation = db.Column('DATECR', db.String(10))
        date_naissance = db.Column('DATENAIS', db.String(10))
        date_derniere_vente = db.Column('DATDVTE', db.String(10))
        date_expiration = db.Column('DATEEXP', db.String(10))
        date_epuise = db.Column('DATEP', db.String(10))
        
        def __repr__(self):
            return f'<Client {self.client_id}: {self.nom} {self.prenom}>'
        
        def to_dict(self):
            """Convertit l'objet Client en dictionnaire pour JSON"""
            return {
                'id': self.id,
                'client_id': self.client_id,
                'nom': self.nom,
                'prenom': self.prenom,
                'compagnie': self.compagnie,
                'telephone': self.telephone,
                'cellulaire': self.cellulaire,
                'email': self.email,
                'ville': self.ville,
                'vendeur': self.vendeur,
                'statut': self.statut,
                'actif': self.actif,
                'loyalid': self.loyalid,
                'date_creation': self.date_creation
            }
        
        @property
        def nom_complet(self):
            """Retourne le nom complet formaté"""
            if self.compagnie:
                return f"{self.compagnie}"
            else:
                return f"{self.prenom or ''} {self.nom or ''}".strip()
        
        @property
        def est_actif(self):
            """Vérifie si le client est actif"""
            return self.actif == 'O' and self.arret != 'O'
        
        @property
        def badge_statut(self):
            """Retourne la classe CSS pour le badge de statut"""
            if not self.est_actif:
                return 'badge bg-secondary'
            elif self.statut == 'VIP':
                return 'badge bg-warning'
            elif self.loyalid:
                return 'badge bg-success' 
            else:
                return 'badge bg-primary'
    
    return Client

# ========================================
# ROUTES PRINCIPALES
# ========================================

@clients_bp.route('/')
def liste_clients():
    """
    Affiche la liste des clients avec recherche, filtres et pagination
    Conforme aux spécifications PRD pour liste.html
    """
    page = request.args.get('page', 1, type=int)
    search = request.args.get('search', '')
    search_type = request.args.get('search_type', 'nom')
    
    # Filtres dynamiques
    filtre_actif = request.args.get('actif', '')
    filtre_type = request.args.get('type', '')
    filtre_vendeur = request.args.get('vendeur', '')
    filtre_province = request.args.get('province', '')
    filtre_groupe = request.args.get('groupe', '')
    
    # Construction de la requête de base
    query = Client.query
    
    # Application de la recherche globale
    if search:
        if search_type == 'nom':
            query = query.filter(
                or_(
                    Client.nom.ilike(f'%{search}%'),
                    Client.prenom.ilike(f'%{search}%'),
                    Client.compagnie.ilike(f'%{search}%')
                )
            )
        elif search_type == 'client_id':
            query = query.filter(Client.client_id.ilike(f'%{search}%'))
        elif search_type == 'telephone':
            query = query.filter(
                or_(
                    Client.telephone.ilike(f'%{search}%'),
                    Client.cellulaire.ilike(f'%{search}%')
                )
            )
        elif search_type == 'vendeur':
            query = query.filter(Client.vendeur.ilike(f'%{search}%'))
        elif search_type == 'email':
            query = query.filter(Client.email.ilike(f'%{search}%'))
    
    # Application des filtres dynamiques
    if filtre_actif:
        if filtre_actif == 'actif':
            query = query.filter(and_(Client.actif == 'O', Client.arret != 'O'))
        elif filtre_actif == 'inactif':
            query = query.filter(or_(Client.actif != 'O', Client.arret == 'O'))
    
    if filtre_type:
        query = query.filter(Client.type_client == filtre_type)
    
    if filtre_vendeur:
        query = query.filter(Client.vendeur == filtre_vendeur)
    
    if filtre_province:
        query = query.filter(Client.province == filtre_province)
        
    if filtre_groupe:
        query = query.filter(Client.groupe == filtre_groupe)
    
    # Tri par défaut : nom
    query = query.order_by(Client.nom.asc(), Client.prenom.asc())
    
    # Pagination
    clients = query.paginate(
        page=page, per_page=25, error_out=False
    )
    
    # Calcul des statistiques pour le dashboard
    stats = calculer_stats_clients()
    
    # Listes pour les filtres dynamiques
    vendeurs = Client.query.with_entities(Client.vendeur).distinct().filter(Client.vendeur.isnot(None)).all()
    provinces = Client.query.with_entities(Client.province).distinct().filter(Client.province.isnot(None)).all()
    types = Client.query.with_entities(Client.type_client).distinct().filter(Client.type_client.isnot(None)).all()
    groupes = Client.query.with_entities(Client.groupe).distinct().filter(Client.groupe.isnot(None)).all()
    
    return render_template('clients/liste.html', 
                         clients=clients,
                         search=search,
                         search_type=search_type,
                         stats=stats,
                         vendeurs=[v[0] for v in vendeurs],
                         provinces=[p[0] for p in provinces],
                         types=[t[0] for t in types],
                         groupes=[g[0] for g in groupes],
                         filtres={
                             'actif': filtre_actif,
                             'type': filtre_type,
                             'vendeur': filtre_vendeur,
                             'province': filtre_province,
                             'groupe': filtre_groupe
                         })

@clients_bp.route('/<int:id>')
def detail_client(id):
    """
    Affiche la fiche complète d'un client
    Conforme aux spécifications PRD pour detail.html
    """
    client = Client.query.get_or_404(id)
    
    # TODO: Charger l'historique des interactions
    # historique_vehicules = []
    # historique_contrats = []
    # historique_factures = []
    
    return render_template('clients/detail.html', 
                         client=client)
                         # historique_vehicules=historique_vehicules,
                         # historique_contrats=historique_contrats,
                         # historique_factures=historique_factures)

@clients_bp.route('/nouveau', methods=['GET', 'POST'])
def nouveau_client():
    """
    Création d'un nouveau client
    Conforme aux spécifications PRD pour formulaire.html
    """
    if request.method == 'POST':
        return traiter_formulaire_client()
    
    return render_template('clients/formulaire.html', client=None)

@clients_bp.route('/<int:id>/modifier', methods=['GET', 'POST'])
def modifier_client(id):
    """
    Modification d'un client existant
    Conforme aux spécifications PRD pour formulaire.html
    """
    client = Client.query.get_or_404(id)
    
    if request.method == 'POST':
        return traiter_formulaire_client(client)
    
    return render_template('clients/formulaire.html', client=client)

@clients_bp.route('/<int:id>/dupliquer')
def dupliquer_client(id):
    """
    Duplique un client existant pour création rapide
    """
    client_source = Client.query.get_or_404(id)
    
    # Création d'un nouveau client avec les données du client source
    # mais avec un nouveau CLIENT_ID
    nouveau_client_id = generer_nouveau_client_id()
    
    return render_template('clients/formulaire.html', 
                         client=client_source, 
                         duplication=True,
                         nouveau_client_id=nouveau_client_id)

@clients_bp.route('/<int:id>/desactiver', methods=['POST'])
def desactiver_client(id):
    """
    Désactive un client (archivage)
    """
    client = Client.query.get_or_404(id)
    
    try:
        client.actif = 'N'
        client.arret = 'O'
        db.session.commit()
        
        if request.is_json:
            return jsonify({'success': True, 'message': 'Client désactivé avec succès'})
        else:
            flash('Client désactivé avec succès', 'success')
            return redirect(url_for('clients.liste_clients'))
            
    except Exception as e:
        db.session.rollback()
        if request.is_json:
            return jsonify({'success': False, 'error': str(e)})
        else:
            flash(f'Erreur lors de la désactivation: {str(e)}', 'error')
            return redirect(url_for('clients.detail_client', id=id))

@clients_bp.route('/<int:id>/supprimer', methods=['POST'])
def supprimer_client(id):
    """
    Supprime définitivement un client (avec vérifications)
    """
    client = Client.query.get_or_404(id)
    
    try:
        # TODO: Vérifier s'il y a des références dans d'autres tables
        # (véhicules, factures, contrats, etc.)
        
        db.session.delete(client)
        db.session.commit()
        
        flash('Client supprimé avec succès', 'success')
        return redirect(url_for('clients.liste_clients'))
        
    except Exception as e:
        db.session.rollback()
        flash(f'Erreur lors de la suppression: {str(e)}', 'error')
        return redirect(url_for('clients.detail_client', id=id))

# ========================================
# API REST
# ========================================

@clients_bp.route('/api/clients')
def api_liste_clients():
    """
    API REST pour récupérer la liste des clients
    Supporte filtres et pagination
    """
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 50, type=int)
    search = request.args.get('search', '')
    
    query = Client.query
    
    if search:
        query = query.filter(
            or_(
                Client.nom.ilike(f'%{search}%'),
                Client.prenom.ilike(f'%{search}%'),
                Client.compagnie.ilike(f'%{search}%'),
                Client.client_id.ilike(f'%{search}%')
            )
        )
    
    clients = query.paginate(
        page=page, per_page=per_page, error_out=False
    )
    
    return jsonify({
        'clients': [client.to_dict() for client in clients.items],
        'total': clients.total,
        'pages': clients.pages,
        'current_page': page,
        'has_next': clients.has_next,
        'has_prev': clients.has_prev
    })

@clients_bp.route('/api/clients/<int:id>')
def api_detail_client(id):
    """
    API REST pour récupérer le détail d'un client
    """
    client = Client.query.get_or_404(id)
    return jsonify(client.to_dict())

@clients_bp.route('/api/clients', methods=['POST'])
def api_creer_client():
    """
    API REST pour créer un nouveau client
    """
    data = request.get_json()
    
    try:
        client = Client()
        # Remplir les champs depuis les données JSON
        remplir_client_depuis_data(client, data)
        
        db.session.add(client)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'client': client.to_dict(),
            'message': 'Client créé avec succès'
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

@clients_bp.route('/api/clients/<int:id>', methods=['PUT'])
def api_modifier_client(id):
    """
    API REST pour modifier un client existant
    """
    client = Client.query.get_or_404(id)
    data = request.get_json()
    
    try:
        # Mettre à jour les champs depuis les données JSON
        remplir_client_depuis_data(client, data)
        
        db.session.commit()
        
        return jsonify({
            'success': True,
            'client': client.to_dict(),
            'message': 'Client modifié avec succès'
        })
        
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

# ========================================
# FONCTIONS UTILITAIRES
# ========================================

def traiter_formulaire_client(client=None):
    """
    Traite le formulaire de création/modification d'un client
    """
    try:
        # Si pas de client fourni, c'est une création
        est_creation = client is None
        if est_creation:
            client = Client()
            # Générer un nouveau CLIENT_ID si pas fourni
            if not request.form.get('client_id'):
                client.client_id = generer_nouveau_client_id()
            else:
                client.client_id = request.form['client_id'].upper().strip()
        
        # Remplir les champs depuis le formulaire
        remplir_client_depuis_formulaire(client, request.form)
        
        if est_creation:
            db.session.add(client)
        
        db.session.commit()
        
        # Gestion des requêtes AJAX (modal)
        if request.is_json or request.headers.get('Content-Type') == 'application/json':
            return jsonify({
                'success': True,
                'client': client.to_dict(),
                'message': 'Client créé avec succès' if est_creation else 'Client modifié avec succès',
                'redirect_url': url_for('clients.detail_client', id=client.id)
            })
        
        message = 'Client créé avec succès!' if est_creation else 'Client modifié avec succès!'
        flash(message, 'success')
        return redirect(url_for('clients.detail_client', id=client.id))
        
    except Exception as e:
        db.session.rollback()
        
        if request.is_json or request.headers.get('Content-Type') == 'application/json':
            return jsonify({
                'success': False,
                'error': str(e)
            }), 400
        
        flash(f'Erreur lors de l\'enregistrement: {str(e)}', 'error')
        return render_template('clients/formulaire.html', client=client)

def remplir_client_depuis_formulaire(client, form_data):
    """
    Remplit un objet Client depuis les données du formulaire
    """
    # Identification
    if form_data.get('client_id'):
        client.client_id = form_data['client_id'].upper().strip()
    client.nom = form_data.get('nom', '').strip()
    client.prenom = form_data.get('prenom', '').strip()
    client.compagnie = form_data.get('compagnie', '').strip()
    client.loyalid = form_data.get('loyalid', '').strip()
    
    # Coordonnées
    client.adresse1 = form_data.get('adresse1', '').strip()
    client.adresse2 = form_data.get('adresse2', '').strip()
    client.ville = form_data.get('ville', '').strip()
    client.code_postal = form_data.get('code_postal', '').strip()
    client.province = form_data.get('province', '').strip()
    client.pays = form_data.get('pays', 'CANADA').strip()
    client.telephone = form_data.get('telephone', '').strip()
    client.cellulaire = form_data.get('cellulaire', '').strip()
    client.email = form_data.get('email', '').strip()
    
    # Contacts
    client.contact = form_data.get('contact', '').strip()
    client.tel_contact = form_data.get('tel_contact', '').strip()
    client.fax = form_data.get('fax', '').strip()
    
    # Statuts
    client.actif = form_data.get('actif', 'O')
    client.arret = form_data.get('arret', 'N')
    client.statut = form_data.get('statut', '').strip()
    client.categorie = form_data.get('categorie', '').strip()
    client.type_client = form_data.get('type_client', '').strip()
    client.type_extended = form_data.get('type_extended', '').strip()
    client.langue = form_data.get('langue', 'FR')
    client.vendeur = form_data.get('vendeur', '').strip()
    client.groupe = form_data.get('groupe', '').strip()
    
    # Finances
    client.no_taxe_federale = form_data.get('no_taxe_federale', 'N')
    client.no_taxe_provinciale = form_data.get('no_taxe_provinciale', 'N')
    client.taux_taxe = form_data.get('taux_taxe', '').strip()
    client.termes = form_data.get('termes', '').strip()
    client.limite_credit = form_data.get('limite_credit', '').strip()
    client.depot = form_data.get('depot', '').strip()
    client.transport = form_data.get('transport', '').strip()
    client.monnaie = form_data.get('monnaie', 'CAD')
    
    # CRM
    client.motcle1 = form_data.get('motcle1', '').strip()
    client.motcle2 = form_data.get('motcle2', '').strip()
    client.commentaire = form_data.get('commentaire', '').strip()
    client.commentaire2 = form_data.get('commentaire2', '').strip()
    client.remarque1 = form_data.get('remarque1', '').strip()
    client.remarque2 = form_data.get('remarque2', '').strip()
    
    # Sécurité
    client.rep_envoi = form_data.get('rep_envoi', '').strip()
    client.rep_sortie = form_data.get('rep_sortie', '').strip()
    client.ftp = form_data.get('ftp', '').strip()
    client.mot_passe = form_data.get('mot_passe', '').strip()
    client.permis = form_data.get('permis', '').strip()
    client.carte = form_data.get('carte', '').strip()
    
    # Dates
    client.date_creation = form_data.get('date_creation', datetime.now().strftime('%Y-%m-%d'))
    client.date_naissance = form_data.get('date_naissance', '').strip()
    client.date_expiration = form_data.get('date_expiration', '').strip()

def remplir_client_depuis_data(client, data):
    """
    Remplit un objet Client depuis des données JSON (API)
    """
    # Identification
    if data.get('client_id'):
        client.client_id = data['client_id'].upper().strip()
    if 'nom' in data:
        client.nom = data['nom'].strip()
    if 'prenom' in data:
        client.prenom = data['prenom'].strip()
    if 'compagnie' in data:
        client.compagnie = data['compagnie'].strip()
    
    # Coordonnées
    if 'telephone' in data:
        client.telephone = data['telephone'].strip()
    if 'email' in data:
        client.email = data['email'].strip()
    if 'ville' in data:
        client.ville = data['ville'].strip()
    
    # Autres champs selon besoin
    # ... (ajouter selon les besoins de l'API)

def generer_nouveau_client_id():
    """
    Génère un nouveau CLIENT_ID unique
    Format : CLI0001, CLI0002, etc.
    """
    # Récupérer le dernier CLIENT_ID numérique
    dernier_client = Client.query.filter(
        Client.client_id.like('CLI%')
    ).order_by(desc(Client.client_id)).first()
    
    if dernier_client:
        try:
            # Extraire le numéro du dernier client
            numero_str = dernier_client.client_id[3:]  # Enlever "CLI"
            numero = int(numero_str) + 1
        except (ValueError, TypeError):
            numero = 1
    else:
        numero = 1
    
    return f"CLI{numero:04d}"

def calculer_stats_clients():
    """
    Calcule les statistiques des clients pour le dashboard
    """
    try:
        total_clients = Client.query.count()
        clients_actifs = Client.query.filter(
            and_(Client.actif == 'O', Client.arret != 'O')
        ).count()
        clients_inactifs = total_clients - clients_actifs
        
        # Clients créés cette semaine
        une_semaine = (datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d')
        nouveaux_clients = Client.query.filter(
            Client.date_creation >= une_semaine
        ).count()
        
        # Clients VIP / Loyauté
        clients_vip = Client.query.filter(Client.statut == 'VIP').count()
        clients_loyaute = Client.query.filter(Client.loyalid.isnot(None)).count()
        
        return {
            'total': total_clients,
            'actifs': clients_actifs,
            'inactifs': clients_inactifs,
            'nouveaux_semaine': nouveaux_clients,
            'vip': clients_vip,
            'loyaute': clients_loyaute
        }
        
    except Exception as e:
        print(f"Erreur calcul stats clients: {e}")
        return {
            'total': 0,
            'actifs': 0,
            'inactifs': 0,
            'nouveaux_semaine': 0,
            'vip': 0,
            'loyaute': 0
        }

# ========================================
# ROUTES POUR MODAL AJAX
# ========================================

@clients_bp.route('/modal/nouveau', methods=['POST'])
def modal_nouveau_client():
    """
    Création rapide d'un client via modal AJAX
    """
    try:
        # Traitement identique au formulaire normal mais retour JSON
        return traiter_formulaire_client()
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

# ========================================
# UTILITAIRES POUR NAVIGATION
# ========================================

@clients_bp.route('/recherche')
def recherche_clients():
    """
    API de recherche rapide pour autocomplete
    """
    q = request.args.get('q', '').strip()
    limite = request.args.get('limit', 10, type=int)
    
    if len(q) < 2:
        return jsonify([])
    
    clients = Client.query.filter(
        or_(
            Client.nom.ilike(f'%{q}%'),
            Client.prenom.ilike(f'%{q}%'),
            Client.compagnie.ilike(f'%{q}%'),
            Client.client_id.ilike(f'%{q}%')
        )
    ).limit(limite).all()
    
    return jsonify([
        {
            'id': client.id,
            'client_id': client.client_id,
            'nom_complet': client.nom_complet,
            'ville': client.ville,
            'telephone': client.telephone
        }
        for client in clients
    ])

# ========================================
# ROUTES ADDITIONNELLES POUR CONFORMITÉ PRD
# ========================================

@clients_bp.route('/stats')
def stats_clients():
    """
    Page dédiée aux statistiques clients
    """
    stats = calculer_stats_clients()
    return jsonify(stats)

@clients_bp.route('/export')
def exporter_clients():
    """
    Export des clients en différents formats
    """
    format_export = request.args.get('format', 'excel')
    # TODO: Implémenter l'export Excel/PDF
    flash('Fonction d\'export en développement', 'info')
    return redirect(url_for('clients.liste_clients'))

@clients_bp.route('/<int:id>/historique')
def historique_client(id):
    """
    Historique des interactions d'un client
    """
    client = Client.query.get_or_404(id)
    # TODO: Charger l'historique depuis les autres modules
    historique = {
        'vehicules': [],
        'contrats': [],
        'factures': [],
        'interactions': []
    }
    return jsonify(historique)

@clients_bp.route('/dashboard')
def dashboard_clients():
    """
    Dashboard avancé pour les clients
    """
    stats = calculer_stats_clients()
    # TODO: Ajouter graphiques et analyses
    return render_template('clients/dashboard.html', stats=stats)

def get_client_model():
    """
    Retourne le modèle Client s'il est initialisé
    Utilisé pour les statistiques globales et les intégrations inter-modules
    """
    global Client
    return Client