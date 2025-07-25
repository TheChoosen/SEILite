"""
Modèles SQLAlchemy simplifiés pour les tables de documents existantes
Basé sur la vraie structure MySQL (COTETE, COMMA, LIGNE, QOMMA)
"""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, date

def init_simple_documents_models(db):
    """Initialise les modèles simplifiés avec les vraies tables existantes"""
    
    # ================================
    # TABLE COTETE (Commandes)
    # ================================
    
    class Cotete(db.Model):
        """Commandes standard (COTETE)"""
        __tablename__ = 'cotete'
        
        id = db.Column(db.Integer, primary_key=True, autoincrement=True)
        STAT = db.Column(db.String(1))  # Statut
        COLLECT = db.Column(db.String(1))  # Collecte
        COUTT = db.Column(db.String(10))  # Coût total
        DATEC = db.Column(db.String(10))  # Date création
        DATEL = db.Column(db.String(10))  # Date livraison
        DEPOT = db.Column(db.String(10))  # Dépôt
        ESC = db.Column(db.String(8))  # Escompte
        FICHE = db.Column(db.String(5))  # Fiche
        FIN = db.Column(db.String(8))  # Financement
        IMP = db.Column(db.String(1))  # Imprimé
        NOCLI = db.Column(db.String(7))  # Code client
        NOCLIL = db.Column(db.String(7))  # Code client livraison
        NOCOM = db.Column(db.String(10))  # Numéro commande
        NOM = db.Column(db.String(80))  # Nom client
        NOML = db.Column(db.String(80))  # Nom client livraison
        POIDT = db.Column(db.String(8))  # Poids total
        TAXE = db.Column(db.String(11))  # Taxe TPS
        TAXEF = db.Column(db.String(11))  # Taxe TVQ
        TERMES = db.Column(db.String(15))  # Termes
        TOTAL = db.Column(db.String(12))  # Total
        TRANS = db.Column(db.String(10))  # Transport
        VENDEUR = db.Column(db.String(15))  # Vendeur
        ADR1 = db.Column(db.String(60))  # Adresse 1
        ADR1L = db.Column(db.String(60))  # Adresse 1 livraison
        CP1 = db.Column(db.String(15))  # Code postal
        CP1L = db.Column(db.String(15))  # Code postal livraison
        PROV = db.Column(db.String(3))  # Province
        PROVL = db.Column(db.String(3))  # Province livraison
        TELCON = db.Column(db.String(20))  # Téléphone
        TPHONECIE = db.Column(db.String(20))  # Téléphone cie
        VILLE = db.Column(db.String(60))  # Ville
        VILLEL = db.Column(db.String(30))  # Ville livraison
        FAXCIE = db.Column(db.String(20))  # Fax
        REMD = db.Column(db.String(62))  # Remarques
        NOACHAT = db.Column(db.String(30))  # No achat
        COMIS = db.Column(db.String(15))  # Commission
        BO = db.Column(db.String(1))  # Back order
        DIV = db.Column(db.String(10))  # Division
        ADR2 = db.Column(db.String(60))  # Adresse 2
        ADR2L = db.Column(db.String(60))  # Adresse 2 livraison
    
    # ================================
    # TABLE QOMMA (Lignes Soumissions)
    # ================================
    
    class Qomma(db.Model):
        """Lignes soumissions standard (QOMMA)"""
        __tablename__ = 'qomma'
        
        id = db.Column(db.Integer, primary_key=True, autoincrement=True)
        CODE = db.Column(db.String(30))  # Code produit
        COUT = db.Column(db.String(10))  # Coût
        DEPT = db.Column(db.String(2))  # Département
        DESC = db.Column(db.String(60))  # Description
        DIV2 = db.Column(db.String(12))  # Division 2
        ESC = db.Column(db.String(8))  # Escompte
        FICHE = db.Column(db.String(5))  # Fiche
        FOURN = db.Column(db.String(7))  # Fournisseur
        MONTANT = db.Column(db.String(13))  # Montant
        MULT2 = db.Column(db.String(12))  # Multiplicateur
        NOCLI = db.Column(db.String(7))  # Code client
        NOCOM = db.Column(db.String(10))  # Numéro document
        PAR = db.Column(db.String(20))  # Paramètre
        POSTVTE = db.Column(db.String(2))  # Post vente
        QUANT = db.Column(db.String(8))  # Quantité
        QUANTL = db.Column(db.String(7))  # Quantité livrée
        STATUS = db.Column(db.String(1))  # Statut
        TAUX = db.Column(db.String(8))  # Taux/Prix
        TAXEFE = db.Column(db.String(11))  # Taxe TVQ
        TAXEPR = db.Column(db.String(11))  # Taxe TPS
        TAXFF = db.Column(db.String(1))  # Taxable TVQ
        TAXPP = db.Column(db.String(1))  # Taxable TPS
        TYPE = db.Column(db.String(15))  # Type
        UMX = db.Column(db.String(1))  # Unité mesure étendue
        UNIT = db.Column(db.String(10))  # Unité
        LOC1 = db.Column(db.String(10))  # Localisation
        DATEL = db.Column(db.String(10))  # Date livraison
        IMPK = db.Column(db.String(1))  # Impression spéciale
        SP = db.Column(db.String(1))  # Spécial
    
    # ================================
    # TABLE COMMA (Lignes Commandes)
    # ================================
    
    class Comma(db.Model):
        """Lignes commandes standard (COMMA)"""
        __tablename__ = 'comma'
        
        id = db.Column(db.Integer, primary_key=True, autoincrement=True)
        CODE = db.Column(db.String(30))  # Code produit
        COUT = db.Column(db.String(10))  # Coût
        DATEC = db.Column(db.String(10))  # Date création
        DATEL = db.Column(db.String(10))  # Date livraison
        DEPT = db.Column(db.String(2))  # Département
        DESC = db.Column(db.String(60))  # Description
        DIV2 = db.Column(db.String(12))  # Division 2
        ESC = db.Column(db.String(8))  # Escompte
        FICHE = db.Column(db.String(5))  # Fiche
        FOURN = db.Column(db.String(7))  # Fournisseur
        LOC1 = db.Column(db.String(10))  # Localisation
        MONTANT = db.Column(db.String(13))  # Montant
        MULT2 = db.Column(db.String(12))  # Multiplicateur
        NOCLI = db.Column(db.String(7))  # Code client
        NOCOM = db.Column(db.String(10))  # Numéro commande
        PAQ_BTE = db.Column(db.String(9))  # Paquet/Boîte
        PAR = db.Column(db.String(20))  # Paramètre
        POID = db.Column(db.String(10))  # Poids
        POIDV = db.Column(db.String(9))  # Poids volumétrique
        POSTVTE = db.Column(db.String(2))  # Post vente
        QUANT = db.Column(db.String(8))  # Quantité
        QUANTL = db.Column(db.String(7))  # Quantité livrée
        STATUS = db.Column(db.String(1))  # Statut
        TAUX = db.Column(db.String(8))  # Taux/Prix
        TAXEFE = db.Column(db.String(11))  # Taxe TVQ
        TAXEPR = db.Column(db.String(11))  # Taxe TPS
        TAXFF = db.Column(db.String(1))  # Taxable TVQ
        TAXPP = db.Column(db.String(1))  # Taxable TPS
        TYPE = db.Column(db.String(15))  # Type
        UMX = db.Column(db.String(1))  # Unité mesure étendue
        UNIT = db.Column(db.String(10))  # Unité
        IMPK = db.Column(db.String(1))  # Impression spéciale
        REF = db.Column(db.String(10))  # Référence
        VENDEUR = db.Column(db.String(15))  # Vendeur
        OUICORE = db.Column(db.String(1))  # Oui core
        FLAGETIQ = db.Column(db.String(1))  # Flag étiquette
        DERNQTEETI = db.Column(db.String(7))  # Dernière quantité étiquetée
        SP = db.Column(db.String(1))  # Spécial
    
    # ================================
    # TABLE LIGNE (Lignes Factures)
    # ================================
    
    class Ligne(db.Model):
        """Lignes factures standard (LIGNE)"""
        __tablename__ = 'ligne'
        
        id = db.Column(db.Integer, primary_key=True, autoincrement=True)
        ADATE = db.Column(db.String(10))  # Date A
        BO = db.Column(db.String(1))  # Back order
        CODE = db.Column(db.String(30))  # Code produit
        COUT = db.Column(db.String(10))  # Coût
        DEPT = db.Column(db.String(2))  # Département
        DESC = db.Column(db.String(60))  # Description
        DIV2 = db.Column(db.String(12))  # Division 2
        ESC = db.Column(db.String(8))  # Escompte
        IMPK = db.Column(db.String(1))  # Impression spéciale
        LOC1 = db.Column(db.String(10))  # Localisation
        MONTANT = db.Column(db.String(13))  # Montant
        MULT2 = db.Column(db.String(12))  # Multiplicateur
        NOCLI = db.Column(db.String(7))  # Code client
        NOF = db.Column(db.String(10))  # Numéro F
        NOFACT = db.Column(db.String(10))  # Numéro facture
        PAR = db.Column(db.String(20))  # Paramètre
        PRIX1 = db.Column(db.String(10))  # Prix 1
        QCOM = db.Column(db.String(8))  # Quantité commandée
        QUANT = db.Column(db.String(8))  # Quantité
        TAUX = db.Column(db.String(8))  # Taux/Prix
        TAXEFE = db.Column(db.String(11))  # Taxe TVQ
        TAXEPR = db.Column(db.String(11))  # Taxe TPS
        TYPE = db.Column(db.String(15))  # Type
        UM = db.Column(db.String(3))  # Unité mesure
        UMX = db.Column(db.String(1))  # Unité mesure étendue
        UNIT = db.Column(db.String(10))  # Unité
        VENDEUR = db.Column(db.String(15))  # Vendeur
        COM = db.Column(db.String(1))  # Commission
        COUTL = db.Column(db.String(10))  # Coût L
        COUTM = db.Column(db.String(10))  # Coût M
        COUTP = db.Column(db.String(10))  # Coût P
        MLOC = db.Column(db.String(1))  # M localisation
        OUICORE = db.Column(db.String(1))  # Oui core
        PAQ_BTE = db.Column(db.String(9))  # Paquet/Boîte
        PRIXSP = db.Column(db.String(1))  # Prix spécial
        TAXF = db.Column(db.String(9))  # Tax F
        TAXP = db.Column(db.String(9))  # Tax P
        VALIPOID = db.Column(db.String(1))  # Validation poids
        OFF = db.Column(db.String(8))  # Off
        POID = db.Column(db.String(10))  # Poids
        CHECK = db.Column(db.String(1))  # Check
        CTAUX = db.Column(db.String(5))  # C taux
        DATEC = db.Column(db.String(10))  # Date création
        DATEL = db.Column(db.String(10))  # Date livraison
        DROP = db.Column(db.String(1))  # Drop
        EFF = db.Column(db.String(1))  # Effectué
        QLOC1 = db.Column(db.String(8))  # Quantité localisation 1
        QLOC2 = db.Column(db.String(8))  # Quantité localisation 2
        QLOC3 = db.Column(db.String(8))  # Quantité localisation 3
        QLOC4 = db.Column(db.String(8))  # Quantité localisation 4
        CODEORIG = db.Column(db.String(30))  # Code original
        KLG = db.Column(db.String(1))  # KLG
        PRIX2 = db.Column(db.String(10))  # Prix 2
        PRIX3 = db.Column(db.String(10))  # Prix 3
        TER = db.Column(db.String(15))  # Territoire
    
    # Retourner tous les modèles dans un dictionnaire
    return {
        'Cotete': Cotete,
        'Qomma': Qomma,
        'Comma': Comma,
        'Ligne': Ligne
    }
