"""
Modèles SQLAlchemy pour les tables de documents commerciaux
Basé sur la structure MySQL existante (ui.md)
"""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, date

def init_documents_models(db):
    """Initialise les modèles de documents avec la base de données"""
    
    # ================================
    # TABLES D'EN-TÊTES (HEADERS)
    # ================================
    
    class QuoteteBase(db.Model):
        """Modèle de base pour les soumissions (QUOTETE)"""
        __abstract__ = True
        
        id = db.Column(db.Integer, primary_key=True, autoincrement=True)
        STAT = db.Column(db.String(1))  # Statut
        NOCLI = db.Column(db.String(7))  # Code client
        NOCLIL = db.Column(db.String(7))  # Code client livraison
        NOM = db.Column(db.String(80))  # Nom client facturation
        NOML = db.Column(db.String(80))  # Nom client livraison
        ADR1 = db.Column(db.String(60))  # Adresse 1 facturation
        ADR2 = db.Column(db.String(60))  # Adresse 2 facturation
        ADR1L = db.Column(db.String(60))  # Adresse 1 livraison
        ADR2L = db.Column(db.String(60))  # Adresse 2 livraison
        VILLE = db.Column(db.String(60))  # Ville facturation
        VILLEL = db.Column(db.String(30))  # Ville livraison
        PROV = db.Column(db.String(3))  # Province facturation
        PROVL = db.Column(db.String(3))  # Province livraison
        CP1 = db.Column(db.String(15))  # Code postal facturation
        CP1L = db.Column(db.String(15))  # Code postal livraison
        TELCON = db.Column(db.String(20))  # Téléphone contact
        TPHONECIE = db.Column(db.String(20))  # Téléphone compagnie
        FAXCIE = db.Column(db.String(20))  # Fax compagnie
        DATEC = db.Column(db.String(10))  # Date création
        DATEL = db.Column(db.String(10))  # Date livraison
        VENDEUR = db.Column(db.String(15))  # Code vendeur
        COMIS = db.Column(db.String(15))  # Commission
        DEPOT = db.Column(db.String(10))  # Dépôt/Magasin
        TERMES = db.Column(db.String(15))  # Termes de paiement
        TRANS = db.Column(db.String(10))  # Transporteur
        TOTAL = db.Column(db.String(12))  # Total avant taxes
        TAXE = db.Column(db.String(11))  # Montant TPS
        TAXEF = db.Column(db.String(11))  # Montant TVQ
        ESC = db.Column(db.String(8))  # Escompte %
        COUTT = db.Column(db.String(10))  # Coût total
        POIDT = db.Column(db.String(8))  # Poids total
        COLLECT = db.Column(db.String(1))  # Collecte (O/N)
        BO = db.Column(db.String(1))  # Back order autorisé
        IMP = db.Column(db.String(1))  # Déjà imprimé
        FICHE = db.Column(db.String(5))  # Numéro de fiche
        NOACHAT = db.Column(db.String(30))  # Numéro bon d'achat client
        REMD = db.Column(db.String(62))  # Remarques/Notes
        DIV = db.Column(db.String(10))  # Division
        FIN = db.Column(db.String(8))  # Financement
    
    class Quotete(QuoteteBase):
        """Soumissions standard (QUOTETE)"""
        __tablename__ = 'quotete'
        NOSOUM = db.Column(db.String(15), unique=True)  # Numéro soumission
    
    class Quotetewo(QuoteteBase):
        """Soumissions bons de travail (QUOTETEWO)"""
        __tablename__ = 'quotetewo'
        NOSOUM = db.Column(db.String(15), unique=True)
        
    class Quoteteve(QuoteteBase):
        """Soumissions contrats de vente (QUOTETEVE)"""
        __tablename__ = 'quoteteve'
        NOSOUM = db.Column(db.String(15), unique=True)
        
    class Quotetelo(QuoteteBase):
        """Soumissions location (QUOTETELO)"""
        __tablename__ = 'quotetelo'
        NOSOUM = db.Column(db.String(15), unique=True)
    
    # ================================
    # TABLES DE COMMANDES
    # ================================
    
    class CoteteBase(db.Model):
        """Modèle de base pour les commandes (COTETE)"""
        __abstract__ = True
        
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
    
    class Cotete(CoteteBase):
        """Commandes standard (COTETE)"""
        __tablename__ = 'cotete'
        
    class Cotetewo(CoteteBase):
        """Commandes bons de travail (COTETEWO)"""
        __tablename__ = 'cotetewo'
        
    class Coteteve(CoteteBase):
        """Commandes contrats de vente (COTETEVE)"""
        __tablename__ = 'coteteve'
        
    class Cotetelo(CoteteBase):
        """Commandes location (COTETELO)"""
        __tablename__ = 'cotetelo'
    
    # ================================
    # TABLES DE FACTURES
    # ================================
    
    class FacturBase(db.Model):
        """Modèle de base pour les factures (FACTUR)"""
        __abstract__ = True
        
        id = db.Column(db.Integer, primary_key=True, autoincrement=True)
        ADR1 = db.Column(db.String(60))  # Adresse 1
        ADR1L = db.Column(db.String(60))  # Adresse 1 livraison
        BO = db.Column(db.String(1))  # Back order
        COLLECT = db.Column(db.String(1))  # Collecte
        COUTT = db.Column(db.String(10))  # Coût total
        CP1 = db.Column(db.String(15))  # Code postal
        CP1L = db.Column(db.String(15))  # Code postal livraison
        DATEC = db.Column(db.String(10))  # Date création
        DATEL = db.Column(db.String(10))  # Date livraison
        DEPOT = db.Column(db.String(10))  # Dépôt
        ESC = db.Column(db.String(8))  # Escompte
        FICHE = db.Column(db.String(5))  # Fiche
        FIN = db.Column(db.String(8))  # Financement
        NOCLI = db.Column(db.String(7))  # Code client
        NOCLIL = db.Column(db.String(7))  # Code client livraison
        NOCOM = db.Column(db.String(10))  # Numéro commande
        NOM = db.Column(db.String(80))  # Nom client
        NOML = db.Column(db.String(80))  # Nom client livraison
        PROV = db.Column(db.String(3))  # Province
        PROVL = db.Column(db.String(3))  # Province livraison
        REMD = db.Column(db.String(62))  # Remarques
        TAXE = db.Column(db.String(11))  # Taxe TPS
        TAXEF = db.Column(db.String(11))  # Taxe TVQ
        TELCON = db.Column(db.String(20))  # Téléphone
        TERMES = db.Column(db.String(15))  # Termes
        TOTAL = db.Column(db.String(12))  # Total
        TRANS = db.Column(db.String(10))  # Transport
        VENDEUR = db.Column(db.String(15))  # Vendeur
        VILLE = db.Column(db.String(60))  # Ville
        VILLEL = db.Column(db.String(30))  # Ville livraison
        STAT = db.Column(db.String(1))  # Statut
        COMIS = db.Column(db.String(15))  # Commission
        NOACHAT = db.Column(db.String(30))  # No achat
    
    class Factur(FacturBase):
        """Factures standard (FACTUR)"""
        __tablename__ = 'factur'
        
    class Factwo(FacturBase):
        """Factures bons de travail (FACTURWO)"""
        __tablename__ = 'facturwo'
        
    class Factve(FacturBase):
        """Factures contrats de vente (FACTURVE)"""
        __tablename__ = 'facturve'
        
    class Facturlo(FacturBase):
        """Factures location (FACTURLO)"""
        __tablename__ = 'facturlo'
    
    # ================================
    # TABLES DE LIGNES
    # ================================
    
    class QommaBase(db.Model):
        """Modèle de base pour les lignes de soumission (QOMMA)"""
        __abstract__ = True
        
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
    
    class Qomma(QommaBase):
        """Lignes soumissions standard (QOMMA)"""
        __tablename__ = 'qomma'
        
    class Qommawo(QommaBase):
        """Lignes soumissions bons de travail (QOMMAWO)"""
        __tablename__ = 'qommawo'
        
    class Qommave(QommaBase):
        """Lignes soumissions contrats de vente (QOMMAVE)"""
        __tablename__ = 'qommave'
        
    class Qommalo(QommaBase):
        """Lignes soumissions location (QOMMALO)"""
        __tablename__ = 'qommalo'
    
    # ================================
    # TABLES DE LIGNES DE COMMANDES
    # ================================
    
    class CommaBase(db.Model):
        """Modèle de base pour les lignes de commande (COMMA)"""
        __abstract__ = True
        
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
    
    class Comma(CommaBase):
        """Lignes commandes standard (COMMA)"""
        __tablename__ = 'comma'
        
    class Commawo(CommaBase):
        """Lignes commandes bons de travail (COMMAWO)"""
        __tablename__ = 'commawo'
        
    class Commave(CommaBase):
        """Lignes commandes contrats de vente (COMMAVE)"""
        __tablename__ = 'commave'
        
    class Commalo(CommaBase):
        """Lignes commandes location (COMMALO)"""
        __tablename__ = 'commalo'
    
    # ================================
    # TABLES DE LIGNES DE FACTURES
    # ================================
    
    class LigneBase(db.Model):
        """Modèle de base pour les lignes de facture (LIGNE)"""
        __abstract__ = True
        
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
    
    class Ligne(LigneBase):
        """Lignes factures standard (LIGNE)"""
        __tablename__ = 'ligne'
        
    class Lignewo(LigneBase):
        """Lignes factures bons de travail (LIGNEWO)"""
        __tablename__ = 'lignewo'
        
    class Ligneve(LigneBase):
        """Lignes factures contrats de vente (LIGNEVE)"""
        __tablename__ = 'ligneve'
        
    class Lignelo(LigneBase):
        """Lignes factures location (LIGNELO)"""
        __tablename__ = 'lignelo'
    
    # Retourner tous les modèles dans un dictionnaire
    return {
        # En-têtes soumissions
        'Quotete': Quotete,
        'Quotetewo': Quotetewo,
        'Quoteteve': Quoteteve,
        'Quotetelo': Quotetelo,
        
        # En-têtes commandes
        'Cotete': Cotete,
        'Cotetewo': Cotetewo,
        'Coteteve': Coteteve,
        'Cotetelo': Cotetelo,
        
        # En-têtes factures
        'Factur': Factur,
        'Factwo': Factwo,
        'Factve': Factve,
        'Facturlo': Facturlo,
        
        # Lignes soumissions
        'Qomma': Qomma,
        'Qommawo': Qommawo,
        'Qommave': Qommave,
        'Qommalo': Qommalo,
        
        # Lignes commandes
        'Comma': Comma,
        'Commawo': Commawo,
        'Commave': Commave,
        'Commalo': Commalo,
        
        # Lignes factures
        'Ligne': Ligne,
        'Lignewo': Lignewo,
        'Ligneve': Ligneve,
        'Lignelo': Lignelo
    }
