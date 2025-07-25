# Routes pour le module véhicules
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from datetime import datetime
import os

# Blueprint pour les véhicules
vehicules_bp = Blueprint('vehicules', __name__, url_prefix='/vehicules')

# Variables globales pour éviter l'import circulaire
db = None
Vehicule = None

def init_vehicules_models(database):
    """Initialise les modèles de données pour les véhicules"""
    global db, Vehicule
    db = database
    
    # Modèle de données pour les véhicules (table unit)
    class VehiculeModel(db.Model):
        __tablename__ = 'unit'
        
        # Identification
        id = db.Column('ID', db.Integer, primary_key=True)
        unite = db.Column('UNITE', db.String(20), unique=True, nullable=False)
        serie = db.Column('SERIE', db.String(50))
        licence = db.Column('LICENCE', db.String(20))
        type = db.Column('TYPE', db.String(20))
        annee = db.Column('ANNEE', db.Integer)
        etat = db.Column('ETAT', db.String(20))
        
        # Spécifications techniques
        marque = db.Column('MARQUE', db.String(30))
        modele = db.Column('MODELE', db.String(30))
        cabine = db.Column('CABINE', db.String(20))
        poids = db.Column('POIDS', db.String(20))
        combustion = db.Column('COMBUSTION', db.String(20))
        capacite = db.Column('CAPACITE', db.String(20))
        
        # Client
        client = db.Column('CLIENT', db.String(20))
        nom = db.Column('NOM', db.String(50))
        tphone = db.Column('TPHONE', db.String(20))
        email = db.Column('EMAIL', db.String(100))
        adr1 = db.Column('ADR1', db.String(100))
        ville = db.Column('VILLE', db.String(50))
        
        # État et suivi
        statut = db.Column('STATUT', db.String(20))
        date_ach = db.Column('DATE_ACH', db.Date)
        date_vte = db.Column('DATE_VTE', db.Date)
        date_cree = db.Column('DATE_CREE', db.DateTime)
        date_modif = db.Column('DATE_MODIF', db.DateTime)
        date_desac = db.Column('DATE_DESAC', db.Date)
        remarque = db.Column('REMARQUE', db.Text)
        
        # Valeur
        prix = db.Column('PRIX', db.Numeric(12, 2))
        cout = db.Column('COUT', db.Numeric(12, 2))
        coutu = db.Column('COUTU', db.Numeric(12, 2))
        profit = db.Column('PROFIT', db.Numeric(12, 2))
        devaluat = db.Column('DEVALUAT', db.Numeric(12, 2))
        
        # Entretien
        duree = db.Column('DUREE', db.Integer)
        entd = db.Column('ENTD', db.Date)
        ent1 = db.Column('ENT1', db.Text)
        ent2 = db.Column('ENT2', db.Text)
        ent3 = db.Column('ENT3', db.Text)
        ent4 = db.Column('ENT4', db.Text)
        ent5 = db.Column('ENT5', db.Text)
        ent6 = db.Column('ENT6', db.Text)
        garantie = db.Column('GARANTIE', db.String(50))
        remunit = db.Column('REMUNIT', db.Text)
        remgarant = db.Column('REMGARANT', db.Text)
        
        # Financement
        four = db.Column('FOUR', db.String(50))
        nofacture = db.Column('NOFACTURE', db.String(30))
        taxfed = db.Column('TAXFED', db.Numeric(10, 2))
        taxpro = db.Column('TAXPRO', db.Numeric(10, 2))
        totalp = db.Column('TOTALP', db.Numeric(12, 2))
        totalco = db.Column('TOTALCO', db.Numeric(12, 2))
    
    Vehicule = VehiculeModel
    return VehiculeModel

def get_vehicule_model():
    """
    Retourne le modèle Vehicule s'il est initialisé
    Utilisé pour les statistiques globales et les intégrations inter-modules
    """
    global Vehicule
    return Vehicule

