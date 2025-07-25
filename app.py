# --- Mise à jour dynamique d'un champ produit depuis la modale référentielle ---
from sqlalchemy.exc import SQLAlchemyError



from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://gsicloud:TCOChoosenOne204$@192.168.50.101/bdm'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'static/uploads'

db = SQLAlchemy(app)

# Import et initialisation du module véhicules (après création de db)
def init_vehicules_module():
    from routes.vehicules_routes import vehicules_bp, init_vehicules_models
    # Initialisation des modèles véhicules avec la base de données
    Vehicule = init_vehicules_models(db)
    # Enregistrement du blueprint
    app.register_blueprint(vehicules_bp)
    return Vehicule

# Import et initialisation du module clients (après création de db)
def init_clients_module():
    from routes.clients_routes import clients_bp, init_clients_models
    # Initialisation des modèles clients avec la base de données
    Client = init_clients_models(db)
    # Enregistrement du blueprint
    app.register_blueprint(clients_bp)
    return Client

# Import et initialisation du module documents (après création de db)
def init_documents_module():
    from routes.documents_routes import register_documents_routes
    # Enregistrement du module documents
    register_documents_routes(app)
    return True

class ProduitWeb(db.Model):
    __tablename__ = 'produitweb'
    id = db.Column(db.Integer, primary_key=True)
    produit_id = db.Column('PRODUIT', db.String(45), index=True)
    ligprod = db.Column('LIGPROD', db.String(45))
    couleur = db.Column('COULEUR', db.String(45))
    grandeur = db.Column('GRANDEUR', db.String(45))
    longueur = db.Column('LONGUEUR', db.String(45))
    largeur = db.Column('LARGEUR', db.String(45))
    hauteur = db.Column('HAUTEUR', db.String(45))
    poid = db.Column('POID', db.String(45))
    lienpho = db.Column('LIENPHO', db.Text)
    marque = db.Column('MARQUE', db.String(45))
    modele = db.Column('MODELE', db.String(45))
    groupe = db.Column('GROUPE', db.String(45))
    famille = db.Column('FAMILLE', db.String(45))
    annee = db.Column('ANNEE', db.String(45))
    actif = db.Column('ACTIF', db.String(45))

class Inpteck(db.Model):
    __tablename__ = 'INPTECK'
    id = db.Column(db.Integer, primary_key=True)
    produit_id = db.Column('PRODUIT', db.String(30), index=True)
    fiche1 = db.Column('FICHE1', db.String(80))
    fiche2 = db.Column('FICHE2', db.String(80))
    fiche3 = db.Column('FICHE3', db.String(80))
    fiche4 = db.Column('FICHE4', db.String(80))
    fiche5 = db.Column('FICHE5', db.String(80))
    fiche6 = db.Column('FICHE6', db.String(80))
    fiche7 = db.Column('FICHE7', db.String(80))
    fiche8 = db.Column('FICHE8', db.String(80))
    fiche9 = db.Column('FICHE9', db.String(80))
    fiche10 = db.Column('FICHE10', db.String(80))
    fiche1a = db.Column('FICHE1A', db.String(80))
    fiche2a = db.Column('FICHE2A', db.String(80))
    fiche3a = db.Column('FICHE3A', db.String(80))
    fiche4a = db.Column('FICHE4A', db.String(80))
    fiche5a = db.Column('FICHE5A', db.String(80))
    fiche6a = db.Column('FICHE6A', db.String(80))
    fiche7a = db.Column('FICHE7A', db.String(80))
    fiche8a = db.Column('FICHE8A', db.String(80))
    fiche9a = db.Column('FICHE9A', db.String(80))
    fiche10a = db.Column('FICHE10A', db.String(80))

class Inven(db.Model):
    __tablename__ = 'INVEN'
    id = db.Column(db.Integer, primary_key=True)
    produit_id = db.Column('PRODUIT', db.String(30))
    entrepot = db.Column('ENTREPOT', db.String(10))
    inventaire = db.Column('INVENTAIRE', db.String(1))
    lot = db.Column('LOT', db.String(1))
    serial = db.Column('SERIAL', db.String(1))
    localisation = db.Column('LOCAT', db.String(10))
    desc_fr = db.Column('DESC', db.String(60))
    desc_en = db.Column('DESCA', db.String(60))
    motclef1 = db.Column('MOTCLE1', db.String(30))
    motclef2 = db.Column('MOTCLE2', db.String(30))
    taxf = db.Column('TAXF', db.String(1))
    taxp = db.Column('TAXP', db.String(1))
    qdebut = db.Column('QDEBUT', db.Numeric(10, 2))
    encom = db.Column('ENCOM', db.Numeric(10, 2))
    dta = db.Column('DTA', db.String(10))
    qrecu = db.Column('QRECU', db.Numeric(10, 2))
    qreser = db.Column('QRESER', db.Numeric(10, 2))
    qcom = db.Column('QCOM', db.Numeric(10, 2))
    qvendu = db.Column('QVENDU', db.Numeric(10, 2))
    qmain = db.Column('QMAIN', db.Numeric(10, 2))
    qgrat = db.Column('QGRAT', db.Numeric(10, 2))
    datepla = db.Column('DATEPLA', db.String(10))
    ajust = db.Column('AJUST', db.Numeric(10, 2))
    qnf = db.Column('QNF', db.Numeric(10, 2))
    qfabri = db.Column('QFABRI', db.Numeric(10, 2))
    qutil = db.Column('QUTIL', db.Numeric(10, 2))
    qtrans = db.Column('QTRANS', db.Numeric(10, 2))
    reorp = db.Column('REORP', db.Numeric(10, 2))
    mincom = db.Column('MINCOM', db.Numeric(10, 2))
    maxinv = db.Column('MAXINV', db.Numeric(10, 2))
    # Ajoutez d'autres champs selon la structure réelle de la table INVEN