@vehicules_bp.route('/')
def liste_vehicules():
    """Liste des véhicules avec filtres et pagination"""
    Vehicule = get_vehicule_model()
    page = request.args.get('page', 1, type=int)
    search = request.args.get('search', '')
    statut = request.args.get('statut', '')
    type_vehicule = request.args.get('type', '')
    marque = request.args.get('marque', '')
    client = request.args.get('client', '')
    
    # Construction de la requête avec filtres
    query = Vehicule.query
    
    if search:
        query = query.filter(
            db.or_(
                Vehicule.unite.contains(search),
                Vehicule.serie.contains(search),
                Vehicule.nom.contains(search),
                Vehicule.marque.contains(search),
                Vehicule.modele.contains(search)
            )
        )
    
    if statut:
        query = query.filter(Vehicule.statut == statut)
    
    if type_vehicule:
        query = query.filter(Vehicule.type == type_vehicule)
        
    if marque:
        query = query.filter(Vehicule.marque.contains(marque))
        
    if client:
        query = query.filter(
            db.or_(
                Vehicule.client.contains(client),
                Vehicule.nom.contains(client)
            )
        )
    
    # Tri par défaut
    query = query.order_by(Vehicule.date_modif.desc())
    
    # Pagination
    vehicules = query.paginate(
        page=page, 
        per_page=20, 
        error_out=False
    )
    
    # Statistiques
    stats = {
        'total': Vehicule.query.count(),
        'internes': Vehicule.query.filter_by(statut='INTERNE').count(),
        'vendus': Vehicule.query.filter_by(statut='VENDU').count(),
        'loues': Vehicule.query.filter_by(statut='LOUE').count(),
        'reparation': Vehicule.query.filter_by(statut='REPARATION').count(),
        'desactives': Vehicule.query.filter_by(statut='DESACTIVE').count()
    }
    
    return render_template('vehicules/liste.html', 
                         vehicules=vehicules,
                         stats=stats,
                         search=search, 
                         statut=statut,
                         type=type_vehicule,
                         marque=marque,
                         client=client)

@vehicules_bp.route('/<int:id>')
def voir_vehicule(id):
    """Afficher le détail d'un véhicule"""
    Vehicule = get_vehicule_model()
    vehicule = Vehicule.query.get_or_404(id)
    return render_template('vehicules/detail.html', vehicule=vehicule)

@vehicules_bp.route('/nouveau', methods=['GET', 'POST'])
def nouveau_vehicule():
    """Créer un nouveau véhicule"""
    Vehicule = get_vehicule_model()
    if request.method == 'POST':
        try:
            vehicule = Vehicule(
                unite=request.form.get('unite').upper(),
                type=request.form.get('type'),
                annee=request.form.get('annee') or None,
                serie=request.form.get('serie'),
                licence=request.form.get('licence'),
                statut=request.form.get('statut', 'INTERNE'),
                etat=request.form.get('etat'),
                marque=request.form.get('marque'),
                modele=request.form.get('modele'),
                cabine=request.form.get('cabine'),
                poids=request.form.get('poids'),
                combustion=request.form.get('combustion'),
                capacite=request.form.get('capacite'),
                client=request.form.get('client'),
                nom=request.form.get('nom'),
                tphone=request.form.get('tphone'),
                email=request.form.get('email'),
                adr1=request.form.get('adr1'),
                ville=request.form.get('ville'),
                prix=request.form.get('prix') or None,
                cout=request.form.get('cout') or None,
                coutu=request.form.get('coutu') or None,
                profit=request.form.get('profit') or None,
                devaluat=request.form.get('devaluat') or None,
                date_ach=datetime.strptime(request.form.get('date_ach'), '%Y-%m-%d').date() if request.form.get('date_ach') else None,
                date_vte=datetime.strptime(request.form.get('date_vte'), '%Y-%m-%d').date() if request.form.get('date_vte') else None,
                date_desac=datetime.strptime(request.form.get('date_desac'), '%Y-%m-%d').date() if request.form.get('date_desac') else None,
                four=request.form.get('four'),
                nofacture=request.form.get('nofacture'),
                duree=request.form.get('duree') or None,
                entd=datetime.strptime(request.form.get('entd'), '%Y-%m-%d').date() if request.form.get('entd') else None,
                garantie=request.form.get('garantie'),
                remunit=request.form.get('remunit'),
                remgarant=request.form.get('remgarant'),
                ent1=request.form.get('ent1'),
                ent2=request.form.get('ent2'),
                ent3=request.form.get('ent3'),
                ent4=request.form.get('ent4'),
                ent5=request.form.get('ent5'),
                ent6=request.form.get('ent6'),
                remarque=request.form.get('remarque'),
                taxfed=request.form.get('taxfed') or None,
                taxpro=request.form.get('taxpro') or None,
                date_cree=datetime.now(),
                date_modif=datetime.now()
            )
            
            db.session.add(vehicule)
            db.session.commit()
            
            flash(f'Véhicule {vehicule.unite} créé avec succès.', 'success')
            
            # Si c'est une requête AJAX, retourner du JSON
            if request.headers.get('Content-Type') == 'application/x-www-form-urlencoded' and \
               request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return jsonify({
                    'success': True,
                    'message': f'Véhicule {vehicule.unite} créé avec succès.',
                    'vehicule_id': vehicule.id,
                    'vehicule_unite': vehicule.unite
                })
            
            return redirect(url_for('vehicules.voir_vehicule', id=vehicule.id))
            
        except Exception as e:
            db.session.rollback()
            flash(f'Erreur lors de la création du véhicule: {str(e)}', 'error')
    
    return render_template('vehicules/formulaire.html')

@vehicules_bp.route('/<int:id>/modifier', methods=['GET', 'POST'])
def modifier_vehicule(id):
    """Modifier un véhicule existant"""
    Vehicule = get_vehicule_model()
    vehicule = Vehicule.query.get_or_404(id)
    
    if request.method == 'POST':
        try:
            vehicule.type = request.form.get('type')
            vehicule.annee = request.form.get('annee') or None
            vehicule.serie = request.form.get('serie')
            vehicule.licence = request.form.get('licence')
            vehicule.statut = request.form.get('statut')
            vehicule.etat = request.form.get('etat')
            vehicule.marque = request.form.get('marque')
            vehicule.modele = request.form.get('modele')
            vehicule.cabine = request.form.get('cabine')
            vehicule.poids = request.form.get('poids')
            vehicule.combustion = request.form.get('combustion')
            vehicule.capacite = request.form.get('capacite')
            vehicule.client = request.form.get('client')
            vehicule.nom = request.form.get('nom')
            vehicule.tphone = request.form.get('tphone')
            vehicule.email = request.form.get('email')
            vehicule.adr1 = request.form.get('adr1')
            vehicule.ville = request.form.get('ville')
            vehicule.prix = request.form.get('prix') or None
            vehicule.cout = request.form.get('cout') or None
            vehicule.coutu = request.form.get('coutu') or None
            vehicule.profit = request.form.get('profit') or None
            vehicule.devaluat = request.form.get('devaluat') or None
            vehicule.date_ach = datetime.strptime(request.form.get('date_ach'), '%Y-%m-%d').date() if request.form.get('date_ach') else None
            vehicule.date_vte = datetime.strptime(request.form.get('date_vte'), '%Y-%m-%d').date() if request.form.get('date_vte') else None
            vehicule.date_desac = datetime.strptime(request.form.get('date_desac'), '%Y-%m-%d').date() if request.form.get('date_desac') else None
            vehicule.four = request.form.get('four')
            vehicule.nofacture = request.form.get('nofacture')
            vehicule.duree = request.form.get('duree') or None
            vehicule.entd = datetime.strptime(request.form.get('entd'), '%Y-%m-%d').date() if request.form.get('entd') else None
            vehicule.garantie = request.form.get('garantie')
            vehicule.remunit = request.form.get('remunit')
            vehicule.remgarant = request.form.get('remgarant')
            vehicule.ent1 = request.form.get('ent1')
            vehicule.ent2 = request.form.get('ent2')
            vehicule.ent3 = request.form.get('ent3')
            vehicule.ent4 = request.form.get('ent4')
            vehicule.ent5 = request.form.get('ent5')
            vehicule.ent6 = request.form.get('ent6')
            vehicule.remarque = request.form.get('remarque')
            vehicule.taxfed = request.form.get('taxfed') or None
            vehicule.taxpro = request.form.get('taxpro') or None
            vehicule.date_modif = datetime.now()
            
            db.session.commit()
            
            flash(f'Véhicule {vehicule.unite} modifié avec succès.', 'success')
            return redirect(url_for('vehicules.voir_vehicule', id=vehicule.id))
            
        except Exception as e:
            db.session.rollback()
            flash(f'Erreur lors de la modification du véhicule: {str(e)}', 'error')
    
    return render_template('vehicules/formulaire.html', vehicule=vehicule)