class TypeRef(db.Model):
    __tablename__ = 'type'
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column('CODE', db.String(30))
    type = db.Column('TYPE', db.String(30))
    desct = db.Column('DESCT', db.String(60))
    descta = db.Column('DESCTA', db.String(60))
    val2 = db.Column('VAL2', db.String(15))
    postc2 = db.Column('POSTC2', db.String(2))
    postca2 = db.Column('POSTCA2', db.String(2))
    postu2 = db.Column('POSTU2', db.String(2))
    postua2 = db.Column('POSTUA2', db.String(2))
    val3 = db.Column('VAL3', db.String(15))
# Modèle de données pour les produits
class Produit(db.Model):
    __tablename__ = 'INPRIX'
    # 🟢 Identification du produit
    id = db.Column('ID', db.Integer, primary_key=True)
    produit_id = db.Column('CAT', db.String(30), unique=True, nullable=False)
    description_fr = db.Column('DESCR', db.String(60))
    description_en = db.Column('DESCA', db.String(60))
    barcode = db.Column('CODEBA', db.String(60))
    famille = db.Column('FORMAT', db.String(20))
    motclef1 = db.Column('MOTCLE1', db.String(30))
    motclef2 = db.Column('MOTCLE2', db.String(30))
    groupe = db.Column('TYPE', db.String(15))
    type_produit = db.Column('TYPEP', db.String(15))
    categorie = db.Column('CATP', db.String(15))
    substitut = db.Column('CODEAP', db.String(30))
    remarques1 = db.Column('DIMMET', db.String(60))
    remarques2 = db.Column('DIMIMP', db.String(60))
    # 🟡 Unités de mesure & quantités
    um_liste = db.Column('UM_LISTE', db.String(10))
    umdef = db.Column('UMDEF', db.String(10))
    umvente = db.Column('UMVENTE', db.String(10))
    um_etiq = db.Column('UM_ETIQ', db.String(10))
    quanven = db.Column('QUANVEN', db.String(10))
    quanach = db.Column('QUANACH', db.String(10))
    # Répétition unité/quantité (exemple pour 5)
    par1 = db.Column('PAR', db.String(10))
    poid1 = db.Column('POID', db.String(10))
    carton1 = db.Column('CARTON', db.String(10))
    itboi1 = db.Column('ITBOI', db.String(10))
    volume1 = db.Column('VOLUME', db.String(10))
    # 🔵 Prix
    prix0 = db.Column('PRIX0', db.String(10, 4))
    prix1 = db.Column('PRIX1', db.String(10, 4))
    prix2 = db.Column('PRIX2', db.String(10, 4))
    prix3 = db.Column('PRIX3', db.String(10, 4))
    prix4 = db.Column('PRIX4', db.String(10, 4))
    prix5 = db.Column('PRIX5', db.String(10, 4))
    prix6 = db.Column('PRIX6', db.String(10, 4))
    prix7 = db.Column('PRIX7', db.String(10, 4))
    prix8 = db.Column('PRIX8', db.String(10, 4))
    prix9 = db.Column('PRIX9', db.String(10, 4))
    prix_sugg = db.Column('PRIXSUGG', db.String(10, 4))
    cout = db.Column('COUT', db.String(10, 4))
    coutl = db.Column('COUTL', db.String(10, 4))
    coutt = db.Column('COUTT', db.String(10, 4))
    coutp = db.Column('COUTP', db.String(10, 4))
    coutm = db.Column('COUTM', db.String(10, 4))
    cout1 = db.Column('COUT1', db.String(10, 4))
    cout2 = db.Column('COUT2', db.String(10, 4))
    cout3 = db.Column('COUT3', db.String(10, 4))
    cout4 = db.Column('COUT4', db.String(10, 4))
    cout5 = db.Column('COUT5', db.String(10, 4))
    # 🟣 Fournisseurs
    fourn = db.Column('FOURN', db.String(30))
    fourn1 = db.Column('FOURN1', db.String(30))
    fourn2 = db.Column('FOURN2', db.String(30))
    fourn3 = db.Column('FOURN3', db.String(30))
    fourn4 = db.Column('FOURN4', db.String(30))
    fourn5 = db.Column('FOURN5', db.String(30))
    prodfour = db.Column('PRODFOUR', db.String(30))
    prodfour1 = db.Column('PRODFOUR1', db.String(30))
    prodfour2 = db.Column('PRODFOUR2', db.String(30))
    prodfour3 = db.Column('PRODFOUR3', db.String(30))
    prodfour4 = db.Column('PRODFOUR4', db.String(30))
    prodfour5 = db.Column('PRODFOUR5', db.String(30))
    codebafo = db.Column('CODEBAFO', db.String(60))
    codebafo1 = db.Column('CODEBAFO1', db.String(60))
    codebafo2 = db.Column('CODEBAFO2', db.String(60))
    codebafo3 = db.Column('CODEBAFO3', db.String(60))
    codebafo4 = db.Column('CODEBAFO4', db.String(60))
    codebafo5 = db.Column('CODEBAFO5', db.String(60))
    descf0 = db.Column('DESCF0', db.String(60))
    descf1 = db.Column('DESCF1', db.String(60))
    descf2 = db.Column('DESCF2', db.String(60))
    descf3 = db.Column('DESCF3', db.String(60))
    descf4 = db.Column('DESCF4', db.String(60))
    descf5 = db.Column('DESCF5', db.String(60))
    # 🟠 Escomptes & promotions
    esc1 = db.Column('ESC1', db.String(10))
    esc2 = db.Column('ESC2', db.String(10))
    esc3 = db.Column('ESC3', db.String(10))
    esc4 = db.Column('ESC4', db.String(10))
    esc5 = db.Column('ESC5', db.String(10))
    esc6 = db.Column('ESC6', db.String(10))
    esc7 = db.Column('ESC7', db.String(10))
    esc8 = db.Column('ESC8', db.String(10))
    esc9 = db.Column('ESC9', db.String(10))
    off = db.Column('OFF', db.String(10))
    qoff = db.Column('QOFF', db.String(10))
    escomptable = db.Column('PROESCTAB', db.String(1), default='O')
    # 🔴 Taxes, frais et transport
    taxfed = db.Column('TAXFED', db.String(1), default='O')
    txf = db.Column('TXF', db.String(1))
    taxpro = db.Column('TAXPRO', db.String(1), default='O')
    dou = db.Column('DOU', db.String(10))
    tr = db.Column('TR', db.String(10))
    court = db.Column('COURT', db.String(10))
    courtm = db.Column('COURTM', db.String(10))
    fr1 = db.Column('FR1', db.String(10))
    fr2 = db.Column('FR2', db.String(10))
    fr3 = db.Column('FR3', db.String(10))
    fr4 = db.Column('FR4', db.String(10))
    fr5 = db.Column('FR5', db.String(10))
    fr6 = db.Column('FR6', db.String(10))
    mfr1 = db.Column('MFR1', db.String(10))
    mfr2 = db.Column('MFR2', db.String(10))
    mfr3 = db.Column('MFR3', db.String(10))
    mfr4 = db.Column('MFR4', db.String(10))
    mfr5 = db.Column('MFR5', db.String(10))
    mfr6 = db.Column('MFR6', db.String(10))
    trm = db.Column('TRM', db.String(10))
    pertem = db.Column('PERTEM', db.String(10))
    doum = db.Column('DOUM', db.String(10))
    # 🟤 Achats, ventes, quantités, délais
    qty1 = db.Column('QTY1', db.String(10))
    qty2 = db.Column('QTY2', db.String(10))
    qty3 = db.Column('QTY3', db.String(10))
    qty4 = db.Column('QTY4', db.String(10))
    qty5 = db.Column('QTY5', db.String(10))
    qty6 = db.Column('QTY6', db.String(10))
    qty7 = db.Column('QTY7', db.String(10))
    qty8 = db.Column('QTY8', db.String(10))
    qty9 = db.Column('QTY9', db.String(10))
    div1 = db.Column('DIV1', db.String(10))
    div2 = db.Column('DIV2', db.String(10))
    mult1 = db.Column('MULT1', db.String(10))
    mult2 = db.Column('MULT2', db.String(10))
    delliv = db.Column('DELLIV', db.String(10))
    delliv1 = db.Column('DELLIV1', db.String(10))
    delliv2 = db.Column('DELLIV2', db.String(10))
    delliv3 = db.Column('DELLIV3', db.String(10))
    delliv4 = db.Column('DELLIV4', db.String(10))
    delliv5 = db.Column('DELLIV5', db.String(10))
    d1 = db.Column('D1', db.String(10))
    m1 = db.Column('M1', db.String(10))
    q1 = db.Column('Q1', db.String(10))
    # ⚫ Suivi produit / statut
    datc = db.Column('DATC', db.String(10))
    dern_achat = db.Column('DERNACHAT', db.String(10))
    creation = db.Column('CREATION', db.String(10), default=datetime.utcnow)
    datemarche = db.Column('DTEMARCHE', db.String(10))
    actif = db.Column('ACTIF', db.String(1), default='O')
    discontinue = db.Column('DISCONT', db.String(1), default='N')
    stat = db.Column('STAT', db.String(1))
    reorp = db.Column('REORP', db.String(10))
    mincom = db.Column('MINCOM', db.String(10))
    maxinv = db.Column('MAXINV', db.String(10))
    majprix = db.Column('MAJPRIX', db.String(1))
    majcout = db.Column('MAJCOUT', db.String(1))
    formcout = db.Column('FORMCOUT', db.String(2))
    calcul = db.Column('CALCUL', db.String(2))
    # 🧩 Autres (divers techniques)
    stype = db.Column('STYPE', db.String(10))
    sstype = db.Column('SSTYPE', db.String(10))
    marche = db.Column('MARCHE', db.String(10))
    marche1 = db.Column('MARCHE1', db.String(10))
    marche2 = db.Column('MARCHE2', db.String(10))
    marche3 = db.Column('MARCHE3', db.String(10))
    marche4 = db.Column('MARCHE4', db.String(10))
    marche5 = db.Column('MARCHE5', db.String(10))
    photo = db.Column('PHOTO', db.String(200))
    ns0 = db.Column('NS0', db.String(30))
    ns1 = db.Column('NS1', db.String(30))
    ns2 = db.Column('NS2', db.String(30))
    ns3 = db.Column('NS3', db.String(30))
    ns4 = db.Column('NS4', db.String(30))
    ns5 = db.Column('NS5', db.String(30))
    poste_vente_can = db.Column('POSTC', db.String(2))
    poste_vente_us = db.Column('POSTU', db.String(2))
    poste_achat_can = db.Column('POSTCA', db.String(2))
    poste_achat_us = db.Column('POSTUA', db.String(2))
    grpcore = db.Column('GRPCORE', db.String(15))
    gcore = db.Column('GCORE', db.String(1))
    prodcore = db.Column('PRODCORE', db.String(30))
    corevalue = db.Column('COREVALUE', db.String(10, 4))
    coreescal = db.Column('COREESCAL', db.String(10, 4))
    # 🟣 Champs existants non modifiés
    inventorie = db.Column('INVENTAIRE', db.String(1), default='O')
    

@app.route('/')
def index():
    return redirect(url_for('liste_produits'))

@app.route('/produits')
def liste_produits():
    page = request.args.get('page', 1, type=int)
    search = request.args.get('search', '')
    search_type = request.args.get('search_type', 'produit_id')
    
    query = Produit.query
    
    if search:
        if search_type == 'produit_id':
            query = query.filter(Produit.produit_id.ilike(f'%{search}%'))
        elif search_type == 'description':
            query = query.filter(
                (Produit.description_fr.ilike(f'%{search}%')) |
                (Produit.description_en.ilike(f'%{search}%'))
            )
        elif search_type == 'barcode':
            query = query.filter(Produit.barcode.ilike(f'%{search}%'))
    
    produits = query.paginate(
        page=page, per_page=20, error_out=False
    )
    
    return render_template('produits/liste.html', produits=produits, search=search, search_type=search_type)

@app.route('/produits/nouveau', methods=['GET', 'POST'])
def nouveau_produit():
    if request.method == 'POST':
        try:
            produit = Produit(
                produit_id=request.form['PRODUIT'].upper(),
                groupe=request.form.get('groupe', '').upper(),
                famille=request.form.get('famille', '').upper(),
                substitut=request.form.get('substitut', '').upper(),
                description_fr=request.form.get('description_fr', ''),
                description_en=request.form.get('description_en', ''),
                barcode=request.form.get('barcode', '').upper(),
                motclef1=request.form.get('motclef1', '').upper(),
                motclef2=request.form.get('motclef2', '').upper(),
                type_produit=request.form.get('type_produit', '').upper(),
                categorie=request.form.get('categorie', '').upper(),
                remarques1=request.form.get('remarques1', '').upper(),
                remarques2=request.form.get('remarques2', '').upper(),
                
                # Gestion
                inventorie=request.form.get('inventorie', 'N'),
                actif=request.form.get('actif', 'O'),
                discontinue=request.form.get('discontinue', 'N'),
                escomptable=request.form.get('escomptable', 'O'),
                etiquettes=request.form.get('etiquettes', 'O'),
                gestion_serie=request.form.get('gestion_serie', 'N'),
                gestion_lot=request.form.get('gestion_lot', 'N'),
                
                # Taxes
                tvp=request.form.get('tvp', 'O'),
                tvf=request.form.get('tvf', 'O'),
                taux_taxe_fed=request.form.get('taux_taxe_fed', ''),
                
                # Postes comptables
                poste_vente_can=request.form.get('poste_vente_can', '').upper(),
                poste_vente_us=request.form.get('poste_vente_us', '').upper(),
                poste_achat_can=request.form.get('poste_achat_can', '').upper(),
                poste_achat_us=request.form.get('poste_achat_us', '').upper(),
                
                # Localisation
                localisation=request.form.get('localisation', '').upper(),
                
                # Coûts
                cout_reference=float(request.form.get('cout_reference', 0) or 0),
                cout_tvf=float(request.form.get('cout_tvf', 0) or 0),
                prix_revient=float(request.form.get('prix_revient', 0) or 0),
                
                # Stocks
                point_commande=float(request.form.get('point_commande', 0) or 0),
                minimum_commander=float(request.form.get('minimum_commander', 0) or 0),
                maximum_inventaire=float(request.form.get('maximum_inventaire', 0) or 0),
                
                # Calculs
                mode_calcul=request.form.get('mode_calcul', ''),
                formule=request.form.get('formule', '').upper(),
                maj_auto=request.form.get('maj_auto', 'N'),
                
                # Core
                produit_core=request.form.get('produit_core', '').upper(),
                groupe_core=request.form.get('groupe_core', '').upper(),
                g_core=request.form.get('g_core', '').upper(),
                core_valeur=float(request.form.get('core_valeur', 0) or 0),
                core_escalade=float(request.form.get('core_escalade', 0) or 0),
                marge=float(request.form.get('marge', 0) or 0),
                
                # Evaluation
                evaluation=request.form.get('evaluation', '').upper()
            )
            
            # Gestion de l'image
            if 'image' in request.files:
                file = request.files['image']
                if file and file.filename:
                    filename = secure_filename(file.filename)
                    filename = f"{produit.produit_id}_{filename}"
                    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                    os.makedirs(os.path.dirname(file_path), exist_ok=True)
                    file.save(file_path)
                    produit.image_path = filename
            
            db.session.add(produit)
            db.session.commit()
            
            flash('Produit créé avec succès!', 'success')
            return redirect(url_for('modifier_produit', id=produit.id))
            
        except Exception as e:
            db.session.rollback()
            flash(f'Erreur lors de la création: {str(e)}', 'error')
    
    return render_template('produits/formulaire.html', produit=None)