@vehicules_bp.route('/<int:id>/desactiver', methods=['POST'])
def desactiver_vehicule(id):
    """Désactiver un véhicule"""
    Vehicule = get_vehicule_model()
    vehicule = Vehicule.query.get_or_404(id)
    
    try:
        vehicule.statut = 'DESACTIVE'
        vehicule.date_desac = datetime.now().date()
        vehicule.date_modif = datetime.now()
        
        db.session.commit()
        
        flash(f'Véhicule {vehicule.unite} désactivé avec succès.', 'warning')
        return redirect(url_for('vehicules.liste_vehicules'))
        
    except Exception as e:
        db.session.rollback()
        flash(f'Erreur lors de la désactivation du véhicule: {str(e)}', 'error')
        return redirect(url_for('vehicules.voir_vehicule', id=id))

@vehicules_bp.route('/<int:id>/dupliquer')
def dupliquer_vehicule(id):
    """Dupliquer un véhicule existant"""
    Vehicule = get_vehicule_model()
    vehicule_original = Vehicule.query.get_or_404(id)
    
    return render_template('vehicules/formulaire.html', 
                         vehicule=vehicule_original,
                         is_duplicate=True)

# API endpoints pour intégration
@vehicules_bp.route('/api/search')
def api_search_vehicules():
    """API de recherche de véhicules pour auto-complétion"""
    Vehicule = get_vehicule_model()
    query = request.args.get('q', '')
    limit = request.args.get('limit', 10, type=int)
    
    vehicules = Vehicule.query.filter(
        db.or_(
            Vehicule.unite.contains(query),
            Vehicule.marque.contains(query),
            Vehicule.modele.contains(query)
        )
    ).limit(limit).all()
    
    results = []
    for v in vehicules:
        results.append({
            'id': v.id,
            'unite': v.unite,
            'marque': v.marque,
            'modele': v.modele,
            'statut': v.statut,
            'prix': float(v.prix) if v.prix else None
        })
    
    return jsonify(results)

@vehicules_bp.route('/api/stats')
def api_stats_vehicules():
    """API pour obtenir les statistiques des véhicules"""
    Vehicule = get_vehicule_model()
    stats = {
        'total': Vehicule.query.count(),
        'by_status': {},
        'by_type': {},
        'maintenance_urgent': Vehicule.query.filter(Vehicule.duree <= 30).count(),
        'average_price': db.session.query(db.func.avg(Vehicule.prix)).scalar() or 0
    }
    
    # Statistiques par statut
    statuts = ['INTERNE', 'VENDU', 'LOUE', 'REPARATION', 'DESACTIVE']
    for statut in statuts:
        stats['by_status'][statut] = Vehicule.query.filter_by(statut=statut).count()
    
    # Statistiques par type
    types = ['CAMION', 'REMORQUE', 'VOITURE', 'EQUIPEMENT']
    for type_v in types:
        stats['by_type'][type_v] = Vehicule.query.filter_by(type=type_v).count()
    
    return jsonify(stats)