@app.route('/produits/<int:id>')
def voir_produit(id):
    produit = Produit.query.get_or_404(id)
    # Charger les quantités INVEN pour ce produit
    quantites = Inven.query.filter_by(produit_id=produit.produit_id).all()

    # Charger la fiche technique INPTECK (si existe)
    inpteck = Inpteck.query.filter_by(produit_id=produit.produit_id).first()

    # Charger les infos web PRODUITWEB (si existe)
    produitweb = ProduitWeb.query.filter_by(produit_id=produit.produit_id).first()

    # Valeurs Apogee (à adapter selon votre logique métier)
    # Ici, exemple: on suppose que les valeurs sont dans le modèle Produit ou à calculer
    categorie_apogee = produit.liencate if hasattr(produit, 'liencate') else ''
    caracteristique_apogee = produit.liencpro if hasattr(produit, 'liencpro') else ''
    type_apogee = produit.type if hasattr(produit, 'type') else ''

    return render_template(
        'produits/detail.html',
        produit=produit,
        quantites=quantites,
        inpteck=inpteck,
        produitweb=produitweb,
        categorie_apogee=categorie_apogee,
        caracteristique_apogee=caracteristique_apogee,
        type_apogee=type_apogee
    )

@app.route('/produits/<int:id>/modifier', methods=['GET', 'POST'])
def modifier_produit(id):
    produit = Produit.query.get_or_404(id)
    
    if request.method == 'POST':
        try:
            # Mise à jour des champs
            produit.produit_id = request.form['PRODUIT'].upper()
            produit.groupe = request.form.get('groupe', '').upper()
            produit.famille = request.form.get('format', '').upper()
            produit.substitut = request.form.get('substitut', '').upper()
            produit.description_fr = request.form.get('description_fr', '')
            produit.description_en = request.form.get('description_en', '')
            produit.barcode = request.form.get('barcode', '').upper()
            produit.motclef1 = request.form.get('motclef1', '').upper()
            produit.motclef2 = request.form.get('motclef2', '').upper()
            produit.type_produit = request.form.get('type_produit', '').upper()
            produit.categorie = request.form.get('categorie', '').upper()
            produit.remarques1 = request.form.get('remarques1', '').upper()
            produit.remarques2 = request.form.get('remarques2', '').upper()
            
            # Gestion
            produit.inventorie = request.form.get('inventorie', 'N')
            produit.actif = request.form.get('actif', 'O')
            produit.discontinue = request.form.get('discontinue', 'N')
            produit.escomptable = request.form.get('escomptable', 'O')
            produit.etiquettes = request.form.get('etiquettes', 'O')
            produit.gestion_serie = request.form.get('gestion_serie', 'N')
            produit.gestion_lot = request.form.get('gestion_lot', 'N')
            
            # Taxes
            produit.tvp = request.form.get('tvp', 'O')
            produit.tvf = request.form.get('tvf', 'O')
            produit.taux_taxe_fed = request.form.get('taux_taxe_fed', '')
            
            # Postes comptables
            produit.poste_vente_can = request.form.get('poste_vente_can', '').upper()
            produit.poste_vente_us = request.form.get('poste_vente_us', '').upper()
            produit.poste_achat_can = request.form.get('poste_achat_can', '').upper()
            produit.poste_achat_us = request.form.get('poste_achat_us', '').upper()
            
            # Localisation
            produit.localisation = request.form.get('localisation', '').upper()
            produit.famille = request.form.get('famille', '').upper()
            
            # Coûts
            produit.cout_reference = float(request.form.get('cout_reference', 0) or 0)
            produit.cout_tvf = float(request.form.get('cout_tvf', 0) or 0)
            produit.prix_revient = float(request.form.get('prix_revient', 0) or 0)
            
            # Stocks
            produit.point_commande = float(request.form.get('point_commande', 0) or 0)
            produit.minimum_commander = float(request.form.get('minimum_commander', 0) or 0)
            produit.maximum_inventaire = float(request.form.get('maximum_inventaire', 0) or 0)
            
            # Calculs
            produit.mode_calcul = request.form.get('mode_calcul', '')
            produit.formule = request.form.get('formule', '').upper()
            produit.maj_auto = request.form.get('maj_auto', 'N')
            
            # Core
            produit.produit_core = request.form.get('produit_core', '').upper()
            produit.groupe_core = request.form.get('groupe_core', '').upper()
            produit.g_core = request.form.get('g_core', '').upper()
            produit.core_valeur = float(request.form.get('core_valeur', 0) or 0)
            produit.core_escalade = float(request.form.get('core_escalade', 0) or 0)
            produit.marge = float(request.form.get('marge', 0) or 0)
            
            # Evaluation
            produit.evaluation = request.form.get('evaluation', '').upper()
            
            # Gestion de l'image
            if 'image' in request.files:
                file = request.files['image']
                if file and file.filename:
                    filename = secure_filename(file.filename)
                    filename = f"{produit.produit_id}_{filename}"
                    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                    os.makedirs(os.path.dirname(file_path), exist_ok=True)
                    file.save(file_path)
                    produit.image_path = filename
            
            db.session.commit()
            flash('Produit modifié avec succès!', 'success')
            
        except Exception as e:
            db.session.rollback()
            flash(f'Erreur lors de la modification: {str(e)}', 'error')
    
    return render_template('produits/formulaire.html', produit=produit)

@app.route('/produits/<int:id>/supprimer', methods=['POST'])
def supprimer_produit(id):
    produit = Produit.query.get_or_404(id)
    try:
        # Supprimer l'image si elle existe
        if produit.image_path:
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], produit.image_path)
            if os.path.exists(image_path):
                os.remove(image_path)
        
        db.session.delete(produit)
        db.session.commit()
        flash('Produit supprimé avec succès!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Erreur lors de la suppression: {str(e)}', 'error')
    
    return redirect(url_for('liste_produits'))

@app.route('/recherche_type')
def recherche_type():
    # Correction : le JS envoie type=PCS, code=PR, donc il faut inverser l'usage
    code_param = request.args.get('code')  # ex: PR, FZ, TY, CP (pour table type)
    type_value = request.args.get('type')
    if type_value is None or str(type_value).lower() == 'none':
        query = ''
    else:
        query = type_value
    # Pour le mapping, il faut retrouver le type métier (groupe, famille, etc.) à partir du code_param
    # On fait l'inverse du mapping JS
    code_to_type = {'PR': 'groupe', 'FZ': 'famille', 'TY': 'type', 'CP': 'categorie'}
    type_ref = code_to_type.get(code_param, code_param)
    print(f"Recherche type: {type_ref}, code: {code_param}, query: {query}")
    # Mapping type -> table/colonne
    # Pour groupe, famille, type, categorie : table 'type' (MySQL), sinon fallback legacy
    # Utiliser le modèle TypeRef défini en dehors de la fonction (évite l'erreur SQLAlchemy)

    mapping = {
        'groupe':   {'model': TypeRef, 'type_value': 'groupe',   'label': 'Groupe'},
        'famille':  {'model': TypeRef, 'type_value': 'famille',  'label': 'Famille'},
        'type':     {'model': TypeRef, 'type_value': 'type',     'label': 'Type'},
        'categorie':{'model': TypeRef, 'type_value': 'categorie','label': 'Catégorie'},
        'entrepot': {'model': Inven,   'col': Inven.entrepot,    'label': 'Entrepôt'},
        # Ajoutez d'autres mappings selon vos besoins
    }
    if type_ref not in mapping:
        return jsonify({'colonnes': [], 'resultats': []})
    conf = mapping[type_ref]
    # Recherche dans la table 'type' pour les référentiels principaux
    if 'type_value' in conf:
        # Si code_param fourni, on filtre sur CODE=code_param, sinon on filtre sur TYPE=type_value
        q = conf['model'].query
        if code_param:
            q = q.filter(conf['model'].code == code_param)
        else:
            q = q.filter(conf['model'].type == conf['type_value'])
        if query:
            q = q.filter(
                (conf['model'].type.ilike(f"%{query}%")) |
                (conf['model'].desct.ilike(f"%{query}%")) |
                (conf['model'].descta.ilike(f"%{query}%"))
            )
        q = q.order_by(conf['model'].type)
        resultats = []
        for r in q.limit(30):
            code = r.type if r.type is not None else ''
            libelle = r.desct if r.desct is not None else (r.descta if r.descta is not None else (r.code if r.code is not None else ''))
            resultats.append({'code': code, 'libelle': libelle})
        return jsonify(resultats)
    # Fallback legacy (ex: entrepot)
    else:
        col = conf['col']
        label = conf['label']
        model = conf['model']
        q = model.query
        if query:
            q = q.filter(col.ilike(f"%{query}%"))
        q = q.with_entities(col).distinct().order_by(col)
        resultats = []
        for r in q.limit(30):
            val = getattr(r, col.key)
            val = val if val is not None else ''
            resultats.append({'code': val, 'libelle': val})
        return jsonify(resultats)

@app.route('/recherche_type/ajouter', methods=['POST'])
def ajouter_recherche_type():
    data = request.get_json()
    code_param = data.get('code')
    type_value = data.get('type')
    libelle = data.get('libelle')
    # On déduit le type métier
    code_to_type = {'PR': 'groupe', 'FZ': 'famille', 'TY': 'type', 'CP': 'categorie'}
    type_ref = code_to_type.get(code_param, code_param)
    if not code_param or not type_value or not libelle:
        return jsonify({'error': 'Champs manquants'}), 400
    # Vérifier unicité
    exist = TypeRef.query.filter_by(code=code_param, type=type_value).first()
    if exist:
        return jsonify({'error': 'Déjà existant'}), 409
    # Créer
    nouvel = TypeRef(code=code_param, type=type_value, desct=libelle)
    db.session.add(nouvel)
    db.session.commit()
    return jsonify({'success': True})

@app.route('/recherche_type/modifier', methods=['PUT'])
def modifier_recherche_type():
    data = request.get_json()
    code_param = data.get('code')
    type_value = data.get('type')
    libelle = data.get('libelle')
    code_to_type = {'PR': 'groupe', 'FZ': 'famille', 'TY': 'type', 'CP': 'categorie'}
    type_ref = code_to_type.get(code_param, code_param)
    if not code_param or not type_value or not libelle:
        return jsonify({'error': 'Champs manquants'}), 400
    ref = TypeRef.query.filter_by(code=code_param, type=type_value).first()
    if not ref:
        return jsonify({'error': 'Introuvable'}), 404
    ref.desct = libelle
    db.session.commit()
    return jsonify({'success': True})

@app.route('/recherche_type/supprimer', methods=['DELETE'])
def supprimer_recherche_type():
    data = request.get_json()
    code_param = data.get('code')
    type_value = data.get('type')
    code_to_type = {'PR': 'groupe', 'FZ': 'famille', 'TY': 'type', 'CP': 'categorie'}
    type_ref = code_to_type.get(code_param, code_param)
    if not code_param or not type_value:
        return jsonify({'error': 'Champs manquants'}), 400
    ref = TypeRef.query.filter_by(code=code_param, type=type_value).first()
    if not ref:
        return jsonify({'error': 'Introuvable'}), 404
    db.session.delete(ref)
    db.session.commit()
    return jsonify({'success': True})

@app.route('/produits/<int:id>/maj_champ', methods=['POST'])
def maj_champ_produit(id):
    print(f"Maj champ produit {id}")
    data = request.get_json()
    champ = data.get('champ')
    valeur = data.get('valeur')
    if valeur is None:
        valeur = ''
    table = data.get('table')
    champ_sql = data.get('champ_sql')
    print(f"Champ à mettre à jour: {champ}, valeur: {valeur}, table: {table}, champ_sql: {champ_sql}")

    # Sécurité : listes blanches
    from sqlalchemy import text
    tables_autorisees = {'inprix': 'INPRIX'}
    champs_sql_autorises = {
        'inprix': ['TYPE', 'FAMILLE', 'TYPEP', 'CATP', 'FORMAT', 'SUBSTITUT', 'REMARQUES1', 'REMARQUES2', 'LOCALISATION',
                   'MOTCLE1', 'MOTCLE2', 'POSTC', 'POSTU', 'POSTCA', 'POSTUA', 'PRODCORE', 'GRPCORE', 'GCORE']
    }
    # Si table et champ_sql sont fournis, on fait une requête SQL générique
    if table and champ_sql:
        table = table.lower()
        champ_sql = champ_sql.upper()
        if table not in tables_autorisees or champ_sql not in champs_sql_autorises.get(table, []):
            return jsonify({'success': False, 'error': 'Table ou champ SQL non autorisé'}), 403
        try:
            if valeur is None:
                valeur = ''
            sql = text(f"UPDATE {tables_autorisees[table]} SET {champ_sql} = :valeur WHERE ID = :id")
            print(f"Exécution SQL: {sql} avec valeur={valeur}, id={id}")
            db.session.execute(sql, {"valeur": valeur, "id": id})
            db.session.commit()
            return jsonify({'success': True})
        except Exception as e:
            db.session.rollback()
            print(f"Erreur SQL: {e}")
            return jsonify({'success': False, 'error': str(e)}), 500

    # Sinon, fallback sur le comportement ORM classique
    if not champ:
        return jsonify({'success': False, 'error': 'Champ manquant'}), 400
    produit = Produit.query.get(id)
    if not produit:
        return jsonify({'success': False, 'error': 'Produit introuvable'}), 404
    champs_autorises = [
        'groupe', 'famille', 'type_produit', 'categorie', 'entrepot',
        'format', 'substitut', 'remarques1', 'remarques2', 'localisation',
        'motclef1', 'motclef2', 'poste_vente_can', 'poste_vente_us',
        'poste_achat_can', 'poste_achat_us', 'produit_core', 'groupe_core', 'g_core'
    ]
    if champ not in champs_autorises:
        return jsonify({'success': False, 'error': 'Champ non autorisé'}), 403
    try:
        if valeur is None:
            valeur = ''
        setattr(produit, champ, valeur)
        db.session.commit()
        return jsonify({'success': True})
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'success': False, 'error': str(e)}), 500
    
# Routes additionnelles pour navigation
@app.route('/vehicules')
def redirect_to_vehicules():
    """Redirection vers la liste des véhicules"""
    return redirect(url_for('vehicules.liste_vehicules'))

@app.route('/vehicules/nouveau')
def redirect_to_nouveau_vehicule():
    """Redirection vers nouveau véhicule"""
    return redirect(url_for('vehicules.nouveau_vehicule'))

# Alias pour compatibilité des URLs - définies comme fonctions
@app.route('/nouveau_vehicule')
def alias_nouveau_vehicule():
    return redirect(url_for('vehicules.nouveau_vehicule'))

@app.route('/voir_vehicule/<int:id>')
def alias_voir_vehicule(id):
    return redirect(url_for('vehicules.voir_vehicule', id=id))

@app.route('/modifier_vehicule/<int:id>')
def alias_modifier_vehicule(id):
    return redirect(url_for('vehicules.modifier_vehicule', id=id))

@app.route('/desactiver_vehicule/<int:id>')
def alias_desactiver_vehicule(id):
    return redirect(url_for('vehicules.desactiver_vehicule', id=id))

@app.route('/dupliquer_vehicule/<int:id>')
def alias_dupliquer_vehicule(id):
    return redirect(url_for('vehicules.dupliquer_vehicule', id=id))

# Contexte global pour les templates - fournit les statistiques au footer
@app.context_processor
def inject_global_stats():
    """Fournit les statistiques globales à tous les templates"""
    try:
        # Import des modèles depuis les modules
        from clients_routes import get_client_model
        from vehicules_routes import get_vehicule_model
        
        # Récupération des modèles
        Client = get_client_model() if get_client_model else None
        Vehicule = get_vehicule_model() if get_vehicule_model else None
        
        # Calcul des statistiques
        stats_globales = {
            'clients_actifs': 0,
            'produits_stock': 0,
            'vehicules_dispo': 0,
            'derniere_maj': datetime.now().strftime('%d/%m %H:%M')
        }
        
        # Stats clients
        if Client:
            try:
                stats_globales['clients_actifs'] = Client.query.filter_by(statut='actif').count()
            except:
                stats_globales['clients_actifs'] = Client.query.count() if hasattr(Client, 'query') else 0
        
        # Stats produits
        try:
            stats_globales['produits_stock'] = ProduitWeb.query.count()
        except:
            stats_globales['produits_stock'] = 0
        
        # Stats véhicules
        if Vehicule:
            try:
                stats_globales['vehicules_dispo'] = Vehicule.query.filter_by(statut='disponible').count()
            except:
                stats_globales['vehicules_dispo'] = Vehicule.query.count() if hasattr(Vehicule, 'query') else 0
        
        return {
            'stats_globales': stats_globales,
            'config': app.config,
            'moment': datetime  # Pour utiliser les fonctions de date dans les templates
        }
    except Exception as e:
        # En cas d'erreur, retourner des valeurs par défaut
        return {
            'stats_globales': {
                'clients_actifs': 0,
                'produits_stock': 0,
                'vehicules_dispo': 0,
                'derniere_maj': datetime.now().strftime('%d/%m %H:%M')
            },
            'config': app.config,
            'moment': datetime
        }

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        # Initialisation du module véhicules après création des tables
        init_vehicules_module()
        # Initialisation du module clients après création des tables
        init_clients_module()
        # Initialisation du module documents après création des tables
        init_documents_module()
    app.run(debug=True)
