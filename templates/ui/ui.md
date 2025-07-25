les modules ce declenche en etant a la fin du type de module. le module s'identifie par deux lettre XX commme un suffixe : commande pieces en a aucun , wo : bon de travail, ve : contrat de vente, lo : location

PRD Gestions des facture soumission : Schema Mysql bdm, Table entete des commandes : qoteteXX, Table ligne de l'entete : 
qommawo
quotetewo

qomma
quotete

QOMMA

# Field, Type, Null, Key, Default, Extra
id, int, NO, PRI, , auto_increment
CODE, varchar(30), YES, , , 
COUT, varchar(10), YES, , , 
DEPT, varchar(2), YES, , , 
DESC, varchar(60), YES, , , 
DIV2, varchar(12), YES, , , 
ESC, varchar(8), YES, , , 
FICHE, varchar(5), YES, , , 
FOURN, varchar(7), YES, , , 
MONTANT, varchar(13), YES, , , 
MULT2, varchar(12), YES, , , 
NOCLI, varchar(7), YES, , , 
NOCOM, varchar(10), YES, , , 
PAR, varchar(20), YES, , , 
POSTVTE, varchar(2), YES, , , 
QUANT, varchar(8), YES, , , 
QUANTL, varchar(7), YES, , , 
STATUS, varchar(1), YES, , , 
TAUX, varchar(8), YES, , , 
TAXEFE, varchar(11), YES, , , 
TAXEPR, varchar(11), YES, , , 
TAXFF, varchar(1), YES, , , 
TAXPP, varchar(1), YES, , , 
TYPE, varchar(15), YES, , , 
UMX, varchar(1), YES, , , 
UNIT, varchar(10), YES, , , 
LOC1, varchar(10), YES, , , 
DATEL, varchar(10), YES, , , 
IMPK, varchar(1), YES, , , 
SP, varchar(1), YES, , , 



PRD Gestions des commandes clients : Schema Mysql bdm, Table entete des commandes : coteteXX, Table ligne de l'entete : commalo
cottelo

commawo
cotetewo

commave
coteteve

comma
cotete

COTETE
id	int	NO	PRI		auto_increment
STAT	varchar(1)	YES			
COLLECT	varchar(1)	YES			
COUTT	varchar(10)	YES			
DATEC	varchar(10)	YES			
DATEL	varchar(10)	YES			
DEPOT	varchar(10)	YES			
ESC	varchar(8)	YES			
FICHE	varchar(5)	YES			
FIN	varchar(8)	YES			
IMP	varchar(1)	YES			
NOCLI	varchar(7)	YES			
NOCLIL	varchar(7)	YES			
NOCOM	varchar(10)	YES			
NOM	varchar(80)	YES			
NOML	varchar(80)	YES			
POIDT	varchar(8)	YES			
TAXE	varchar(11)	YES			
TAXEF	varchar(11)	YES			
TERMES	varchar(15)	YES			
TOTAL	varchar(12)	YES			
TRANS	varchar(10)	YES			
VENDEUR	varchar(15)	YES			
ADR1	varchar(60)	YES			
ADR1L	varchar(60)	YES			
CP1	varchar(15)	YES			
CP1L	varchar(15)	YES			
PROV	varchar(3)	YES			
PROVL	varchar(3)	YES			
TELCON	varchar(20)	YES			
TPHONECIE	varchar(20)	YES			
VILLE	varchar(60)	YES			
VILLEL	varchar(30)	YES			
FAXCIE	varchar(20)	YES			
REMD	varchar(62)	YES			
NOACHAT	varchar(30)	YES			
COMIS	varchar(15)	YES			
BO	varchar(1)	YES			
DIV	varchar(10)	YES			
ADR2	varchar(60)	YES			
ADR2L	varchar(60)	YES			

COMMA
id	int	NO	PRI		auto_increment
CODE	varchar(30)	YES			
COUT	varchar(10)	YES			
DATEC	varchar(10)	YES			
DATEL	varchar(10)	YES			
DEPT	varchar(2)	YES			
DESC	varchar(60)	YES			
DIV2	varchar(12)	YES			
ESC	varchar(8)	YES			
FICHE	varchar(5)	YES			
FOURN	varchar(7)	YES			
LOC1	varchar(10)	YES			
MONTANT	varchar(13)	YES			
MULT2	varchar(12)	YES			
NOCLI	varchar(7)	YES			
NOCOM	varchar(10)	YES			
PAQ_BTE	varchar(9)	YES			
PAR	varchar(20)	YES			
POID	varchar(10)	YES			
POIDV	varchar(9)	YES			
POSTVTE	varchar(2)	YES			
QUANT	varchar(8)	YES			
QUANTL	varchar(7)	YES			
STATUS	varchar(1)	YES			
TAUX	varchar(8)	YES			
TAXEFE	varchar(11)	YES			
TAXEPR	varchar(11)	YES			
TAXFF	varchar(1)	YES			
TAXPP	varchar(1)	YES			
TYPE	varchar(15)	YES			
UMX	varchar(1)	YES			
UNIT	varchar(10)	YES			
IMPK	varchar(1)	YES			
REF	varchar(10)	YES			
VENDEUR	varchar(15)	YES			
OUICORE	varchar(1)	YES			
FLAGETIQ	varchar(1)	YES			
DERNQTEETI	varchar(7)	YES			
SP	varchar(1)	YES			

PRD Gestions des facture clients : Schema Mysql bdm, Table entete des commandes : coteteXX, Table ligne de l'entete : f
factlo
lignelo

factwo
lignewo

factve
ligneve

factur
ligne

FACTUR
# Field, Type, Null, Key, Default, Extra
id, int, NO, PRI, , auto_increment
ADR1, varchar(60), YES, , , 
ADR1L, varchar(60), YES, , , 
BO, varchar(1), YES, , , 
COLLECT, varchar(1), YES, , , 
COUTT, varchar(10), YES, , , 
CP1, varchar(15), YES, , , 
CP1L, varchar(15), YES, , , 
DATEC, varchar(10), YES, , , 
DATEL, varchar(10), YES, , , 
DEPOT, varchar(10), YES, , , 
ESC, varchar(8), YES, , , 
FICHE, varchar(5), YES, , , 
FIN, varchar(8), YES, , , 
NOCLI, varchar(7), YES, , , 
NOCLIL, varchar(7), YES, , , 
NOCOM, varchar(10), YES, , , 
NOM, varchar(80), YES, , , 
NOML, varchar(80), YES, , , 
PROV, varchar(3), YES, , , 
PROVL, varchar(3), YES, , , 
REMD, varchar(62), YES, , , 
TAXE, varchar(11), YES, , , 
TAXEF, varchar(11), YES, , , 
TELCON, varchar(20), YES, , , 
TERMES, varchar(15), YES, , , 
TOTAL, varchar(12), YES, , , 
TRANS, varchar(10), YES, , , 
VENDEUR, varchar(15), YES, , , 
VILLE, varchar(60), YES, , , 
VILLEL, varchar(30), YES, , , 
STAT, varchar(1), YES, , , 
COMIS, varchar(15), YES, , , 
NOACHAT, varchar(30), YES, , , 


LIGNE
# Field, Type, Null, Key, Default, Extra
id, int, NO, PRI, , auto_increment
ADATE, varchar(10), YES, , , 
BO, varchar(1), YES, , , 
CODE, varchar(30), YES, , , 
COUT, varchar(10), YES, , , 
DEPT, varchar(2), YES, , , 
DESC, varchar(60), YES, , , 
DIV2, varchar(12), YES, , , 
ESC, varchar(8), YES, , , 
IMPK, varchar(1), YES, , , 
LOC1, varchar(10), YES, , , 
MONTANT, varchar(13), YES, , , 
MULT2, varchar(12), YES, , , 
NOCLI, varchar(7), YES, , , 
NOF, varchar(10), YES, , , 
NOFACT, varchar(10), YES, , , 
PAR, varchar(20), YES, , , 
PRIX1, varchar(10), YES, , , 
QCOM, varchar(8), YES, , , 
QUANT, varchar(8), YES, , , 
TAUX, varchar(8), YES, , , 
TAXEFE, varchar(11), YES, , , 
TAXEPR, varchar(11), YES, , , 
TYPE, varchar(15), YES, , , 
UM, varchar(3), YES, , , 
UMX, varchar(1), YES, , , 
UNIT, varchar(10), YES, , , 
VENDEUR, varchar(15), YES, , , 
COM, varchar(1), YES, , , 
COUTL, varchar(10), YES, , , 
COUTM, varchar(10), YES, , , 
COUTP, varchar(10), YES, , , 
MLOC, varchar(1), YES, , , 
OUICORE, varchar(1), YES, , , 
PAQ_BTE, varchar(9), YES, , , 
PRIXSP, varchar(1), YES, , , 
TAXF, varchar(9), YES, , , 
TAXP, varchar(9), YES, , , 
VALIPOID, varchar(1), YES, , , 
OFF, varchar(8), YES, , , 
POID, varchar(10), YES, , , 
CHECK, varchar(1), YES, , , 
CTAUX, varchar(5), YES, , , 
DATEC, varchar(10), YES, , , 
DATEL, varchar(10), YES, , , 
DROP, varchar(1), YES, , , 
EFF, varchar(1), YES, , , 
QLOC1, varchar(8), YES, , , 
QLOC2, varchar(8), YES, , , 
QLOC3, varchar(8), YES, , , 
QLOC4, varchar(8), YES, , , 
CODEORIG, varchar(30), YES, , , 
KLG, varchar(1), YES, , , 
PRIX2, varchar(10), YES, , , 
PRIX3, varchar(10), YES, , , 
TER, varchar(15), YES, , , 



FACTURE
# Field, Type, Null, Key, Default, Extra
id, int, NO, PRI, , auto_increment
ADATE, varchar(10), YES, , , 
ADR1, varchar(60), YES, , , 
ADR1L, varchar(60), YES, , , 
CODEMAG, varchar(3), YES, , , 
COLLECT, varchar(1), YES, , , 
COMIS, varchar(15), YES, , , 
COMMIS, varchar(15), YES, , , 
COUT, varchar(10), YES, , , 
CP1, varchar(15), YES, , , 
CP1L, varchar(15), YES, , , 
CTAUX, varchar(5), YES, , , 
DATEC, varchar(10), YES, , , 
DATEL, varchar(10), YES, , , 
DEPOT, varchar(10), YES, , , 
DIV, varchar(10), YES, , , 
ESC1, varchar(10), YES, , , 
F2, varchar(1), YES, , , 
FIN, varchar(8), YES, , , 
FL1, varchar(1), YES, , , 
FL3, varchar(1), YES, , , 
FLAG, varchar(1), YES, , , 
GT1, varchar(30), YES, , , 
GT10, varchar(30), YES, , , 
GT2, varchar(30), YES, , , 
GT3, varchar(30), YES, , , 
GT4, varchar(30), YES, , , 
GT5, varchar(30), YES, , , 
GT6, varchar(30), YES, , , 
GT7, varchar(30), YES, , , 
GT8, varchar(30), YES, , , 
GT9, varchar(30), YES, , , 
GTCA, varchar(30), YES, , , 
GTCR, varchar(12), YES, , , 
MET1, varchar(2), YES, , , 
METH, varchar(2), YES, , , 
MON, varchar(4), YES, , , 
NOCLI, varchar(7), YES, , , 
NOCLIL, varchar(7), YES, , , 
NOFACT, varchar(10), YES, , , 
NOM, varchar(80), YES, , , 
NOML, varchar(80), YES, , , 
PAR, varchar(20), YES, , , 
POSTV, varchar(3), YES, , , 
POUR, varchar(5), YES, , , 
PROV, varchar(3), YES, , , 
PROVL, varchar(3), YES, , , 
RETOUR, varchar(10), YES, , , 
STAT, varchar(1), YES, , , 
T1, varchar(11), YES, , , 
T10, varchar(11), YES, , , 
T11, varchar(11), YES, , , 
T2, varchar(11), YES, , , 
T3, varchar(11), YES, , , 
T4, varchar(11), YES, , , 
T5, varchar(11), YES, , , 
T6, varchar(11), YES, , , 
T7, varchar(11), YES, , , 
T8, varchar(11), YES, , , 
T9, varchar(11), YES, , , 
TAXE, varchar(11), YES, , , 
TAXEF, varchar(11), YES, , , 
TERME, varchar(2), YES, , , 
TERMES, varchar(15), YES, , , 
TOTAL, varchar(12), YES, , , 
TRANS, varchar(10), YES, , , 
TXF, varchar(10), YES, , , 
VENDEUR, varchar(15), YES, , , 
VILLE, varchar(60), YES, , , 
VILLEL, varchar(60), YES, , , 
EXPEDIE, varchar(15), YES, , , 
NOCLIF, varchar(7), YES, , , 
NOCOM, varchar(10), YES, , , 
PAYS, varchar(50), YES, , , 
PAYSL, varchar(40), YES, , , 
NOTAXPRO, varchar(20), YES, , , 
EXP, varchar(5), YES, , , 
NOACHAT, varchar(30), YES, , , 
CAT, varchar(30), YES, , , 
TER, varchar(15), YES, , , 
ADR2, varchar(60), YES, , , 
ADR2L, varchar(60), YES, , , 
NOTAXFED, varchar(20), YES, , , 
MET2, varchar(2), YES, , , 
TELCON, varchar(20), YES, , , 
HEURE, varchar(8), YES, , , 
CARTE, varchar(20), YES, , , 
ESTIME, varchar(8), YES, , , 
MET3, varchar(2), YES, , , 
MET4, varchar(2), YES, , , 


<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()> _
Partial Class FrmPieceCommande
    Inherits System.Windows.Forms.Form

    'Form overrides dispose to clean up the component list.
    <System.Diagnostics.DebuggerNonUserCode()> _
    Protected Overrides Sub Dispose(ByVal disposing As Boolean)
        If disposing AndAlso components IsNot Nothing Then
            components.Dispose()
        End If
        MyBase.Dispose(disposing)
    End Sub

    'Required by the Windows Form Designer
    Private components As System.ComponentModel.IContainer

    'NOTE: The following procedure is required by the Windows Form Designer
    'It can be modified using the Windows Form Designer.  
    'Do not modify it using the code editor.
    <System.Diagnostics.DebuggerStepThrough()> _
    Private Sub InitializeComponent()
        Me.components = New System.ComponentModel.Container()
        Dim TabTotal_TabPage1 As System.Windows.Forms.TabPage
        Dim resources As System.ComponentModel.ComponentResourceManager = New System.ComponentModel.ComponentResourceManager(GetType(FrmPieceCommande))
        Me.TxtLocat = New System.Windows.Forms.TextBox()
        Me.lblLocat = New System.Windows.Forms.Label()
        Me.TxtDispo = New System.Windows.Forms.TextBox()
        Me.LblDisponible = New System.Windows.Forms.Label()
        Me.LblQuantite = New System.Windows.Forms.Label()
        Me.LblQmain = New System.Windows.Forms.Label()
        Me.LblQcom = New System.Windows.Forms.Label()
        Me.LblEncom = New System.Windows.Forms.Label()
        Me.LblAttendu = New System.Windows.Forms.Label()
        Me.LblProduitTab = New System.Windows.Forms.Label()
        Me.TxtCat = New System.Windows.Forms.TextBox()
        Me.TxtQmain = New System.Windows.Forms.TextBox()
        Me.TxtQcom = New System.Windows.Forms.TextBox()
        Me.TxtEncom = New System.Windows.Forms.TextBox()
        Me.TxtAttendu = New System.Windows.Forms.TextBox()
        Me.TxtPrix5 = New System.Windows.Forms.TextBox()
        Me.TxtPrix4 = New System.Windows.Forms.TextBox()
        Me.TxtPrix3 = New System.Windows.Forms.TextBox()
        Me.TxtPrix2 = New System.Windows.Forms.TextBox()
        Me.TxtPrix1 = New System.Windows.Forms.TextBox()
        Me.TxtPar1 = New System.Windows.Forms.TextBox()
        Me.Shape6 = New System.Windows.Forms.Label()
        Me.Shape7 = New System.Windows.Forms.Label()
        Me.BTmodifier = New System.Windows.Forms.ToolStripButton()
        Me.BTnouveau = New System.Windows.Forms.ToolStripButton()
        Me.bindingNavigatorCountItem = New System.Windows.Forms.ToolStripLabel()
        Me.ToolStripSeparator2 = New System.Windows.Forms.ToolStripSeparator()
        Me.BTannule = New System.Windows.Forms.ToolStripButton()
        Me.BindingNavigator1 = New System.Windows.Forms.BindingNavigator(Me.components)
        Me.BTeffacer = New System.Windows.Forms.ToolStripButton()
        Me.BTsauve = New System.Windows.Forms.ToolStripButton()
        Me.ToolStripSeparator4 = New System.Windows.Forms.ToolStripSeparator()
        Me.BTimprime = New System.Windows.Forms.ToolStripButton()
        Me.Btenvoieoutlook = New System.Windows.Forms.ToolStripButton()
        Me.bindingNavigatorSeparator2 = New System.Windows.Forms.ToolStripSeparator()
        Me.BTdebut = New System.Windows.Forms.ToolStripButton()
        Me.BTprecedent = New System.Windows.Forms.ToolStripButton()
        Me.bindingNavigatorSeparator = New System.Windows.Forms.ToolStripSeparator()
        Me.bindingNavigatorPositionItem = New System.Windows.Forms.ToolStripTextBox()
        Me.bindingNavigatorSeparator1 = New System.Windows.Forms.ToolStripSeparator()
        Me.BTprochain = New System.Windows.Forms.ToolStripButton()
        Me.BTfin = New System.Windows.Forms.ToolStripButton()
        Me.ToolStripSeparator3 = New System.Windows.Forms.ToolStripSeparator()
        Me.BTaide = New System.Windows.Forms.ToolStripButton()
        Me.toolStripSeparator = New System.Windows.Forms.ToolStripSeparator()
        Me.toolStripSeparator1 = New System.Windows.Forms.ToolStripSeparator()
        Me.ToolStripLabel1 = New System.Windows.Forms.ToolStripLabel()
        Me.Tclientliv = New System.Windows.Forms.TextBox()
        Me.Tcommis = New System.Windows.Forms.TextBox()
        Me.Tclient = New System.Windows.Forms.TextBox()
        Me.Ddateouverture = New System.Windows.Forms.DateTimePicker()
        Me.Label2 = New System.Windows.Forms.Label()
        Me.Ddaterequis = New System.Windows.Forms.DateTimePicker()
        Me.Tajoutdepot = New System.Windows.Forms.TextBox()
        Me.Label21 = New System.Windows.Forms.Label()
        Me.Ttransport = New System.Windows.Forms.TextBox()
        Me.Label22 = New System.Windows.Forms.Label()
        Me.Ttotal = New System.Windows.Forms.TextBox()
        Me.Ttps = New System.Windows.Forms.TextBox()
        Me.Ttvq = New System.Windows.Forms.TextBox()
        Me.Tnocom = New System.Windows.Forms.TextBox()
        Me.Tgtotal = New System.Windows.Forms.TextBox()
        Me.Label25 = New System.Windows.Forms.Label()
        Me.Tdepot = New System.Windows.Forms.TextBox()
        Me.Tentrepot = New System.Windows.Forms.TextBox()
        Me.Label46 = New System.Windows.Forms.Label()
        Me.Label26 = New System.Windows.Forms.Label()
        Me.Label45 = New System.Windows.Forms.Label()
        Me.Tnoachat = New System.Windows.Forms.TextBox()
        Me.Label44 = New System.Windows.Forms.Label()
        Me.Label43 = New System.Windows.Forms.Label()
        Me.Btclientliv = New System.Windows.Forms.Button()
        Me.Button3 = New System.Windows.Forms.Button()
        Me.BCommis = New System.Windows.Forms.Button()
        Me.Bvendeur = New System.Windows.Forms.Button()
        Me.Tnocomrech = New System.Windows.Forms.TextBox()
        Me.Label47 = New System.Windows.Forms.Label()
        Me.Tprovinceliv = New System.Windows.Forms.TextBox()
        Me.lfd = New System.Windows.Forms.Label()
        Me.Tprovince = New System.Windows.Forms.TextBox()
        Me.Tville = New System.Windows.Forms.TextBox()
        Me.Tcodepostal = New System.Windows.Forms.TextBox()
        Me.Ttelephone = New System.Windows.Forms.TextBox()
        Me.Tfax = New System.Windows.Forms.TextBox()
        Me.Tadresse2 = New System.Windows.Forms.TextBox()
        Me.Tadresse1 = New System.Windows.Forms.TextBox()
        Me.Tnom = New System.Windows.Forms.TextBox()
        Me.Label10 = New System.Windows.Forms.Label()
        Me.Label9 = New System.Windows.Forms.Label()
        Me.Label7 = New System.Windows.Forms.Label()
        Me.Label6 = New System.Windows.Forms.Label()
        Me.Label5 = New System.Windows.Forms.Label()
        Me.Label4 = New System.Windows.Forms.Label()
        Me.Button4 = New System.Windows.Forms.Button()
        Me.Label39 = New System.Windows.Forms.Label()
        Me.Label12 = New System.Windows.Forms.Label()
        Me.Label11 = New System.Windows.Forms.Label()
        Me.Tadresse1liv = New System.Windows.Forms.TextBox()
        Me.Tadresse2liv = New System.Windows.Forms.TextBox()
        Me.Tfaxliv = New System.Windows.Forms.TextBox()
        Me.Ttelephoneliv = New System.Windows.Forms.TextBox()
        Me.Tcodepostalliv = New System.Windows.Forms.TextBox()
        Me.Tvilleliv = New System.Windows.Forms.TextBox()
        Me.Label18 = New System.Windows.Forms.Label()
        Me.Label14 = New System.Windows.Forms.Label()
        Me.Label42 = New System.Windows.Forms.Label()
        Me.Label41 = New System.Windows.Forms.Label()
        Me.Label40 = New System.Windows.Forms.Label()
        Me.ToolTip1 = New System.Windows.Forms.ToolTip(Me.components)
        Me.Btnmajdesprix = New System.Windows.Forms.Button()
        Me.Label38 = New System.Windows.Forms.Label()
        Me.Tnomliv = New System.Windows.Forms.TextBox()
        Me.Label17 = New System.Windows.Forms.Label()
        Me.Label15 = New System.Windows.Forms.Label()
        Me.LblVendu = New System.Windows.Forms.Label()
        Me.BRectangleHaut = New System.Windows.Forms.Button()
        Me.TxtTermes = New System.Windows.Forms.TextBox()
        Me.TxtExpediteur = New System.Windows.Forms.TextBox()
        Me.LblStatus = New System.Windows.Forms.Label()
        Me.LblCollect = New System.Windows.Forms.Label()
        Me.Txtstatus = New System.Windows.Forms.TextBox()
        Me.Txtcollect = New System.Windows.Forms.TextBox()
        Me.BRectangleBas = New System.Windows.Forms.Button()
        Me.LblDivers = New System.Windows.Forms.Label()
        Me.TxtDivers = New System.Windows.Forms.TextBox()
        Me.LblEscompte = New System.Windows.Forms.Label()
        Me.TxtEscompte = New System.Windows.Forms.TextBox()
        Me.TabTotal = New System.Windows.Forms.TabControl()
        Me.TabTotal_TabPage2 = New System.Windows.Forms.TabPage()
        Me.TxtA1 = New System.Windows.Forms.TextBox()
        Me.TxtA2 = New System.Windows.Forms.TextBox()
        Me.TxtA3 = New System.Windows.Forms.TextBox()
        Me.TxtA4 = New System.Windows.Forms.TextBox()
        Me.TxtA5 = New System.Windows.Forms.TextBox()
        Me.LblA1 = New System.Windows.Forms.Label()
        Me.LblA2 = New System.Windows.Forms.Label()
        Me.LblA3 = New System.Windows.Forms.Label()
        Me.LblA4 = New System.Windows.Forms.Label()
        Me.LblA5 = New System.Windows.Forms.Label()
        Me.LblAge = New System.Windows.Forms.Label()
        Me.Txtvendeur = New System.Windows.Forms.TextBox()
        Me.Button5 = New System.Windows.Forms.Button()
        Me.Button6 = New System.Windows.Forms.Button()
        Me.bidon = New System.Windows.Forms.TextBox()
        Me.ToolStrip1 = New System.Windows.Forms.ToolStrip()
        Me.BAjout = New System.Windows.Forms.ToolStripButton()
        Me.Binsere = New System.Windows.Forms.ToolStripButton()
        Me.Beffacer = New System.Windows.Forms.ToolStripButton()
        Me.Binfo = New System.Windows.Forms.ToolStripButton()
        Me.BCatalog = New System.Windows.Forms.ToolStripButton()
        Me.Bhistorique = New System.Windows.Forms.ToolStripButton()
        Me.BtnSubstitut = New System.Windows.Forms.ToolStripButton()
        Me.ToolStrip2 = New System.Windows.Forms.ToolStrip()
        Me.BtImpSoum = New System.Windows.Forms.ToolStripButton()
        Me.BtFacture = New System.Windows.Forms.ToolStripButton()
        Me.Bttrieproduit = New System.Windows.Forms.ToolStripButton()
        Me.btnconnaissement = New System.Windows.Forms.ToolStripButton()
        Me.btnroute = New System.Windows.Forms.ToolStripButton()
        Me.ToolStrip3 = New System.Windows.Forms.ToolStrip()
        Me.BtTermes = New System.Windows.Forms.ToolStripButton()
        Me.ToolStrip4 = New System.Windows.Forms.ToolStrip()
        Me.BtVia = New System.Windows.Forms.ToolStripButton()
        Me.ToolStrip5 = New System.Windows.Forms.ToolStrip()
        Me.BClient = New System.Windows.Forms.ToolStripButton()
        Me.TsProfit = New System.Windows.Forms.ToolStrip()
        Me.Bprofit = New System.Windows.Forms.ToolStripButton()
        Me.BtnMultisite = New System.Windows.Forms.ToolStripButton()
        Me.BTFournis = New System.Windows.Forms.ToolStripButton()
        Me.BtCreation = New System.Windows.Forms.ToolStripButton()
        Me.Btnlocalisateurproduit = New System.Windows.Forms.ToolStripButton()
        Me.Btnnapa = New System.Windows.Forms.ToolStripButton()
        Me.Lblroute = New System.Windows.Forms.Label()
        Me.Lblroutedef = New System.Windows.Forms.Label()
        Me.Tstotal = New System.Windows.Forms.TextBox()
        Me.ToolStrip9 = New System.Windows.Forms.ToolStrip()
        Me.BtDepot = New System.Windows.Forms.ToolStripButton()
        Me.LblMag = New System.Windows.Forms.Label()
        Me.Label1 = New System.Windows.Forms.Label()
        Me.lblnbimp = New System.Windows.Forms.Label()
        Me.Btncomfact = New System.Windows.Forms.Button()
        Me.ToolTip2 = New System.Windows.Forms.ToolTip(Me.components)
        Me.PictureBox2 = New System.Windows.Forms.PictureBox()
        Me.Btnbarcodeauto = New System.Windows.Forms.Button()
        Me.Pgrid = New Inventaire.SolGrid()
        Me.SolGrid1 = New Inventaire.SolGrid()
        TabTotal_TabPage1 = New System.Windows.Forms.TabPage()
        TabTotal_TabPage1.SuspendLayout()
        CType(Me.BindingNavigator1, System.ComponentModel.ISupportInitialize).BeginInit()
        Me.BindingNavigator1.SuspendLayout()
        Me.TabTotal.SuspendLayout()
        Me.TabTotal_TabPage2.SuspendLayout()
        Me.ToolStrip1.SuspendLayout()
        Me.ToolStrip2.SuspendLayout()
        Me.ToolStrip3.SuspendLayout()
        Me.ToolStrip4.SuspendLayout()
        Me.ToolStrip5.SuspendLayout()
        Me.TsProfit.SuspendLayout()
        Me.ToolStrip9.SuspendLayout()
        CType(Me.PictureBox2, System.ComponentModel.ISupportInitialize).BeginInit()
        CType(Me.Pgrid, System.ComponentModel.ISupportInitialize).BeginInit()
        CType(Me.SolGrid1, System.ComponentModel.ISupportInitialize).BeginInit()
        Me.SuspendLayout()
        '
        'TabTotal_TabPage1
        '
        TabTotal_TabPage1.Controls.Add(Me.TxtLocat)
        TabTotal_TabPage1.Controls.Add(Me.lblLocat)
        TabTotal_TabPage1.Controls.Add(Me.TxtDispo)
        TabTotal_TabPage1.Controls.Add(Me.LblDisponible)
        TabTotal_TabPage1.Controls.Add(Me.LblQuantite)
        TabTotal_TabPage1.Controls.Add(Me.LblQmain)
        TabTotal_TabPage1.Controls.Add(Me.LblQcom)
        TabTotal_TabPage1.Controls.Add(Me.LblEncom)
        TabTotal_TabPage1.Controls.Add(Me.LblAttendu)
        TabTotal_TabPage1.Controls.Add(Me.LblProduitTab)
        TabTotal_TabPage1.Controls.Add(Me.TxtCat)
        TabTotal_TabPage1.Controls.Add(Me.TxtQmain)
        TabTotal_TabPage1.Controls.Add(Me.TxtQcom)
        TabTotal_TabPage1.Controls.Add(Me.TxtEncom)
        TabTotal_TabPage1.Controls.Add(Me.TxtAttendu)
        TabTotal_TabPage1.Controls.Add(Me.TxtPrix5)
        TabTotal_TabPage1.Controls.Add(Me.TxtPrix4)
        TabTotal_TabPage1.Controls.Add(Me.TxtPrix3)
        TabTotal_TabPage1.Controls.Add(Me.TxtPrix2)
        TabTotal_TabPage1.Controls.Add(Me.TxtPrix1)
        TabTotal_TabPage1.Controls.Add(Me.TxtPar1)
        TabTotal_TabPage1.Controls.Add(Me.Shape6)
        TabTotal_TabPage1.Controls.Add(Me.Shape7)
        TabTotal_TabPage1.Location = New System.Drawing.Point(4, 22)
        TabTotal_TabPage1.Name = "TabTotal_TabPage1"
        TabTotal_TabPage1.Size = New System.Drawing.Size(725, 113)
        TabTotal_TabPage1.TabIndex = 1
        TabTotal_TabPage1.Text = "&2- Produit"
        TabTotal_TabPage1.UseVisualStyleBackColor = True
        '
        'TxtLocat
        '
        Me.TxtLocat.AcceptsReturn = True
        Me.TxtLocat.BackColor = System.Drawing.SystemColors.Window
        Me.TxtLocat.Cursor = System.Windows.Forms.Cursors.IBeam
        Me.TxtLocat.Font = New System.Drawing.Font("Arial", 6.75!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.TxtLocat.ForeColor = System.Drawing.SystemColors.WindowText
        Me.TxtLocat.Location = New System.Drawing.Point(637, 74)
        Me.TxtLocat.MaxLength = 10
        Me.TxtLocat.Name = "TxtLocat"
        Me.TxtLocat.RightToLeft = System.Windows.Forms.RightToLeft.No
        Me.TxtLocat.Size = New System.Drawing.Size(81, 18)
        Me.TxtLocat.TabIndex = 102
        Me.TxtLocat.TabStop = False
        '
        'lblLocat
        '
        Me.lblLocat.AutoSize = True
        Me.lblLocat.Location = New System.Drawing.Point(573, 75)
        Me.lblLocat.Name = "lblLocat"
        Me.lblLocat.Size = New System.Drawing.Size(64, 14)
        Me.lblLocat.TabIndex = 101
        Me.lblLocat.Text = "Localisation"
        '
        'TxtDispo
        '
        Me.TxtDispo.Location = New System.Drawing.Point(510, 72)
        Me.TxtDispo.Name = "TxtDispo"
        Me.TxtDispo.Size = New System.Drawing.Size(49, 20)
        Me.TxtDispo.TabIndex = 92
        '
        'LblDisponible
        '
        Me.LblDisponible.AutoSize = True
        Me.LblDisponible.Location = New System.Drawing.Point(437, 78)
        Me.LblDisponible.Name = "LblDisponible"
        Me.LblDisponible.Size = New System.Drawing.Size(56, 14)
        Me.LblDisponible.TabIndex = 91
        Me.LblDisponible.Text = "Disponible"
        '
        'LblQuantite
        '
        Me.LblQuantite.BackColor = System.Drawing.SystemColors.Control
        Me.LblQuantite.Cursor = System.Windows.Forms.Cursors.Default
        Me.LblQuantite.Font = New System.Drawing.Font("Arial", 8.25!, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.LblQuantite.ForeColor = System.Drawing.SystemColors.ControlText
        Me.LblQuantite.Location = New System.Drawing.Point(471, 9)
        Me.LblQuantite.Name = "LblQuantite"
        Me.LblQuantite.RightToLeft = System.Windows.Forms.RightToLeft.No
        Me.LblQuantite.Size = New System.Drawing.Size(173, 17)
        Me.LblQuantite.TabIndex = 71
        Me.LblQuantite.Text = "Quantités"
        '
        'LblQmain
        '
        Me.LblQmain.BackColor = System.Drawing.SystemColors.Control
        Me.LblQmain.Cursor = System.Windows.Forms.Cursors.Default
        Me.LblQmain.Font = New System.Drawing.Font("Arial", 8.25!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.LblQmain.ForeColor = System.Drawing.SystemColors.ControlText
        Me.LblQmain.Location = New System.Drawing.Point(437, 30)
        Me.LblQmain.Name = "LblQmain"
        Me.LblQmain.RightToLeft = System.Windows.Forms.RightToLeft.No
        Me.LblQmain.Size = New System.Drawing.Size(57, 17)
        Me.LblQmain.TabIndex = 72
        Me.LblQmain.Text = "En main:"
        '
        'LblQcom
        '
        Me.LblQcom.BackColor = System.Drawing.SystemColors.Control
        Me.LblQcom.Cursor = System.Windows.Forms.Cursors.Default
        Me.LblQcom.Font = New System.Drawing.Font("Arial", 8.25!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.LblQcom.ForeColor = System.Drawing.SystemColors.ControlText
        Me.LblQcom.Location = New System.Drawing.Point(437, 52)
        Me.LblQcom.Name = "LblQcom"
        Me.LblQcom.RightToLeft = System.Windows.Forms.RightToLeft.No
        Me.LblQcom.Size = New System.Drawing.Size(67, 17)
        Me.LblQcom.TabIndex = 74
        Me.LblQcom.Text = "Commandée:"
        '
        'LblEncom
        '
        Me.LblEncom.BackColor = System.Drawing.SystemColors.Control
        Me.LblEncom.Cursor = System.Windows.Forms.Cursors.Default
        Me.LblEncom.Font = New System.Drawing.Font("Arial", 8.25!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.LblEncom.ForeColor = System.Drawing.SystemColors.ControlText
        Me.LblEncom.Location = New System.Drawing.Point(573, 30)
        Me.LblEncom.Name = "LblEncom"
        Me.LblEncom.RightToLeft = System.Windows.Forms.RightToLeft.No
        Me.LblEncom.Size = New System.Drawing.Size(90, 17)
        Me.LblEncom.TabIndex = 76
        Me.LblEncom.Text = "En commande:"
        '
        'LblAttendu
        '
        Me.LblAttendu.BackColor = System.Drawing.SystemColors.Control
        Me.LblAttendu.Cursor = System.Windows.Forms.Cursors.Default
        Me.LblAttendu.Font = New System.Drawing.Font("Arial", 8.25!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.LblAttendu.ForeColor = System.Drawing.SystemColors.ControlText
        Me.LblAttendu.Location = New System.Drawing.Point(573, 52)
        Me.LblAttendu.Name = "LblAttendu"
        Me.LblAttendu.RightToLeft = System.Windows.Forms.RightToLeft.No
        Me.LblAttendu.Size = New System.Drawing.Size(73, 17)
        Me.LblAttendu.TabIndex = 80
        Me.LblAttendu.Text = "Dte. Attendue"
        '
        'LblProduitTab
        '
        Me.LblProduitTab.BackColor = System.Drawing.SystemColors.Control
        Me.LblProduitTab.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        Me.LblProduitTab.Cursor = System.Windows.Forms.Cursors.Default
        Me.LblProduitTab.Font = New System.Drawing.Font("Arial", 9.75!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.LblProduitTab.ForeColor = System.Drawing.SystemColors.ControlText
        Me.LblProduitTab.Location = New System.Drawing.Point(24, 44)
        Me.LblProduitTab.Name = "LblProduitTab"
        Me.LblProduitTab.RightToLeft = System.Windows.Forms.RightToLeft.No
        Me.LblProduitTab.Size = New System.Drawing.Size(405, 25)
        Me.LblProduitTab.TabIndex = 90
        Me.LblProduitTab.Text = "  U/ M                Prix(1)      Prix(2)      Prix(3)      Prix(4)       Prix(5" &
    ")    "
        '
        'TxtCat
        '
        Me.TxtCat.AcceptsReturn = True
        Me.TxtCat.BackColor = System.Drawing.SystemColors.Window
        Me.TxtCat.Cursor = System.Windows.Forms.Cursors.IBeam
        Me.TxtCat.Font = New System.Drawing.Font("Arial", 8.25!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.TxtCat.ForeColor = System.Drawing.SystemColors.WindowText
        Me.TxtCat.Location = New System.Drawing.Point(24, 20)
        Me.TxtCat.MaxLength = 30
        Me.TxtCat.Name = "TxtCat"
        Me.TxtCat.RightToLeft = System.Windows.Forms.RightToLeft.No
        Me.TxtCat.Size = New System.Drawing.Size(129, 20)
        Me.TxtCat.TabIndex = 69
        Me.TxtCat.TabStop = False
        '
        'TxtQmain
        '
        Me.TxtQmain.AcceptsReturn = True
        Me.TxtQmain.BackColor = System.Drawing.SystemColors.Window
        Me.TxtQmain.Cursor = System.Windows.Forms.Cursors.IBeam
        Me.TxtQmain.Font = New System.Drawing.Font("Arial", 8.25!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.TxtQmain.ForeColor = System.Drawing.SystemColors.WindowText
        Me.TxtQmain.Location = New System.Drawing.Point(510, 28)
        Me.TxtQmain.MaxLength = 0
        Me.TxtQmain.Name = "TxtQmain"
        Me.TxtQmain.RightToLeft = System.Windows.Forms.RightToLeft.No
        Me.TxtQmain.Size = New System.Drawing.Size(49, 20)
        Me.TxtQmain.TabIndex = 73
        Me.TxtQmain.TabStop = False
        '
        'TxtQcom
        '
        Me.TxtQcom.AcceptsReturn = True
        Me.TxtQcom.BackColor = System.Drawing.SystemColors.Window
        Me.TxtQcom.Cursor = System.Windows.Forms.Cursors.IBeam
        Me.TxtQcom.Font = New System.Drawing.Font("Arial", 8.25!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.TxtQcom.ForeColor = System.Drawing.SystemColors.WindowText
        Me.TxtQcom.Location = New System.Drawing.Point(510, 49)
        Me.TxtQcom.MaxLength = 0
        Me.TxtQcom.Name = "TxtQcom"
        Me.TxtQcom.RightToLeft = System.Windows.Forms.RightToLeft.No
        Me.TxtQcom.Size = New System.Drawing.Size(49, 20)
        Me.TxtQcom.TabIndex = 75
        Me.TxtQcom.TabStop = False
        '
        'TxtEncom
        '
        Me.TxtEncom.AcceptsReturn = True
        Me.TxtEncom.BackColor = System.Drawing.SystemColors.Window
        Me.TxtEncom.Cursor = System.Windows.Forms.Cursors.IBeam
        Me.TxtEncom.Font = New System.Drawing.Font("Arial", 8.25!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.TxtEncom.ForeColor = System.Drawing.SystemColors.WindowText
        Me.TxtEncom.Location = New System.Drawing.Point(669, 27)
        Me.TxtEncom.MaxLength = 0
        Me.TxtEncom.Name = "TxtEncom"
        Me.TxtEncom.RightToLeft = System.Windows.Forms.RightToLeft.No
        Me.TxtEncom.Size = New System.Drawing.Size(49, 20)
        Me.TxtEncom.TabIndex = 77
        Me.TxtEncom.TabStop = False
        '
        'TxtAttendu
        '
        Me.TxtAttendu.AcceptsReturn = True
        Me.TxtAttendu.BackColor = System.Drawing.SystemColors.Window
        Me.TxtAttendu.Cursor = System.Windows.Forms.Cursors.IBeam
        Me.TxtAttendu.Font = New System.Drawing.Font("Arial", 8.25!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.TxtAttendu.ForeColor = System.Drawing.SystemColors.WindowText
        Me.TxtAttendu.Location = New System.Drawing.Point(659, 49)
        Me.TxtAttendu.MaxLength = 10
        Me.TxtAttendu.Name = "TxtAttendu"
        Me.TxtAttendu.RightToLeft = System.Windows.Forms.RightToLeft.No
        Me.TxtAttendu.Size = New System.Drawing.Size(59, 20)
        Me.TxtAttendu.TabIndex = 81
        Me.TxtAttendu.TabStop = False
        '
        'TxtPrix5
        '
        Me.TxtPrix5.AcceptsReturn = True
        Me.TxtPrix5.BackColor = System.Drawing.SystemColors.Window
        Me.TxtPrix5.Cursor = System.Windows.Forms.Cursors.IBeam
        Me.TxtPrix5.Font = New System.Drawing.Font("Arial", 8.25!, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.TxtPrix5.ForeColor = System.Drawing.SystemColors.WindowText
        Me.TxtPrix5.Location = New System.Drawing.Point(364, 72)
        Me.TxtPrix5.MaxLength = 0
        Me.TxtPrix5.Name = "TxtPrix5"
        Me.TxtPrix5.RightToLeft = System.Windows.Forms.RightToLeft.No
        Me.TxtPrix5.Size = New System.Drawing.Size(65, 20)
        Me.TxtPrix5.TabIndex = 84
        Me.TxtPrix5.TabStop = False
        Me.TxtPrix5.Tag = "          X"
        '
        'TxtPrix4
        '
        Me.TxtPrix4.AcceptsReturn = True
        Me.TxtPrix4.BackColor = System.Drawing.SystemColors.Window
        Me.TxtPrix4.Cursor = System.Windows.Forms.Cursors.IBeam
        Me.TxtPrix4.Font = New System.Drawing.Font("Arial", 8.25!, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.TxtPrix4.ForeColor = System.Drawing.SystemColors.WindowText
        Me.TxtPrix4.Location = New System.Drawing.Point(300, 72)
        Me.TxtPrix4.MaxLength = 0
        Me.TxtPrix4.Name = "TxtPrix4"
        Me.TxtPrix4.RightToLeft = System.Windows.Forms.RightToLeft.No
        Me.TxtPrix4.Size = New System.Drawing.Size(65, 20)
        Me.TxtPrix4.TabIndex = 85
        Me.TxtPrix4.TabStop = False
        Me.TxtPrix4.Tag = "          X"
        '
        'TxtPrix3
        '
        Me.TxtPrix3.AcceptsReturn = True
        Me.TxtPrix3.BackColor = System.Drawing.SystemColors.Window
        Me.TxtPrix3.Cursor = System.Windows.Forms.Cursors.IBeam
        Me.TxtPrix3.Font = New System.Drawing.Font("Arial", 8.25!, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.TxtPrix3.ForeColor = System.Drawing.SystemColors.WindowText
        Me.TxtPrix3.Location = New System.Drawing.Point(236, 72)
        Me.TxtPrix3.MaxLength = 0
        Me.TxtPrix3.Name = "TxtPrix3"
        Me.TxtPrix3.RightToLeft = System.Windows.Forms.RightToLeft.No
        Me.TxtPrix3.Size = New System.Drawing.Size(65, 20)
        Me.TxtPrix3.TabIndex = 86
        Me.TxtPrix3.TabStop = False
        Me.TxtPrix3.Tag = "          X"
        '
        'TxtPrix2
        '
        Me.TxtPrix2.AcceptsReturn = True
        Me.TxtPrix2.BackColor = System.Drawing.SystemColors.Window
        Me.TxtPrix2.Cursor = System.Windows.Forms.Cursors.IBeam
        Me.TxtPrix2.Font = New System.Drawing.Font("Arial", 8.25!, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.TxtPrix2.ForeColor = System.Drawing.SystemColors.WindowText
        Me.TxtPrix2.Location = New System.Drawing.Point(172, 72)
        Me.TxtPrix2.MaxLength = 0
        Me.TxtPrix2.Name = "TxtPrix2"
        Me.TxtPrix2.RightToLeft = System.Windows.Forms.RightToLeft.No
        Me.TxtPrix2.Size = New System.Drawing.Size(65, 20)
        Me.TxtPrix2.TabIndex = 87
        Me.TxtPrix2.TabStop = False
        Me.TxtPrix2.Tag = "          X"
        '
        'TxtPrix1
        '
        Me.TxtPrix1.AcceptsReturn = True
        Me.TxtPrix1.BackColor = System.Drawing.SystemColors.Window
        Me.TxtPrix1.Cursor = System.Windows.Forms.Cursors.IBeam
        Me.TxtPrix1.Font = New System.Drawing.Font("Arial", 8.25!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.TxtPrix1.ForeColor = System.Drawing.SystemColors.WindowText
        Me.TxtPrix1.Location = New System.Drawing.Point(108, 72)
        Me.TxtPrix1.MaxLength = 10
        Me.TxtPrix1.Name = "TxtPrix1"
        Me.TxtPrix1.RightToLeft = System.Windows.Forms.RightToLeft.No
        Me.TxtPrix1.Size = New System.Drawing.Size(65, 20)
        Me.TxtPrix1.TabIndex = 88
        Me.TxtPrix1.TabStop = False
        Me.TxtPrix1.Tag = "          X"
        '
        'TxtPar1
        '
        Me.TxtPar1.AcceptsReturn = True
        Me.TxtPar1.BackColor = System.Drawing.SystemColors.Window
        Me.TxtPar1.Cursor = System.Windows.Forms.Cursors.IBeam
        Me.TxtPar1.Font = New System.Drawing.Font("Arial", 8.25!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.TxtPar1.ForeColor = System.Drawing.SystemColors.WindowText
        Me.TxtPar1.Location = New System.Drawing.Point(24, 72)
        Me.TxtPar1.MaxLength = 3
        Me.TxtPar1.Name = "TxtPar1"
        Me.TxtPar1.RightToLeft = System.Windows.Forms.RightToLeft.No
        Me.TxtPar1.Size = New System.Drawing.Size(48, 20)
        Me.TxtPar1.TabIndex = 89
        Me.TxtPar1.TabStop = False
        Me.TxtPar1.Tag = "          X"
        '
        'Shape6
        '
        Me.Shape6.BackColor = System.Drawing.Color.Transparent
        Me.Shape6.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        Me.Shape6.Location = New System.Drawing.Point(435, 20)
        Me.Shape6.Name = "Shape6"
        Me.Shape6.Size = New System.Drawing.Size(287, 84)
        Me.Shape6.TabIndex = 0
        '
        'Shape7
        '
        Me.Shape7.BackColor = System.Drawing.Color.Transparent
        Me.Shape7.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        Me.Shape7.Location = New System.Drawing.Point(7, 8)
        Me.Shape7.Name = "Shape7"
        Me.Shape7.Size = New System.Drawing.Size(737, 97)
        Me.Shape7.TabIndex = 77
        '
        'BTmodifier
        '
        Me.BTmodifier.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image
        Me.BTmodifier.Image = CType(resources.GetObject("BTmodifier.Image"), System.Drawing.Image)
        Me.BTmodifier.ImageTransparentColor = System.Drawing.Color.Magenta
        Me.BTmodifier.Name = "BTmodifier"
        Me.BTmodifier.Size = New System.Drawing.Size(23, 25)
        Me.BTmodifier.Tag = "bouton"
        Me.BTmodifier.Text = "&Open"
        Me.BTmodifier.ToolTipText = "F11- Modifier"
        '
        'BTnouveau
        '
        Me.BTnouveau.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image
        Me.BTnouveau.Image = CType(resources.GetObject("BTnouveau.Image"), System.Drawing.Image)
        Me.BTnouveau.ImageTransparentColor = System.Drawing.Color.Magenta
        Me.BTnouveau.Name = "BTnouveau"
        Me.BTnouveau.Size = New System.Drawing.Size(23, 25)
        Me.BTnouveau.Tag = "bouton"
        Me.BTnouveau.Text = "&New"
        Me.BTnouveau.ToolTipText = "F4- Nouveau"
        '
        'bindingNavigatorCountItem
        '
        Me.bindingNavigatorCountItem.Name = "bindingNavigatorCountItem"
        Me.bindingNavigatorCountItem.Size = New System.Drawing.Size(37, 25)
        Me.bindingNavigatorCountItem.Text = "de {0}"
        Me.bindingNavigatorCountItem.ToolTipText = "Total number of items"
        '
        'ToolStripSeparator2
        '
        Me.ToolStripSeparator2.Name = "ToolStripSeparator2"
        Me.ToolStripSeparator2.Size = New System.Drawing.Size(6, 28)
        '
        'BTannule
        '
        Me.BTannule.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image
        Me.BTannule.Image = CType(resources.GetObject("BTannule.Image"), System.Drawing.Image)
        Me.BTannule.ImageTransparentColor = System.Drawing.Color.Magenta
        Me.BTannule.Name = "BTannule"
        Me.BTannule.Size = New System.Drawing.Size(23, 25)
        Me.BTannule.Tag = "bouton"
        Me.BTannule.Text = "ToolStripButton1"
        Me.BTannule.ToolTipText = "F2- Annuler"
        '
        'BindingNavigator1
        '
        Me.BindingNavigator1.AddNewItem = Nothing
        Me.BindingNavigator1.AutoSize = False
        Me.BindingNavigator1.BackgroundImage = CType(resources.GetObject("BindingNavigator1.BackgroundImage"), System.Drawing.Image)
        Me.BindingNavigator1.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
        Me.BindingNavigator1.CountItem = Me.bindingNavigatorCountItem
        Me.BindingNavigator1.CountItemFormat = "de {0}"
        Me.BindingNavigator1.DeleteItem = Nothing
        Me.BindingNavigator1.GripStyle = System.Windows.Forms.ToolStripGripStyle.Hidden
        Me.BindingNavigator1.Items.AddRange(New System.Windows.Forms.ToolStripItem() {Me.BTnouveau, Me.BTmodifier, Me.ToolStripSeparator2, Me.BTannule, Me.BTeffacer, Me.BTsauve, Me.ToolStripSeparator4, Me.BTimprime, Me.Btenvoieoutlook, Me.bindingNavigatorSeparator2, Me.BTdebut, Me.BTprecedent, Me.bindingNavigatorSeparator, Me.bindingNavigatorPositionItem, Me.bindingNavigatorCountItem, Me.bindingNavigatorSeparator1, Me.BTprochain, Me.BTfin, Me.ToolStripSeparator3, Me.BTaide, Me.toolStripSeparator, Me.toolStripSeparator1, Me.ToolStripLabel1})
        Me.BindingNavigator1.Location = New System.Drawing.Point(0, 0)
        Me.BindingNavigator1.MoveFirstItem = Me.BTdebut
        Me.BindingNavigator1.MoveLastItem = Me.BTfin
        Me.BindingNavigator1.MoveNextItem = Me.BTprochain
        Me.BindingNavigator1.MovePreviousItem = Me.BTprecedent
        Me.BindingNavigator1.Name = "BindingNavigator1"
        Me.BindingNavigator1.PositionItem = Me.bindingNavigatorPositionItem
        Me.BindingNavigator1.Size = New System.Drawing.Size(932, 28)
        Me.BindingNavigator1.TabIndex = 281
        Me.BindingNavigator1.Text = "BindingNavigator1"
        '
        'BTeffacer
        '
        Me.BTeffacer.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image
        Me.BTeffacer.Image = CType(resources.GetObject("BTeffacer.Image"), System.Drawing.Image)
        Me.BTeffacer.Name = "BTeffacer"
        Me.BTeffacer.Size = New System.Drawing.Size(23, 25)
        Me.BTeffacer.Tag = "bouton"
        Me.BTeffacer.Text = "Delete"
        Me.BTeffacer.ToolTipText = "F9- Effacer"
        '
        'BTsauve
        '
        Me.BTsauve.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image
        Me.BTsauve.Image = CType(resources.GetObject("BTsauve.Image"), System.Drawing.Image)
        Me.BTsauve.ImageTransparentColor = System.Drawing.Color.Magenta
        Me.BTsauve.Name = "BTsauve"
        Me.BTsauve.Size = New System.Drawing.Size(23, 25)
        Me.BTsauve.Tag = "bouton"
        Me.BTsauve.Text = "&Save"
        Me.BTsauve.ToolTipText = "F5- Enregistrer"
        '
        'ToolStripSeparator4
        '
        Me.ToolStripSeparator4.Name = "ToolStripSeparator4"
        Me.ToolStripSeparator4.Size = New System.Drawing.Size(6, 28)
        '
        'BTimprime
        '
        Me.BTimprime.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image
        Me.BTimprime.Image = CType(resources.GetObject("BTimprime.Image"), System.Drawing.Image)
        Me.BTimprime.ImageTransparentColor = System.Drawing.Color.Magenta
        Me.BTimprime.Name = "BTimprime"
        Me.BTimprime.Size = New System.Drawing.Size(23, 25)
        Me.BTimprime.Tag = "bouton"
        Me.BTimprime.Text = "&Print"
        Me.BTimprime.ToolTipText = "F12- Imprimer"
        '
        'Btenvoieoutlook
        '
        Me.Btenvoieoutlook.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image
        Me.Btenvoieoutlook.Image = CType(resources.GetObject("Btenvoieoutlook.Image"), System.Drawing.Image)
        Me.Btenvoieoutlook.ImageTransparentColor = System.Drawing.Color.Magenta
        Me.Btenvoieoutlook.Name = "Btenvoieoutlook"
        Me.Btenvoieoutlook.Size = New System.Drawing.Size(23, 25)
        Me.Btenvoieoutlook.Text = "Envoie outlook"
        '
        'bindingNavigatorSeparator2
        '
        Me.bindingNavigatorSeparator2.Name = "bindingNavigatorSeparator2"
        Me.bindingNavigatorSeparator2.Size = New System.Drawing.Size(6, 28)
        '
        'BTdebut
        '
        Me.BTdebut.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image
        Me.BTdebut.Image = CType(resources.GetObject("BTdebut.Image"), System.Drawing.Image)
        Me.BTdebut.Name = "BTdebut"
        Me.BTdebut.Size = New System.Drawing.Size(23, 25)
        Me.BTdebut.Tag = "bouton"
        Me.BTdebut.Text = "Move first"
        '
        'BTprecedent
        '
        Me.BTprecedent.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image
        Me.BTprecedent.Image = CType(resources.GetObject("BTprecedent.Image"), System.Drawing.Image)
        Me.BTprecedent.Name = "BTprecedent"
        Me.BTprecedent.Size = New System.Drawing.Size(23, 25)
        Me.BTprecedent.Tag = "bouton"
        Me.BTprecedent.Text = "Move previous"
        '
        'bindingNavigatorSeparator
        '
        Me.bindingNavigatorSeparator.Name = "bindingNavigatorSeparator"
        Me.bindingNavigatorSeparator.Size = New System.Drawing.Size(6, 28)
        '
        'bindingNavigatorPositionItem
        '
        Me.bindingNavigatorPositionItem.Font = New System.Drawing.Font("Segoe UI", 9.0!)
        Me.bindingNavigatorPositionItem.Name = "bindingNavigatorPositionItem"
        Me.bindingNavigatorPositionItem.Size = New System.Drawing.Size(50, 28)
        Me.bindingNavigatorPositionItem.Text = "0"
        Me.bindingNavigatorPositionItem.ToolTipText = "Current position"
        '
        'bindingNavigatorSeparator1
        '
        Me.bindingNavigatorSeparator1.Name = "bindingNavigatorSeparator1"
        Me.bindingNavigatorSeparator1.Size = New System.Drawing.Size(6, 28)
        '
        'BTprochain
        '
        Me.BTprochain.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image
        Me.BTprochain.Image = CType(resources.GetObject("BTprochain.Image"), System.Drawing.Image)
        Me.BTprochain.Name = "BTprochain"
        Me.BTprochain.Size = New System.Drawing.Size(23, 25)
        Me.BTprochain.Tag = "bouton"
        Me.BTprochain.Text = "Move next"
        '
        'BTfin
        '
        Me.BTfin.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image
        Me.BTfin.Image = CType(resources.GetObject("BTfin.Image"), System.Drawing.Image)
        Me.BTfin.Name = "BTfin"
        Me.BTfin.Size = New System.Drawing.Size(23, 25)
        Me.BTfin.Tag = "bouton"
        Me.BTfin.Text = "Move last"
        '
        'ToolStripSeparator3
        '
        Me.ToolStripSeparator3.Name = "ToolStripSeparator3"
        Me.ToolStripSeparator3.Size = New System.Drawing.Size(6, 28)
        '
        'BTaide
        '
        Me.BTaide.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image
        Me.BTaide.Image = CType(resources.GetObject("BTaide.Image"), System.Drawing.Image)
        Me.BTaide.ImageTransparentColor = System.Drawing.Color.Magenta
        Me.BTaide.Name = "BTaide"
        Me.BTaide.Size = New System.Drawing.Size(23, 25)
        Me.BTaide.Tag = "bouton"
        Me.BTaide.Text = "He&lp"
        '
        'toolStripSeparator
        '
        Me.toolStripSeparator.Name = "toolStripSeparator"
        Me.toolStripSeparator.Size = New System.Drawing.Size(6, 28)
        '
        'toolStripSeparator1
        '
        Me.toolStripSeparator1.Name = "toolStripSeparator1"
        Me.toolStripSeparator1.Size = New System.Drawing.Size(6, 28)
        '
        'ToolStripLabel1
        '
        Me.ToolStripLabel1.Name = "ToolStripLabel1"
        Me.ToolStripLabel1.Size = New System.Drawing.Size(150, 25)
        Me.ToolStripLabel1.Text = "Recherche de commandes:"
        '
        'Tclientliv
        '
        Me.Tclientliv.BackColor = System.Drawing.Color.FromArgb(CType(CType(255, Byte), Integer), CType(CType(255, Byte), Integer), CType(CType(192, Byte), Integer))
        Me.Tclientliv.CharacterCasing = System.Windows.Forms.CharacterCasing.Upper
        Me.Tclientliv.Location = New System.Drawing.Point(536, 32)
        Me.Tclientliv.MaxLength = 7
        Me.Tclientliv.Name = "Tclientliv"
        Me.Tclientliv.Size = New System.Drawing.Size(67, 20)
        Me.Tclientliv.TabIndex = 279
        Me.Tclientliv.Tag = "texte"
        '
        'Tcommis
        '
        Me.Tcommis.BackColor = System.Drawing.Color.FromArgb(CType(CType(255, Byte), Integer), CType(CType(255, Byte), Integer), CType(CType(192, Byte), Integer))
        Me.Tcommis.CharacterCasing = System.Windows.Forms.CharacterCasing.Upper
        Me.Tcommis.Location = New System.Drawing.Point(853, 236)
        Me.Tcommis.MaxLength = 15
        Me.Tcommis.Name = "Tcommis"
        Me.Tcommis.Size = New System.Drawing.Size(67, 20)
        Me.Tcommis.TabIndex = 11
        Me.Tcommis.Tag = "X"
        '
        'Tclient
        '
        Me.Tclient.BackColor = System.Drawing.Color.FromArgb(CType(CType(255, Byte), Integer), CType(CType(255, Byte), Integer), CType(CType(192, Byte), Integer))
        Me.Tclient.CharacterCasing = System.Windows.Forms.CharacterCasing.Upper
        Me.Tclient.Cursor = System.Windows.Forms.Cursors.Hand
        Me.Tclient.Location = New System.Drawing.Point(229, 32)
        Me.Tclient.MaxLength = 7
        Me.Tclient.Name = "Tclient"
        Me.Tclient.Size = New System.Drawing.Size(67, 20)
        Me.Tclient.TabIndex = 0
        Me.Tclient.Tag = "X"
        '
        'Ddateouverture
        '
        Me.Ddateouverture.CustomFormat = "yyyy/MM/dd"
        Me.Ddateouverture.Format = System.Windows.Forms.DateTimePickerFormat.Custom
        Me.Ddateouverture.Location = New System.Drawing.Point(279, 236)
        Me.Ddateouverture.Name = "Ddateouverture"
        Me.Ddateouverture.Size = New System.Drawing.Size(88, 20)
        Me.Ddateouverture.TabIndex = 4
        Me.Ddateouverture.Tag = "texte"
        '
        'Label2
        '
        Me.Label2.AutoSize = True
        Me.Label2.BackColor = System.Drawing.SystemColors.GradientActiveCaption
        Me.Label2.Font = New System.Drawing.Font("Microsoft Sans Serif", 8.25!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.Label2.Location = New System.Drawing.Point(5, 218)
        Me.Label2.Name = "Label2"
        Me.Label2.Size = New System.Drawing.Size(79, 13)
        Me.Label2.TabIndex = 217
        Me.Label2.Text = "No. commande"
        '
        'Ddaterequis
        '
        Me.Ddaterequis.CustomFormat = "yyyy/MM/dd"
        Me.Ddaterequis.Format = System.Windows.Forms.DateTimePickerFormat.Custom
        Me.Ddaterequis.Location = New System.Drawing.Point(386, 236)
        Me.Ddaterequis.Name = "Ddaterequis"
        Me.Ddaterequis.Size = New System.Drawing.Size(88, 20)
        Me.Ddaterequis.TabIndex = 5
        Me.Ddaterequis.Tag = "texte"
        '
        'Tajoutdepot
        '
        Me.Tajoutdepot.BackColor = System.Drawing.SystemColors.Window
        Me.Tajoutdepot.Location = New System.Drawing.Point(439, 492)
        Me.Tajoutdepot.Name = "Tajoutdepot"
        Me.Tajoutdepot.Size = New System.Drawing.Size(67, 20)
        Me.Tajoutdepot.TabIndex = 15
        Me.Tajoutdepot.Tag = "N"
        Me.Tajoutdepot.TextAlign = System.Windows.Forms.HorizontalAlignment.Right
        '
        'Label21
        '
        Me.Label21.AutoSize = True
        Me.Label21.BackColor = System.Drawing.SystemColors.GradientActiveCaption
        Me.Label21.Font = New System.Drawing.Font("Microsoft Sans Serif", 8.25!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.Label21.Location = New System.Drawing.Point(101, 219)
        Me.Label21.Name = "Label21"
        Me.Label21.Size = New System.Drawing.Size(47, 13)
        Me.Label21.TabIndex = 222
        Me.Label21.Text = "Entrepot"
        '
        'Ttransport
        '
        Me.Ttransport.BackColor = System.Drawing.SystemColors.Window
        Me.Ttransport.Location = New System.Drawing.Point(239, 492)
        Me.Ttransport.Name = "Ttransport"
        Me.Ttransport.Size = New System.Drawing.Size(66, 20)
        Me.Ttransport.TabIndex = 14
        Me.Ttransport.Tag = "N"
        Me.Ttransport.TextAlign = System.Windows.Forms.HorizontalAlignment.Right
        '
        'Label22
        '
        Me.Label22.AutoSize = True
        Me.Label22.BackColor = System.Drawing.SystemColors.GradientActiveCaption
        Me.Label22.Font = New System.Drawing.Font("Microsoft Sans Serif", 8.25!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.Label22.Location = New System.Drawing.Point(156, 218)
        Me.Label22.Name = "Label22"
        Me.Label22.Size = New System.Drawing.Size(63, 13)
        Me.Label22.TabIndex = 224
        Me.Label22.Text = "No. d'Achat"
        '
        'Ttotal
        '
        Me.Ttotal.BackColor = System.Drawing.SystemColors.GradientActiveCaption
        Me.Ttotal.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        Me.Ttotal.ForeColor = System.Drawing.Color.Black
        Me.Ttotal.Location = New System.Drawing.Point(807, 571)
        Me.Ttotal.Name = "Ttotal"
        Me.Ttotal.Size = New System.Drawing.Size(100, 20)
        Me.Ttotal.TabIndex = 271
        Me.Ttotal.TabStop = False
        Me.Ttotal.Tag = "texte"
        Me.Ttotal.TextAlign = System.Windows.Forms.HorizontalAlignment.Right
        '
        'Ttps
        '
        Me.Ttps.BackColor = System.Drawing.SystemColors.GradientActiveCaption
        Me.Ttps.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        Me.Ttps.ForeColor = System.Drawing.Color.Black
        Me.Ttps.Location = New System.Drawing.Point(807, 519)
        Me.Ttps.Name = "Ttps"
        Me.Ttps.Size = New System.Drawing.Size(100, 20)
        Me.Ttps.TabIndex = 270
        Me.Ttps.TabStop = False
        Me.Ttps.Tag = "texte"
        Me.Ttps.TextAlign = System.Windows.Forms.HorizontalAlignment.Right
        '
        'Ttvq
        '
        Me.Ttvq.BackColor = System.Drawing.SystemColors.GradientActiveCaption
        Me.Ttvq.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        Me.Ttvq.ForeColor = System.Drawing.Color.Black
        Me.Ttvq.Location = New System.Drawing.Point(807, 545)
        Me.Ttvq.Name = "Ttvq"
        Me.Ttvq.Size = New System.Drawing.Size(100, 20)
        Me.Ttvq.TabIndex = 269
        Me.Ttvq.TabStop = False
        Me.Ttvq.Tag = "texte"
        Me.Ttvq.TextAlign = System.Windows.Forms.HorizontalAlignment.Right
        '
        'Tnocom
        '
        Me.Tnocom.BackColor = System.Drawing.Color.FromArgb(CType(CType(255, Byte), Integer), CType(CType(224, Byte), Integer), CType(CType(192, Byte), Integer))
        Me.Tnocom.CharacterCasing = System.Windows.Forms.CharacterCasing.Upper
        Me.Tnocom.Location = New System.Drawing.Point(7, 235)
        Me.Tnocom.MaxLength = 10
        Me.Tnocom.Name = "Tnocom"
        Me.Tnocom.Size = New System.Drawing.Size(91, 20)
        Me.Tnocom.TabIndex = 1
        Me.Tnocom.Tag = "X"
        Me.Tnocom.TextAlign = System.Windows.Forms.HorizontalAlignment.Right
        '
        'Tgtotal
        '
        Me.Tgtotal.BackColor = System.Drawing.SystemColors.GradientActiveCaption
        Me.Tgtotal.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        Me.Tgtotal.ForeColor = System.Drawing.Color.Black
        Me.Tgtotal.Location = New System.Drawing.Point(807, 627)
        Me.Tgtotal.Name = "Tgtotal"
        Me.Tgtotal.Size = New System.Drawing.Size(100, 20)
        Me.Tgtotal.TabIndex = 268
        Me.Tgtotal.TabStop = False
        Me.Tgtotal.Tag = "texte"
        Me.Tgtotal.TextAlign = System.Windows.Forms.HorizontalAlignment.Right
        '
        'Label25
        '
        Me.Label25.AutoSize = True
        Me.Label25.BackColor = System.Drawing.SystemColors.GradientActiveCaption
        Me.Label25.Font = New System.Drawing.Font("Microsoft Sans Serif", 8.25!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.Label25.Location = New System.Drawing.Point(281, 220)
        Me.Label25.Name = "Label25"
        Me.Label25.Size = New System.Drawing.Size(86, 13)
        Me.Label25.TabIndex = 228
        Me.Label25.Text = "Date d'ouverture"
        '
        'Tdepot
        '
        Me.Tdepot.BackColor = System.Drawing.SystemColors.GradientActiveCaption
        Me.Tdepot.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        Me.Tdepot.ForeColor = System.Drawing.Color.Black
        Me.Tdepot.Location = New System.Drawing.Point(807, 597)
        Me.Tdepot.Name = "Tdepot"
        Me.Tdepot.Size = New System.Drawing.Size(100, 20)
        Me.Tdepot.TabIndex = 267
        Me.Tdepot.Tag = "texte"
        Me.Tdepot.TextAlign = System.Windows.Forms.HorizontalAlignment.Right
        '
        'Tentrepot
        '
        Me.Tentrepot.BackColor = System.Drawing.SystemColors.Window
        Me.Tentrepot.CharacterCasing = System.Windows.Forms.CharacterCasing.Upper
        Me.Tentrepot.Location = New System.Drawing.Point(104, 235)
        Me.Tentrepot.MaxLength = 1000
        Me.Tentrepot.Name = "Tentrepot"
        Me.Tentrepot.RightToLeft = System.Windows.Forms.RightToLeft.No
        Me.Tentrepot.Size = New System.Drawing.Size(39, 20)
        Me.Tentrepot.TabIndex = 2
        Me.Tentrepot.Tag = "X"
        '
        'Label46
        '
        Me.Label46.AutoSize = True
        Me.Label46.BackColor = System.Drawing.Color.Transparent
        Me.Label46.Location = New System.Drawing.Point(739, 573)
        Me.Label46.Name = "Label46"
        Me.Label46.Size = New System.Drawing.Size(31, 13)
        Me.Label46.TabIndex = 266
        Me.Label46.Text = "Total"
        Me.Label46.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        '
        'Label26
        '
        Me.Label26.AutoSize = True
        Me.Label26.BackColor = System.Drawing.SystemColors.GradientActiveCaption
        Me.Label26.Font = New System.Drawing.Font("Microsoft Sans Serif", 8.25!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.Label26.Location = New System.Drawing.Point(391, 220)
        Me.Label26.Name = "Label26"
        Me.Label26.Size = New System.Drawing.Size(66, 13)
        Me.Label26.TabIndex = 230
        Me.Label26.Text = "Date Requis"
        '
        'Label45
        '
        Me.Label45.AutoSize = True
        Me.Label45.BackColor = System.Drawing.Color.Transparent
        Me.Label45.Location = New System.Drawing.Point(739, 599)
        Me.Label45.Name = "Label45"
        Me.Label45.Size = New System.Drawing.Size(36, 13)
        Me.Label45.TabIndex = 265
        Me.Label45.Text = "Depot"
        Me.Label45.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        '
        'Tnoachat
        '
        Me.Tnoachat.BackColor = System.Drawing.SystemColors.Window
        Me.Tnoachat.CharacterCasing = System.Windows.Forms.CharacterCasing.Upper
        Me.Tnoachat.Location = New System.Drawing.Point(149, 236)
        Me.Tnoachat.Name = "Tnoachat"
        Me.Tnoachat.Size = New System.Drawing.Size(115, 20)
        Me.Tnoachat.TabIndex = 3
        Me.Tnoachat.Tag = "X"
        '
        'Label44
        '
        Me.Label44.AutoSize = True
        Me.Label44.BackColor = System.Drawing.SystemColors.GradientActiveCaption
        Me.Label44.Location = New System.Drawing.Point(345, 496)
        Me.Label44.Name = "Label44"
        Me.Label44.Size = New System.Drawing.Size(76, 13)
        Me.Label44.TabIndex = 264
        Me.Label44.Text = "Ajout de dépot"
        '
        'Label43
        '
        Me.Label43.AutoSize = True
        Me.Label43.BackColor = System.Drawing.Color.Transparent
        Me.Label43.Location = New System.Drawing.Point(739, 496)
        Me.Label43.Name = "Label43"
        Me.Label43.Size = New System.Drawing.Size(58, 13)
        Me.Label43.TabIndex = 263
        Me.Label43.Text = "Sous-Total"
        Me.Label43.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        '
        'Btclientliv
        '
        Me.Btclientliv.BackColor = System.Drawing.SystemColors.ControlLightLight
        Me.Btclientliv.BackgroundImage = CType(resources.GetObject("Btclientliv.BackgroundImage"), System.Drawing.Image)
        Me.Btclientliv.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
        Me.Btclientliv.Location = New System.Drawing.Point(465, 33)
        Me.Btclientliv.Name = "Btclientliv"
        Me.Btclientliv.Size = New System.Drawing.Size(67, 19)
        Me.Btclientliv.TabIndex = 302
        Me.Btclientliv.Text = "No. Client"
        Me.Btclientliv.TextAlign = System.Drawing.ContentAlignment.TopCenter
        Me.Btclientliv.UseVisualStyleBackColor = False
        '
        'Button3
        '
        Me.Button3.Enabled = False
        Me.Button3.Location = New System.Drawing.Point(721, 29)
        Me.Button3.Name = "Button3"
        Me.Button3.Size = New System.Drawing.Size(222, 183)
        Me.Button3.TabIndex = 299
        Me.Button3.TabStop = False
        Me.Button3.UseVisualStyleBackColor = True
        '
        'BCommis
        '
        Me.BCommis.BackColor = System.Drawing.SystemColors.ControlLightLight
        Me.BCommis.BackgroundImage = CType(resources.GetObject("BCommis.BackgroundImage"), System.Drawing.Image)
        Me.BCommis.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
        Me.BCommis.Location = New System.Drawing.Point(853, 214)
        Me.BCommis.Name = "BCommis"
        Me.BCommis.Size = New System.Drawing.Size(66, 21)
        Me.BCommis.TabIndex = 294
        Me.BCommis.Text = "Commis"
        Me.BCommis.TextAlign = System.Drawing.ContentAlignment.TopCenter
        Me.BCommis.UseVisualStyleBackColor = False
        '
        'Bvendeur
        '
        Me.Bvendeur.BackColor = System.Drawing.SystemColors.ControlLightLight
        Me.Bvendeur.BackgroundImage = CType(resources.GetObject("Bvendeur.BackgroundImage"), System.Drawing.Image)
        Me.Bvendeur.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
        Me.Bvendeur.Location = New System.Drawing.Point(776, 214)
        Me.Bvendeur.Name = "Bvendeur"
        Me.Bvendeur.Size = New System.Drawing.Size(66, 21)
        Me.Bvendeur.TabIndex = 293
        Me.Bvendeur.Text = "Vendeur"
        Me.Bvendeur.TextAlign = System.Drawing.ContentAlignment.TopCenter
        Me.Bvendeur.UseVisualStyleBackColor = False
        '
        'Tnocomrech
        '
        Me.Tnocomrech.BackColor = System.Drawing.Color.LemonChiffon
        Me.Tnocomrech.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        Me.Tnocomrech.CharacterCasing = System.Windows.Forms.CharacterCasing.Upper
        Me.Tnocomrech.Location = New System.Drawing.Point(569, 4)
        Me.Tnocomrech.MaxLength = 10
        Me.Tnocomrech.Name = "Tnocomrech"
        Me.Tnocomrech.Size = New System.Drawing.Size(118, 20)
        Me.Tnocomrech.TabIndex = 284
        Me.Tnocomrech.Tag = "texte"
        Me.Tnocomrech.TextAlign = System.Windows.Forms.HorizontalAlignment.Right
        '
        'Label47
        '
        Me.Label47.AutoSize = True
        Me.Label47.Font = New System.Drawing.Font("Microsoft Sans Serif", 8.25!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.Label47.Location = New System.Drawing.Point(499, 146)
        Me.Label47.Name = "Label47"
        Me.Label47.Size = New System.Drawing.Size(52, 13)
        Me.Label47.TabIndex = 283
        Me.Label47.Text = "Province "
        '
        'Tprovinceliv
        '
        Me.Tprovinceliv.BackColor = System.Drawing.SystemColors.Window
        Me.Tprovinceliv.CharacterCasing = System.Windows.Forms.CharacterCasing.Upper
        Me.Tprovinceliv.Location = New System.Drawing.Point(559, 143)
        Me.Tprovinceliv.Name = "Tprovinceliv"
        Me.Tprovinceliv.Size = New System.Drawing.Size(44, 20)
        Me.Tprovinceliv.TabIndex = 229
        Me.Tprovinceliv.Tag = "X"
        '
        'lfd
        '
        Me.lfd.AutoSize = True
        Me.lfd.Font = New System.Drawing.Font("Microsoft Sans Serif", 8.25!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.lfd.Location = New System.Drawing.Point(182, 144)
        Me.lfd.Name = "lfd"
        Me.lfd.Size = New System.Drawing.Size(52, 13)
        Me.lfd.TabIndex = 282
        Me.lfd.Text = "Province "
        '
        'Tprovince
        '
        Me.Tprovince.BackColor = System.Drawing.SystemColors.Window
        Me.Tprovince.CharacterCasing = System.Windows.Forms.CharacterCasing.Upper
        Me.Tprovince.Location = New System.Drawing.Point(250, 139)
        Me.Tprovince.Name = "Tprovince"
        Me.Tprovince.Size = New System.Drawing.Size(46, 20)
        Me.Tprovince.TabIndex = 218
        Me.Tprovince.Tag = "X"
        '
        'Tville
        '
        Me.Tville.BackColor = System.Drawing.SystemColors.Window
        Me.Tville.Location = New System.Drawing.Point(71, 118)
        Me.Tville.Name = "Tville"
        Me.Tville.Size = New System.Drawing.Size(225, 20)
        Me.Tville.TabIndex = 215
        Me.Tville.Tag = "X"
        '
        'Tcodepostal
        '
        Me.Tcodepostal.BackColor = System.Drawing.SystemColors.Window
        Me.Tcodepostal.CharacterCasing = System.Windows.Forms.CharacterCasing.Upper
        Me.Tcodepostal.Location = New System.Drawing.Point(71, 139)
        Me.Tcodepostal.Name = "Tcodepostal"
        Me.Tcodepostal.Size = New System.Drawing.Size(100, 20)
        Me.Tcodepostal.TabIndex = 216
        Me.Tcodepostal.Tag = "X"
        '
        'Ttelephone
        '
        Me.Ttelephone.BackColor = System.Drawing.SystemColors.Window
        Me.Ttelephone.CharacterCasing = System.Windows.Forms.CharacterCasing.Upper
        Me.Ttelephone.Location = New System.Drawing.Point(71, 160)
        Me.Ttelephone.Name = "Ttelephone"
        Me.Ttelephone.Size = New System.Drawing.Size(147, 20)
        Me.Ttelephone.TabIndex = 219
        Me.Ttelephone.Tag = "X"
        '
        'Tfax
        '
        Me.Tfax.BackColor = System.Drawing.SystemColors.Window
        Me.Tfax.CharacterCasing = System.Windows.Forms.CharacterCasing.Upper
        Me.Tfax.Location = New System.Drawing.Point(71, 181)
        Me.Tfax.Name = "Tfax"
        Me.Tfax.Size = New System.Drawing.Size(147, 20)
        Me.Tfax.TabIndex = 220
        Me.Tfax.Tag = "X"
        '
        'Tadresse2
        '
        Me.Tadresse2.BackColor = System.Drawing.SystemColors.Window
        Me.Tadresse2.Location = New System.Drawing.Point(71, 97)
        Me.Tadresse2.Name = "Tadresse2"
        Me.Tadresse2.Size = New System.Drawing.Size(225, 20)
        Me.Tadresse2.TabIndex = 214
        Me.Tadresse2.Tag = "X"
        '
        'Tadresse1
        '
        Me.Tadresse1.BackColor = System.Drawing.SystemColors.Window
        Me.Tadresse1.Location = New System.Drawing.Point(71, 76)
        Me.Tadresse1.Name = "Tadresse1"
        Me.Tadresse1.Size = New System.Drawing.Size(225, 20)
        Me.Tadresse1.TabIndex = 213
        Me.Tadresse1.Tag = "X"
        '
        'Tnom
        '
        Me.Tnom.BackColor = System.Drawing.SystemColors.Window
        Me.Tnom.Cursor = System.Windows.Forms.Cursors.Hand
        Me.Tnom.ImeMode = System.Windows.Forms.ImeMode.NoControl
        Me.Tnom.Location = New System.Drawing.Point(71, 55)
        Me.Tnom.Name = "Tnom"
        Me.Tnom.Size = New System.Drawing.Size(225, 20)
        Me.Tnom.TabIndex = 210
        Me.Tnom.Tag = "X"
        '
        'Label10
        '
        Me.Label10.AutoSize = True
        Me.Label10.Font = New System.Drawing.Font("Microsoft Sans Serif", 8.25!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.Label10.Location = New System.Drawing.Point(5, 56)
        Me.Label10.Name = "Label10"
        Me.Label10.Size = New System.Drawing.Size(29, 13)
        Me.Label10.TabIndex = 204
        Me.Label10.Text = "Nom"
        '
        'Label9
        '
        Me.Label9.AutoSize = True
        Me.Label9.Font = New System.Drawing.Font("Microsoft Sans Serif", 8.25!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.Label9.Location = New System.Drawing.Point(5, 78)
        Me.Label9.Name = "Label9"
        Me.Label9.Size = New System.Drawing.Size(48, 13)
        Me.Label9.TabIndex = 202
        Me.Label9.Text = "Adresse "
        '
        'Label7
        '
        Me.Label7.AutoSize = True
        Me.Label7.Font = New System.Drawing.Font("Microsoft Sans Serif", 8.25!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.Label7.Location = New System.Drawing.Point(5, 122)
        Me.Label7.Name = "Label7"
        Me.Label7.Size = New System.Drawing.Size(26, 13)
        Me.Label7.TabIndex = 200
        Me.Label7.Text = "Ville"
        '
        'Label6
        '
        Me.Label6.AutoSize = True
        Me.Label6.Font = New System.Drawing.Font("Microsoft Sans Serif", 8.25!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.Label6.Location = New System.Drawing.Point(5, 144)
        Me.Label6.Name = "Label6"
        Me.Label6.Size = New System.Drawing.Size(64, 13)
        Me.Label6.TabIndex = 198
        Me.Label6.Text = "Code Postal"
        '
        'Label5
        '
        Me.Label5.AutoSize = True
        Me.Label5.Font = New System.Drawing.Font("Microsoft Sans Serif", 8.25!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.Label5.Location = New System.Drawing.Point(4, 165)
        Me.Label5.Name = "Label5"
        Me.Label5.Size = New System.Drawing.Size(58, 13)
        Me.Label5.TabIndex = 195
        Me.Label5.Text = "Téléphone"
        '
        'Label4
        '
        Me.Label4.AutoSize = True
        Me.Label4.Font = New System.Drawing.Font("Microsoft Sans Serif", 8.25!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.Label4.Location = New System.Drawing.Point(5, 188)
        Me.Label4.Name = "Label4"
        Me.Label4.Size = New System.Drawing.Size(24, 13)
        Me.Label4.TabIndex = 193
        Me.Label4.Text = "Fax"
        '
        'Button4
        '
        Me.Button4.BackColor = System.Drawing.SystemColors.GradientActiveCaption
        Me.Button4.Enabled = False
        Me.Button4.FlatStyle = System.Windows.Forms.FlatStyle.Flat
        Me.Button4.Location = New System.Drawing.Point(0, 484)
        Me.Button4.Name = "Button4"
        Me.Button4.Size = New System.Drawing.Size(581, 36)
        Me.Button4.TabIndex = 301
        Me.Button4.TabStop = False
        Me.Button4.UseVisualStyleBackColor = False
        '
        'Label39
        '
        Me.Label39.AutoSize = True
        Me.Label39.BackColor = System.Drawing.SystemColors.GradientActiveCaption
        Me.Label39.Location = New System.Drawing.Point(171, 496)
        Me.Label39.Name = "Label39"
        Me.Label39.Size = New System.Drawing.Size(52, 13)
        Me.Label39.TabIndex = 259
        Me.Label39.Text = "Transport"
        '
        'Label12
        '
        Me.Label12.AutoSize = True
        Me.Label12.Font = New System.Drawing.Font("Microsoft Sans Serif", 8.25!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.Label12.Location = New System.Drawing.Point(319, 79)
        Me.Label12.Name = "Label12"
        Me.Label12.Size = New System.Drawing.Size(45, 13)
        Me.Label12.TabIndex = 256
        Me.Label12.Text = "Adresse"
        '
        'Label11
        '
        Me.Label11.AutoSize = True
        Me.Label11.Font = New System.Drawing.Font("Microsoft Sans Serif", 8.25!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.Label11.Location = New System.Drawing.Point(319, 58)
        Me.Label11.Name = "Label11"
        Me.Label11.Size = New System.Drawing.Size(29, 13)
        Me.Label11.TabIndex = 257
        Me.Label11.Text = "Nom"
        '
        'Tadresse1liv
        '
        Me.Tadresse1liv.BackColor = System.Drawing.SystemColors.Window
        Me.Tadresse1liv.Location = New System.Drawing.Point(385, 79)
        Me.Tadresse1liv.Name = "Tadresse1liv"
        Me.Tadresse1liv.Size = New System.Drawing.Size(218, 20)
        Me.Tadresse1liv.TabIndex = 223
        Me.Tadresse1liv.Tag = "X"
        '
        'Tadresse2liv
        '
        Me.Tadresse2liv.BackColor = System.Drawing.SystemColors.Window
        Me.Tadresse2liv.Location = New System.Drawing.Point(385, 100)
        Me.Tadresse2liv.Name = "Tadresse2liv"
        Me.Tadresse2liv.Size = New System.Drawing.Size(218, 20)
        Me.Tadresse2liv.TabIndex = 225
        Me.Tadresse2liv.Tag = "X"
        '
        'Tfaxliv
        '
        Me.Tfaxliv.BackColor = System.Drawing.SystemColors.Window
        Me.Tfaxliv.CharacterCasing = System.Windows.Forms.CharacterCasing.Upper
        Me.Tfaxliv.Location = New System.Drawing.Point(385, 183)
        Me.Tfaxliv.Name = "Tfaxliv"
        Me.Tfaxliv.Size = New System.Drawing.Size(147, 20)
        Me.Tfaxliv.TabIndex = 232
        Me.Tfaxliv.Tag = "X"
        '
        'Ttelephoneliv
        '
        Me.Ttelephoneliv.BackColor = System.Drawing.SystemColors.Window
        Me.Ttelephoneliv.CharacterCasing = System.Windows.Forms.CharacterCasing.Upper
        Me.Ttelephoneliv.Location = New System.Drawing.Point(385, 162)
        Me.Ttelephoneliv.Name = "Ttelephoneliv"
        Me.Ttelephoneliv.Size = New System.Drawing.Size(147, 20)
        Me.Ttelephoneliv.TabIndex = 231
        Me.Ttelephoneliv.Tag = "X"
        '
        'Tcodepostalliv
        '
        Me.Tcodepostalliv.BackColor = System.Drawing.SystemColors.Window
        Me.Tcodepostalliv.CharacterCasing = System.Windows.Forms.CharacterCasing.Upper
        Me.Tcodepostalliv.Location = New System.Drawing.Point(385, 142)
        Me.Tcodepostalliv.Name = "Tcodepostalliv"
        Me.Tcodepostalliv.Size = New System.Drawing.Size(100, 20)
        Me.Tcodepostalliv.TabIndex = 227
        Me.Tcodepostalliv.Tag = "X"
        '
        'Tvilleliv
        '
        Me.Tvilleliv.BackColor = System.Drawing.SystemColors.Window
        Me.Tvilleliv.Location = New System.Drawing.Point(385, 121)
        Me.Tvilleliv.Name = "Tvilleliv"
        Me.Tvilleliv.Size = New System.Drawing.Size(218, 20)
        Me.Tvilleliv.TabIndex = 226
        Me.Tvilleliv.Tag = "X"
        '
        'Label18
        '
        Me.Label18.AutoSize = True
        Me.Label18.Font = New System.Drawing.Font("Microsoft Sans Serif", 9.75!, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.Label18.Location = New System.Drawing.Point(383, 38)
        Me.Label18.Name = "Label18"
        Me.Label18.Size = New System.Drawing.Size(55, 16)
        Me.Label18.TabIndex = 252
        Me.Label18.Text = "Livré à"
        '
        'Label14
        '
        Me.Label14.AutoSize = True
        Me.Label14.Font = New System.Drawing.Font("Microsoft Sans Serif", 8.25!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.Label14.Location = New System.Drawing.Point(319, 124)
        Me.Label14.Name = "Label14"
        Me.Label14.Size = New System.Drawing.Size(26, 13)
        Me.Label14.TabIndex = 255
        Me.Label14.Text = "Ville"
        '
        'Label42
        '
        Me.Label42.AutoSize = True
        Me.Label42.BackColor = System.Drawing.Color.Transparent
        Me.Label42.Location = New System.Drawing.Point(739, 521)
        Me.Label42.Name = "Label42"
        Me.Label42.Size = New System.Drawing.Size(34, 13)
        Me.Label42.TabIndex = 262
        Me.Label42.Text = "T.P.S"
        Me.Label42.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        '
        'Label41
        '
        Me.Label41.AutoSize = True
        Me.Label41.BackColor = System.Drawing.Color.Transparent
        Me.Label41.Location = New System.Drawing.Point(739, 547)
        Me.Label41.Name = "Label41"
        Me.Label41.Size = New System.Drawing.Size(35, 13)
        Me.Label41.TabIndex = 261
        Me.Label41.Text = "T.V.Q"
        Me.Label41.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        '
        'Label40
        '
        Me.Label40.AutoSize = True
        Me.Label40.BackColor = System.Drawing.Color.Transparent
        Me.Label40.Location = New System.Drawing.Point(739, 629)
        Me.Label40.Name = "Label40"
        Me.Label40.Size = New System.Drawing.Size(34, 13)
        Me.Label40.TabIndex = 260
        Me.Label40.Text = "Solde"
        Me.Label40.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        '
        'Btnmajdesprix
        '
        Me.Btnmajdesprix.BackgroundImage = CType(resources.GetObject("Btnmajdesprix.BackgroundImage"), System.Drawing.Image)
        Me.Btnmajdesprix.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
        Me.Btnmajdesprix.Image = CType(resources.GetObject("Btnmajdesprix.Image"), System.Drawing.Image)
        Me.Btnmajdesprix.Location = New System.Drawing.Point(904, 2)
        Me.Btnmajdesprix.Name = "Btnmajdesprix"
        Me.Btnmajdesprix.Size = New System.Drawing.Size(26, 23)
        Me.Btnmajdesprix.TabIndex = 611
        Me.Btnmajdesprix.TabStop = False
        Me.ToolTip1.SetToolTip(Me.Btnmajdesprix, "Maj des prix")
        Me.Btnmajdesprix.UseVisualStyleBackColor = True
        '
        'Label38
        '
        Me.Label38.AutoSize = True
        Me.Label38.Font = New System.Drawing.Font("Microsoft Sans Serif", 8.25!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.Label38.Location = New System.Drawing.Point(319, 165)
        Me.Label38.Name = "Label38"
        Me.Label38.Size = New System.Drawing.Size(58, 13)
        Me.Label38.TabIndex = 258
        Me.Label38.Text = "Téléphone"
        '
        'Tnomliv
        '
        Me.Tnomliv.BackColor = System.Drawing.SystemColors.Window
        Me.Tnomliv.Location = New System.Drawing.Point(385, 58)
        Me.Tnomliv.Name = "Tnomliv"
        Me.Tnomliv.Size = New System.Drawing.Size(218, 20)
        Me.Tnomliv.TabIndex = 221
        Me.Tnomliv.Tag = "X"
        '
        'Label17
        '
        Me.Label17.AutoSize = True
        Me.Label17.Font = New System.Drawing.Font("Microsoft Sans Serif", 8.25!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.Label17.Location = New System.Drawing.Point(319, 186)
        Me.Label17.Name = "Label17"
        Me.Label17.Size = New System.Drawing.Size(24, 13)
        Me.Label17.TabIndex = 253
        Me.Label17.Text = "Fax"
        '
        'Label15
        '
        Me.Label15.AutoSize = True
        Me.Label15.Font = New System.Drawing.Font("Microsoft Sans Serif", 8.25!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.Label15.Location = New System.Drawing.Point(319, 146)
        Me.Label15.Name = "Label15"
        Me.Label15.Size = New System.Drawing.Size(64, 13)
        Me.Label15.TabIndex = 254
        Me.Label15.Text = "Code Postal"
        '
        'LblVendu
        '
        Me.LblVendu.AutoSize = True
        Me.LblVendu.Font = New System.Drawing.Font("Microsoft Sans Serif", 9.75!, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.LblVendu.Location = New System.Drawing.Point(69, 35)
        Me.LblVendu.Name = "LblVendu"
        Me.LblVendu.Size = New System.Drawing.Size(65, 16)
        Me.LblVendu.TabIndex = 251
        Me.LblVendu.Text = "Vendu à"
        '
        'BRectangleHaut
        '
        Me.BRectangleHaut.BackColor = System.Drawing.SystemColors.GradientActiveCaption
        Me.BRectangleHaut.Enabled = False
        Me.BRectangleHaut.FlatStyle = System.Windows.Forms.FlatStyle.Flat
        Me.BRectangleHaut.Location = New System.Drawing.Point(0, 212)
        Me.BRectangleHaut.Name = "BRectangleHaut"
        Me.BRectangleHaut.Size = New System.Drawing.Size(935, 47)
        Me.BRectangleHaut.TabIndex = 191
        Me.BRectangleHaut.TabStop = False
        Me.BRectangleHaut.UseVisualStyleBackColor = False
        '
        'TxtTermes
        '
        Me.TxtTermes.BackColor = System.Drawing.Color.FromArgb(CType(CType(255, Byte), Integer), CType(CType(255, Byte), Integer), CType(CType(192, Byte), Integer))
        Me.TxtTermes.CharacterCasing = System.Windows.Forms.CharacterCasing.Upper
        Me.TxtTermes.Location = New System.Drawing.Point(494, 236)
        Me.TxtTermes.Name = "TxtTermes"
        Me.TxtTermes.Size = New System.Drawing.Size(67, 20)
        Me.TxtTermes.TabIndex = 6
        Me.TxtTermes.Tag = "X"
        '
        'TxtExpediteur
        '
        Me.TxtExpediteur.AcceptsReturn = True
        Me.TxtExpediteur.BackColor = System.Drawing.Color.FromArgb(CType(CType(255, Byte), Integer), CType(CType(255, Byte), Integer), CType(CType(192, Byte), Integer))
        Me.TxtExpediteur.CharacterCasing = System.Windows.Forms.CharacterCasing.Upper
        Me.TxtExpediteur.Location = New System.Drawing.Point(580, 236)
        Me.TxtExpediteur.Name = "TxtExpediteur"
        Me.TxtExpediteur.Size = New System.Drawing.Size(67, 20)
        Me.TxtExpediteur.TabIndex = 7
        Me.TxtExpediteur.Tag = "X"
        '
        'LblStatus
        '
        Me.LblStatus.AutoSize = True
        Me.LblStatus.BackColor = System.Drawing.SystemColors.GradientActiveCaption
        Me.LblStatus.Location = New System.Drawing.Point(665, 218)
        Me.LblStatus.Name = "LblStatus"
        Me.LblStatus.Size = New System.Drawing.Size(37, 13)
        Me.LblStatus.TabIndex = 311
        Me.LblStatus.Text = "Status"
        '
        'LblCollect
        '
        Me.LblCollect.AutoSize = True
        Me.LblCollect.BackColor = System.Drawing.SystemColors.GradientActiveCaption
        Me.LblCollect.Location = New System.Drawing.Point(718, 218)
        Me.LblCollect.Name = "LblCollect"
        Me.LblCollect.Size = New System.Drawing.Size(39, 13)
        Me.LblCollect.TabIndex = 312
        Me.LblCollect.Text = "Collect"
        '
        'Txtstatus
        '
        Me.Txtstatus.CharacterCasing = System.Windows.Forms.CharacterCasing.Upper
        Me.Txtstatus.Location = New System.Drawing.Point(666, 235)
        Me.Txtstatus.Name = "Txtstatus"
        Me.Txtstatus.Size = New System.Drawing.Size(36, 20)
        Me.Txtstatus.TabIndex = 8
        '
        'Txtcollect
        '
        Me.Txtcollect.Location = New System.Drawing.Point(721, 235)
        Me.Txtcollect.Name = "Txtcollect"
        Me.Txtcollect.Size = New System.Drawing.Size(36, 20)
        Me.Txtcollect.TabIndex = 9
        '
        'BRectangleBas
        '
        Me.BRectangleBas.BackColor = System.Drawing.SystemColors.ButtonFace
        Me.BRectangleBas.Enabled = False
        Me.BRectangleBas.Location = New System.Drawing.Point(735, 484)
        Me.BRectangleBas.Name = "BRectangleBas"
        Me.BRectangleBas.Size = New System.Drawing.Size(197, 176)
        Me.BRectangleBas.TabIndex = 276
        Me.BRectangleBas.TabStop = False
        Me.BRectangleBas.UseVisualStyleBackColor = False
        '
        'LblDivers
        '
        Me.LblDivers.AutoSize = True
        Me.LblDivers.BackColor = System.Drawing.SystemColors.ButtonFace
        Me.LblDivers.Location = New System.Drawing.Point(610, 496)
        Me.LblDivers.Name = "LblDivers"
        Me.LblDivers.Size = New System.Drawing.Size(37, 13)
        Me.LblDivers.TabIndex = 315
        Me.LblDivers.Text = "Divers"
        '
        'TxtDivers
        '
        Me.TxtDivers.BackColor = System.Drawing.SystemColors.GradientActiveCaption
        Me.TxtDivers.Location = New System.Drawing.Point(656, 492)
        Me.TxtDivers.Name = "TxtDivers"
        Me.TxtDivers.ReadOnly = True
        Me.TxtDivers.Size = New System.Drawing.Size(66, 20)
        Me.TxtDivers.TabIndex = 16
        Me.TxtDivers.TabStop = False
        Me.TxtDivers.Tag = "N"
        Me.TxtDivers.TextAlign = System.Windows.Forms.HorizontalAlignment.Right
        '
        'LblEscompte
        '
        Me.LblEscompte.AutoSize = True
        Me.LblEscompte.BackColor = System.Drawing.SystemColors.GradientActiveCaption
        Me.LblEscompte.Location = New System.Drawing.Point(7, 496)
        Me.LblEscompte.Name = "LblEscompte"
        Me.LblEscompte.Size = New System.Drawing.Size(54, 13)
        Me.LblEscompte.TabIndex = 317
        Me.LblEscompte.Text = "Escompte"
        '
        'TxtEscompte
        '
        Me.TxtEscompte.AcceptsReturn = True
        Me.TxtEscompte.BackColor = System.Drawing.SystemColors.Window
        Me.TxtEscompte.Location = New System.Drawing.Point(91, 492)
        Me.TxtEscompte.Name = "TxtEscompte"
        Me.TxtEscompte.Size = New System.Drawing.Size(66, 20)
        Me.TxtEscompte.TabIndex = 13
        Me.TxtEscompte.Tag = "N"
        Me.TxtEscompte.TextAlign = System.Windows.Forms.HorizontalAlignment.Right
        '
        'TabTotal
        '
        Me.TabTotal.Controls.Add(TabTotal_TabPage1)
        Me.TabTotal.Controls.Add(Me.TabTotal_TabPage2)
        Me.TabTotal.Font = New System.Drawing.Font("Arial", 8.25!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.TabTotal.ItemSize = New System.Drawing.Size(42, 18)
        Me.TabTotal.Location = New System.Drawing.Point(0, 521)
        Me.TabTotal.Name = "TabTotal"
        Me.TabTotal.SelectedIndex = 0
        Me.TabTotal.Size = New System.Drawing.Size(733, 139)
        Me.TabTotal.TabIndex = 319
        Me.TabTotal.TabStop = False
        '
        'TabTotal_TabPage2
        '
        Me.TabTotal_TabPage2.Controls.Add(Me.TxtA1)
        Me.TabTotal_TabPage2.Controls.Add(Me.TxtA2)
        Me.TabTotal_TabPage2.Controls.Add(Me.TxtA3)
        Me.TabTotal_TabPage2.Controls.Add(Me.TxtA4)
        Me.TabTotal_TabPage2.Controls.Add(Me.TxtA5)
        Me.TabTotal_TabPage2.Controls.Add(Me.LblA1)
        Me.TabTotal_TabPage2.Controls.Add(Me.LblA2)
        Me.TabTotal_TabPage2.Controls.Add(Me.LblA3)
        Me.TabTotal_TabPage2.Controls.Add(Me.LblA4)
        Me.TabTotal_TabPage2.Controls.Add(Me.LblA5)
        Me.TabTotal_TabPage2.Controls.Add(Me.LblAge)
        Me.TabTotal_TabPage2.Location = New System.Drawing.Point(4, 22)
        Me.TabTotal_TabPage2.Name = "TabTotal_TabPage2"
        Me.TabTotal_TabPage2.Size = New System.Drawing.Size(725, 113)
        Me.TabTotal_TabPage2.TabIndex = 2
        Me.TabTotal_TabPage2.Text = "&3- Client"
        Me.TabTotal_TabPage2.UseVisualStyleBackColor = True
        '
        'TxtA1
        '
        Me.TxtA1.AcceptsReturn = True
        Me.TxtA1.BackColor = System.Drawing.SystemColors.Window
        Me.TxtA1.Cursor = System.Windows.Forms.Cursors.IBeam
        Me.TxtA1.Enabled = False
        Me.TxtA1.Font = New System.Drawing.Font("Arial", 8.25!, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.TxtA1.ForeColor = System.Drawing.SystemColors.WindowText
        Me.TxtA1.Location = New System.Drawing.Point(168, 72)
        Me.TxtA1.MaxLength = 0
        Me.TxtA1.Name = "TxtA1"
        Me.TxtA1.RightToLeft = System.Windows.Forms.RightToLeft.No
        Me.TxtA1.Size = New System.Drawing.Size(65, 20)
        Me.TxtA1.TabIndex = 96
        Me.TxtA1.TabStop = False
        '
        'TxtA2
        '
        Me.TxtA2.AcceptsReturn = True
        Me.TxtA2.BackColor = System.Drawing.SystemColors.Window
        Me.TxtA2.Cursor = System.Windows.Forms.Cursors.IBeam
        Me.TxtA2.Enabled = False
        Me.TxtA2.Font = New System.Drawing.Font("Arial", 8.25!, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.TxtA2.ForeColor = System.Drawing.SystemColors.WindowText
        Me.TxtA2.Location = New System.Drawing.Point(256, 73)
        Me.TxtA2.MaxLength = 0
        Me.TxtA2.Name = "TxtA2"
        Me.TxtA2.RightToLeft = System.Windows.Forms.RightToLeft.No
        Me.TxtA2.Size = New System.Drawing.Size(65, 20)
        Me.TxtA2.TabIndex = 98
        Me.TxtA2.TabStop = False
        '
        'TxtA3
        '
        Me.TxtA3.AcceptsReturn = True
        Me.TxtA3.BackColor = System.Drawing.SystemColors.Window
        Me.TxtA3.Cursor = System.Windows.Forms.Cursors.IBeam
        Me.TxtA3.Enabled = False
        Me.TxtA3.Font = New System.Drawing.Font("Arial", 8.25!, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.TxtA3.ForeColor = System.Drawing.SystemColors.WindowText
        Me.TxtA3.Location = New System.Drawing.Point(344, 73)
        Me.TxtA3.MaxLength = 0
        Me.TxtA3.Name = "TxtA3"
        Me.TxtA3.RightToLeft = System.Windows.Forms.RightToLeft.No
        Me.TxtA3.Size = New System.Drawing.Size(65, 20)
        Me.TxtA3.TabIndex = 100
        Me.TxtA3.TabStop = False
        '
        'TxtA4
        '
        Me.TxtA4.AcceptsReturn = True
        Me.TxtA4.BackColor = System.Drawing.SystemColors.Window
        Me.TxtA4.Cursor = System.Windows.Forms.Cursors.IBeam
        Me.TxtA4.Enabled = False
        Me.TxtA4.Font = New System.Drawing.Font("Arial", 8.25!, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.TxtA4.ForeColor = System.Drawing.SystemColors.WindowText
        Me.TxtA4.Location = New System.Drawing.Point(432, 73)
        Me.TxtA4.MaxLength = 0
        Me.TxtA4.Name = "TxtA4"
        Me.TxtA4.RightToLeft = System.Windows.Forms.RightToLeft.No
        Me.TxtA4.Size = New System.Drawing.Size(65, 20)
        Me.TxtA4.TabIndex = 102
        Me.TxtA4.TabStop = False
        '
        'TxtA5
        '
        Me.TxtA5.AcceptsReturn = True
        Me.TxtA5.BackColor = System.Drawing.SystemColors.Window
        Me.TxtA5.Cursor = System.Windows.Forms.Cursors.IBeam
        Me.TxtA5.Enabled = False
        Me.TxtA5.Font = New System.Drawing.Font("Arial", 8.25!, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.TxtA5.ForeColor = System.Drawing.SystemColors.WindowText
        Me.TxtA5.Location = New System.Drawing.Point(520, 73)
        Me.TxtA5.MaxLength = 0
        Me.TxtA5.Name = "TxtA5"
        Me.TxtA5.RightToLeft = System.Windows.Forms.RightToLeft.No
        Me.TxtA5.Size = New System.Drawing.Size(65, 20)
        Me.TxtA5.TabIndex = 104
        Me.TxtA5.TabStop = False
        '
        'LblA1
        '
        Me.LblA1.BackColor = System.Drawing.SystemColors.Control
        Me.LblA1.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        Me.LblA1.Cursor = System.Windows.Forms.Cursors.Default
        Me.LblA1.Font = New System.Drawing.Font("Arial", 8.0!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.LblA1.ForeColor = System.Drawing.SystemColors.ControlText
        Me.LblA1.Location = New System.Drawing.Point(160, 47)
        Me.LblA1.Name = "LblA1"
        Me.LblA1.RightToLeft = System.Windows.Forms.RightToLeft.No
        Me.LblA1.Size = New System.Drawing.Size(81, 49)
        Me.LblA1.TabIndex = 95
        Me.LblA1.Text = "Per1"
        Me.LblA1.TextAlign = System.Drawing.ContentAlignment.TopCenter
        '
        'LblA2
        '
        Me.LblA2.BackColor = System.Drawing.SystemColors.Control
        Me.LblA2.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        Me.LblA2.Cursor = System.Windows.Forms.Cursors.Default
        Me.LblA2.Font = New System.Drawing.Font("Arial", 8.0!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.LblA2.ForeColor = System.Drawing.SystemColors.ControlText
        Me.LblA2.Location = New System.Drawing.Point(248, 48)
        Me.LblA2.Name = "LblA2"
        Me.LblA2.RightToLeft = System.Windows.Forms.RightToLeft.No
        Me.LblA2.Size = New System.Drawing.Size(81, 49)
        Me.LblA2.TabIndex = 97
        Me.LblA2.Text = "Per1"
        Me.LblA2.TextAlign = System.Drawing.ContentAlignment.TopCenter
        '
        'LblA3
        '
        Me.LblA3.BackColor = System.Drawing.SystemColors.Control
        Me.LblA3.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        Me.LblA3.Cursor = System.Windows.Forms.Cursors.Default
        Me.LblA3.Font = New System.Drawing.Font("Arial", 8.0!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.LblA3.ForeColor = System.Drawing.SystemColors.ControlText
        Me.LblA3.Location = New System.Drawing.Point(336, 48)
        Me.LblA3.Name = "LblA3"
        Me.LblA3.RightToLeft = System.Windows.Forms.RightToLeft.No
        Me.LblA3.Size = New System.Drawing.Size(81, 49)
        Me.LblA3.TabIndex = 99
        Me.LblA3.Text = "Per1"
        Me.LblA3.TextAlign = System.Drawing.ContentAlignment.TopCenter
        '
        'LblA4
        '
        Me.LblA4.BackColor = System.Drawing.SystemColors.Control
        Me.LblA4.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        Me.LblA4.Cursor = System.Windows.Forms.Cursors.Default
        Me.LblA4.Font = New System.Drawing.Font("Arial", 8.0!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.LblA4.ForeColor = System.Drawing.SystemColors.ControlText
        Me.LblA4.Location = New System.Drawing.Point(424, 48)
        Me.LblA4.Name = "LblA4"
        Me.LblA4.RightToLeft = System.Windows.Forms.RightToLeft.No
        Me.LblA4.Size = New System.Drawing.Size(81, 49)
        Me.LblA4.TabIndex = 101
        Me.LblA4.Text = "Per1"
        Me.LblA4.TextAlign = System.Drawing.ContentAlignment.TopCenter
        '
        'LblA5
        '
        Me.LblA5.BackColor = System.Drawing.SystemColors.Control
        Me.LblA5.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        Me.LblA5.Cursor = System.Windows.Forms.Cursors.Default
        Me.LblA5.Font = New System.Drawing.Font("Arial", 8.0!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.LblA5.ForeColor = System.Drawing.SystemColors.ControlText
        Me.LblA5.Location = New System.Drawing.Point(512, 48)
        Me.LblA5.Name = "LblA5"
        Me.LblA5.RightToLeft = System.Windows.Forms.RightToLeft.No
        Me.LblA5.Size = New System.Drawing.Size(81, 49)
        Me.LblA5.TabIndex = 103
        Me.LblA5.Text = "Per1"
        Me.LblA5.TextAlign = System.Drawing.ContentAlignment.TopCenter
        '
        'LblAge
        '
        Me.LblAge.BackColor = System.Drawing.Color.Transparent
        Me.LblAge.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        Me.LblAge.Cursor = System.Windows.Forms.Cursors.Default
        Me.LblAge.Font = New System.Drawing.Font("Arial", 8.0!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.LblAge.ForeColor = System.Drawing.SystemColors.ControlText
        Me.LblAge.Location = New System.Drawing.Point(152, 24)
        Me.LblAge.Name = "LblAge"
        Me.LblAge.RightToLeft = System.Windows.Forms.RightToLeft.No
        Me.LblAge.Size = New System.Drawing.Size(449, 79)
        Me.LblAge.TabIndex = 94
        Me.LblAge.Text = "_________________    Age des comptes  _______________"
        Me.LblAge.TextAlign = System.Drawing.ContentAlignment.TopCenter
        '
        'Txtvendeur
        '
        Me.Txtvendeur.BackColor = System.Drawing.Color.FromArgb(CType(CType(255, Byte), Integer), CType(CType(255, Byte), Integer), CType(CType(192, Byte), Integer))
        Me.Txtvendeur.CharacterCasing = System.Windows.Forms.CharacterCasing.Upper
        Me.Txtvendeur.Cursor = System.Windows.Forms.Cursors.IBeam
        Me.Txtvendeur.Location = New System.Drawing.Point(776, 236)
        Me.Txtvendeur.MaxLength = 15
        Me.Txtvendeur.Name = "Txtvendeur"
        Me.Txtvendeur.Size = New System.Drawing.Size(67, 20)
        Me.Txtvendeur.TabIndex = 10
        Me.Txtvendeur.Tag = "X"
        '
        'Button5
        '
        Me.Button5.BackColor = System.Drawing.SystemColors.ButtonFace
        Me.Button5.Enabled = False
        Me.Button5.Location = New System.Drawing.Point(580, 484)
        Me.Button5.Name = "Button5"
        Me.Button5.Size = New System.Drawing.Size(153, 36)
        Me.Button5.TabIndex = 323
        Me.Button5.TabStop = False
        Me.Button5.UseVisualStyleBackColor = False
        '
        'Button6
        '
        Me.Button6.BackColor = System.Drawing.SystemColors.ButtonShadow
        Me.Button6.Enabled = False
        Me.Button6.Location = New System.Drawing.Point(270, 212)
        Me.Button6.Name = "Button6"
        Me.Button6.Size = New System.Drawing.Size(214, 48)
        Me.Button6.TabIndex = 324
        Me.Button6.TabStop = False
        Me.Button6.UseVisualStyleBackColor = False
        '
        'bidon
        '
        Me.bidon.Location = New System.Drawing.Point(913, 626)
        Me.bidon.Name = "bidon"
        Me.bidon.Size = New System.Drawing.Size(10, 20)
        Me.bidon.TabIndex = 432
        '
        'ToolStrip1
        '
        Me.ToolStrip1.BackColor = System.Drawing.SystemColors.ControlDark
        Me.ToolStrip1.CanOverflow = False
        Me.ToolStrip1.Dock = System.Windows.Forms.DockStyle.None
        Me.ToolStrip1.GripStyle = System.Windows.Forms.ToolStripGripStyle.Hidden
        Me.ToolStrip1.Items.AddRange(New System.Windows.Forms.ToolStripItem() {Me.BAjout, Me.Binsere, Me.Beffacer, Me.Binfo, Me.BCatalog, Me.Bhistorique, Me.BtnSubstitut})
        Me.ToolStrip1.Location = New System.Drawing.Point(11, 263)
        Me.ToolStrip1.Name = "ToolStrip1"
        Me.ToolStrip1.RenderMode = System.Windows.Forms.ToolStripRenderMode.Professional
        Me.ToolStrip1.Size = New System.Drawing.Size(164, 25)
        Me.ToolStrip1.Stretch = True
        Me.ToolStrip1.TabIndex = 434
        Me.ToolStrip1.Text = "ToolStrip1"
        '
        'BAjout
        '
        Me.BAjout.BackColor = System.Drawing.SystemColors.ButtonFace
        Me.BAjout.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Zoom
        Me.BAjout.Checked = True
        Me.BAjout.CheckState = System.Windows.Forms.CheckState.Checked
        Me.BAjout.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image
        Me.BAjout.Image = CType(resources.GetObject("BAjout.Image"), System.Drawing.Image)
        Me.BAjout.ImageTransparentColor = System.Drawing.Color.Magenta
        Me.BAjout.Name = "BAjout"
        Me.BAjout.Size = New System.Drawing.Size(23, 22)
        Me.BAjout.Text = "ToolStripButton1"
        '
        'Binsere
        '
        Me.Binsere.BackColor = System.Drawing.SystemColors.ButtonFace
        Me.Binsere.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
        Me.Binsere.Checked = True
        Me.Binsere.CheckState = System.Windows.Forms.CheckState.Checked
        Me.Binsere.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image
        Me.Binsere.Image = CType(resources.GetObject("Binsere.Image"), System.Drawing.Image)
        Me.Binsere.ImageTransparentColor = System.Drawing.Color.Magenta
        Me.Binsere.Name = "Binsere"
        Me.Binsere.Size = New System.Drawing.Size(23, 22)
        Me.Binsere.Text = "ToolStripButton1"
        '
        'Beffacer
        '
        Me.Beffacer.BackColor = System.Drawing.SystemColors.ButtonFace
        Me.Beffacer.Checked = True
        Me.Beffacer.CheckState = System.Windows.Forms.CheckState.Checked
        Me.Beffacer.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image
        Me.Beffacer.Image = CType(resources.GetObject("Beffacer.Image"), System.Drawing.Image)
        Me.Beffacer.ImageTransparentColor = System.Drawing.Color.Magenta
        Me.Beffacer.Name = "Beffacer"
        Me.Beffacer.Size = New System.Drawing.Size(23, 22)
        Me.Beffacer.Text = "ToolStripButton2"
        '
        'Binfo
        '
        Me.Binfo.Checked = True
        Me.Binfo.CheckState = System.Windows.Forms.CheckState.Checked
        Me.Binfo.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image
        Me.Binfo.Image = CType(resources.GetObject("Binfo.Image"), System.Drawing.Image)
        Me.Binfo.ImageTransparentColor = System.Drawing.Color.Magenta
        Me.Binfo.Name = "Binfo"
        Me.Binfo.Size = New System.Drawing.Size(23, 22)
        Me.Binfo.Text = "ToolStripButton4"
        '
        'BCatalog
        '
        Me.BCatalog.BackColor = System.Drawing.SystemColors.ButtonFace
        Me.BCatalog.Checked = True
        Me.BCatalog.CheckState = System.Windows.Forms.CheckState.Checked
        Me.BCatalog.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image
        Me.BCatalog.Image = CType(resources.GetObject("BCatalog.Image"), System.Drawing.Image)
        Me.BCatalog.ImageTransparentColor = System.Drawing.Color.Magenta
        Me.BCatalog.Name = "BCatalog"
        Me.BCatalog.Size = New System.Drawing.Size(23, 22)
        Me.BCatalog.Text = "ToolStripButton3"
        '
        'Bhistorique
        '
        Me.Bhistorique.Checked = True
        Me.Bhistorique.CheckState = System.Windows.Forms.CheckState.Checked
        Me.Bhistorique.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image
        Me.Bhistorique.Image = CType(resources.GetObject("Bhistorique.Image"), System.Drawing.Image)
        Me.Bhistorique.ImageTransparentColor = System.Drawing.Color.Magenta
        Me.Bhistorique.Name = "Bhistorique"
        Me.Bhistorique.Size = New System.Drawing.Size(23, 22)
        Me.Bhistorique.Text = "ToolStripButton7"
        Me.Bhistorique.ToolTipText = "Alt F11 Historique"
        '
        'BtnSubstitut
        '
        Me.BtnSubstitut.Checked = True
        Me.BtnSubstitut.CheckState = System.Windows.Forms.CheckState.Checked
        Me.BtnSubstitut.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image
        Me.BtnSubstitut.Image = CType(resources.GetObject("BtnSubstitut.Image"), System.Drawing.Image)
        Me.BtnSubstitut.ImageTransparentColor = System.Drawing.Color.Magenta
        Me.BtnSubstitut.Name = "BtnSubstitut"
        Me.BtnSubstitut.Size = New System.Drawing.Size(23, 22)
        Me.BtnSubstitut.Text = "ToolStripButton4"
        Me.BtnSubstitut.ToolTipText = "SF6- Info substitut"
        '
        'ToolStrip2
        '
        Me.ToolStrip2.AutoSize = False
        Me.ToolStrip2.Dock = System.Windows.Forms.DockStyle.None
        Me.ToolStrip2.GripMargin = New System.Windows.Forms.Padding(0)
        Me.ToolStrip2.GripStyle = System.Windows.Forms.ToolStripGripStyle.Hidden
        Me.ToolStrip2.Items.AddRange(New System.Windows.Forms.ToolStripItem() {Me.BtImpSoum, Me.BtFacture, Me.Bttrieproduit, Me.btnconnaissement, Me.btnroute})
        Me.ToolStrip2.LayoutStyle = System.Windows.Forms.ToolStripLayoutStyle.Table
        Me.ToolStrip2.Location = New System.Drawing.Point(730, 35)
        Me.ToolStrip2.Name = "ToolStrip2"
        Me.ToolStrip2.Padding = New System.Windows.Forms.Padding(3)
        Me.ToolStrip2.RenderMode = System.Windows.Forms.ToolStripRenderMode.Professional
        Me.ToolStrip2.Size = New System.Drawing.Size(197, 106)
        Me.ToolStrip2.TabIndex = 435
        '
        'BtImpSoum
        '
        Me.BtImpSoum.AutoSize = False
        Me.BtImpSoum.BackgroundImage = CType(resources.GetObject("BtImpSoum.BackgroundImage"), System.Drawing.Image)
        Me.BtImpSoum.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
        Me.BtImpSoum.ImageScaling = System.Windows.Forms.ToolStripItemImageScaling.None
        Me.BtImpSoum.ImageTransparentColor = System.Drawing.Color.Magenta
        Me.BtImpSoum.Name = "BtImpSoum"
        Me.BtImpSoum.Size = New System.Drawing.Size(179, 17)
        Me.BtImpSoum.Text = "Imp. Soumission"
        Me.BtImpSoum.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        Me.BtImpSoum.TextImageRelation = System.Windows.Forms.TextImageRelation.TextBeforeImage
        '
        'BtFacture
        '
        Me.BtFacture.AutoSize = False
        Me.BtFacture.BackgroundImage = CType(resources.GetObject("BtFacture.BackgroundImage"), System.Drawing.Image)
        Me.BtFacture.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
        Me.BtFacture.ImageTransparentColor = System.Drawing.Color.Magenta
        Me.BtFacture.Name = "BtFacture"
        Me.BtFacture.Size = New System.Drawing.Size(179, 17)
        Me.BtFacture.Text = "Shift-F7 Facturation"
        Me.BtFacture.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        Me.BtFacture.TextImageRelation = System.Windows.Forms.TextImageRelation.TextBeforeImage
        '
        'Bttrieproduit
        '
        Me.Bttrieproduit.AutoSize = False
        Me.Bttrieproduit.BackgroundImage = CType(resources.GetObject("Bttrieproduit.BackgroundImage"), System.Drawing.Image)
        Me.Bttrieproduit.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
        Me.Bttrieproduit.ImageTransparentColor = System.Drawing.Color.Magenta
        Me.Bttrieproduit.Name = "Bttrieproduit"
        Me.Bttrieproduit.Size = New System.Drawing.Size(179, 17)
        Me.Bttrieproduit.Text = "Alt-F5 Trier en ordre de produit"
        Me.Bttrieproduit.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        Me.Bttrieproduit.TextImageRelation = System.Windows.Forms.TextImageRelation.TextBeforeImage
        Me.Bttrieproduit.ToolTipText = "Trier en ordre de produit"
        '
        'btnconnaissement
        '
        Me.btnconnaissement.AutoSize = False
        Me.btnconnaissement.BackgroundImage = CType(resources.GetObject("btnconnaissement.BackgroundImage"), System.Drawing.Image)
        Me.btnconnaissement.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
        Me.btnconnaissement.ImageTransparentColor = System.Drawing.Color.Magenta
        Me.btnconnaissement.Name = "btnconnaissement"
        Me.btnconnaissement.Size = New System.Drawing.Size(179, 17)
        Me.btnconnaissement.Text = "S-F2 Connaissement"
        Me.btnconnaissement.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        Me.btnconnaissement.TextImageRelation = System.Windows.Forms.TextImageRelation.TextBeforeImage
        Me.btnconnaissement.ToolTipText = "imprimer le connaissement"
        '
        'btnroute
        '
        Me.btnroute.AutoSize = False
        Me.btnroute.BackgroundImage = CType(resources.GetObject("btnroute.BackgroundImage"), System.Drawing.Image)
        Me.btnroute.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
        Me.btnroute.ImageTransparentColor = System.Drawing.Color.Magenta
        Me.btnroute.Name = "btnroute"
        Me.btnroute.Size = New System.Drawing.Size(179, 17)
        Me.btnroute.Text = "S-F5 Route"
        Me.btnroute.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        Me.btnroute.TextImageRelation = System.Windows.Forms.TextImageRelation.TextBeforeImage
        Me.btnroute.ToolTipText = "Changer route"
        Me.btnroute.Visible = False
        '
        'ToolStrip3
        '
        Me.ToolStrip3.Dock = System.Windows.Forms.DockStyle.None
        Me.ToolStrip3.GripStyle = System.Windows.Forms.ToolStripGripStyle.Hidden
        Me.ToolStrip3.Items.AddRange(New System.Windows.Forms.ToolStripItem() {Me.BtTermes})
        Me.ToolStrip3.Location = New System.Drawing.Point(494, 212)
        Me.ToolStrip3.Name = "ToolStrip3"
        Me.ToolStrip3.Size = New System.Drawing.Size(69, 25)
        Me.ToolStrip3.TabIndex = 436
        Me.ToolStrip3.Text = "ToolStrip3"
        '
        'BtTermes
        '
        Me.BtTermes.AutoSize = False
        Me.BtTermes.BackgroundImage = CType(resources.GetObject("BtTermes.BackgroundImage"), System.Drawing.Image)
        Me.BtTermes.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
        Me.BtTermes.ImageTransparentColor = System.Drawing.Color.Magenta
        Me.BtTermes.Margin = New System.Windows.Forms.Padding(0)
        Me.BtTermes.Name = "BtTermes"
        Me.BtTermes.Size = New System.Drawing.Size(66, 22)
        Me.BtTermes.Text = "Termes"
        Me.BtTermes.TextImageRelation = System.Windows.Forms.TextImageRelation.TextBeforeImage
        '
        'ToolStrip4
        '
        Me.ToolStrip4.Dock = System.Windows.Forms.DockStyle.None
        Me.ToolStrip4.GripStyle = System.Windows.Forms.ToolStripGripStyle.Hidden
        Me.ToolStrip4.Items.AddRange(New System.Windows.Forms.ToolStripItem() {Me.BtVia})
        Me.ToolStrip4.Location = New System.Drawing.Point(580, 212)
        Me.ToolStrip4.Name = "ToolStrip4"
        Me.ToolStrip4.Size = New System.Drawing.Size(68, 25)
        Me.ToolStrip4.TabIndex = 437
        Me.ToolStrip4.Text = "ToolStrip4"
        '
        'BtVia
        '
        Me.BtVia.AutoSize = False
        Me.BtVia.BackgroundImage = CType(resources.GetObject("BtVia.BackgroundImage"), System.Drawing.Image)
        Me.BtVia.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
        Me.BtVia.ImageTransparentColor = System.Drawing.Color.Magenta
        Me.BtVia.Name = "BtVia"
        Me.BtVia.Size = New System.Drawing.Size(65, 22)
        Me.BtVia.Text = "Via"
        Me.BtVia.TextImageRelation = System.Windows.Forms.TextImageRelation.TextBeforeImage
        '
        'ToolStrip5
        '
        Me.ToolStrip5.Dock = System.Windows.Forms.DockStyle.None
        Me.ToolStrip5.GripStyle = System.Windows.Forms.ToolStripGripStyle.Hidden
        Me.ToolStrip5.Items.AddRange(New System.Windows.Forms.ToolStripItem() {Me.BClient})
        Me.ToolStrip5.Location = New System.Drawing.Point(167, 29)
        Me.ToolStrip5.Name = "ToolStrip5"
        Me.ToolStrip5.Size = New System.Drawing.Size(63, 25)
        Me.ToolStrip5.TabIndex = 438
        Me.ToolStrip5.Text = "ToolStrip5"
        '
        'BClient
        '
        Me.BClient.AutoSize = False
        Me.BClient.BackgroundImage = CType(resources.GetObject("BClient.BackgroundImage"), System.Drawing.Image)
        Me.BClient.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
        Me.BClient.ImageTransparentColor = System.Drawing.Color.Magenta
        Me.BClient.Name = "BClient"
        Me.BClient.Size = New System.Drawing.Size(60, 22)
        Me.BClient.Text = "No. Client"
        Me.BClient.TextImageRelation = System.Windows.Forms.TextImageRelation.TextBeforeImage
        '
        'TsProfit
        '
        Me.TsProfit.Dock = System.Windows.Forms.DockStyle.None
        Me.TsProfit.Items.AddRange(New System.Windows.Forms.ToolStripItem() {Me.Bprofit, Me.BtnMultisite, Me.BTFournis, Me.BtCreation, Me.Btnlocalisateurproduit, Me.Btnnapa})
        Me.TsProfit.Location = New System.Drawing.Point(170, 262)
        Me.TsProfit.Name = "TsProfit"
        Me.TsProfit.Size = New System.Drawing.Size(150, 25)
        Me.TsProfit.TabIndex = 544
        Me.TsProfit.Text = "ToolStrip6"
        '
        'Bprofit
        '
        Me.Bprofit.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image
        Me.Bprofit.Image = CType(resources.GetObject("Bprofit.Image"), System.Drawing.Image)
        Me.Bprofit.ImageTransparentColor = System.Drawing.Color.Magenta
        Me.Bprofit.Name = "Bprofit"
        Me.Bprofit.Size = New System.Drawing.Size(23, 22)
        Me.Bprofit.Text = "ToolStripButton1"
        Me.Bprofit.ToolTipText = "SF3 - Profit"
        '
        'BtnMultisite
        '
        Me.BtnMultisite.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image
        Me.BtnMultisite.Image = CType(resources.GetObject("BtnMultisite.Image"), System.Drawing.Image)
        Me.BtnMultisite.ImageTransparentColor = System.Drawing.Color.Magenta
        Me.BtnMultisite.Name = "BtnMultisite"
        Me.BtnMultisite.Size = New System.Drawing.Size(23, 22)
        Me.BtnMultisite.Text = "Inventaire multi site"
        '
        'BTFournis
        '
        Me.BTFournis.Checked = True
        Me.BTFournis.CheckState = System.Windows.Forms.CheckState.Checked
        Me.BTFournis.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image
        Me.BTFournis.Image = CType(resources.GetObject("BTFournis.Image"), System.Drawing.Image)
        Me.BTFournis.ImageTransparentColor = System.Drawing.Color.Magenta
        Me.BTFournis.Name = "BTFournis"
        Me.BTFournis.Size = New System.Drawing.Size(23, 22)
        Me.BTFournis.Text = "Commande Fournisseur"
        '
        'BtCreation
        '
        Me.BtCreation.BackColor = System.Drawing.SystemColors.ControlDark
        Me.BtCreation.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
        Me.BtCreation.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image
        Me.BtCreation.Image = CType(resources.GetObject("BtCreation.Image"), System.Drawing.Image)
        Me.BtCreation.ImageTransparentColor = System.Drawing.Color.Magenta
        Me.BtCreation.Name = "BtCreation"
        Me.BtCreation.Size = New System.Drawing.Size(23, 22)
        Me.BtCreation.Text = "ToolStripButton1"
        Me.BtCreation.ToolTipText = "SF6 Créer un produit"
        '
        'Btnlocalisateurproduit
        '
        Me.Btnlocalisateurproduit.Checked = True
        Me.Btnlocalisateurproduit.CheckState = System.Windows.Forms.CheckState.Checked
        Me.Btnlocalisateurproduit.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image
        Me.Btnlocalisateurproduit.Image = CType(resources.GetObject("Btnlocalisateurproduit.Image"), System.Drawing.Image)
        Me.Btnlocalisateurproduit.ImageTransparentColor = System.Drawing.Color.Magenta
        Me.Btnlocalisateurproduit.Name = "Btnlocalisateurproduit"
        Me.Btnlocalisateurproduit.Size = New System.Drawing.Size(23, 22)
        Me.Btnlocalisateurproduit.Text = "Commande Fournisseur"
        '
        'Btnnapa
        '
        Me.Btnnapa.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image
        Me.Btnnapa.Image = CType(resources.GetObject("Btnnapa.Image"), System.Drawing.Image)
        Me.Btnnapa.ImageTransparentColor = System.Drawing.Color.Magenta
        Me.Btnnapa.Name = "Btnnapa"
        Me.Btnnapa.Size = New System.Drawing.Size(23, 22)
        Me.Btnnapa.Text = "ToolStripButton1"
        '
        'Lblroute
        '
        Me.Lblroute.AutoSize = True
        Me.Lblroute.ForeColor = System.Drawing.Color.Red
        Me.Lblroute.Location = New System.Drawing.Point(768, 266)
        Me.Lblroute.Name = "Lblroute"
        Me.Lblroute.Size = New System.Drawing.Size(0, 13)
        Me.Lblroute.TabIndex = 545
        '
        'Lblroutedef
        '
        Me.Lblroutedef.AutoSize = True
        Me.Lblroutedef.ForeColor = System.Drawing.Color.Red
        Me.Lblroutedef.Location = New System.Drawing.Point(709, 266)
        Me.Lblroutedef.Name = "Lblroutedef"
        Me.Lblroutedef.Size = New System.Drawing.Size(0, 13)
        Me.Lblroutedef.TabIndex = 546
        '
        'Tstotal
        '
        Me.Tstotal.BackColor = System.Drawing.SystemColors.GradientActiveCaption
        Me.Tstotal.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        Me.Tstotal.ForeColor = System.Drawing.Color.Black
        Me.Tstotal.Location = New System.Drawing.Point(807, 493)
        Me.Tstotal.Name = "Tstotal"
        Me.Tstotal.Size = New System.Drawing.Size(100, 20)
        Me.Tstotal.TabIndex = 547
        Me.Tstotal.TabStop = False
        Me.Tstotal.Tag = "texte"
        Me.Tstotal.TextAlign = System.Windows.Forms.HorizontalAlignment.Right
        '
        'ToolStrip9
        '
        Me.ToolStrip9.AutoSize = False
        Me.ToolStrip9.Dock = System.Windows.Forms.DockStyle.None
        Me.ToolStrip9.GripMargin = New System.Windows.Forms.Padding(0)
        Me.ToolStrip9.GripStyle = System.Windows.Forms.ToolStripGripStyle.Hidden
        Me.ToolStrip9.Items.AddRange(New System.Windows.Forms.ToolStripItem() {Me.BtDepot})
        Me.ToolStrip9.Location = New System.Drawing.Point(776, 595)
        Me.ToolStrip9.Name = "ToolStrip9"
        Me.ToolStrip9.RenderMode = System.Windows.Forms.ToolStripRenderMode.Professional
        Me.ToolStrip9.Size = New System.Drawing.Size(27, 27)
        Me.ToolStrip9.Stretch = True
        Me.ToolStrip9.TabIndex = 548
        Me.ToolStrip9.Text = "ToolStrip9"
        '
        'BtDepot
        '
        Me.BtDepot.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Zoom
        Me.BtDepot.Checked = True
        Me.BtDepot.CheckState = System.Windows.Forms.CheckState.Checked
        Me.BtDepot.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image
        Me.BtDepot.Image = CType(resources.GetObject("BtDepot.Image"), System.Drawing.Image)
        Me.BtDepot.ImageTransparentColor = System.Drawing.Color.Magenta
        Me.BtDepot.Name = "BtDepot"
        Me.BtDepot.Padding = New System.Windows.Forms.Padding(2)
        Me.BtDepot.Size = New System.Drawing.Size(24, 24)
        '
        'LblMag
        '
        Me.LblMag.AutoSize = True
        Me.LblMag.BackColor = System.Drawing.SystemColors.Control
        Me.LblMag.ForeColor = System.Drawing.Color.Red
        Me.LblMag.Location = New System.Drawing.Point(230, 163)
        Me.LblMag.Name = "LblMag"
        Me.LblMag.Size = New System.Drawing.Size(0, 13)
        Me.LblMag.TabIndex = 549
        Me.LblMag.Visible = False
        '
        'Label1
        '
        Me.Label1.AutoSize = True
        Me.Label1.BackColor = System.Drawing.Color.SkyBlue
        Me.Label1.Font = New System.Drawing.Font("Microsoft Sans Serif", 12.0!, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.Label1.ForeColor = System.Drawing.Color.Black
        Me.Label1.Location = New System.Drawing.Point(740, 5)
        Me.Label1.Name = "Label1"
        Me.Label1.Size = New System.Drawing.Size(158, 20)
        Me.Label1.TabIndex = 550
        Me.Label1.Text = "Bon de commande"
        '
        'lblnbimp
        '
        Me.lblnbimp.AutoSize = True
        Me.lblnbimp.Font = New System.Drawing.Font("Microsoft Sans Serif", 8.25!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.lblnbimp.Location = New System.Drawing.Point(556, 190)
        Me.lblnbimp.Name = "lblnbimp"
        Me.lblnbimp.Size = New System.Drawing.Size(87, 13)
        Me.lblnbimp.TabIndex = 551
        Me.lblnbimp.Text = "Nb d'impression :"
        '
        'Btncomfact
        '
        Me.Btncomfact.BackColor = System.Drawing.SystemColors.ControlLightLight
        Me.Btncomfact.BackgroundImage = CType(resources.GetObject("Btncomfact.BackgroundImage"), System.Drawing.Image)
        Me.Btncomfact.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
        Me.Btncomfact.Location = New System.Drawing.Point(730, 181)
        Me.Btncomfact.Name = "Btncomfact"
        Me.Btncomfact.Size = New System.Drawing.Size(189, 27)
        Me.Btncomfact.TabIndex = 552
        Me.Btncomfact.TabStop = False
        Me.Btncomfact.Text = "Fact. B/O. Billing"
        Me.Btncomfact.UseVisualStyleBackColor = False
        '
        'PictureBox2
        '
        Me.PictureBox2.BackColor = System.Drawing.Color.SkyBlue
        Me.PictureBox2.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
        Me.PictureBox2.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        Me.PictureBox2.Location = New System.Drawing.Point(737, 2)
        Me.PictureBox2.Name = "PictureBox2"
        Me.PictureBox2.Size = New System.Drawing.Size(166, 23)
        Me.PictureBox2.TabIndex = 433
        Me.PictureBox2.TabStop = False
        '
        'Btnbarcodeauto
        '
        Me.Btnbarcodeauto.BackColor = System.Drawing.Color.LightGray
        Me.Btnbarcodeauto.Location = New System.Drawing.Point(649, 30)
        Me.Btnbarcodeauto.Name = "Btnbarcodeauto"
        Me.Btnbarcodeauto.Size = New System.Drawing.Size(73, 48)
        Me.Btnbarcodeauto.TabIndex = 612
        Me.Btnbarcodeauto.Text = "F3-Scan automatique"
        Me.Btnbarcodeauto.UseVisualStyleBackColor = False
        '
        'Pgrid
        '
        Me.Pgrid.AllowUserToAddRows = False
        Me.Pgrid.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        Me.Pgrid.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize
        Me.Pgrid.Location = New System.Drawing.Point(229, 266)
        Me.Pgrid.Name = "Pgrid"
        Me.Pgrid.RowHeadersVisible = False
        Me.Pgrid.RowTemplate.Height = 19
        Me.Pgrid.ScrollBars = System.Windows.Forms.ScrollBars.Vertical
        Me.Pgrid.SelectionMode = System.Windows.Forms.DataGridViewSelectionMode.CellSelect
        Me.Pgrid.Size = New System.Drawing.Size(24, 14)
        Me.Pgrid.TabIndex = 543
        '
        'SolGrid1
        '
        Me.SolGrid1.AllowUserToAddRows = False
        Me.SolGrid1.BackgroundColor = System.Drawing.SystemColors.Control
        Me.SolGrid1.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        Me.SolGrid1.ColumnHeadersHeight = 28
        Me.SolGrid1.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.DisableResizing
        Me.SolGrid1.Location = New System.Drawing.Point(0, 291)
        Me.SolGrid1.MultiSelect = False
        Me.SolGrid1.Name = "SolGrid1"
        Me.SolGrid1.RowHeadersVisible = False
        Me.SolGrid1.RowTemplate.Height = 19
        Me.SolGrid1.ScrollBars = System.Windows.Forms.ScrollBars.Vertical
        Me.SolGrid1.SelectionMode = System.Windows.Forms.DataGridViewSelectionMode.CellSelect
        Me.SolGrid1.Size = New System.Drawing.Size(935, 195)
        Me.SolGrid1.TabIndex = 12
        '
        'FrmPieceCommande
        '
        Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
        Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        Me.ClientSize = New System.Drawing.Size(932, 649)
        Me.Controls.Add(Me.Btnbarcodeauto)
        Me.Controls.Add(Me.Btnmajdesprix)
        Me.Controls.Add(Me.Btncomfact)
        Me.Controls.Add(Me.lblnbimp)
        Me.Controls.Add(Me.Label1)
        Me.Controls.Add(Me.LblMag)
        Me.Controls.Add(Me.ToolStrip9)
        Me.Controls.Add(Me.Tstotal)
        Me.Controls.Add(Me.Lblroutedef)
        Me.Controls.Add(Me.Lblroute)
        Me.Controls.Add(Me.TsProfit)
        Me.Controls.Add(Me.Pgrid)
        Me.Controls.Add(Me.ToolStrip5)
        Me.Controls.Add(Me.ToolStrip4)
        Me.Controls.Add(Me.ToolStrip3)
        Me.Controls.Add(Me.ToolStrip2)
        Me.Controls.Add(Me.ToolStrip1)
        Me.Controls.Add(Me.PictureBox2)
        Me.Controls.Add(Me.Txtvendeur)
        Me.Controls.Add(Me.TxtEscompte)
        Me.Controls.Add(Me.LblEscompte)
        Me.Controls.Add(Me.TxtDivers)
        Me.Controls.Add(Me.LblDivers)
        Me.Controls.Add(Me.Txtcollect)
        Me.Controls.Add(Me.Txtstatus)
        Me.Controls.Add(Me.LblCollect)
        Me.Controls.Add(Me.LblStatus)
        Me.Controls.Add(Me.TxtExpediteur)
        Me.Controls.Add(Me.TxtTermes)
        Me.Controls.Add(Me.Tclientliv)
        Me.Controls.Add(Me.Tcommis)
        Me.Controls.Add(Me.Tclient)
        Me.Controls.Add(Me.Ddateouverture)
        Me.Controls.Add(Me.Label2)
        Me.Controls.Add(Me.Ddaterequis)
        Me.Controls.Add(Me.Tajoutdepot)
        Me.Controls.Add(Me.Label21)
        Me.Controls.Add(Me.Ttransport)
        Me.Controls.Add(Me.Label22)
        Me.Controls.Add(Me.Ttotal)
        Me.Controls.Add(Me.Ttps)
        Me.Controls.Add(Me.Ttvq)
        Me.Controls.Add(Me.Tnocom)
        Me.Controls.Add(Me.Tgtotal)
        Me.Controls.Add(Me.Label25)
        Me.Controls.Add(Me.Tdepot)
        Me.Controls.Add(Me.Tentrepot)
        Me.Controls.Add(Me.Label46)
        Me.Controls.Add(Me.Label26)
        Me.Controls.Add(Me.Label45)
        Me.Controls.Add(Me.Tnoachat)
        Me.Controls.Add(Me.Label44)
        Me.Controls.Add(Me.Label43)
        Me.Controls.Add(Me.Btclientliv)
        Me.Controls.Add(Me.Button3)
        Me.Controls.Add(Me.BCommis)
        Me.Controls.Add(Me.Bvendeur)
        Me.Controls.Add(Me.Tnocomrech)
        Me.Controls.Add(Me.Label47)
        Me.Controls.Add(Me.Tprovinceliv)
        Me.Controls.Add(Me.lfd)
        Me.Controls.Add(Me.Tprovince)
        Me.Controls.Add(Me.Tville)
        Me.Controls.Add(Me.Tcodepostal)
        Me.Controls.Add(Me.Ttelephone)
        Me.Controls.Add(Me.Tfax)
        Me.Controls.Add(Me.Tadresse2)
        Me.Controls.Add(Me.Tadresse1)
        Me.Controls.Add(Me.Tnom)
        Me.Controls.Add(Me.Label10)
        Me.Controls.Add(Me.Label9)
        Me.Controls.Add(Me.Label7)
        Me.Controls.Add(Me.Label6)
        Me.Controls.Add(Me.Label5)
        Me.Controls.Add(Me.Label4)
        Me.Controls.Add(Me.Label39)
        Me.Controls.Add(Me.Label12)
        Me.Controls.Add(Me.Label11)
        Me.Controls.Add(Me.Tadresse1liv)
        Me.Controls.Add(Me.Tadresse2liv)
        Me.Controls.Add(Me.Tfaxliv)
        Me.Controls.Add(Me.Ttelephoneliv)
        Me.Controls.Add(Me.Tcodepostalliv)
        Me.Controls.Add(Me.Tvilleliv)
        Me.Controls.Add(Me.Label18)
        Me.Controls.Add(Me.Label14)
        Me.Controls.Add(Me.Label42)
        Me.Controls.Add(Me.Label41)
        Me.Controls.Add(Me.Label40)
        Me.Controls.Add(Me.Label38)
        Me.Controls.Add(Me.Tnomliv)
        Me.Controls.Add(Me.Label17)
        Me.Controls.Add(Me.Label15)
        Me.Controls.Add(Me.LblVendu)
        Me.Controls.Add(Me.BRectangleBas)
        Me.Controls.Add(Me.BindingNavigator1)
        Me.Controls.Add(Me.Button4)
        Me.Controls.Add(Me.Button5)
        Me.Controls.Add(Me.TabTotal)
        Me.Controls.Add(Me.Button6)
        Me.Controls.Add(Me.BRectangleHaut)
        Me.Controls.Add(Me.bidon)
        Me.Controls.Add(Me.SolGrid1)
        Me.FormBorderStyle = System.Windows.Forms.FormBorderStyle.Fixed3D
        Me.Icon = CType(resources.GetObject("$this.Icon"), System.Drawing.Icon)
        Me.KeyPreview = True
        Me.Name = "FrmPieceCommande"
        Me.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen
        TabTotal_TabPage1.ResumeLayout(False)
        TabTotal_TabPage1.PerformLayout()
        CType(Me.BindingNavigator1, System.ComponentModel.ISupportInitialize).EndInit()
        Me.BindingNavigator1.ResumeLayout(False)
        Me.BindingNavigator1.PerformLayout()
        Me.TabTotal.ResumeLayout(False)
        Me.TabTotal_TabPage2.ResumeLayout(False)
        Me.TabTotal_TabPage2.PerformLayout()
        Me.ToolStrip1.ResumeLayout(False)
        Me.ToolStrip1.PerformLayout()
        Me.ToolStrip2.ResumeLayout(False)
        Me.ToolStrip2.PerformLayout()
        Me.ToolStrip3.ResumeLayout(False)
        Me.ToolStrip3.PerformLayout()
        Me.ToolStrip4.ResumeLayout(False)
        Me.ToolStrip4.PerformLayout()
        Me.ToolStrip5.ResumeLayout(False)
        Me.ToolStrip5.PerformLayout()
        Me.TsProfit.ResumeLayout(False)
        Me.TsProfit.PerformLayout()
        Me.ToolStrip9.ResumeLayout(False)
        Me.ToolStrip9.PerformLayout()
        CType(Me.PictureBox2, System.ComponentModel.ISupportInitialize).EndInit()
        CType(Me.Pgrid, System.ComponentModel.ISupportInitialize).EndInit()
        CType(Me.SolGrid1, System.ComponentModel.ISupportInitialize).EndInit()
        Me.ResumeLayout(False)
        Me.PerformLayout()

    End Sub
    Friend WithEvents BTmodifier As System.Windows.Forms.ToolStripButton
    Friend WithEvents BTnouveau As System.Windows.Forms.ToolStripButton
    Friend WithEvents bindingNavigatorCountItem As System.Windows.Forms.ToolStripLabel
    Friend WithEvents ToolStripSeparator2 As System.Windows.Forms.ToolStripSeparator
    Friend WithEvents BTannule As System.Windows.Forms.ToolStripButton
    Friend WithEvents ToolTip1 As System.Windows.Forms.ToolTip
    Friend WithEvents BindingNavigator1 As System.Windows.Forms.BindingNavigator
    Friend WithEvents BTeffacer As System.Windows.Forms.ToolStripButton
    Friend WithEvents BTsauve As System.Windows.Forms.ToolStripButton
    Friend WithEvents ToolStripSeparator4 As System.Windows.Forms.ToolStripSeparator
    Friend WithEvents BTimprime As System.Windows.Forms.ToolStripButton
    Friend WithEvents bindingNavigatorSeparator2 As System.Windows.Forms.ToolStripSeparator
    Friend WithEvents BTdebut As System.Windows.Forms.ToolStripButton
    Friend WithEvents BTprecedent As System.Windows.Forms.ToolStripButton
    Friend WithEvents bindingNavigatorSeparator As System.Windows.Forms.ToolStripSeparator
    Friend WithEvents bindingNavigatorPositionItem As System.Windows.Forms.ToolStripTextBox
    Friend WithEvents bindingNavigatorSeparator1 As System.Windows.Forms.ToolStripSeparator
    Friend WithEvents BTprochain As System.Windows.Forms.ToolStripButton
    Friend WithEvents BTfin As System.Windows.Forms.ToolStripButton
    Friend WithEvents ToolStripSeparator3 As System.Windows.Forms.ToolStripSeparator
    Friend WithEvents BTaide As System.Windows.Forms.ToolStripButton
    Friend WithEvents toolStripSeparator As System.Windows.Forms.ToolStripSeparator
    Friend WithEvents ToolStripLabel1 As System.Windows.Forms.ToolStripLabel
    Friend WithEvents toolStripSeparator1 As System.Windows.Forms.ToolStripSeparator
    Friend WithEvents Tclientliv As System.Windows.Forms.TextBox
    Friend WithEvents Tcommis As System.Windows.Forms.TextBox
    Friend WithEvents Tclient As System.Windows.Forms.TextBox
    Friend WithEvents Ddateouverture As System.Windows.Forms.DateTimePicker
    Friend WithEvents Label2 As System.Windows.Forms.Label
    Friend WithEvents Ddaterequis As System.Windows.Forms.DateTimePicker
    Friend WithEvents Tajoutdepot As System.Windows.Forms.TextBox
    Friend WithEvents Label21 As System.Windows.Forms.Label
    Friend WithEvents Ttransport As System.Windows.Forms.TextBox
    Friend WithEvents Label22 As System.Windows.Forms.Label
    Friend WithEvents Ttotal As System.Windows.Forms.TextBox
    Friend WithEvents Ttps As System.Windows.Forms.TextBox
    Friend WithEvents Ttvq As System.Windows.Forms.TextBox
    Friend WithEvents Tnocom As System.Windows.Forms.TextBox
    Friend WithEvents Tgtotal As System.Windows.Forms.TextBox
    Friend WithEvents Label25 As System.Windows.Forms.Label
    Friend WithEvents Tdepot As System.Windows.Forms.TextBox
    Friend WithEvents Tentrepot As System.Windows.Forms.TextBox
    Friend WithEvents Label46 As System.Windows.Forms.Label
    Friend WithEvents Label26 As System.Windows.Forms.Label
    Friend WithEvents Label45 As System.Windows.Forms.Label
    Friend WithEvents Tnoachat As System.Windows.Forms.TextBox
    Friend WithEvents Label44 As System.Windows.Forms.Label
    Friend WithEvents Label43 As System.Windows.Forms.Label
    Friend WithEvents Btclientliv As System.Windows.Forms.Button
    Friend WithEvents Button3 As System.Windows.Forms.Button
    Friend WithEvents BCommis As System.Windows.Forms.Button
    Friend WithEvents Bvendeur As System.Windows.Forms.Button
    Friend WithEvents Tnocomrech As System.Windows.Forms.TextBox
    Friend WithEvents Label47 As System.Windows.Forms.Label
    Friend WithEvents Tprovinceliv As System.Windows.Forms.TextBox
    Friend WithEvents lfd As System.Windows.Forms.Label
    Friend WithEvents Tprovince As System.Windows.Forms.TextBox
    Friend WithEvents Tville As System.Windows.Forms.TextBox
    Friend WithEvents Tcodepostal As System.Windows.Forms.TextBox
    Friend WithEvents Ttelephone As System.Windows.Forms.TextBox
    Friend WithEvents Tfax As System.Windows.Forms.TextBox
    Friend WithEvents Tadresse2 As System.Windows.Forms.TextBox
    Friend WithEvents Tadresse1 As System.Windows.Forms.TextBox
    Friend WithEvents Tnom As System.Windows.Forms.TextBox
    Friend WithEvents Label10 As System.Windows.Forms.Label
    Friend WithEvents Label9 As System.Windows.Forms.Label
    Friend WithEvents Label7 As System.Windows.Forms.Label
    Friend WithEvents Label6 As System.Windows.Forms.Label
    Friend WithEvents Label5 As System.Windows.Forms.Label
    Friend WithEvents Label4 As System.Windows.Forms.Label
    Friend WithEvents Button4 As System.Windows.Forms.Button
    Friend WithEvents SolGrid1 As Inventaire.SolGrid
    Friend WithEvents Label39 As System.Windows.Forms.Label
    Friend WithEvents Label12 As System.Windows.Forms.Label
    Friend WithEvents Label11 As System.Windows.Forms.Label
    Friend WithEvents Tadresse1liv As System.Windows.Forms.TextBox
    Friend WithEvents Tadresse2liv As System.Windows.Forms.TextBox
    Friend WithEvents Tfaxliv As System.Windows.Forms.TextBox
    Friend WithEvents Ttelephoneliv As System.Windows.Forms.TextBox
    Friend WithEvents Tcodepostalliv As System.Windows.Forms.TextBox
    Friend WithEvents Tvilleliv As System.Windows.Forms.TextBox
    Friend WithEvents Label18 As System.Windows.Forms.Label
    Friend WithEvents Label14 As System.Windows.Forms.Label
    Friend WithEvents Label42 As System.Windows.Forms.Label
    Friend WithEvents Label41 As System.Windows.Forms.Label
    Friend WithEvents Label40 As System.Windows.Forms.Label
    Friend WithEvents Label38 As System.Windows.Forms.Label
    Friend WithEvents Tnomliv As System.Windows.Forms.TextBox
    Friend WithEvents Label17 As System.Windows.Forms.Label
    Friend WithEvents Label15 As System.Windows.Forms.Label
    Friend WithEvents LblVendu As System.Windows.Forms.Label
    Friend WithEvents BRectangleHaut As System.Windows.Forms.Button
    Friend WithEvents TxtTermes As System.Windows.Forms.TextBox
    Friend WithEvents TxtExpediteur As System.Windows.Forms.TextBox
    Friend WithEvents LblStatus As System.Windows.Forms.Label
    Friend WithEvents LblCollect As System.Windows.Forms.Label
    Friend WithEvents Txtstatus As System.Windows.Forms.TextBox
    Friend WithEvents Txtcollect As System.Windows.Forms.TextBox
    Friend WithEvents BRectangleBas As System.Windows.Forms.Button
    Friend WithEvents LblDivers As System.Windows.Forms.Label
    Friend WithEvents TxtDivers As System.Windows.Forms.TextBox
    Friend WithEvents LblEscompte As System.Windows.Forms.Label
    Friend WithEvents TxtEscompte As System.Windows.Forms.TextBox
    Public WithEvents TabTotal As System.Windows.Forms.TabControl
    Public WithEvents Shape6 As System.Windows.Forms.Label
    Public WithEvents LblQuantite As System.Windows.Forms.Label
    Public WithEvents LblQmain As System.Windows.Forms.Label
    Public WithEvents LblQcom As System.Windows.Forms.Label
    Public WithEvents LblEncom As System.Windows.Forms.Label
    Public WithEvents Shape7 As System.Windows.Forms.Label
    Public WithEvents LblAttendu As System.Windows.Forms.Label
    Public WithEvents LblProduitTab As System.Windows.Forms.Label
    Public WithEvents TxtCat As System.Windows.Forms.TextBox
    Public WithEvents TxtQmain As System.Windows.Forms.TextBox
    Public WithEvents TxtQcom As System.Windows.Forms.TextBox
    Public WithEvents TxtEncom As System.Windows.Forms.TextBox
    Public WithEvents TxtAttendu As System.Windows.Forms.TextBox
    Public WithEvents TxtPrix5 As System.Windows.Forms.TextBox
    Public WithEvents TxtPrix4 As System.Windows.Forms.TextBox
    Public WithEvents TxtPrix3 As System.Windows.Forms.TextBox
    Public WithEvents TxtPrix2 As System.Windows.Forms.TextBox
    Public WithEvents TxtPrix1 As System.Windows.Forms.TextBox
    Public WithEvents TxtPar1 As System.Windows.Forms.TextBox
    Public WithEvents TabTotal_TabPage2 As System.Windows.Forms.TabPage
    Public WithEvents LblAge As System.Windows.Forms.Label
    Public WithEvents LblA1 As System.Windows.Forms.Label
    Public WithEvents LblA2 As System.Windows.Forms.Label
    Public WithEvents LblA3 As System.Windows.Forms.Label
    Public WithEvents LblA4 As System.Windows.Forms.Label
    Public WithEvents LblA5 As System.Windows.Forms.Label
    Public WithEvents TxtA1 As System.Windows.Forms.TextBox
    Public WithEvents TxtA2 As System.Windows.Forms.TextBox
    Public WithEvents TxtA3 As System.Windows.Forms.TextBox
    Public WithEvents TxtA4 As System.Windows.Forms.TextBox
    Public WithEvents TxtA5 As System.Windows.Forms.TextBox
    Friend WithEvents LblDisponible As System.Windows.Forms.Label
    Friend WithEvents TxtDispo As System.Windows.Forms.TextBox
    Friend WithEvents Txtvendeur As System.Windows.Forms.TextBox
    Friend WithEvents Button5 As System.Windows.Forms.Button
    Friend WithEvents Button6 As System.Windows.Forms.Button
    Friend WithEvents bidon As System.Windows.Forms.TextBox
    Friend WithEvents ToolStrip1 As System.Windows.Forms.ToolStrip
    Friend WithEvents BAjout As System.Windows.Forms.ToolStripButton
    Friend WithEvents Beffacer As System.Windows.Forms.ToolStripButton
    Friend WithEvents BCatalog As System.Windows.Forms.ToolStripButton
    Friend WithEvents Binfo As System.Windows.Forms.ToolStripButton
    Friend WithEvents ToolStrip2 As System.Windows.Forms.ToolStrip
    Friend WithEvents BtImpSoum As System.Windows.Forms.ToolStripButton
    Friend WithEvents BtFacture As System.Windows.Forms.ToolStripButton
    Friend WithEvents ToolStrip3 As System.Windows.Forms.ToolStrip
    Friend WithEvents BtTermes As System.Windows.Forms.ToolStripButton
    Friend WithEvents ToolStrip4 As System.Windows.Forms.ToolStrip
    Friend WithEvents BtVia As System.Windows.Forms.ToolStripButton
    Public WithEvents TxtLocat As System.Windows.Forms.TextBox
    Friend WithEvents lblLocat As System.Windows.Forms.Label
    Friend WithEvents ToolStrip5 As System.Windows.Forms.ToolStrip
    Friend WithEvents BClient As System.Windows.Forms.ToolStripButton
    Friend WithEvents Bhistorique As System.Windows.Forms.ToolStripButton
    Friend WithEvents Binsere As System.Windows.Forms.ToolStripButton
    Friend WithEvents Bttrieproduit As System.Windows.Forms.ToolStripButton
    Friend WithEvents Pgrid As Inventaire.SolGrid
    Friend WithEvents TsProfit As System.Windows.Forms.ToolStrip
    Friend WithEvents Bprofit As System.Windows.Forms.ToolStripButton
    Friend WithEvents btnroute As System.Windows.Forms.ToolStripButton
    Friend WithEvents Lblroute As System.Windows.Forms.Label
    Friend WithEvents Lblroutedef As System.Windows.Forms.Label
    Friend WithEvents Tstotal As System.Windows.Forms.TextBox
    Friend WithEvents ToolStrip9 As System.Windows.Forms.ToolStrip
    Friend WithEvents BtDepot As System.Windows.Forms.ToolStripButton
    Friend WithEvents BtnSubstitut As System.Windows.Forms.ToolStripButton
    Friend WithEvents LblMag As System.Windows.Forms.Label
    Friend WithEvents BtnMultisite As System.Windows.Forms.ToolStripButton
    Friend WithEvents Label1 As System.Windows.Forms.Label
    Friend WithEvents btnconnaissement As System.Windows.Forms.ToolStripButton
    Friend WithEvents lblnbimp As System.Windows.Forms.Label
    Friend WithEvents Btncomfact As System.Windows.Forms.Button
    Friend WithEvents BTFournis As System.Windows.Forms.ToolStripButton
    Friend WithEvents ToolTip2 As System.Windows.Forms.ToolTip
    Protected WithEvents Btenvoieoutlook As System.Windows.Forms.ToolStripButton
    Friend WithEvents PictureBox2 As PictureBox
    Friend WithEvents Btnlocalisateurproduit As ToolStripButton
    Friend WithEvents Btnnapa As ToolStripButton
    Friend WithEvents BtCreation As ToolStripButton
    Friend WithEvents Btnmajdesprix As Button
    Friend WithEvents Btnbarcodeauto As Button
End Class


Public Class FrmPieceCommande


#Region "Déclaration des variables"
    Dim ActiverBarcodeautomatique As Boolean = False
    Dim tbb2 As System.Windows.Forms.Control
    Dim Bcommenceligne As Boolean = False
    Dim genrem As Boolean
    Dim trouvrem As Boolean
    Dim bsourceenteteCom As New BindingSource
    'pour calcul de taxe provinciale
    Dim prosufed As Integer 'si on ajoute tps sur tvq 0 si non 1 si oui
    Dim tauxtvqs As Double ' taux taxe prov de livraison
    Dim btajoutcli As Boolean
    Dim lang4 As String
    Dim creer As Boolean 'savoir quand creer une nouvelle ligne dans cell validated ou row validated cas de divers et main d'oeuvre
    Dim sollignefocus As Integer ' index de la ligne dans la grille ayant le focus lors de la sortie
    Dim solcelfocus As Integer 'la cellule ayant le focus
    Dim BonTrav As Boolean
    Dim tauxfournis As Double
    Dim cl_interne10 As String
    Dim DCompteur As Integer = 10000
    Dim Dancienneqte As Double = 0
    Dim Bancienneqte As Boolean = False
    Dim comboboxTravail As New DataGridViewComboBoxColumn()
    Dim IndexT As Integer = 0
    Dim Bcellchanged As Boolean = True
    Dim Bafficheseulement As Boolean = False
    Dim BnouveauBT As Boolean = False
    Dim Imprimeouinon As Boolean = False
    Dim BAfficheDepart As Boolean = False
    Dim tbb As System.Windows.Forms.Control
    Dim efflignevide As Boolean
    Dim promener As Boolean
    Dim gridfocus As Boolean
    Dim dnarr As Boolean
    Dim uparr As Boolean = False 'is clef ver haut dans la grille pour derniere ligne vide
    Dim lfarr As Boolean = False 'fleche gauche
    Dim pgup As Boolean
    Dim pgdn As Boolean
    Dim dscotete1 As DataTable = New DataSetInventaire.TCoteteDataTable
    Dim dscomma1 As DataTable = New DataSetInventaire.TCommaDataTable
    Dim quant_old() As Double
    Dim quant_paqbte() As Double
    Dim prod_old() As String
    Dim um_old() As String
    Dim quant_org() As Double
    Dim sauvage As Boolean
    Dim clientclick As Boolean
    Dim modifesc As Boolean
    Dim barcodeauto As Boolean 'declaneche barcode auto
    Dim peueffacer As Boolean
    Dim peumodifier As Boolean
    Dim peunouveau As Boolean
    Dim entrepotold As String = "*"
    Dim DsPoids As New DataTable 'pour la viande contient les poids
    Dim inserelig As Boolean
    Dim insererfiche As Double = -1
    Dim prodarret As Boolean 'arreter si on change le produti
    Dim arretbar As Boolean 'si on arrete sur quantite lors de barcode auto
    Dim ancienclient As String = ""

    Dim solrow As Integer = -1
    Dim solcol As Integer = -1
    Dim trclicom As Boolean
    Dim impcom As String = "" 'pour impression si f12 sans faire f5
#End Region
#Region "Load"

    Private Sub FrmBonTravail_Load(ByVal sender As Object, ByVal e As System.EventArgs) Handles Me.Load
        '  If My.Settings.napaurl.Trim <> "" Then Btnnapa.Visible = True
        'LUnite.Text = rm.GetString("LUnite", New CultureInfo("en-US"))
        If My.Settings.napaurl.Trim <> "" Then
            Btnnapa.Enabled = False
            Btnnapa.Visible = True
        Else
            Btnnapa.Visible = False
        End If

        Bencommandeclient = False
        Benmodification = False
        Bafficheseulement = False
        SysOpen(fcotete)
        SysOpen(fcomma)
        Pgrid.Visible = False
        'Dim dscotete11 As New datatable =dscotete1
        'definition des la table des poids
        DsPoids.Columns.Add(New DataColumn("code", GetType(String)))
        DsPoids.Columns.Add(New DataColumn("poidv", GetType(String)))
        DsPoids.Columns.Add(New DataColumn("paq_bte", GetType(String)))
        dscotete1.Clear()
        dscomma1.Clear()
        SetEcran(Me)
        BAjout.Visible = False
        If AVBcs(AVBfiditemstub("RECH1", AVB + fCompagni, 0)).Trim = "" Then
            Btnlocalisateurproduit.Visible = False
        End If
        langue()
        DisableEcran()
        promener = True
        AVBSTAT = AVBread(AVB + fCompagni, 1)
        BonTrav = True
        If gespoids10 = oui10 Then BtFacture.Visible = False
        Definitionsolgrid1()
        BindEnteteBT()
        affichebTbinding()
        TabTotal.SelectTab(1)
        TabTotal.TabPages(1).Show()

        If AVBcs(AVBfiditemstub("RECH1", AVB + fCompagni, 0)).Trim = "" Then
            Btnlocalisateurproduit.Visible = False
        End If


        SysOpen(fcor)
        AVBSTAT = AVBread(AVB + fcor, 0)
        LblA1.Text = Trim(AVBcs(AVBfiditemstub("DESC1", AVB + fcor, 0)))
        LblA2.Text = Trim(AVBcs(AVBfiditemstub("DESC2", AVB + fcor, 0)))
        LblA3.Text = Trim(AVBcs(AVBfiditemstub("DESC3", AVB + fcor, 0)))
        LblA4.Text = Trim(AVBcs(AVBfiditemstub("DESC4", AVB + fcor, 0)))
        LblA5.Text = Trim(AVBcs(AVBfiditemstub("DESC5", AVB + fcor, 0)))
        '        LblA6.Text = Trim(AVBcs(AVBfiditemstub("DESC6", AVB + fcor, 0)))
        SysClose(fcor)
        If troptit = False Then
            peueffacer = dsrutilisateurcli.Item("commandee")
            peunouveau = dsrutilisateurcli.Item("commanden")
            peumodifier = dsrutilisateurcli.Item("commandem")
        End If
        If dsrutilisateur.Item("tousacces") = True Then
            peueffacer = True
            peunouveau = True
            peumodifier = True
        End If
        ico_promener(True)
        Me.BtImpSoum.Enabled = False
        If ent10 > 1 Then Tentrepot.BackColor = Color.LemonChiffon
        SolGrid1.ClearSelection()
        Tnocomrech.Focus()
        Tnocomrech.Select()
    End Sub
    Private Sub langue()
        navigateurlang()
        If lang = "F" Then

            BAjout.Text = "F4 - Nouvelle ligne sur la commande"
            BCatalog.Text = "Alt-F7 - Visionnement du catalogue"
            BCommis.Text = "Commis"
            Beffacer.Text = "SF9 - Effacer le produit sélectionné"
            Binfo.Text = "F6 - Visionnement de l'information sur le produit sélectionné"
            Binsere.ToolTipText = "Insérer [F7]"
            BTeffacer.ToolTipText = "Effacer la Commande [F9]"
            BtFacture.Text = "Shift-F7 Facturation"
            BTimprime.ToolTipText = "Imprimer [F12]"
            BtImpSoum.Text = "Importation Soumis."
            BTmodifier.ToolTipText = "Modifier [F11]"
            btnconnaissement.Text = "Connaissement"
            BtTermes.Text = "Termes"
            BtCreation.ToolTipText = "SF6 Créer un produit"
            Bttrieproduit.Text = "Alt-F5 Trier en ordre de produit"
            Bvendeur.Text = "Vendeur"
            Label1.Text = "Bon de commande"
            Label10.Text = "Nom"
            Label11.Text = "Nom"
            Label12.Text = "Adresse"
            Label14.Text = "Ville"
            Label15.Text = "Code Postal"
            Label18.Text = "Livré à"
            Label2.Text = "Nº commande"
            Label21.Text = "Entrepôt"
            Label22.Text = "Nº d'achat"
            Label25.Text = "Date d'ouverture"
            Label26.Text = "Date Requis"
            Label38.Text = "Téléphone"
            Label41.Text = "T.V.P"
            Label42.Text = "T.V.F"
            Label43.Text = "Sous-Total"
            Label44.Text = "Ajout de dépot"
            Label45.Text = "Dépot"
            Label5.Text = "Téléphone"
            Label7.Text = "Ville"
            Label9.Text = "Adresse"
            LblAge.Text = "_________________    Age des comptes  _______________"
            LblAttendu.Text = "Dte. Attendue"
            LblDisponible.Text = "Disponible"
            LblDivers.Text = "Divers"
            LblEncom.Text = "Attendue(s)"
            LblEscompte.Text = "Escompte"
            lblLocat.Text = "Localisation"
            lblnbimp.Text = "Nb. Printing"
            LblProduitTab.Text = "   U/M                  Prix(1)      Prix(2)       Prix(3)      Prix(4)     Prix(5)    "
            LblQcom.Text = "Commandées:"
            LblQmain.Text = "En main:"
            LblQuantite.Text = "Quantités"
            LblVendu.Text = "Vendu à"
            Me.Text = "Commandes client Entrez / Modification"
            TabTotal.TabPages.Item(0).Text = "- Produit"
            TabTotal.TabPages.Item(1).Text = "- Client"
            ToolStripLabel1.Text = "Recherche de commandes"


        Else
            BtCreation.ToolTipText = "SF6 Create a product"
            BAjout.Text = "F4 - New line in this order"
            BCatalog.Text = "Alt-F7 - View the catalog"
            BCommis.Text = "Clerk"
            Beffacer.Text = "SF9 - Erase the selected product line"
            Binfo.Text = "F6 - Visualize information on the selected product"
            Binsere.ToolTipText = "Insert [F7]"
            BTeffacer.ToolTipText = "Delete order [F9]"
            BtFacture.Text = "Shift-F7 Billing"
            BTimprime.ToolTipText = "Print [F12]"
            BtImpSoum.Text = "Import Quotes"
            BTmodifier.ToolTipText = "Edit [F11]"
            btnconnaissement.Text = "Bill of lading"
            BtTermes.Text = "Terms"
            Bttrieproduit.Text = "Alt-F5 Sort by order of product "
            Bvendeur.Text = "Salesman"
            Label1.Text = "Order Entry"
            Label10.Text = "Name"
            Label11.Text = "Name"
            Label12.Text = "Address"
            Label14.Text = "City"
            Label15.Text = "Postal Code"
            Label18.Text = "Shipped to"
            Label2.Text = "Order Nº"
            Label21.Text = "Whse"
            Label22.Text = "Purchasing Order Nº"
            Label25.Text = "Opening Date"
            Label26.Text = "Date Required"
            Label38.Text = "Phone"
            Label41.Text = "P.S.T"
            Label42.Text = "F.S.T"
            Label43.Text = "Subtotal"
            Label44.Text = "Adding deposit"
            Label45.Text = "Deposit"
            Label5.Text = "Phone"
            Label7.Text = "City"
            Label9.Text = "Address"
            LblAge.Text = "_________________    Age of Accounts    _______________"
            LblAttendu.Text = "Expected Dte."
            LblDisponible.Text = "Available"
            LblDivers.Text = "Misc."
            LblEncom.Text = "Expected"
            LblEscompte.Text = "Discount"
            lblLocat.Text = "Location"
            lblnbimp.Text = "Nb. Printing"
            LblProduitTab.Text = "   U/M                 Price(1)     Price(2)      Price(3)     Price(4)    Price(5)   "
            LblQcom.Text = "Ordered:"
            LblQmain.Text = "On hand:"
            LblQuantite.Text = "Quantity"
            LblVendu.Text = "Sold to"
            Me.Text = "Customer Order entry / Modification"
            TabTotal.TabPages.Item(0).Text = "- Product"
            TabTotal.TabPages.Item(1).Text = "- Customer"
            ToolStripLabel1.Text = "Order search"

        End If

        'Me.Text = "Commandes client Entrez / Modification"
        'Binsere.ToolTipText = "Insérer [F7]"
        'BAjout.Text = "F4 - Nouvelle ligne sur la commande"
        ''ToolTip1.SetToolTip(Beffacer, "Effacer [SF9]")
        ''ToolTip1.SetToolTip(BAjout, "Ajouter une ligne [F4]")
        ''ToolTip1.SetToolTip(Binfo, "Information sur produit [F6]")
        ''ToolTip1.SetToolTip(BCatalog, "Catalogue [AF7]")
        'ToolStripLabel1.Text = "Recherche de commandes"
        'LblVendu.Text = "Vendu à"
        'Label18.Text = "Livré à"
        'Label10.Text = "Nom"
        'Label11.Text = "Nom"
        'Label9.Text = "Adresse"
        'Label12.Text = "Adresse"
        'Beffacer.Text = "SF9 - Effacer le produit sélectionné"
        'Binfo.Text = "F6 - Visionnement de l'information sur le produit sélectionné"
        'BCatalog.Text = "Alt-F7 - Visionnement du catalogue"
        'LblQmain.Text = "En main:"
        'LblQuantite.Text = "Quantités"
        'LblQcom.Text = "Commandées:"
        'LblEncom.Text = "Attendue(s)"
        'LblAttendu.Text = "Dte. Attendue"
        'BtTermes.Text = "Termes"
        'LblProduitTab.Text = "   U/M                  Prix(1)      Prix(2)       Prix(3)      Prix(4)     Prix(5)    "
        ''CmdDrop.Text = "Drop inactif"
        'LblAge.Text = "_________________    Age des comptes  _______________"
        'TabTotal.TabPages.Item(0).Text = "- Produit"
        'TabTotal.TabPages.Item(1).Text = "- Client"
        'LblDivers.Text = "Divers"
        'LblDisponible.Text = "Disponible"
        'BtImpSoum.Text = "Importation Soumis."
        'Label2.Text = "No. commande"
        'lblLocat.Text = "Localisation"
        'Label1.Text = "Bon de commande"
        'BtFacture.Text = "Shift-F7 Facturation"
        'Bttrieproduit.Text = "Alt-F5 Trier en ordre de produit"
        'Label12.Text = "Adresse"
        'Label14.Text = "Ville"
        'Label15.Text = "Code Postal"
        'Label38.Text = "Téléphone"
        'Label5.Text = "Téléphone"
        'Label7.Text = "Ville"
        'Label21.Text = "Entrepôt"
        'Label22.Text = "No. d'achat"
        'Bvendeur.Text = "Vendeur"
        'BCommis.Text = "Commis"
        'Label25.Text = "Date d'ouverture"
        'Label26.Text = "Date Requis"
        'LblEscompte.Text = "Escompte"
        'Label44.Text = "Ajout de dépot"
        'Label43.Text = "Sous-Total"
        'Label45.Text = "Dépot"
        'Label42.Text = "T.V.F"
        'Label41.Text = "T.V.P"

        'Else
        'btnconnaissement.Text = "Bill of landing"
        'lblnbimp.Text = "Nb. Printing"
        'Label41.Text = "P.S.T"
        'Label42.Text = "F.S.T"
        'Label45.Text = "Deposit"
        'Label43.Text = "Subtotal"
        'Label44.Text = "Adding deposit"
        'LblEscompte.Text = "Discount"
        'Label26.Text = "Date Required"
        'Label25.Text = "Opening Date"
        'BCommis.Text = "Cleck"
        'Bvendeur.Text = "Salesman"
        'Label22.Text = "Purchasing Order #"

        'Label21.Text = "Whse"
        'Label7.Text = "City"
        'Label5.Text = "Phone"
        'Label38.Text = "Phone"
        'Label15.Text = "Postal Code"
        'Label14.Text = "City"
        'Label12.Text = "Adress"
        'Bttrieproduit.Text = "Alt-F5 Sort order of product "
        'BtFacture.Text = "Shift-F7 Billing"
        'Label1.Text = "     Order Entry"
        'lblLocat.Text = "Location"
        'Label2.Text = "Order No."
        'BtImpSoum.Text = "Quote Import"
        ''ToolTip1.SetToolTip(Beffacer, "Delete line [SF9]")
        ''ToolTip1.SetToolTip(BCatalog, "Catalog [AF7]")
        ''ToolTip1.SetToolTip(Binfo, "Product information [F6]")
        '' ToolTip1.SetToolTip(BAjout, "Add a line [F4]")
        'LblDisponible.Text = "Available"
        'LblDivers.Text = "Various"
        'BtTermes.Text = "Terms"
        'TabTotal.TabPages.Item(0).Text = "- Product"
        'TabTotal.TabPages.Item(1).Text = "- Client"
        'LblAge.Text = "_________________    Account aging    _______________"
        '' CmdDrop.Text = "Inactive drops"
        'LblProduitTab.Text = "   U/M                 Price(1)     Price(2)      Price(3)     Price(4)    Price(5)   "
        'LblAttendu.Text = "Expected Dte."
        'LblEncom.Text = "Expected"
        'LblQcom.Text = "Ordered:"
        'LblQuantite.Text = "Quantity"
        'LblQmain.Text = "On hand:"
        '' LblDispo.Text = "Available"
        'Me.Text = "Order entry / Modification"
        'BCatalog.Text = "Alt-F7 - View the catalog"
        'Binfo.Text = "F6 - Visualize information on the selected product"
        'Beffacer.Text = "SF9 - Erase the selected product line"
        'BAjout.Text = "F4 - New line in this order"
        'Label2.Text = "Order N"
        'Label9.Text = "Address"
        'Label11.Text = "Name"
        'Label10.Text = "Name"
        'Label18.Text = "Shipped to"
        'LblVendu.Text = "Sold to"
        'ToolStripLabel1.Text = "Order search"
        'Binsere.ToolTipText = "Insert [F7]"
        'BTmodifier.ToolTipText = "Edit [F11]"
        'BTimprime.ToolTipText = "Print [F12]"
        'BTeffacer.ToolTipText = "Delete order [F9]"

    End Sub
    Private Sub navigateurlang()
        With BindingNavigator1
            If lang = "F" Then
                BTaide.ToolTipText = "Aide [ F1 ]"
                BTannule.ToolTipText = "Annuler [F2]"
                BTdebut.ToolTipText = "Début [ Ctrl PgUp ]"
                BTeffacer.ToolTipText = "Effacer [F9]"
                BTfin.ToolTipText = "Fin [ Ctrl PgDn ]"
                BTimprime.ToolTipText = "Imprimer [F12]"
                BTmodifier.ToolTipText = "Modifier [F11]"
                BTnouveau.ToolTipText = "Nouveau [F4]"
                BTprecedent.ToolTipText = "Précédent [ PgUp ]"
                BTprochain.ToolTipText = "Prochain [ PgDn ]"
                BTsauve.ToolTipText = "Enregistrer [F5]"
            Else
                BTaide.ToolTipText = "Help [ F1 ]"
                BTannule.ToolTipText = "Cancel [F2]"
                BTdebut.ToolTipText = "Start [ Ctrl PgUp ]"
                BTeffacer.ToolTipText = "Delete [F9]"
                BTfin.ToolTipText = "End [ Ctrl PgDn ]"
                BTimprime.ToolTipText = "Print [F12]"
                BTmodifier.ToolTipText = "Edit [F11]"
                BTnouveau.ToolTipText = "New [F4]"
                BTprecedent.ToolTipText = "Previous [ PgUp ]"
                BTprochain.ToolTipText = "Next [ PgDn ]"
                BTsauve.ToolTipText = "Save [F5]"
            End If
        End With
    End Sub
    Private Sub ico_promener(ByVal acces As Boolean)
        BTprochain.Enabled = acces
        BTprecedent.Enabled = acces
        BTdebut.Enabled = acces
        BTfin.Enabled = acces
        BTnouveau.Enabled = acces
        BTmodifier.Enabled = acces
        Me.Btnmajdesprix.Enabled = acces
        If dscotete1.Rows.Count <= 0 Then BTmodifier.Enabled = False
        BTeffacer.Enabled = Not (acces)
        BTannule.Enabled = Not (acces)
        BTsauve.Enabled = Not (acces)
        BTimprime.Enabled = True
        BtFacture.Enabled = acces
        '    BtCreation.Enabled = Not (acces)
        Btncomfact.Enabled = acces
        ToolStrip1.Enabled = Not (acces)
        Me.BtImpSoum.Enabled = False

        If troptit = False Then
            If peunouveau = False Then BTnouveau.Visible = peunouveau
            If peumodifier = False Then BTmodifier.Visible = peumodifier
            If peueffacer = False Then BTeffacer.Visible = peueffacer
            If peunouveau = False Or peueffacer = False Or peumodifier = False Then Bprofit.Visible = False
        End If
     
    End Sub
#End Region
#Region "Setup"
    'pour capturer les clefs de la grid
    Protected Overrides Function ProcessCmdKey(ByRef msg As Message, ByVal keyData As Keys) As Boolean
        If SolGrid1.ContainsFocus = True Then
            pgup = False
            pgdn = False
            uparr = False
            dnarr = False
            lfarr = False
            Const WM_KEYDOWN As Integer = 256
            Const WM_SYSKEYDOWN As Integer = 260
            If ((msg.Msg = WM_KEYDOWN) _
                        OrElse (msg.Msg = WM_SYSKEYDOWN)) Then
                Select Case (keyData)
                    Case Keys.Escape
                        Return True
                    Case Keys.Down
                        If inserelig = True Then
                            If lang = "F" Then MsgBox("Vous êtes en mode insertion. Complétez la ligne avant de modifier autre chose")
                            If lang <> "F" Then MsgBox("Complete the line before modifying anything else, you are in Edit Mode")
                            Return True
                        End If
                        dnarr = True
                        If SolGrid1.CurrentRow.Index <> SolGrid1.Rows.Count - 1 Then
                            SolGrid1.CurrentRow.Cells("produit").Value = prod_old(SolGrid1.CurrentRow.Index)
                            SolGrid1.CurrentRow.Cells("quantite").Value = Val(quant_old(SolGrid1.CurrentRow.Index))
                            SolGrid1.CurrentRow.Cells("paq_bte").Value = Val(quant_paqbte(SolGrid1.CurrentRow.Index))
                            SolGrid1.RefreshEdit()
                        End If
                        Dim lig As Integer = SolGrid1.CurrentRow.Index
                        If lig < SolGrid1.Rows.Count - 1 Then
                            posproduit(SolGrid1.Rows(lig + 1).Cells("produit").EditedFormattedValue.ToString, SolGrid1.Rows(lig + 1).Cells("um").EditedFormattedValue.ToString)
                        End If
                    Case Keys.Up
                        If inserelig = True Then
                            If lang = "F" Then MsgBox("Vous êtes en mode insertion. Complétez la ligne avant de modifier autre chose")
                            If lang <> "F" Then MsgBox("Complete the line before modifying anything else, you are in Edit Mode")
                            Return True
                        End If
                        uparr = True
                        If SolGrid1.CurrentRow.Index <> SolGrid1.Rows.Count - 1 Then
                            SolGrid1.CurrentRow.Cells("produit").Value = prod_old(SolGrid1.CurrentRow.Index)
                            SolGrid1.CurrentRow.Cells("quantite").Value = quant_old(SolGrid1.CurrentRow.Index)
                            SolGrid1.CurrentRow.Cells("paq_bte").Value = quant_paqbte(SolGrid1.CurrentRow.Index)
                            SolGrid1.RefreshEdit()
                        End If
                        Dim lig As Integer = SolGrid1.CurrentRow.Index
                        If lig > 0 Then
                            posproduit(SolGrid1.Rows(lig - 1).Cells("produit").EditedFormattedValue.ToString, SolGrid1.Rows(lig - 1).Cells("um").EditedFormattedValue.ToString)
                        End If
                    Case Keys.Left
                        lfarr = True
                    Case (Keys.Shift + Keys.Tab)
                        lfarr = True
                        keyData = Keys.Left
                        If SolGrid1.CurrentCell.ColumnIndex = SolGrid1.Columns("produit").Index Then
                            Return True
                        End If
                    Case Keys.PageDown
                        pgdn = True
                        SolGrid1.CurrentRow.Cells("produit").Selected = True
                        Dim lig As Integer = SolGrid1.CurrentRow.Index
                        posproduit(SolGrid1.Rows(lig).Cells("produit").EditedFormattedValue.ToString, SolGrid1.Rows(lig).Cells("um").EditedFormattedValue.ToString)
                    Case Keys.PageUp
                        pgup = True
                        SolGrid1.CurrentRow.Cells("produit").Selected = True
                        Dim lig As Integer = SolGrid1.CurrentRow.Index
                        posproduit(SolGrid1.Rows(lig).Cells("produit").EditedFormattedValue.ToString, SolGrid1.Rows(lig).Cells("um").EditedFormattedValue.ToString)
                        'Case Keys.NumLock
                        '    MessageBox.Show("NumLock")
                        'Case Keys.Escape
                        '    MessageBox.Show("Escape")
                    Case Keys.Enter
                        'remarque automatique
                        If SolGrid1.ContainsFocus = True Then
                            Dim noligne As Integer = SolGrid1.CurrentRow.Index
                            If Trim(SolGrid1.CurrentRow.Cells("produit").EditedFormattedValue.ToString) = "" _
                            And noligne <> 0 Then
                                If Mid(SolGrid1.Rows(noligne - 1).Cells("produit").EditedFormattedValue.ToString, 1, 3) = Mid(Rem10, 1, 3) Then
                                    SolGrid1.CurrentRow.Cells("produit").Value = SolGrid1.Rows(noligne - 1).Cells("produit").EditedFormattedValue.ToString
                                    SolGrid1.RefreshEdit()
                                End If
                            End If
                        End If
                End Select
                If keyData <> Keys.Enter And keyData <> Keys.Return _
                And SolGrid1.Columns("escompte").Index = SolGrid1.CurrentCell.ColumnIndex _
                And SolGrid1.CurrentRow.Index = SolGrid1.RowCount - 1 Then modifesc = True
            End If
        End If
        Return MyBase.ProcessCmdKey(msg, keyData)
    End Function
    Private Sub Definitionsolgrid1()
        With SolGrid1
            .AutoGenerateColumns = False
            .Columns.Add("produit", "produit")
            .Columns("Produit").Width = 170
            .Columns("Produit").DefaultCellStyle.Format.ToUpper()
            .Columns("produit").DefaultCellStyle.Alignment = DataGridViewContentAlignment.MiddleLeft
            .Columns("produit").DataPropertyName = dscomma1.Columns("Produit").ToString
            .Columns("produit").DefaultCellStyle.BackColor = Color.LemonChiffon
            .Columns("produit").SortMode = DataGridViewColumnSortMode.NotSortable
            .Columns.Add("description", "Description")
            .Columns("Description").Width = 310
            .Columns("description").DataPropertyName = dscomma1.Columns("description").ToString
            .Columns("description").SortMode = DataGridViewColumnSortMode.NotSortable
            .Columns.Add("dept", "Dept.")
            .Columns("dept").DefaultCellStyle.BackColor = Color.LightBlue
            .Columns("dept").HeaderCell.Style.Alignment = DataGridViewContentAlignment.MiddleCenter
            .Columns("dept").Width = 33
            .Columns("dept").DataPropertyName = dscomma1.Columns("dept").ToString
            .Columns("dept").SortMode = DataGridViewColumnSortMode.NotSortable
            .Columns("dept").ReadOnly = True
            .Columns.Add("um", "U/M")
            .Columns("UM").Width = 35
            .Columns("um").DataPropertyName = dscomma1.Columns("um").ToString
            .Columns("um").DefaultCellStyle.Alignment = DataGridViewContentAlignment.MiddleCenter
            .Columns("um").DefaultCellStyle.BackColor = Color.LemonChiffon
            .Columns("um").SortMode = DataGridViewColumnSortMode.NotSortable
            .Columns.Add("quantite", "quantite")
            .Columns("Quantite").Width = 50
            .Columns("quantite").HeaderCell.Style.Alignment = DataGridViewContentAlignment.MiddleRight
            .Columns("Quantite").DefaultCellStyle.Alignment = DataGridViewContentAlignment.MiddleRight
            .Columns("quantite").DataPropertyName = dscomma1.Columns("quantite").ToString
            .Columns("quantite").SortMode = DataGridViewColumnSortMode.NotSortable

            .Columns.Add("quantiteliv", "quantitel")
            .Columns("Quantiteliv").Width = 48
            .Columns("Quantiteliv").DefaultCellStyle.BackColor = Color.LightBlue
            .Columns("quantiteliv").HeaderCell.Style.Alignment = DataGridViewContentAlignment.MiddleRight
            .Columns("Quantiteliv").DefaultCellStyle.Alignment = DataGridViewContentAlignment.MiddleRight
            .Columns("quantiteliv").DataPropertyName = dscomma1.Columns("quantitelivre").ToString
            .Columns("quantiteliv").SortMode = DataGridViewColumnSortMode.NotSortable
            .Columns("quantiteliv").ReadOnly = True
            .Columns.Add("prix", "prix")
            .Columns("Prix").Width = 90
            .Columns("Prix").DefaultCellStyle.Alignment = DataGridViewContentAlignment.MiddleRight
            .Columns("prix").HeaderCell.Style.Alignment = DataGridViewContentAlignment.MiddleRight
            .Columns("prix").DataPropertyName = dscomma1.Columns("prix").ToString
            .Columns("Prix").DefaultCellStyle.Format = Masque_Vendant
            .Columns("prix").SortMode = DataGridViewColumnSortMode.NotSortable
            .Columns.Add("montant", "montant")
            .Columns("Montant").Width = 90
            .Columns("Montant").DefaultCellStyle.BackColor = Color.LightBlue
            .Columns("montant").DefaultCellStyle.Alignment = DataGridViewContentAlignment.MiddleRight
            .Columns("montant").HeaderCell.Style.Alignment = DataGridViewContentAlignment.MiddleRight
            .Columns("montant").DataPropertyName = dscomma1.Columns("montant").ToString
            .Columns("Montant").DefaultCellStyle.Format = format8
            .Columns("montant").SortMode = DataGridViewColumnSortMode.NotSortable
            .Columns.Add("escompte", "escompte")
            .Columns("Escompte").Width = 58
            .Columns("escompte").HeaderCell.Style.Alignment = DataGridViewContentAlignment.MiddleRight
            .Columns("Escompte").DefaultCellStyle.Alignment = DataGridViewContentAlignment.MiddleRight
            .Columns("escompte").DataPropertyName = dscomma1.Columns("escompte").ToString
            .Columns("escompte").SortMode = DataGridViewColumnSortMode.NotSortable
            .Columns.Add("status", "ST")
            .Columns("status").Width = 25
            .Columns("status").DataPropertyName = dscomma1.Columns("status").ToString
            .Columns("status").DefaultCellStyle.BackColor = Color.LightBlue
            .Columns("status").SortMode = DataGridViewColumnSortMode.NotSortable
            If lang = "F" Then
                .Columns("produit").HeaderText = "Produit"
                .Columns("Quantite").HeaderText = "Quantité"
                .Columns("Quantiteliv").HeaderText = "Quant. liv."
                .Columns("prix").HeaderText = "Prix"
                .Columns("montant").HeaderText = "Montant"
                .Columns("escompte").HeaderText = "Escompte"
            Else
                .Columns("Quantite").HeaderText = "Quantity"
                .Columns("Quantiteliv").HeaderText = "Del. Quant."
                .Columns("prix").HeaderText = "Price"
                .Columns("montant").HeaderText = "Amount"
                .Columns("produit").HeaderText = "Product"
                .Columns("escompte").HeaderText = "Discount"
            End If
            '            .Columns("quantite").DefaultCellStyle.Format = "n"


            '            .Columns("Escompte").DefaultCellStyle.Format = "n"
            .Columns.Add("taxe provincial", "taxe provincial")
            .Columns("Taxe provincial").DefaultCellStyle.Alignment = DataGridViewContentAlignment.MiddleRight
            '.Columns("Taxe provincial").DefaultCellStyle.Format = format7
            .Columns("taxe provincial").DataPropertyName = dscomma1.Columns("taxeprovincial").ToString
            .Columns.Add("taxe fédéral", "taxe fédéral")
            .Columns("Taxe fédéral").DefaultCellStyle.Alignment = DataGridViewContentAlignment.MiddleRight
            '.Columns("Taxe fédéral").DefaultCellStyle.Format = format7
            .Columns("taxe fédéral").DataPropertyName = dscomma1.Columns("taxefederal").ToString
            .Columns("Taxe provincial").Visible = False
            .Columns("Taxe fédéral").Visible = False
            .Columns.Add("no commande", "no commande")
            .Columns("no commande").DataPropertyName = dscomma1.Columns("Nocommande").ToString
            .Columns("No commande").Visible = False
            .Columns.Add("client", "client")
            .Columns("Client").Visible = False
            .Columns.Add("quantité livré", "quantite livre")
            .Columns("quantité Livré").Visible = False
            .Columns.Add("coutant", "coutant")
            .Columns("Coutant").Visible = False
            .Columns("coutant").DataPropertyName = DsComma.Columns("coutant").ToString
            .Columns.Add("Date Livré", "Date Livre")
            .Columns("Date Livré").Visible = False
            .Columns.Add("Date commandé", "Date commande")
            .Columns("Date commandé").Visible = False
            .Columns.Add("Poste Vente", "Poste Vente")
            .Columns("Poste Vente").Visible = False
            .Columns("poste vente").DataPropertyName = dscomma1.Columns("postevente").ToString
            .Columns.Add("Core oui", "Core oui")
            .Columns("Core oui").Visible = False
            .Columns.Add("groupe", "groupe")
            .Columns("groupe").Visible = False
            .Columns("groupe").DataPropertyName = dscomma1.Columns("groupe").ToString
            .Columns.Add("Ligne", "Ligne")
            .Columns("ligne").DataPropertyName = dscomma1.Columns("ligne").ToString
            .Columns("Ligne").Visible = False

            .Columns.Add("mult2", "mult2")
            .Columns("mult2").DataPropertyName = dscomma1.Columns("mult2").ToString
            .Columns("mult2").Visible = False
         
            .Columns.Add("ID", "ID")
            .Columns("ID").Visible = False
            .Columns.Add("Travail", "Travail")
            .Columns("Travail").Visible = False
            .Columns.Add("Newline", "Newline")
            .Columns("Newline").Visible = False
            .Columns("Montant").ReadOnly = True
            .Columns("Status").ReadOnly = True
            .Columns("UM").ReadOnly = True
            .Columns.Add("paq_bte", "paq_bte")
            .Columns("paq_bte").DataPropertyName = dscomma1.Columns("paq_bte").ToString
            .Columns("paq_bte").Visible = False

            .Columns.Add("sp", "sp")
            .Columns("sp").DataPropertyName = dscomma1.Columns("sp").ToString
            .Columns("sp").Visible = False


            .ReadOnly = False

        End With
    End Sub
    Private Sub Debarre()
        Tnocom.ReadOnly = True
    End Sub
    Private Sub DisableEcran()
        Dim ctl As Control
        For Each ctl In Me.Controls
            If ctl Is BTdebut Then

            Else
                If TypeOf ctl Is System.Windows.Forms.TextBox _
                Or (TypeOf ctl Is Button) Then

                    ctl.Enabled = False
                    ' ctl.BackColor = Color.White
                End If
            End If
        Next
        BTprochain.Enabled = True
        BTprecedent.Enabled = True
        BTdebut.Enabled = True
        BTfin.Enabled = True
        Ddateouverture.Enabled = False
        Ddaterequis.Enabled = False
        Me.SolGrid1.Enabled = False
        Me.Tnocomrech.Enabled = True
        Me.Bttrieproduit.Enabled = False
        bidon.Enabled = True

        'SolGrid1.ClearSelection()
        'SolGrid1.Enabled = True
        'SolGrid1.ReadOnly = True
    End Sub
    Private Sub EnableEcran()
        Dim ctl As Control
        For Each ctl In Me.Controls
            If TypeOf ctl Is System.Windows.Forms.TextBox _
            Or TypeOf ctl Is Button Then
                ctl.Enabled = True
            End If
        Next
        BtImpSoum.Enabled = False
        Me.Tnocomrech.Enabled = False
        Me.BTprochain.Enabled = False
        Me.BTprecedent.Enabled = False
        Me.BTdebut.Enabled = False
        Me.BTfin.Enabled = False
        Me.SolGrid1.Enabled = True
        Me.BTeffacer.Enabled = peueffacer
        Me.BTannule.Enabled = True
        Me.BTsauve.Enabled = True
        Me.BTimprime.Enabled = True
        Ddateouverture.Enabled = True
        Ddaterequis.Enabled = True
        Me.Bttrieproduit.Enabled = True
    End Sub
#End Region
#Region "Événement FrmBonTravail"
    Private Sub Frmbontravail_KeyPress(ByVal sender As Object, ByVal e As System.Windows.Forms.KeyPressEventArgs) Handles Me.KeyPress
        Dim keyascii As Integer = Asc(e.KeyChar)
        tbb = ActiveControl
        FldEntry(keyascii, tbb)
        If keyascii = 0 Then
            e.Handled = True
        End If
    End Sub
    Private Sub FrmBonTravail_KeyDown(ByVal sender As Object, ByVal e As System.Windows.Forms.KeyEventArgs) Handles Me.KeyDown

        Dim Shift As Integer = e.KeyData \ &H10000
        Dim clefshift As Integer
        uparr = False
        dnarr = False
        pgup = False
        pgdn = False
        lfarr = False
        clefshift = Shift And 7
        Select Case clefshift
            Case 0
                If e.KeyCode = Keys.Escape Then
                    sortir()
                ElseIf e.KeyCode = Keys.F2 Then
                    If BTannule.Enabled = True Then ProcedureAnnule()
                ElseIf e.KeyCode = Keys.F3 Then
                    scanauto()
                ElseIf e.KeyCode = Keys.F4 Then
                    ProcedureNouveau()
                ElseIf e.KeyCode = Keys.F5 Then
                    If BTsauve.Enabled = True And Tnocom.Text.Trim <> "" Then
                        'Imprimeouinon = True
                        ProcedureSauve()
                    End If

                ElseIf e.KeyCode = Keys.F6 Then
                    If SolGrid1.ContainsFocus = True Then infoproduit()
                ElseIf e.KeyCode = Keys.F7 Then
                    inserer()
                ElseIf e.KeyCode = Keys.F8 Then
                    recherche()
                ElseIf e.KeyCode = Keys.F9 Then
                    effaceentete()
                ElseIf e.KeyCode = Keys.F10 Then
                ElseIf e.KeyCode = Keys.F11 Then
                    ProcedureModifier()
                ElseIf e.KeyCode = Keys.F12 Then
                    'Imprimeouinon = False
                    ProcedureImprime()
                ElseIf e.KeyCode = Keys.Enter Then
                    If SolGrid1.ContainsFocus = False Then SendKeys.Send("{TAB}")
                    If SolGrid1.ContainsFocus = True Then
                        If SolGrid1.CurrentCell.ColumnIndex = SolGrid1.Columns("escompte").Index _
                         And SolGrid1.CurrentRow.Index = dscomma1.Rows.Count - 1 Then SendKeys.Send("{TAB}")
                    End If
                ElseIf e.KeyCode = Keys.Up Then
                    If SolGrid1.ContainsFocus = True Then
                        If SolGrid1.CurrentCell.ColumnIndex = SolGrid1.Columns("produit").Index Then
                            If SolGrid1.CurrentRow.Index = SolGrid1.Rows.Count - 1 Then uparr = True
                        Else
                            e.SuppressKeyPress = True
                        End If
                    End If
                    ' SendKeys.Send("+" & "{TAB}")
                ElseIf e.KeyCode = Keys.Down Then
                    If SolGrid1.ContainsFocus = True Then
                        If SolGrid1.CurrentCell.ColumnIndex = SolGrid1.Columns("produit").Index Then
                            If SolGrid1.CurrentRow.Index = SolGrid1.Rows.Count - 1 Then dnarr = True
                        Else
                            e.SuppressKeyPress = True

                        End If
                    End If
                    ' SendKeys.Send("{TAB}")
                ElseIf e.KeyCode = Keys.PageUp Then
                    If promener = True Then BindingNavigator1.MovePreviousItem.PerformClick()
                ElseIf e.KeyCode = Keys.PageDown Then
                    If promener = True Then BindingNavigator1.MoveNextItem.PerformClick()
                End If
            Case 1
                'Shift
                If e.KeyCode = Keys.F8 Then
                    rechercheentrepot()
                ElseIf e.KeyCode = Keys.F6 Then
                    creerproduit()
                ElseIf e.KeyCode = Keys.F7 Then
                    If promener = False Then
                        If lang = "F" Then MsgBox("Terminez et sauvez ce bon avant de procéder!")
                        If lang <> "F" Then MsgBox("Complete and save this work before proceeding!")
                        Exit Sub
                    End If
                    SNocommande = Tnocom.Text
                    AVBSTAT = AVBPosn(AVB + fcotete, Tnocom.Text.PadLeft(10), 1, "", &H100)
                    AVBSTAT = AVBread(AVB + fcotete, 1)
                    If AVBSTAT <> 0 Or AVBcs(AVBfiditemstub("NOCOM", AVB + fcotete, 0)).Trim <> Tnocom.Text.Trim Then
                        If lang = "F" Then MsgBox("Cette commande n'existe plus")
                        If lang <> "F" Then MsgBox("This order does not exist any more")
                        Exit Sub
                    End If
                    If Trim(AVBcs(AVBfiditemstub("GROUPE", AVB + fClient, 0))) = "INTERNE" Then
                        If lang = "F" Then MsgBox("Vous ne pouvez pas facturer un client ayant le groupe INTERNE")
                        If lang <> "F" Then MsgBox("You can not invoice a client when his group is INTERNE")
                        Exit Sub
                    End If
                    If gserie10 = oui10 Then
                        SysOpen(fserie)
                        Dim str As String
                        Dim pasassez As Boolean
                        AVBSTAT = AVBPosn(AVB + fcomma, Tnocom.Text.PadLeft(10), 1, "", 0)
                        AVBSTAT = AVBread(AVB + fcomma, 0)
                        Do While AVBSTAT = 0 And Tnocom.Text.Trim = AVBcs(AVBfiditemstub("NOCOM", AVB + fcomma, 0)).Trim
                            str = Tentrepot.Text + AVBcs(AVBfiditemstub("CODE", AVB + fcomma, 0)).PadRight(30)
                            AVBSTAT = AVBPosn(AVB + fInven, str, 1, "", &H100)
                            AVBSTAT = AVBread(AVB + fInven, 1)
                            If AVBcs(AVBfiditemstub("TYPE1", AVB + fInprix, 0)).Trim <> "U" _
                            And AVBcs(AVBfiditemstub("SERIAL", AVB + fInven, 0)).Trim = oui10 _
                            And Val(AVBcs(AVBfiditemstub("QUANT", AVB + fcomma, 0))) > 0 Then
                                pasassez = verifquantserie(AVBcs(AVBfiditemstub("CODE", AVB + fcomma, 0)), Val(AVBcs(AVBfiditemstub("QUANT", AVB + fcomma, 0))))
                                If pasassez = True Then
                                    SysClose(fserie)
                                    Exit Sub
                                End If
                            End If
                            AVBSTAT = AVBread(AVB + fcomma, 0)
                        Loop
                        SysClose(fserie)
                    End If
                    Dim newfactwo As New FrmFactureComComplet
                    If Gcaisse10 = oui10 And My.Settings.MaCaisse.Trim = "" Then
                        Dim frmca As New FrmCaisseDemande
                        frmca.ShowDialog()
                        If frmca.DialogResult = Windows.Forms.DialogResult.OK Then
                            frmca.Dispose()
                            newfactwo.ShowDialog()
                        End If
                    Else
                        newfactwo.ShowDialog()
                    End If
                    BindEnteteBT()
                    ProcedureDebut()
                ElseIf e.KeyCode = Keys.F6 Then
                    infosubstitut()
                ElseIf e.KeyCode = Keys.F9 Then
                    Effaceligne()
                ElseIf e.KeyCode = Keys.F3 Then
                    profit()

                ElseIf e.KeyCode = Keys.F2 Then
                    If Imprimeouinon = False Then

                        If impcom.Trim <> "" Then Tnocom.Text = impcom
                        ImpSorte = "Bon de connaissement"
                        ImpRapport = "connaissement.rpt"
                        reponse = "*"
                        FormImp(Tnocom.Text.Trim.PadLeft(10))
                        'Imprimeouinon = False
                        impcom = ""
                    Else
                        impcom = ""
                        Imprimeouinon = False
                    End If
                End If
            Case 2
                'Ctrl
                If e.KeyCode = System.Windows.Forms.Keys.PageUp Then
                    'debut
                    If promener = True Then BindingNavigator1.MoveFirstItem.PerformClick()
                ElseIf e.KeyCode = System.Windows.Forms.Keys.PageDown Then
                    'fin
                    If promener = True Then BindingNavigator1.MoveLastItem.PerformClick()
                ElseIf e.KeyCode = Keys.F7 Then
                    'tiroir caisse
                    declanchetiroir()
                ElseIf e.KeyCode = Keys.F3 Then
                    crfournis(True)
                End If
            Case 4
                'Alt
                If e.KeyCode = Keys.F1 Then
                    acces_add()
                ElseIf e.KeyCode = Keys.F5 Then
                    If promener = False And Me.Bttrieproduit.Enabled = True Then
                        Trier_code(2)
                    End If

                ElseIf e.KeyCode = Keys.F2 Then
                    If BTmodifier.Enabled = False Then Ecrantraiteur()
                ElseIf e.KeyCode = Keys.F7 Then
                    If promener = False And BCatalog.Enabled = True Then
                        recherchecata()
                    End If
                ElseIf e.KeyCode = Keys.F11 Then
                    showhisto()
                End If
        End Select
    End Sub

#End Region
#Region "Trier ligne"
    Private Sub Trier_code(ByVal Icle As Integer)
        Dim str As String
        str = Me.ActiveControl.Name
        tbb = Me.ActiveControl
        If (tbb IsNot TxtEscompte And tbb IsNot Ttransport And tbb IsNot Tajoutdepot) Then
            MsgBox("Vous devez faire la clé F5 ou appuyer sur sauver pour pouvoir Trier les lignes")
            Exit Sub
        End If
        'If Bsauver = False Or Me.SolGrid1.ContainsFocus = True Then
        '    MsgBox("Vous devez faire la clé F5 ou appuyer sur sauver pour pouvoir Trier les lignes")
        '    Exit Sub
        'End If
        Bafficheseulement = True
        SaveLigneCom(Tnocom.Text, dscomma1, Tclient.Text)
        Dim strdat As String
        Dim stridx As String
        Dim strfid As String


        strdat = chemin + compagnie + "\" + "prof.dat"
        stridx = chemin + compagnie + "\" + "prof.idx"
        strfid = chemin + "comma.fid"

        AVBSTAT = AVBmake(strdat, strfid, stridx, AVB + 295, 3, 0)
        If AVBSTAT <> 0 Then
            If lang = "F" Then MsgBox("Je ne peux pas créer le fichier!")
            If lang <> "F" Then MsgBox("I can not create the file")
            Exit Sub
        End If


        AVBSTAT = AVBPosn(AVB + fcomma, AVBcs(AVBfiditemstub("NOCOM", AVB + fcotete, 0)), 1, "", 0)
        AVBSTAT = AVBread(AVB + fcomma, 0)
        Do While AVBSTAT = 0
            If AVBcs(AVBfiditemstub("NOCOM", AVB + fcotete, 0)) <> AVBcs(AVBfiditemstub("NOCOM", AVB + fcomma, 0)) Then
                Exit Do
            End If

            AVBrclear(AVB + 295)
            AVBcopy(AVB + fcomma, AVB + 295)
            AVBwrite(AVB + 295, 0, 0)
            AVBsecure(AVB + 295)

            AVBfree(AVB + fcomma)

            AVBSTAT = AVBread(AVB + fcomma, 0)
        Loop
        Dim Icompligne As Double = 10000
        AVBSTAT = AVBPosn(AVB + 295, AVBcs(AVBfiditemstub("NOCOM", AVB + fcotete, 0)), Icle, "", 0)
        AVBSTAT = AVBread(AVB + 295, 0)
        Dim Sproduit As String = ""
        Do While AVBSTAT = 0
            If AVBcs(AVBfiditemstub("NOCOM", AVB + fcotete, 0)) <> AVBcs(AVBfiditemstub("NOCOM", AVB + 295, 0)) Then
                Exit Do
            End If
            AVBrclear(AVB + fcomma)
            AVBcopy(AVB + 295, AVB + fcomma)
            Sproduit = AVBcs(AVBfiditemstub("CODE", AVB + fcomma, 0))
            Icompligne = Icompligne + 100
            AVBfput(Icompligne.ToString, "FICHE", AVB + fcomma, 0, 0)
            AVBwrite(AVB + fcomma, 0, 0)
            AVBsecure(AVB + fcomma)
            AVBfree(AVB + 295)

            AVBSTAT = AVBread(AVB + 295, 0)
        Loop
        AVBclose(AVB + 295)

        'SolGrid1.DataSource = CreateDataSourceLigneCom(Tnocom.Text, dscomma1, DsPoids)
        CreateDataSourceLigneCom(Tnocom.Text, dscomma1, DsPoids)
        If dscomma1.Rows.Count <> SolGrid1.Rows.Count Then
            MsgBox("ligne pas pareil")
        End If
        If dscomma1.Rows.Count > 0 Then DCompteur = Val(dscomma1.Rows(dscomma1.Rows.Count - 1).Item("Ligne"))
        ReDim quant_old(dscomma1.Rows.Count - 1)
        ReDim prod_old(dscomma1.Rows.Count - 1)
        ReDim um_old(dscomma1.Rows.Count - 1)
        ReDim quant_paqbte(dscomma1.Rows.Count - 1)
        For compteur As Integer = 0 To dscomma1.Rows.Count - 1
            quant_old(compteur) = Val(dscomma1.Rows(compteur).Item("quantite"))
            prod_old(compteur) = dscomma1.Rows(compteur).Item("produit")
            um_old(compteur) = dscomma1.Rows(compteur).Item("um")
            quant_paqbte(compteur) = Val(dscomma1.Rows(compteur).Item("paq_Bte"))
        Next
        creerligne()
        Bafficheseulement = False
        TxtEscompte.Focus()

    End Sub

    Private Sub Bttrieproduit_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Bttrieproduit.Click
        Trier_code(2)
    End Sub


    Private Sub Trier_codeum(ByVal Icle As Integer)
        Dim str As String
        str = Me.ActiveControl.Name
        tbb = Me.ActiveControl
        'If (tbb IsNot TxtEscompte And tbb IsNot Ttransport And tbb IsNot Tajoutdepot) Then
        '    MsgBox("Vous devez faire la clé F5 ou appuyer sur sauver pour pouvoir Trier les lignes")
        '    Exit Sub
        'End If
        'If Bsauver = False Or Me.SolGrid1.ContainsFocus = True Then
        '    MsgBox("Vous devez faire la clé F5 ou appuyer sur sauver pour pouvoir Trier les lignes")
        '    Exit Sub
        'End If
        Bafficheseulement = True
        'SaveLigneCom(Tnocom.Text, dscomma1, Tclient.Text)
        Dim strdat As String
        Dim stridx As String
        Dim strfid As String


        strdat = chemin + compagnie + "\" + utilisateur.Trim + ".dat"
        stridx = chemin + compagnie + "\" + utilisateur.Trim + ".idx"
        strfid = chemin + "commaum.fid"

        AVBSTAT = AVBmake(strdat, strfid, stridx, AVB + 295, 3, 0)
        If AVBSTAT <> 0 Then
            If lang = "F" Then MsgBox("Je ne peux pas créer le fichier!")
            If lang <> "F" Then MsgBox("I can not create the file")
            Exit Sub
        End If


        AVBSTAT = AVBPosn(AVB + fcomma, AVBcs(AVBfiditemstub("NOCOM", AVB + fcotete, 0)), 1, "", 0)
        AVBSTAT = AVBread(AVB + fcomma, 0)
        Dim oldumx As String = Trim(AVBcs(AVBfiditemstub("PAR", AVB + fcomma, 0)))
        Do While AVBSTAT = 0
            If AVBcs(AVBfiditemstub("NOCOM", AVB + fcotete, 0)) <> AVBcs(AVBfiditemstub("NOCOM", AVB + fcomma, 0)) Then
                Exit Do
            End If

            AVBrclear(AVB + 295)
            AVBcopy(AVB + fcomma, AVB + 295)


            If Mid(AVBcs(AVBfiditemstub("CODE", AVB + fcomma, 0)).Trim, 1, 3) = "REM" Then
                If Trim(AVBcs(AVBfiditemstub("CODE", AVB + fcomma, 0))) = "REMZ" Then
                    AVBfput("ZZZ".Trim & AVBcs(AVBfiditemstub("FICHE", AVB + fcomma, 0)).Trim, "CLEUM", AVB + 295, 0, 0)
                Else
                    AVBfput(oldumx.Trim & AVBcs(AVBfiditemstub("FICHE", AVB + fcomma, 0)).Trim, "CLEUM", AVB + 295, 0, 0)
                End If

            Else
                AVBfput(AVBcs(AVBfiditemstub("PAR", AVB + fcomma, 0)).Trim & AVBcs(AVBfiditemstub("FICHE", AVB + fcomma, 0)).Trim, "CLEUM", AVB + 295, 0, 0)
            End If



            AVBwrite(AVB + 295, 0, 0)
            AVBsecure(AVB + 295)
            If Mid(Trim(AVBcs(AVBfiditemstub("CODE", AVB + fcomma, 0))), 1, 3) <> "REM" Then oldumx = Trim(AVBcs(AVBfiditemstub("PAR", AVB + fcomma, 0)))
            AVBfree(AVB + fcomma)

            AVBSTAT = AVBread(AVB + fcomma, 0)
        Loop
        Dim Icompligne As Double = 10000
        AVBSTAT = AVBPosn(AVB + 295, "", Icle, "", 0)
        AVBSTAT = AVBread(AVB + 295, 0)
        Dim Sproduit As String = ""
        Do While AVBSTAT = 0
            If AVBcs(AVBfiditemstub("NOCOM", AVB + fcotete, 0)) <> AVBcs(AVBfiditemstub("NOCOM", AVB + 295, 0)) Then
                Exit Do
            End If
            AVBrclear(AVB + fcomma)
            AVBcopy(AVB + 295, AVB + fcomma)
            Sproduit = AVBcs(AVBfiditemstub("CODE", AVB + fcomma, 0))
            Icompligne = Icompligne + 100
            AVBfput(Icompligne.ToString, "FICHE", AVB + fcomma, 0, 0)
            AVBwrite(AVB + fcomma, 0, 0)
            AVBsecure(AVB + fcomma)
            AVBfree(AVB + 295)

            AVBSTAT = AVBread(AVB + 295, 0)
        Loop
        AVBclose(AVB + 295)

        'SolGrid1.DataSource = CreateDataSourceLigneCom(Tnocom.Text, dscomma1, DsPoids)
        CreateDataSourceLigneCom(Tnocom.Text, dscomma1, DsPoids)
        If dscomma1.Rows.Count <> SolGrid1.Rows.Count Then
            MsgBox("ligne pas pareil")
        End If
        If dscomma1.Rows.Count > 0 Then DCompteur = Val(dscomma1.Rows(dscomma1.Rows.Count - 1).Item("Ligne"))
        ReDim quant_old(dscomma1.Rows.Count - 1)
        ReDim prod_old(dscomma1.Rows.Count - 1)
        ReDim um_old(dscomma1.Rows.Count - 1)
        ReDim quant_paqbte(dscomma1.Rows.Count - 1)
        For compteur As Integer = 0 To dscomma1.Rows.Count - 1
            quant_paqbte(compteur) = Val(dscomma1.Rows(compteur).Item("paq_bte"))
            quant_old(compteur) = Val(dscomma1.Rows(compteur).Item("quantite"))
            prod_old(compteur) = dscomma1.Rows(compteur).Item("produit")
            um_old(compteur) = dscomma1.Rows(compteur).Item("um")
        Next
        creerligne()
        Bafficheseulement = False
        TxtEscompte.Focus()

    End Sub
    Private Sub Trier_codelocum(ByVal Icle As Integer)
        Dim str As String
        str = Me.ActiveControl.Name
        tbb = Me.ActiveControl
        'If (tbb IsNot TxtEscompte And tbb IsNot Ttransport And tbb IsNot Tajoutdepot) Then
        '    MsgBox("Vous devez faire la clé F5 ou appuyer sur sauver pour pouvoir Trier les lignes")
        '    Exit Sub
        'End If

        Bafficheseulement = True
        'SaveLigneCom(Tnocom.Text, dscomma1, Tclient.Text)
        Dim strdat As String
        Dim stridx As String
        Dim strfid As String


        strdat = chemin + compagnie + "\" + utilisateur.Trim + ".dat"
        stridx = chemin + compagnie + "\" + utilisateur.Trim + ".idx"
        strfid = chemin + "commaum.fid"

        AVBSTAT = AVBmake(strdat, strfid, stridx, AVB + 295, 3, 0)
        If AVBSTAT <> 0 Then
            If lang = "F" Then MsgBox("Je ne peux pas créer le fichier!")
            If lang <> "F" Then MsgBox("I can not create the file")
            Exit Sub
        End If


        AVBSTAT = AVBPosn(AVB + fcomma, AVBcs(AVBfiditemstub("NOCOM", AVB + fcotete, 0)), 1, "", 0)
        AVBSTAT = AVBread(AVB + fcomma, 0)
        Dim oldumx As String = AVBcs(AVBfiditemstub("LOC1", AVB + fcomma, 0)) & Trim(AVBcs(AVBfiditemstub("PAR", AVB + fcomma, 0)))

        Do While AVBSTAT = 0
            If AVBcs(AVBfiditemstub("NOCOM", AVB + fcotete, 0)) <> AVBcs(AVBfiditemstub("NOCOM", AVB + fcomma, 0)) Then
                Exit Do
            End If

            AVBrclear(AVB + 295)
            AVBcopy(AVB + fcomma, AVB + 295)


            If Mid(AVBcs(AVBfiditemstub("CODE", AVB + fcomma, 0)).Trim, 1, 3) = "REM" Then
                If Trim(AVBcs(AVBfiditemstub("CODE", AVB + fcomma, 0))) = "REMZ" Then
                    AVBfput("ZZZZZZZZZZ" & "ZZZ".Trim & AVBcs(AVBfiditemstub("FICHE", AVB + fcomma, 0)).Trim, "CLEUM", AVB + 295, 0, 0)
                Else
                    AVBfput(oldumx & AVBcs(AVBfiditemstub("FICHE", AVB + fcomma, 0)).Trim, "CLEUM", AVB + 295, 0, 0)
                End If

            Else
                AVBfput(AVBcs(AVBfiditemstub("LOC1", AVB + fcomma, 0)) & AVBcs(AVBfiditemstub("PAR", AVB + fcomma, 0)).Trim & AVBcs(AVBfiditemstub("FICHE", AVB + fcomma, 0)).Trim, "CLEUM", AVB + 295, 0, 0)
            End If



            AVBwrite(AVB + 295, 0, 0)
            AVBsecure(AVB + 295)
            If Mid(Trim(AVBcs(AVBfiditemstub("CODE", AVB + fcomma, 0))), 1, 3) <> "REM" Then oldumx = AVBcs(AVBfiditemstub("LOC1", AVB + fcomma, 0)) & Trim(AVBcs(AVBfiditemstub("PAR", AVB + fcomma, 0)))
            AVBfree(AVB + fcomma)

            AVBSTAT = AVBread(AVB + fcomma, 0)
        Loop
        Dim Icompligne As Double = 10000
        AVBSTAT = AVBPosn(AVB + 295, "", Icle, "", 0)
        AVBSTAT = AVBread(AVB + 295, 0)
        Dim Sproduit As String = ""
        Do While AVBSTAT = 0
            If AVBcs(AVBfiditemstub("NOCOM", AVB + fcotete, 0)) <> AVBcs(AVBfiditemstub("NOCOM", AVB + 295, 0)) Then
                Exit Do
            End If
            AVBrclear(AVB + fcomma)
            AVBcopy(AVB + 295, AVB + fcomma)
            Sproduit = AVBcs(AVBfiditemstub("CODE", AVB + fcomma, 0))
            Icompligne = Icompligne + 100
            AVBfput(Icompligne.ToString, "FICHE", AVB + fcomma, 0, 0)
            AVBwrite(AVB + fcomma, 0, 0)
            AVBsecure(AVB + fcomma)
            AVBfree(AVB + 295)

            AVBSTAT = AVBread(AVB + 295, 0)
        Loop
        AVBclose(AVB + 295)

        'SolGrid1.DataSource = CreateDataSourceLigneCom(Tnocom.Text, dscomma1, DsPoids)
        CreateDataSourceLigneCom(Tnocom.Text, dscomma1, DsPoids)
        If dscomma1.Rows.Count <> SolGrid1.Rows.Count Then
            MsgBox("ligne pas pareil")
        End If
        If dscomma1.Rows.Count > 0 Then DCompteur = Val(dscomma1.Rows(dscomma1.Rows.Count - 1).Item("Ligne"))
        ReDim quant_old(dscomma1.Rows.Count - 1)
        ReDim prod_old(dscomma1.Rows.Count - 1)
        ReDim um_old(dscomma1.Rows.Count - 1)
        ReDim quant_paqbte(dscomma1.Rows.Count - 1)
        For compteur As Integer = 0 To dscomma1.Rows.Count - 1
            quant_paqbte(compteur) = Val(dscomma1.Rows(compteur).Item("paq_bte"))
            quant_old(compteur) = Val(dscomma1.Rows(compteur).Item("quantite"))
            prod_old(compteur) = dscomma1.Rows(compteur).Item("produit")
            um_old(compteur) = dscomma1.Rows(compteur).Item("um")
        Next
        creerligne()
        Bafficheseulement = False
        TxtEscompte.Focus()

    End Sub

#End Region
#Region "Événement solgrid1"
    Private Sub SolGrid1_Click(ByVal sender As Object, ByVal e As System.EventArgs) Handles SolGrid1.Click
        If Tnocom.Text.Trim = "" Then
            Tnocom.Focus()
            Exit Sub
        End If
        SolGrid1.Focus()
        SolGrid1.BeginEdit(True)
        Trouvelignefocus()
    End Sub
    Private Sub SolGrid1_KeyDown(ByVal sender As Object, ByVal e As System.Windows.Forms.KeyEventArgs) Handles SolGrid1.KeyDown
        If Bafficheseulement = True Then Exit Sub
        If SolGrid1.ContainsFocus = False Then Exit Sub
        pgup = False
        pgdn = False
        uparr = False
        dnarr = False
        lfarr = False
        If e.KeyCode = Keys.PageUp Then
            pgup = True
            SolGrid1.CurrentRow.Cells("produit").Selected = True
        ElseIf e.KeyCode = Keys.PageDown Then
            pgdn = True
            SolGrid1.CurrentRow.Cells("produit").Selected = True
        ElseIf e.KeyCode = Keys.Down Then
            If SolGrid1.CurrentRow.Cells("produit").Selected = False Then
                e.SuppressKeyPress = True
                dnarr = True
                System.Windows.Forms.SendKeys.SendWait("+" & "{TAB}")
                Exit Sub
            End If
    

        ElseIf e.KeyCode = Keys.Escape Then
            e.SuppressKeyPress = True
        End If
        If e.KeyCode = Keys.Up Then uparr = True
        If e.KeyCode = Keys.Down Then dnarr = True
        If e.KeyCode = Keys.Left Then lfarr = True
        SolGrid1.BeginEdit(True)
    End Sub
    Private Sub SolGrid1_CellLeave1(ByVal sender As Object, ByVal e As System.Windows.Forms.DataGridViewCellEventArgs) Handles SolGrid1.CellLeave
        If SolGrid1.ContainsFocus = False Then Exit Sub
        If gridfocus = False Or uparr = True Or dnarr = True Or pgup = True Or pgdn = True Or lfarr = True Then Exit Sub
        If Bafficheseulement = True Then Exit Sub
        If prodarret = True Then Exit Sub
        Dim index As Integer = SolGrid1.CurrentCell.ColumnIndex
        If index = SolGrid1.Columns("produit").Index And SolGrid1.CurrentCell.EditedFormattedValue.ToString.Trim = "" Then
            Exit Sub
        End If
        If SolGrid1.CurrentCell.ColumnIndex <> SolGrid1.Columns("description").Index Then
            SolGrid1.CurrentCell.Value = UCase(SolGrid1.CurrentCell.EditedFormattedValue)
            SolGrid1.RefreshEdit()
        End If
        Dim prodtemp As String = UCase(SolGrid1.CurrentRow.Cells("produit").EditedFormattedValue.ToString.PadRight(30))
        '******************* gerance du deplacement dans les colonnes ************************************
        'remarque va a description
        'remarque ou divers va a description
        If (Mid(prodtemp, 1, 3) = Mid(Rem10, 1, 3) _
             Or (Mid(prodtemp, 1, 3) = Mid(Div10, 1, 3)) _
             Or (Mid(prodtemp, 1, 3) = Mid(Ndiv10, 1, 3))) _
            And SolGrid1.CurrentCell.ColumnIndex = SolGrid1.Columns("produit").Index Then
            dscomma1.Rows(SolGrid1.CurrentRow.Index).BeginEdit()
            Exit Sub
        End If
        'SolGrid1.RefreshEdit()
        Select Case index
            Case SolGrid1.Columns("produit").Index
                'DsComma1.Rows(SolGrid1.CurrentRow.Index).BeginEdit()
                SendKeys.Send("{TAB}")
                SendKeys.Send("{TAB}")
            Case SolGrid1.Columns("description").Index
                If Mid(prodtemp, 1, 3) = Mid(Rem10, 1, 3) Then
                    Bafficheseulement = True
                    creernouvligne(False)
                    SendKeys.Send("{TAB}")
                    SendKeys.Send("{TAB}")
                    SendKeys.Send("{TAB}")
                    SendKeys.Send("{TAB}")
                    SendKeys.Send("{TAB}")
                    inserelig = False
                    Bafficheseulement = False
                    Exit Sub
                End If
                SendKeys.Send("{TAB}")
            Case SolGrid1.Columns("quantite").Index
                SendKeys.Send("{TAB}")
            Case SolGrid1.Columns("prix").Index
                SendKeys.Send("{TAB}")
            Case SolGrid1.Columns("escompte").Index
                claireinfoproduit()
                If SolGrid1.CurrentRow.Index <> SolGrid1.Rows.Count - 1 Then SendKeys.Send("{TAB}")
                If modifesc = True Then SendKeys.Send("{TAB}")
                modifesc = False
            Case SolGrid1.Columns("status").Index

        End Select
    End Sub
    Private Sub SolGrid1_CellValidating(ByVal sender As Object, ByVal e As System.Windows.Forms.DataGridViewCellValidatingEventArgs) Handles SolGrid1.CellValidating
        If SolGrid1.ContainsFocus = False Then Exit Sub
        If efflignevide = True Or promener = True Or gridfocus = False Or pgup = True Or pgdn = True Or uparr = True Or dnarr = True Or lfarr = True Then Exit Sub
        If Bafficheseulement = True Then Exit Sub
        'If barcodeauto = True And arretbar = False Then Exit Sub
        'prodarret = False
        'If SolGrid1.CurrentCell.ColumnIndex <> SolGrid1.Columns("description").Index Then
        'End If
        ' SolGrid1.CurrentCell.Value = UCase(SolGrid1.CurrentCell.EditedFormattedValue)
        'SolGrid1.RefreshEdit()
        Dim index As Integer = SolGrid1.CurrentCell.ColumnIndex
        Dim noligne As Integer = SolGrid1.CurrentRow.Index
        If noligne = SolGrid1.Rows.Count - 1 _
         And Trim(SolGrid1.CurrentRow.Cells("produit").EditedFormattedValue.ToString) = "" Then
            'If lang = "F" Then MsgBox("Il faut entrer un produit")
            'If lang <> "F" Then MsgBox("You must enter a product")
            e.Cancel = True
            Exit Sub
        End If

        Dim prodtemp As String = SolGrid1.CurrentRow.Cells("produit").EditedFormattedValue.ToString
        prodtemp = prodtemp.PadRight(30)
        's'ils ont change de ligne en plein milieu
        If index <> SolGrid1.Columns("Produit").Index Then
            AVBSTAT = AVBPosn(AVB + fInprix, prodtemp, 1, "", &H100)
            AVBSTAT = AVBread(AVB + fInprix, 1)
            AVBSTAT = AVBPosn(AVB + fInven, Tentrepot.Text.PadLeft(3) + prodtemp, 1, "", &H100)
            AVBSTAT = AVBread(AVB + fInven, 1)
        End If
        Select Case index
            Case SolGrid1.Columns("Produit").Index
                If Trim(prodtemp) = "" Then
                    e.Cancel = True
                    Exit Sub
                End If

                If AVBisopen(AVB + fcomma) = 0 Then SysOpen(fcomma)
                If AVBisopen(AVB + fcotete) = 0 Then SysOpen(fcotete)
                If AVBisopen(AVB + fClient) = 0 Then SysOpen(fClient)

                SolGrid1.CurrentRow.Cells("Produit").Value = SolGrid1.CurrentRow.Cells("Produit").Value.ToUpper
                SolGrid1.RefreshEdit()
                If Trim(prodtemp) = "!" Then
                    If lang = "F" Then MsgBox("Vous ne pouvez pas utiliser le produit par défaut")
                    If lang <> "F" Then MsgBox("You can not use the default product")
                    e.Cancel = True
                    Exit Sub
                End If
                If Trim(prodtemp) <> prod_old(noligne).Trim _
                    And prod_old(noligne).Trim <> "" Then
                    If lang = "F" Then MsgBox("Vous ne pouvez pas changer le numéro de produit d'une ligne existante")
                    If lang <> "F" Then MsgBox("You can not change the product number of an existing line")
                    SolGrid1.CurrentRow.Cells("Produit").Value = prod_old(noligne)
                    SolGrid1.RefreshEdit()
                    e.Cancel = True
                    Exit Sub
                End If
                Dim sorte As String = "commande"
                If lang <> "F" Then sorte = "order"
                'chkexistproduit(prodtemp, SolGrid1, sorte, noligne, inserelig)
                AVBSTAT = AVBPosn(AVB + fInprix, prodtemp, 1, "", &H100)
                AVBSTAT = AVBread(AVB + fInprix, 1)
                'si divers ou remarque et pas dans inprix
                'si remarque 
                If (Mid(prodtemp, 1, 3) = Mid(Rem10, 1, 3)) Then
                    If AVBSTAT = 0 _
                    And (SolGrid1.CurrentRow.Index = SolGrid1.Rows.Count - 1 Or inserelig = True) Then
                        If lang4 = "F" Then dscomma1.Rows(SolGrid1.CurrentRow.Index).Item("description") = AVBcs(AVBfiditemstub("DESCR", AVB + fInprix, 0))
                        If lang4 <> "F" Then dscomma1.Rows(SolGrid1.CurrentRow.Index).Item("description") = AVBcs(AVBfiditemstub("DESCA", AVB + fInprix, 0))
                    End If
                    SolGrid1.CurrentRow.Cells("um").Value = "UNI"
                    dscomma1.Rows(noligne).Item("groupe") = ""
                    SolGrid1.CurrentRow.Cells("poste vente").Value = "1"
                    SolGrid1.CurrentRow.Cells("dept").Value = "1"
                    SolGrid1.CurrentRow.Cells("status").Value = "I"
                    'pour calcul de taxe apogee
                    dscomma1.Rows(noligne).Item("taxff") = "0"
                    dscomma1.Rows(noligne).Item("taxpp") = "0"
                    dscomma1.Rows(noligne).Item("loc1") = ""
                    dscomma1.Rows(noligne).Item("taux") = "1"
                    SolGrid1.RefreshEdit()
                    dscomma1.Rows(noligne).Item("umx") = 0
                    dscomma1.Rows(noligne).Item("mult2") = 1
                    dscomma1.Rows(noligne).Item("div2") = 1
                    'um_old(SolGrid1.CurrentRow.Index) = ""
                    dscomma1.Rows(SolGrid1.CurrentRow.Index).Item("coutant") = 0
                    prod_old(SolGrid1.CurrentRow.Index) = SolGrid1.CurrentRow.Cells("produit").Value
                    quant_old(SolGrid1.CurrentRow.Index) = 0
                    quant_paqbte(SolGrid1.CurrentRow.Index) = 0
                    um_old(SolGrid1.CurrentRow.Index) = ""
                    Exit Sub
                End If
                If ActiverBarcodeautomatique = False Then


                    If AVBSTAT = 0 And Trim(AVBcs(AVBfiditemstub("CODEAP", AVB + fInprix, 0))) <> "" And quant_old(SolGrid1.CurrentRow.Index) = 0 Then

                        'recherche et visionnement des equivalents
                        Dim diag As DialogResult = chksubstitut(prodtemp, Tentrepot.Text, SolGrid1, 0)
                        If diag = Windows.Forms.DialogResult.OK Then
                            SendKeys.Send("{TAB}")
                        ElseIf diag <> Windows.Forms.DialogResult.No Then
                            e.Cancel = True
                            Exit Sub
                        End If
                    End If
                End If


                If AVBSTAT <> 0 Then
                        'mot clef 1
                        AVBSTAT = AVBPosn(AVB + fInprix, prodtemp, 10, "", &H100)
                        AVBSTAT = AVBread(AVB + fInprix, 1)
                        If AVBSTAT = 0 Then

                        If ActiverBarcodeautomatique = False Then
                            chkproduitplus(AVBcs(AVBfiditemstub("MOTCLE1", AVB + fInprix, 0)))
                            SolGrid1.CurrentRow.Cells("Produit").Value = AVBcs(AVBfiditemstub("CAT", AVB + fInprix, 0))
                            SolGrid1.RefreshEdit()
                            'recherche et visionnement des equivalents
                            prodtemp = AVBcs(AVBfiditemstub("CAT", AVB + fInprix, 0))
                            AVBSTAT = AVBPosn(AVB + fInprix, prodtemp, 1, "", &H100)
                            AVBSTAT = AVBread(AVB + fInprix, 1)
                            Dim diag As DialogResult = chksubstitut(prodtemp, Tentrepot.Text, SolGrid1, 0)
                            If diag = Windows.Forms.DialogResult.OK Then
                                SendKeys.Send("{TAB}")
                            ElseIf diag <> Windows.Forms.DialogResult.No Then
                                e.Cancel = True
                                Exit Sub
                            End If

                        End If

                        If (Mid(prodtemp, 1, 3) = Mid(Rem10, 1, 3) _
                             Or (Mid(prodtemp, 1, 3) = Mid(Div10, 1, 3)) _
                                Or (Mid(prodtemp, 1, 3) = Mid(Ndiv10, 1, 3))) Then System.Windows.Forms.SendKeys.SendWait("+" & "{TAB}")

                        End If
                End If
                'barcode
                If AVBSTAT <> 0 Then
                    AVBSTAT = AVBPosn(AVB + fInprix, prodtemp, 5, "", &H100)
                    AVBSTAT = AVBread(AVB + fInprix, 1)
                    If AVBSTAT = 0 Then
                        SolGrid1.CurrentRow.Cells("Produit").Value = AVBcs(AVBfiditemstub("CAT", AVB + fInprix, 0))
                        prodtemp = AVBcs(AVBfiditemstub("CAT", AVB + fInprix, 0))
                        AVBSTAT = AVBPosn(AVB + fInprix, prodtemp, 1, "", &H100)
                        AVBSTAT = AVBread(AVB + fInprix, 1)
                        'gestion du declenchement du barcode
                        barcodeauto = False
                        If prod_old(noligne).Trim = "" _
                        And (QteBarcode10 <> 0) _
                         And noligne = SolGrid1.Rows.Count - 1 Then
                            'And RepCabCais = oui10
                            barcodeauto = True
                        End If
                    End If
                End If
                'barcode additionnel
                If AVBSTAT <> 0 Then
                    SysOpen(fbarcode)
                    AVBSTAT = AVBPosn(AVB + fbarcode, prodtemp, 2, "", &H100)
                    AVBSTAT = AVBread(AVB + fbarcode, 1)
                    If AVBSTAT = 0 Then
                        SolGrid1.CurrentRow.Cells("Produit").Value = AVBcs(AVBfiditemstub("PRODUIT", AVB + fbarcode, 0))
                        prodtemp = AVBcs(AVBfiditemstub("PRODUIT", AVB + fbarcode, 0))
                        AVBSTAT = AVBPosn(AVB + fInprix, prodtemp, 1, "", &H100)
                        AVBSTAT = AVBread(AVB + fInprix, 1)
                        'gestion du declenchement du barcode
                        barcodeauto = False
                        If prod_old(noligne).Trim = "" _
                        And QteBarcode10 <> 0 _
                         And noligne = SolGrid1.Rows.Count - 1 Then
                            'And RepCabCais = oui10
                            barcodeauto = True
                        End If
                    End If
                    ' SysClose(fbarcode)
                End If
                'catalog
                If AVBSTAT <> 0 Then
                    Dim result As DialogResult = TrouveCatalogue(prodtemp)
                    If result = Windows.Forms.DialogResult.No Then
                        AVBSTAT = 1
                        If lang = "F" Then MsgBox("Ce produit n'existe pas")
                        If lang <> "F" Then MsgBox("This product does not exist")
                        e.Cancel = True
                        recherche()
                        Exit Sub
                    ElseIf result = Windows.Forms.DialogResult.Cancel Or result = Windows.Forms.DialogResult.No Then
                        e.Cancel = True
                        SolGrid1.CurrentRow.Cells("produit").Value = ""
                        Bcommenceligne = False
                        SolGrid1.RefreshEdit()
                        Exit Sub
                    ElseIf result = Windows.Forms.DialogResult.Yes Then
                        'si on trouve le produit dans inprix
                        SolGrid1.CurrentRow.Cells("produit").Value = AVBTrouveproduit
                        prodtemp = AVBTrouveproduit
                        SolGrid1.RefreshEdit()
                    Else
                        SolGrid1.CurrentRow.Cells("produit").Value = AVBTrouveproduit
                        prodtemp = AVBTrouveproduit
                        AVBSTAT = AVBPosn(AVB + fInprix, prodtemp, 1, "", &H100)
                        AVBSTAT = AVBread(AVB + fInprix, 1)
                        SolGrid1.RefreshEdit()
                        SendKeys.Send("{TAB}")
                    End If
                End If
                If Trim(AVBcs(AVBfiditemstub("PAR", AVB + fInprix, 0))) = "" Then
                    If lang = "F" Then MsgBox("Ce produit n'a pas d'unité de mesure!")
                    If lang <> "F" Then MsgBox("This product does not have U/M!")
                    e.Cancel = True
                    Exit Sub
                End If
                AVBSTAT = AVBPosn(AVB + fInven, Tentrepot.Text.PadLeft(3) + prodtemp, 1, "", &H100)
                AVBSTAT = AVBread(AVB + fInven, 1)
                If AVBSTAT <> 0 Then
                    If lang = "F" Then MsgBox("Le produit " & prodtemp.Trim & " n'existe pas dans cet entrepôt")
                    If lang <> "F" Then MsgBox("Can not find the product " & prodtemp.Trim & " in this warehouse")
                    barcodeauto = False
                    e.Cancel = True
                    Exit Sub
                End If
                If chkbarreprod(prodtemp, Tentrepot.Text) = True Then
                    e.Cancel = True
                    Bcommenceligne = False
                    If SolGrid1.CurrentRow.Index = SolGrid1.Rows.Count - 1 Or inserelig = True Then SolGrid1.CurrentCell.Value = ""
                    SolGrid1.RefreshEdit()
                    Exit Sub
                End If
                'discontinue
                If AVBcs(AVBfiditemstub("DISCONT", AVB + fInprix, 0)) = oui10 Then
                    Dim frq As New FrmQuestion
                    If lang = "F" Then frq.LblMessage.Text = "Ce produit est discontinué! - Voulez-vous continuer"
                    If lang <> "F" Then frq.LblMessage.Text = "Discontinued product ! - Do you want to continue"
                    frq.ShowDialog()
                    If frq.DialogResult = Windows.Forms.DialogResult.No Then
                        Bcommenceligne = False
                        e.Cancel = True
                        Exit Sub
                    End If
                    SendKeys.Send("{TAB}")
                End If
                'actif
                If AVBcs(AVBfiditemstub("ACTIF", AVB + fInprix, 0)) = "N" Then
                    If lang = "F" Then MsgBox("Ce produit est inactif")
                    If lang <> "F" Then MsgBox("This product is not active")
                    Bcommenceligne = False
                    e.Cancel = True
                    Exit Sub
                End If
                If ActiverBarcodeautomatique = True Then
                    barcodeauto = True
                End If
                If barcodeauto = False Then chkexistproduit(AVBcs(AVBfiditemstub("CAT", AVB + fInprix, 0)), SolGrid1, sorte, noligne, inserelig)




                'memo
                Dim chaine As String
                SysOpen(fmemo)
                chaine = "P" + prodtemp
                AVBSTAT = AVBPosn(AVB + fmemo, chaine, 4, "", 0)
                If AVBSTAT = 0 Then
                    AVBSTAT = AVBread(AVB + fmemo, 1)
                    If AVBSTAT = 0 And Trim(AVBcs(AVBfiditemstub("CDE", AVB + fmemo, 0))) = Trim(prodtemp) _
                    And Val(AVBcs(AVBfiditemstub("NOMEMO", AVB + fmemo, 0))) < 101 _
                    And AVBcs(AVBfiditemstub("CHOIX", AVB + fmemo, 0)) = "P" Then
                        Dim frmem As New FrmMemoShow
                        frmem.ShowDialog()
                        SendKeys.Send("{TAB}")
                    End If
                End If
                SysClose(fmemo)
                Bcommenceligne = True
                TxtCat.Text = AVBcs(AVBfiditemstub("CAT", AVB + fInprix, 0))
                If noligne = SolGrid1.Rows.Count - 1 Then
                    showinfoprod(AVBcs(AVBfiditemstub("PAR", AVB + fInprix, 0)), prodtemp)
                Else
                    showinfoprod(dscomma1.Rows(noligne).Item("um"), prodtemp)
                End If
                'si derniere ligne donc nouvelle ligne
                If noligne = SolGrid1.Rows.Count - 1 Or inserelig = True Then
                    'mettre les valeurs dans les champs et collonnes
                    completeproduit(noligne)
                    If Mid(prodtemp, 1, 3) = Mid(Rem10, 1, 3) Then
                        SolGrid1.CurrentRow.Cells("um").Value = " "
                        dscomma1.Rows(noligne).Item("coutant") = 0
                        Exit Sub
                    End If
                    dscomma1.Rows(index).Item("datelivre") = Ddaterequis.Text
                    DsPoids.Rows(SolGrid1.CurrentRow.Index).Item("code") = prodtemp
                    SolGrid1.CurrentRow.Cells("um").Value = AVBcs(AVBfiditemstub("PAR", AVB + fInprix, 0))
                    If Mid(AVBcs(AVBfiditemstub("TYPE", AVB + fInprix, 0)), 1, 3) = Mid(AVBcs(AVBfiditemstub("MO", AVB + fCompagni, 0)), 1, 3) Then
                        SolGrid1.CurrentRow.Cells("status").Value = "I"
                    End If
                    If Convert.ToBoolean(Mid(AVBcs(AVBfiditemstub("INVENTAIRE", AVB + fInven, 0)), 1, 1) <> oui10 And dscomma1.Rows(noligne).Item("status") <> "I") Then
                        SolGrid1.CurrentRow.Cells("status").Value = "S"
                    End If
                    SolGrid1.RefreshEdit()
                    Dim strsql As String = dscomma1.Rows(noligne).Item("taux").ToString
                    'SolGrid1.RefreshEdit()
                    'unite de mesure si plusieurs 
                    If Trim(AVBcs(AVBfiditemstub("PAR", AVB + fInprix, 1))) <> "" Then
                        Sposum = dscomma1.Rows(SolGrid1.CurrentRow.Index).Item("um")
                        Dim frmum As New FrmUmShow
                        frmum.ShowDialog()
                        If frmum.DialogResult = Windows.Forms.DialogResult.OK Then
                            If Trim(SolGrid1.CurrentRow.Cells("um").Value) <> Trim(AVBTrouveproduit) Then
                                SolGrid1.CurrentRow.Cells("prix").Value = ""
                                SolGrid1.CurrentRow.Cells("montant").Value = ""
                                SolGrid1.CurrentRow.Cells("escompte").Value = ""
                            End If
                            SolGrid1.CurrentRow.Cells("um").Value = AVBTrouveproduit
                            dscomma1.Rows(SolGrid1.CurrentRow.Index).Item("um") = AVBTrouveproduit
                            Dim umx As Integer = TrouveUm(SolGrid1.CurrentRow.Cells("produit").Value.ToString, SolGrid1.CurrentRow.Cells("um").Value.ToString)
                            dscomma1.Rows(SolGrid1.CurrentRow.Index).Item("umx") = umx
                            dscomma1.Rows(SolGrid1.CurrentRow.Index).Item("mult2") = AVBcs(AVBfiditemstub("MULT1", AVB + fInprix, umx))
                            dscomma1.Rows(SolGrid1.CurrentRow.Index).Item("coutant") = Val(AVBcs(AVBfiditemstub("COUT", AVB + fInprix, 0)))
                            dscomma1.Rows(SolGrid1.CurrentRow.Index).Item("div2") = AVBcs(AVBfiditemstub("DIV1", AVB + fInprix, umx))
                            dscomma1.Rows(SolGrid1.CurrentRow.Index).Item("quantite") = AVBcs(AVBfiditemstub("QUANVEN", AVB + fInprix, umx))
                        End If
                        SolGrid1.RefreshEdit()
                        SendKeys.Send("{TAB}")
                        showinfoprod(dscomma1.Rows(noligne).Item("um"), prodtemp)
                        'TrouveDispo(prodtemp, SolGrid1.CurrentRow.Index, Tentrepot.Text.PadLeft(3), SolGrid1.CurrentRow.Cells("um").Value.ToString)
                    End If
                    'se promener et completer la ligne si gestion de barcode auto
                    '********************************
                    If barcodeauto = True Then
                        SolGrid1.CurrentRow.Cells("quantite").Value = QteBarcode10
                        If ArretBarcode10 = oui10 Then
                            arretbar = True
                        Else 'si on arrete pas sur la quantite
                            If getstatus() = True Then
                                If lang = "F" Then MsgBox("La quantité disponible de ce produit est insuffisante.")
                                If lang <> "F" Then MsgBox("The quantity on hand is insufficient")
                                SendKeys.Send("{TAB}")
                                SendKeys.Send("{TAB}")
                            End If
                            Bafficheseulement = True
                            Prixspéciaux(SolGrid1.CurrentRow.Cells("UM").Value.ToString, Tclient.Text.PadRight(7), SolGrid1.CurrentRow.Cells("Produit").Value.ToString, 0, 0, False, False, SolGrid1.CurrentRow.Cells("quantite").Value, False, "")
                            SolGrid1.CurrentRow.Cells("Prix").Value = Format(DresultPrixPS, Masque_Vendant)
                            If Bokprixspeciaux = True Then
                                SolGrid1.CurrentRow.DefaultCellStyle.BackColor = Color.LightGreen
                                SolGrid1.CurrentRow.Cells("sp").Value = "S"
                            End If



                            SolGrid1.CurrentRow.Cells("Escompte").Value = DresultEscPs
                            If Tclientliv.Text.Trim <> "" Then
                                Prixspéciaux(SolGrid1.CurrentRow.Cells("UM").Value.ToString, Tclientliv.Text.PadRight(7), SolGrid1.CurrentRow.Cells("Produit").Value.ToString, 0, 0, False, False, SolGrid1.CurrentRow.Cells("quantite").Value, True, "")
                                If DresultPrixPS <> 0 Then
                                    SolGrid1.CurrentRow.Cells("Prix").Value = Format(DresultPrixPS, Masque_Vendant)
                                    If Bokprixspeciaux = True Then
                                        SolGrid1.CurrentRow.DefaultCellStyle.BackColor = Color.LightGreen
                                        SolGrid1.CurrentRow.Cells("sp").Value = "S"
                                    End If
                                    SolGrid1.CurrentRow.Cells("Escompte").Value = DresultEscPs
                                End If
                            End If
                            SolGrid1.RefreshEdit()
                            prod_old(SolGrid1.CurrentRow.Index) = SolGrid1.CurrentRow.Cells("produit").Value
                            'quant_old(SolGrid1.CurrentRow.Index) = QteBarcode10
                            um_old(SolGrid1.CurrentRow.Index) = SolGrid1.CurrentRow.Cells("UM").Value.ToString
                            SendKeys.Send("{TAB}")
                            SendKeys.Send("{TAB}")
                            SendKeys.Send("{TAB}")
                            Bafficheseulement = False
                        End If
                    End If
                    'gestion des lots
                End If
                '***********************************************************
            Case SolGrid1.Columns("quantite").Index

                If Mid(prodtemp, 1, 3) = Mid(Rem10, 1, 3) Then Exit Sub
                'si quantite trop grande pour inventaire
                'Dim temp As Double
                e.Cancel = chkcar(SolGrid1.CurrentRow.Cells("quantite").EditedFormattedValue)
                If e.Cancel = True Then Exit Sub


                If Val(SolGrid1.CurrentRow.Cells("quantite").EditedFormattedValue) > "9999999" Then
                        MsgBox("Vous ne pouvez inscrire une quantité supérieure a 9999999")

                        e.Cancel = True
                        Exit Sub
                    End If

                If AVBcs(AVBfiditemstub("TYPE1", AVB + fInprix, 0)).Trim <> "U" _
               And AVBcs(AVBfiditemstub("SERIAL", AVB + fInven, 0)).Trim = oui10 _
               And Val(SolGrid1.CurrentRow.Cells("quantite").EditedFormattedValue.ToString) <> 0 _
               And gserie10 = oui10 Then
                    If SolGrid1.CurrentRow.Cells("quantite").Value < 0 Then
                        If lang = "F" Then
                            MsgBox("Vous pouver retourner seulement un item avec un numéro de série en facturation direct !")
                        Else
                            MsgBox("You must be on invoicing form to return a product with a serial number !")
                        End If
                        e.Cancel = True
                        Exit Sub
                        'SolGrid1.CurrentRow.Cells("quantite").Value = -1
                    End If


                End If


                Dim cat As String = AVBcs(AVBfiditemstub("CAT", AVB + fInprix, 0))
                If dscomma1.Rows(noligne).Item("status").ToString.Trim <> "F" And dscomma1.Rows(noligne).Item("status").ToString.Trim <> "R" Then
                    'status
                    If getstatus() = True Then
                        If lang = "F" Then MsgBox("La quantité disponible de ce produit est insuffisante.")
                        If lang <> "F" Then MsgBox("The quantity on hand is insufficient")
                        SendKeys.Send("{TAB}")
                    End If
                End If
                If ArretBarcode10 = "N" And AVBcs(AVBfiditemstub("LOT", AVB + fInven, 0)).Trim = "N" Then Exit Sub
                'gestion de lot
                If AVBcs(AVBfiditemstub("LOT", AVB + fInven, 0)).Trim = oui10 _
                And Glot10 = oui10 Then

                    Dim frlot As New FrmChoixLot
                    frlot.TxtProduit.Text = SolGrid1.CurrentRow.Cells("produit").EditedFormattedValue.ToString
                    frlot.TxtEntrepot.Text = Tentrepot.Text
                    frlot.TxtMult.Text = dscomma1.Rows(SolGrid1.CurrentRow.Index).Item("mult2").ToString
                    frlot.TxtQuant.Text = SolGrid1.CurrentRow.Cells("quantite").EditedFormattedValue.ToString
                    frlot.TxtLot.Text = dscomma1.Rows(SolGrid1.CurrentRow.Index).Item("lot")
                    frlot.Chkcommande.Checked = True
                    frlot.ShowDialog()
                    If frlot.DialogResult = Windows.Forms.DialogResult.Cancel Then
                        e.Cancel = True
                        frlot.Dispose()
                        Exit Sub
                    End If
                    If frlot.DialogResult = Windows.Forms.DialogResult.OK Then
                        dscomma1.Rows(SolGrid1.CurrentRow.Index).Item("lot") = frlot.TxtLot.Text
                    End If
                    frlot.Dispose()
                    SendKeys.Send("{TAB}")
                End If
                SolGrid1.RefreshEdit()
            Case SolGrid1.Columns("prix").Index
                If Mid(prodtemp, 1, 3) = Mid(Rem10, 1, 3) Then Exit Sub
                If SolGrid1.CurrentRow.Cells("prix").Value Is DBNull.Value Then SolGrid1.CurrentRow.Cells("prix").Value = 0
                e.Cancel = chkcar(SolGrid1.CurrentRow.Cells("prix").EditedFormattedValue)
                If e.Cancel = True Then Exit Sub
                If Val(Trim(SolGrid1.CurrentRow.Cells("prix").Value.ToString)) < 0 Then
                    If lang = "F" Then MsgBox("Le prix ne peut être négatif")
                    If lang <> "F" Then MsgBox("The price should not be negative")
                    e.Cancel = True
                    Exit Sub
                End If
                'prix colonne
                Dim prixc As Double = prixcollonne(SolGrid1.CurrentRow.Cells("prix").FormattedValue.ToString, SolGrid1.CurrentRow.Cells("UM").Value.ToString)
                If prixc <> 0 Then SolGrid1.CurrentRow.Cells("prix").Value = prixc
                SolGrid1.RefreshEdit()
                'en bas du prix coutant
                If (Val(SolGrid1.CurrentRow.Cells("prix").EditedFormattedValue.ToString) / Val(SolGrid1.CurrentRow.Cells("mult2").EditedFormattedValue.ToString)) < Math.Round(Val(AVBcs(AVBfiditemstub("COUT", AVB + fInprix, 0))), 2, MidpointRounding.AwayFromZero) Then
                    If lang = "F" Then MsgBox("Prix de vente inférieur au coûtant")
                    If lang <> "F" Then MsgBox("Selling price lower then the cost")
                    SendKeys.Send("{TAB}")
                End If
                'sur nouvelle ligne seulement
                If noligne = SolGrid1.Rows.Count - 1 Then
                    'indice de l'unite de mesure =0 a 4
                    chkmarge(SolGrid1, e.Cancel, " ")
                    If e.Cancel = True Then
                        Exit Sub
                    End If
                End If
            Case SolGrid1.Columns("escompte").Index
                If AVBcs(AVBfiditemstub("PROESCTAB", AVB + fInprix, 0)) = "N" Then
                    SolGrid1.CurrentRow.Cells("escompte").Value = ""
                    'fle SolGrid1.RefreshEdit()
                End If
                If SolGrid1.CurrentRow.Cells("escompte").EditedFormattedValue.ToString.Trim = "" Then
                    SolGrid1.CurrentRow.Cells("escompte").Value = 0
                    'fle SolGrid1.RefreshEdit()
                End If
                e.Cancel = chkcar(SolGrid1.CurrentRow.Cells("escompte").EditedFormattedValue)
                If e.Cancel = True Then Exit Sub
                Dim esc As Double = Val(SolGrid1.CurrentRow.Cells("escompte").EditedFormattedValue.ToString)
                If esc > 1 Or esc < 0 Then
                    If lang = "F" Then MsgBox("L'escompte ne peut-être plus grand que 1 et du format " + vbCrLf + ".05 pour donner 5% d'escompte")
                    If lang <> "F" Then MsgBox("Discount must be less then 1 and of the format " + vbCrLf + ".05 for 5% discount")
                    e.Cancel = True
                    Exit Sub
                End If
                Bcommenceligne = False
        End Select
    End Sub

    Private Function getstatuskit(Il As Integer) As Boolean
        Dim noligne As Integer = Il
        Dim Sp As String = AVBcs(AVBfiditemstub("CAT", AVB + fInprix, 0)).Trim
        Dim Spi As String = AVBcs(AVBfiditemstub("PRODUIT", AVB + fInven, 0)).Trim
        If Mid(SolGrid1.Rows(Il).Cells("produit").Value.ToString, 1, 3) <> Mid(AVBcs(AVBfiditemstub("MO", AVB + fCompagni, 0)), 1, 3) _
        And AVBcs(AVBfiditemstub("INVENTAIRE", AVB + fInven, 0)) <> "N" Then
            Dim varquantl As Double
            Dim statusl As String = SolGrid1.Rows(Il).Cells("status").EditedFormattedValue.ToString
            Dim qty As Double
            Dim mult As Double
            Dim protemp As String = SolGrid1.Rows(Il).Cells("produit").EditedFormattedValue.ToString
            Dim umtemp As String = SolGrid1.Rows(Il).Cells("um").EditedFormattedValue.ToString
            Dim umx As Integer = TrouveUm(protemp, umtemp)
            mult = Val(AVBcs(AVBfiditemstub("MULT1", AVB + fInprix, umx)))
            qty = Val(AVBcs(AVBfiditemstub("QMAIN", AVB + fInven, 0))) - Val(AVBcs(AVBfiditemstub("QCOM", AVB + fInven, 0))) - Val(AVBcs(AVBfiditemstub("QNF", AVB + fInven, 0)))
            qty = Val(qty + ((quant_old(noligne) * mult)))
            If qty > (Val(SolGrid1.Rows(Il).Cells("quantite").EditedFormattedValue) * mult) Then
                varquantl = Val(SolGrid1.Rows(Il).Cells("quantite").EditedFormattedValue.ToString) * mult
            ElseIf qty > 0 Then
                varquantl = qty
            Else
                varquantl = 0
            End If
            'If statusl <> "F" And statusl <> "I" And statusl <> "R" And statusl <> "P" And statusl <> "B" Then
            SolGrid1.Rows(Il).Cells("status").Value = "S"
                If varquantl < (Val(SolGrid1.Rows(Il).Cells("quantite").EditedFormattedValue) * mult) _
                And SolGrid1.Rows(Il).Cells("quantite").EditedFormattedValue > 0 Then
                    If AVBcs(AVBfiditemstub("MESSAGEINV", AVB + fCompagni, 0)) = oui10 Then
                        getstatuskit = True
                    End If
                    SolGrid1.Rows(Il).Cells("status").Value = "A"
                End If
            'End If
            'dscomma1.Rows(noligne).Item("quantitelivre") = Val(SolGrid1.CurrentRow.Cells("quantite").Value)
            'SolGrid1.CurrentRow.Cells("poid").Value = Val(SolGrid1.CurrentRow.Cells("quantite").Value) * Val(AVBcs(AVBfiditemstub("POID", AVB + fInprix, umx)))
        Else
            Dim protemp As String = SolGrid1.Rows(Il).Cells("produit").EditedFormattedValue.ToString
            Dim umtemp As String = SolGrid1.Rows(Il).Cells("um").EditedFormattedValue.ToString
            Dim umx As Integer = TrouveUm(protemp, umtemp)
            SolGrid1.Rows(Il).Cells("status").Value = "I"
            'dscomma1.Rows(noligne).Item("quantitelivre") = Val(SolGrid1.CurrentRow.Cells("quantite").Value)
            'SolGrid1.CurrentRow.Cells("poid").Value = Val(SolGrid1.CurrentRow.Cells("quantite").Value) * Val(AVBcs(AVBfiditemstub("POID", AVB + fInprix, umx)))
        End If
        If noligne = SolGrid1.Rows.Count - 1 Then
            If Convert.ToBoolean(AVBcs(AVBfiditemstub("INVENTAIRE", AVB + fInven, 0)) = "N" _
            And SolGrid1.Rows(Il).Cells("status").EditedFormattedValue <> "I") Then
                SolGrid1.Rows(Il).Cells("status").Value = "S"
            End If
        End If

    End Function


    Private Function getstatus() As Boolean
        Dim noligne As Integer = SolGrid1.CurrentRow.Index
        Dim Sp As String = AVBcs(AVBfiditemstub("CAT", AVB + fInprix, 0)).Trim
        Dim Spi As String = AVBcs(AVBfiditemstub("PRODUIT", AVB + fInven, 0)).Trim
        If Mid(SolGrid1.CurrentRow.Cells("produit").Value.ToString, 1, 3) <> Mid(AVBcs(AVBfiditemstub("MO", AVB + fCompagni, 0)), 1, 3) _
        And AVBcs(AVBfiditemstub("INVENTAIRE", AVB + fInven, 0)) <> "N" Then
            Dim varquantl As Double
            Dim statusl As String = dscomma1.Rows(noligne).Item("status").ToString
            Dim qty As Double
            Dim mult As Double
            Dim protemp As String = SolGrid1.CurrentRow.Cells("produit").EditedFormattedValue.ToString
            Dim umtemp As String = SolGrid1.CurrentRow.Cells("um").EditedFormattedValue.ToString
            Dim umx As Integer = TrouveUm(protemp, umtemp)
            mult = Val(AVBcs(AVBfiditemstub("MULT1", AVB + fInprix, umx)))
            qty = Val(AVBcs(AVBfiditemstub("QMAIN", AVB + fInven, 0))) - Val(AVBcs(AVBfiditemstub("QCOM", AVB + fInven, 0))) - Val(AVBcs(AVBfiditemstub("QNF", AVB + fInven, 0)))
            qty = Val(qty + ((quant_old(noligne) * mult)))
            If qty > (Val(SolGrid1.CurrentRow.Cells("quantite").EditedFormattedValue) * mult) Then
                varquantl = Val(SolGrid1.CurrentRow.Cells("quantite").Value.ToString) * mult
            ElseIf qty > 0 Then
                varquantl = qty
            Else
                varquantl = 0
            End If
            If statusl <> "F" And statusl <> "I" And statusl <> "R" And statusl <> "P" And statusl <> "B" Then
                SolGrid1.CurrentRow.Cells("status").Value = "S"
                If varquantl < (Val(SolGrid1.CurrentRow.Cells("quantite").Value) * mult) _
                And SolGrid1.CurrentRow.Cells("quantite").Value > 0 Then
                    If My.Settings.qtedispenattente.Trim = "O" And barcodeauto = False Then



                        Dim Dqtecomsl As Double = trouveqtecomsanslien(protemp, SNocommande, noligne.ToString)
                        Dim Dqteattsl As Double = trouveqteattenduesanslien(protemp, SNocommande)
                        varquantl = varquantl + Dqteattsl


                        Dim frq As New Frmquestionlongue


                        If lang = "F" Then frq.LblMessage.Text = "Voulez-vous associer cette commande à une commande fournisseur? Si Non, fonction des qtés attendues pour inventaire.  Qté Attendues (" & Dqteattsl & ")  Qté commandé (" & Dqtecomsl & ") (sans lien)"
                        If lang <> "F" Then frq.LblMessage.Text = "Voulez-vous associer cette commande à une commande fournisseur? Si Non, fonction des qtés attendues pour inventaire.  Qté Attendues (" & Dqteattsl & ")  Qté commandé (" & Dqtecomsl & ") (sans lien)"
                        frq.BtOui.Focus()
                        frq.ShowDialog()
                        If frq.DialogResult = Windows.Forms.DialogResult.Yes Then
                            If AVBcs(AVBfiditemstub("MESSAGEINV", AVB + fCompagni, 0)) = oui10 Then
                                getstatus = False
                            End If
                            SolGrid1.CurrentRow.Cells("status").Value = "A"
                        Else
                            If AVBcs(AVBfiditemstub("MESSAGEINV", AVB + fCompagni, 0)) = oui10 Then
                                getstatus = False
                            End If
                            SolGrid1.CurrentRow.Cells("status").Value = "G"
                        End If
                        SendKeys.Send("{TAB}")



                    Else
                        If AVBcs(AVBfiditemstub("MESSAGEINV", AVB + fCompagni, 0)) = oui10 Then
                            getstatus = True
                        End If
                        SolGrid1.CurrentRow.Cells("status").Value = "A"
                    End If
                End If

            End If
            'dscomma1.Rows(noligne).Item("quantitelivre") = Val(SolGrid1.CurrentRow.Cells("quantite").Value)
            dscomma1.Rows(noligne).Item("poid") = Val(SolGrid1.CurrentRow.Cells("quantite").Value) * Val(AVBcs(AVBfiditemstub("POID", AVB + fInprix, umx)))
        Else
            Dim protemp As String = SolGrid1.CurrentRow.Cells("produit").EditedFormattedValue.ToString
            Dim umtemp As String = SolGrid1.CurrentRow.Cells("um").EditedFormattedValue.ToString
            Dim umx As Integer = TrouveUm(protemp, umtemp)
            dscomma1.Rows(noligne).Item("status") = "I"
            'dscomma1.Rows(noligne).Item("quantitelivre") = Val(SolGrid1.CurrentRow.Cells("quantite").Value)
            dscomma1.Rows(noligne).Item("poid") = Val(SolGrid1.CurrentRow.Cells("quantite").Value) * Val(AVBcs(AVBfiditemstub("POID", AVB + fInprix, umx)))
        End If
        If noligne = SolGrid1.Rows.Count - 1 Then
            If Convert.ToBoolean(AVBcs(AVBfiditemstub("INVENTAIRE", AVB + fInven, 0)) = "N" _
            And dscomma1.Rows(noligne).Item("status") <> "I") Then
                dscomma1.Rows(noligne).Item("status") = "S"
            End If
        End If

    End Function
    Private Function getstatusprodcore(noligne As Integer, Sp As String, Spi As String) As Boolean
        ' Dim noligne As Integer = SolGrid1.CurrentRow.Index
        'Dim Sp As String = AVBcs(AVBfiditemstub("CAT", AVB + fInprix, 0)).Trim
        'Dim Spi As String = AVBcs(AVBfiditemstub("PRODUIT", AVB + fInven, 0)).Trim

        AVBSTAT = AVBPosn(AVB + fInprix, Sp.PadRight(30), 1, "", &H100)
        AVBSTAT = AVBread(AVB + fInprix, 1)
        If AVBSTAT = 0 Then

            AVBSTAT = AVBPosn(AVB + fInven, Tentrepot.Text.PadLeft(3) + Sp.PadRight(30), 1, "", &H100)
            AVBSTAT = AVBread(AVB + fInven, 1)
        End If

        If Mid(SolGrid1.Rows(noligne).Cells("produit").Value.ToString, 1, 3) <> Mid(AVBcs(AVBfiditemstub("MO", AVB + fCompagni, 0)), 1, 3) _
        And AVBcs(AVBfiditemstub("INVENTAIRE", AVB + fInven, 0)) <> "N" Then
            Dim varquantl As Double
            Dim statusl As String = dscomma1.Rows(noligne).Item("status").ToString
            Dim qty As Double
            Dim mult As Double
            Dim protemp As String = SolGrid1.Rows(noligne).Cells("produit").EditedFormattedValue.ToString
            Dim umtemp As String = SolGrid1.Rows(noligne).Cells("um").EditedFormattedValue.ToString
            Dim umx As Integer = TrouveUm(protemp, umtemp)
            mult = Val(AVBcs(AVBfiditemstub("MULT1", AVB + fInprix, umx)))
            qty = Val(AVBcs(AVBfiditemstub("QMAIN", AVB + fInven, 0))) - Val(AVBcs(AVBfiditemstub("QCOM", AVB + fInven, 0))) - Val(AVBcs(AVBfiditemstub("QNF", AVB + fInven, 0)))
            qty = Val(qty + ((quant_old(noligne) * mult)))
            If qty > (Val(SolGrid1.Rows(noligne).Cells("quantite").EditedFormattedValue) * mult) Then
                varquantl = Val(SolGrid1.Rows(noligne).Cells("quantite").Value.ToString) * mult
            ElseIf qty > 0 Then
                varquantl = qty
            Else
                varquantl = 0
            End If
            If statusl <> "F" And statusl <> "I" And statusl <> "R" And statusl <> "P" And statusl <> "B" Then
                SolGrid1.Rows(noligne).Cells("status").Value = "S"
                If varquantl < (Val(SolGrid1.Rows(noligne).Cells("quantite").Value) * mult) _
                And SolGrid1.Rows(noligne).Cells("quantite").Value > 0 Then
                    If AVBcs(AVBfiditemstub("MESSAGEINV", AVB + fCompagni, 0)) = oui10 Then
                        getstatusprodcore = True
                    End If
                    SolGrid1.Rows(noligne).Cells("status").Value = "A"
                End If
            End If
            'dscomma1.Rows(noligne).Item("quantitelivre") = Val(SolGrid1.CurrentRow.Cells("quantite").Value)
            dscomma1.Rows(noligne).Item("poid") = Val(SolGrid1.Rows(noligne).Cells("quantite").Value) * Val(AVBcs(AVBfiditemstub("POID", AVB + fInprix, umx)))
        Else
            Dim protemp As String = SolGrid1.Rows(noligne).Cells("produit").EditedFormattedValue.ToString
            Dim umtemp As String = SolGrid1.Rows(noligne).Cells("um").EditedFormattedValue.ToString
            Dim umx As Integer = TrouveUm(protemp, umtemp)
            dscomma1.Rows(noligne).Item("status") = "I"
            dscomma1.Rows(noligne).Item("poid") = Val(SolGrid1.Rows(noligne).Cells("quantite").Value) * Val(AVBcs(AVBfiditemstub("POID", AVB + fInprix, umx)))
        End If
        If noligne = SolGrid1.Rows.Count - 1 Then
            If Convert.ToBoolean(AVBcs(AVBfiditemstub("INVENTAIRE", AVB + fInven, 0)) = "N" _
            And dscomma1.Rows(noligne).Item("status") <> "I") Then
                dscomma1.Rows(noligne).Item("status") = "S"
            End If
        End If

    End Function
    Private Sub completeproduit(ByVal index As Integer)
        SolGrid1.Rows(index).Cells("description").Value = AVBcs(AVBfiditemstub("DESCR", AVB + fInprix, 0))
        If lang4 <> "F" And AVBcs(AVBfiditemstub("DESCA", AVB + fInprix, 0)).Trim <> "" Then SolGrid1.Rows(index).Cells("description").Value = AVBcs(AVBfiditemstub("DESCA", AVB + fInprix, 0))
        dscomma1.Rows(index).Item("client") = Tclient.Text
        SolGrid1.Rows(index).Cells("um").Value = AVBcs(AVBfiditemstub("PAR", AVB + fInprix, 0))
        um_old(index) = AVBcs(AVBfiditemstub("PAR", AVB + fInprix, 0))
        dscomma1.Rows(index).Item("coutant") = Val(AVBcs(AVBfiditemstub("COUT", AVB + fInprix, 0)))
        dscomma1.Rows(index).Item("groupe") = AVBcs(AVBfiditemstub("TYPE", AVB + fInprix, 0))
        dscomma1.Rows(index).Item("postevente") = AVBcs(AVBfiditemstub("POSTC", AVB + fInprix, 0))
        dscomma1.Rows(index).Item("vendeur") = Txtvendeur.Text
        'departement de vente pour transfert au cr
        If AVBcs(AVBfiditemstub("DEPT", AVB + fCompagni, 0)) = oui10 Then
            dscomma1.Rows(index).Item("dept") = "1"
            If Trim(AVBcs(AVBfiditemstub("POSTC", AVB + fInprix, 0))) <> "" Then
                dscomma1.Rows(index).Item("dept") = AVBcs(AVBfiditemstub("POSTC", AVB + fInprix, 0))
            End If
            If Mid(AVBcs(AVBfiditemstub("MON", AVB + fClient, 0)), 1, 1) <> "C" _
            And Trim(AVBcs(AVBfiditemstub("POSTU", AVB + fInprix, 0))) <> "" Then
                dscomma1.Rows(index).Item("dept") = AVBcs(AVBfiditemstub("POSTU", AVB + fInprix, 0))
            End If
        End If
        If Convert.ToBoolean(Mid(AVBcs(AVBfiditemstub("INVENTAIRE", AVB + fInven, 0)), 1, 1) <> oui10 And dscomma1.Rows(index).Item("status") <> "I") Then
            SolGrid1.Rows(index).Cells("status").Value = "S"
        End If
        dscomma1.Rows(index).Item("quantite") = AVBcs(AVBfiditemstub("QUANVEN", AVB + fInprix, 0))
        'pour calcul de taxe apogee
        dscomma1.Rows(index).Item("taxff") = "0"
        dscomma1.Rows(index).Item("fournisseur") = AVBcs(AVBfiditemstub("FOURN1", AVB + fInprix, 0))
        If Trim(AVBcs(AVBfiditemstub("TAXFED", AVB + fInprix, 0))) = "X" Then dscomma1.Rows(index).Item("taxff") = "2"
        If Trim(AVBcs(AVBfiditemstub("TAXFED", AVB + fInprix, 0))) = "N" Then dscomma1.Rows(index).Item("taxff") = "1"
        dscomma1.Rows(index).Item("taxpp") = "0"
        If Trim(AVBcs(AVBfiditemstub("TAXPRO", AVB + fInprix, 0))) = oui10 Or Trim(AVBcs(AVBfiditemstub("TAXPRO", AVB + fInprix, 0))) = "P" Then dscomma1.Rows(index).Item("taxpp") = "1"
        If Trim(AVBcs(AVBfiditemstub("TAXPRO", AVB + fInprix, 0))) = "S" Then dscomma1.Rows(index).Item("taxpp") = "2"
        dscomma1.Rows(index).Item("loc1") = AVBcs(AVBfiditemstub("LOCAT", AVB + fInven, 0))
        dscomma1.Rows(index).Item("taux") = AVBcs(AVBfiditemstub("TXF", AVB + fInprix, 0))
        If Val(AVBcs(AVBfiditemstub("TAUX", AVB + fClient, 0))) <> 0 Then
            dscomma1.Rows(index).Item("taux") = AVBcs(AVBfiditemstub("TAUX", AVB + fClient, 0))
        End If
        Dim strsql As String = dscomma1.Rows(index).Item("taux").ToString
        dscomma1.Rows(index).Item("datelivre") = Ddaterequis.Text
        dscomma1.Rows(index).Item("umx") = 0
        dscomma1.Rows(index).Item("mult2") = AVBcs(AVBfiditemstub("MULT1", AVB + fInprix, 0))
        dscomma1.Rows(index).Item("div2") = AVBcs(AVBfiditemstub("DIV1", AVB + fInprix, 0))
        SolGrid1.Rows(index).Cells("prix").Value = ""
        SolGrid1.Rows(index).Cells("montant").Value = ""
        SolGrid1.Rows(index).Cells("escompte").Value = ""
        dscomma1.Rows(index).Item("impk") = "O"
        SolGrid1.RefreshEdit()
    End Sub
    Private Sub SolGrid1_CellValidated1(ByVal sender As Object, ByVal e As System.Windows.Forms.DataGridViewCellEventArgs) Handles SolGrid1.CellValidated
        If SolGrid1.ContainsFocus = False Then Exit Sub
        If Bafficheseulement = True Or pgup = True Or pgdn = True Or gridfocus = False Or uparr = True Or dnarr = True Or lfarr = True Then Exit Sub
        'If SolGrid1.Focused = False Then Exit Sub
        Dim prodtemp As String = SolGrid1.CurrentRow.Cells("produit").EditedFormattedValue.ToString.PadRight(30)
       

        Dim remdiv As Boolean
        'si remarque ou divers
        If (Mid(prodtemp, 1, 3) = Mid(Rem10, 1, 3)) Then Exit Sub
        If (Mid(prodtemp, 1, 3) = Mid(Div10, 1, 3)) _
        Or (Mid(prodtemp, 1, 3) = Mid(Ndiv10, 1, 3)) Then remdiv = True
        Dim index As Integer = SolGrid1.CurrentCell.ColumnIndex
        Select Case index
            Case SolGrid1.Columns("Produit").Index
                If remdiv = True Then Exit Sub
                'TrouveDispo(prodtemp, SolGrid1.CurrentRow.Index, Tentrepot.Text.PadLeft(3), SolGrid1.CurrentRow.Cells("um").Value.ToString)
            Case SolGrid1.Columns("quantite").Index
                'If remdiv = True Then Exit Sub
                'gestion des poids pour la viande
                'If SolGrid1.CurrentRow.Cells("quantiteliv").EditedFormattedValue.ToString.Trim = "" Then SolGrid1.CurrentRow.Cells("quantiteliv").Value = 0
                If gespoids10 = oui10 Then
                    Dim envtab As Boolean
                    Dim klg As String = AVBcs(AVBfiditemstub("KLG", AVB + fInprix, TrouveUm(prodtemp, SolGrid1.CurrentRow.Cells("UM").EditedFormattedValue)))
                    If klg = "?" Then
                        Dim frmq As New FrmQuestion
                        If lang = "F" Then frmq.LblMessage.Text = "Est-ce que ce produit a une gestion de poids?"
                        If lang <> "F" Then frmq.LblMessage.Text = "Does this product have weight management?"
                        frmq.ShowDialog()
                        If frmq.DialogResult <> Windows.Forms.DialogResult.Yes Then
                            klg = oui10
                            envtab = True
                        End If
                        frmq.Dispose()
                    End If
                    If klg = oui10 Or klg = "X" Then
                        'Dim frmpoid As New FrmPoidsboite
                        'frmpoid.StartPosition = FormStartPosition.Manual
                        'Dim working_are As Rectangle = SystemInformation.WorkingArea
                        'Dim x As Integer = Me.Location.X + SolGrid1.Location.X + 606
                        'Dim y As Integer = Me.Location.Y + SolGrid1.Location.Y + 6
                        'frmpoid.Location = New Point(x, y)
                        'frmpoid.Height = SolGrid1.Height + 5



                        'frmpoid.TxtQuant.Text = SolGrid1.CurrentRow.Cells("quantite").EditedFormattedValue
                        'frmpoid.TxtLigne.Text = SolGrid1.CurrentRow.Index
                        'frmpoid.SolGrid1.DataSource = DsPoids
                        'frmpoid.txtligorg.Text = SolGrid1.FirstDisplayedScrollingRowIndex.ToString
                        'frmpoid.ShowDialog()
                        'envtab = True
                        'frmpoid.Dispose()
                        'dscomma1.Rows(SolGrid1.CurrentRow.Index).Item("poidv") = DsPoids.Rows(SolGrid1.CurrentRow.Index).Item("poidv")
                        'dscomma1.Rows(SolGrid1.CurrentRow.Index).Item("paq_bte") = DsPoids.Rows(SolGrid1.CurrentRow.Index).Item("paq_bte")
                        Dim frmpoid As New FrmPoidsboite
                        frmpoid.StartPosition = FormStartPosition.Manual
                        Dim working_are As Rectangle = SystemInformation.WorkingArea
                        Dim x As Integer = Me.Location.X + SolGrid1.Location.X + 606
                        Dim y As Integer = Me.Location.Y + SolGrid1.Location.Y + 6
                        frmpoid.Location = New Point(x, y)
                        frmpoid.Height = SolGrid1.Height + 5
                        'si valeur negative
                        frmpoid.TxtQuant.Text = Math.Round(Math.Abs(Val(SolGrid1.CurrentRow.Cells("quantite").EditedFormattedValue)), 0, MidpointRounding.AwayFromZero)
                        frmpoid.TxtLigne.Text = SolGrid1.CurrentRow.Index
                        frmpoid.SolGrid1.DataSource = DsPoids
                        frmpoid.txtligorg.Text = SolGrid1.FirstDisplayedScrollingRowIndex.ToString
                        frmpoid.ShowDialog()
                        If frmpoid.DialogResult = Windows.Forms.DialogResult.OK Then
                            envtab = True
                            Dim Iindexpoid As Integer = Val(frmpoid.txtlignecourante.Text.Trim)
                            Dim Dpaq_bte As Double = Val(frmpoid.SolGrid1.Rows(Iindexpoid).Cells("paq_bte").EditedFormattedValue.ToString)
                            Dim Dpoidv As Double = Val(frmpoid.SolGrid1.Rows(Iindexpoid).Cells("Poidv").EditedFormattedValue.ToString)

                            dscomma1.Rows(Me.SolGrid1.CurrentRow.Index).Item("poid") = DsPoids.Rows(Iindexpoid).Item("poidv")
                            dscomma1.Rows(Me.SolGrid1.CurrentRow.Index).Item("paq_bte") = DsPoids.Rows(Iindexpoid).Item("paq_bte")

                            'dscomma1.Rows(Me.SolGrid1.CurrentRow.Index).Item("poid") = DsPoids.Rows(SolGrid1.CurrentRow.Index).Item("poidv")
                            'dscomma1.Rows(Me.SolGrid1.CurrentRow.Index).Item("paq_bte") = DsPoids.Rows(SolGrid1.CurrentRow.Index).Item("paq_bte")
                            If klg = oui10 Then
                                dscomma1.Rows(Me.SolGrid1.CurrentRow.Index).Item("paq_bte") = Dpaq_bte
                                DsPoids.Rows(SolGrid1.CurrentRow.Index).Item("poidv") = Val(frmpoid.SolGrid1.Rows(Iindexpoid).Cells("Poidv").EditedFormattedValue.ToString)
                                DsPoids.Rows(SolGrid1.CurrentRow.Index).Item("paq_bte") = Val(frmpoid.SolGrid1.Rows(Iindexpoid).Cells("paq_bte").EditedFormattedValue.ToString)
                            End If
                            If SolGrid1.CurrentRow.DefaultCellStyle.BackColor = Color.Coral Then
                                SolGrid1.CurrentRow.DefaultCellStyle = SolGrid1.RowsDefaultCellStyle
                            End If
                            frmpoid.Dispose()
                        Else
                            frmpoid.Dispose()

                            Exit Sub
                        End If
                    End If
                    If envtab = True Then SendKeys.Send("{TAB}")
                End If
                If SolGrid1.CurrentRow.Cells("prix").Value.ToString.Trim = "" Then
                    Dim dd As String = SolGrid1.CurrentRow.Cells("UM").Value.ToString
                    Dim qte As Double = Val(SolGrid1.CurrentRow.Cells("quantite").EditedFormattedValue.ToString)
                    If Val(dscomma1.Rows(SolGrid1.CurrentRow.Index).Item("paq_bte")) <> 0 Then qte = Val(dscomma1.Rows(SolGrid1.CurrentRow.Index).Item("paq_bte"))

                    Prixspéciaux(SolGrid1.CurrentRow.Cells("UM").Value.ToString, Tclient.Text.PadRight(7), SolGrid1.CurrentRow.Cells("Produit").Value.ToString, 0, 0, False, False, qte, False, "")
                    SolGrid1.CurrentRow.Cells("Prix").Value = Format(DresultPrixPS, Masque_Vendant)

                    If Bokprixspeciaux = True Then
                        SolGrid1.CurrentRow.DefaultCellStyle.BackColor = Color.LightGreen
                        SolGrid1.CurrentRow.Cells("sp").Value = "S"
                    End If

                    SolGrid1.CurrentRow.Cells("Escompte").Value = DresultEscPs
                    If Tclientliv.Text.Trim <> "" Then
                        Prixspéciaux(SolGrid1.CurrentRow.Cells("UM").Value.ToString, Tclientliv.Text.PadRight(7), SolGrid1.CurrentRow.Cells("Produit").Value.ToString, 0, 0, False, False, SolGrid1.CurrentRow.Cells("quantite").Value, True, "")
                        If DresultPrixPS <> 0 Then
                            SolGrid1.CurrentRow.Cells("Prix").Value = Format(DresultPrixPS, Masque_Vendant)
                            If Bokprixspeciaux = True Then
                                SolGrid1.CurrentRow.DefaultCellStyle.BackColor = Color.LightGreen
                                SolGrid1.CurrentRow.Cells("sp").Value = "S"
                            End If
                            SolGrid1.CurrentRow.Cells("Escompte").Value = DresultEscPs
                        End If
                    End If
                    SolGrid1.RefreshEdit()
                End If
                If AVBcs(AVBfiditemstub("GCORE", AVB + fInprix, 0)) = oui10 And gcore10 = "I" Then
                    Dim frmq As New FrmQuestion
                    If lang = "F" Then frmq.LblMessage.Text = "Retournez-vous un core?"
                    If lang <> "F" Then frmq.LblMessage.Text = "Are you returning a core?"
                    frmq.ShowDialog()
                    If frmq.DialogResult = Windows.Forms.DialogResult.Yes Then
                        If SolGrid1.CurrentRow.Cells("quantite").Value = 0 Then SolGrid1.CurrentRow.Cells("prix").Value = Format(Val(AVBcs(AVBfiditemstub("COREVALUE", AVB + fInprix, 0))), Masque_Vendant)
                        dscomma1.Rows(SolGrid1.CurrentRow.Index).Item("coutant") = Val(AVBcs(AVBfiditemstub("COREVALUE", AVB + fInprix, 0)))
                    Else
                        'si nouvelle ligne
                        If prod_old(SolGrid1.CurrentRow.Index).Trim = "" Then SolGrid1.CurrentRow.Cells("prix").Value = Val(SolGrid1.CurrentRow.Cells("prix").FormattedValue) + Val(AVBcs(AVBfiditemstub("COREVALUE", AVB + fInprix, 0)))
                    End If
                    SendKeys.Send("{TAB}")
                End If
            Case SolGrid1.Columns("prix").Index
                Dim ppr As Double = Val(SolGrid1.CurrentRow.Cells("Prix").EditedFormattedValue)
                SolGrid1.CurrentRow.Cells("Prix").Value = Format(ppr, Masque_Vendant)
            Case SolGrid1.Columns("escompte").Index
                Calculegrid(SolGrid1.CurrentRow.Index, True, SolGrid1)
                Dim dd As Double = Val(dscomma1.Rows(SolGrid1.CurrentRow.Index).Item("mult2").ToString)
                If dd = 0 Then dd = 1
                'demande le cost du divers
                If remdiv = True Then
                    Dim frcout As New FrmCoutDivers
                    frcout.TxtCout.Text = Format(dscomma1.Rows(SolGrid1.CurrentRow.Index).Item("coutant"), Masque_Coutant)
                    frcout.ShowDialog()
                    dscomma1.Rows(SolGrid1.CurrentRow.Index).Item("coutant") = avbcout
                    frcout.Dispose()
                    SendKeys.Send("{TAB}")
                End If
        End Select
    End Sub
    Private Sub SolGrid1_RowValidated1(ByVal sender As Object, ByVal e As System.Windows.Forms.DataGridViewCellEventArgs) Handles SolGrid1.RowValidated
        If SolGrid1.Rows.Count - 1 < 0 Then Exit Sub
        If SolGrid1.ContainsFocus = False Then Exit Sub
        If efflignevide = True Or promener = True Or pgup = True Or pgdn = True Or gridfocus = False Or uparr = True Or dnarr = True Then Exit Sub
        If Bafficheseulement = True Then Exit Sub
        Bcommenceligne = False
        prod_old(SolGrid1.CurrentRow.Index) = SolGrid1.CurrentRow.Cells("Produit").Value.ToString
        If Mid(SolGrid1.CurrentRow.Cells("Produit").EditedFormattedValue.ToString, 1, 3) = Mid(Rem10, 1, 3) Then Exit Sub
        If dscomma1.Rows(SolGrid1.CurrentRow.Index) IsNot DBNull.Value And dscomma1.Rows(SolGrid1.CurrentRow.Index).RowState <> DataRowState.Deleted Then
            Dim quant As Double = Val(SolGrid1.CurrentRow.Cells("quantite").Value)
            Dim quantpb As Double = Val(SolGrid1.CurrentRow.Cells("paq_bte").Value)
            If quantpb <> 0 Then

                If quant_paqbte(SolGrid1.CurrentRow.Index) <> quantpb Or um_old(SolGrid1.CurrentRow.Index).Trim <> SolGrid1.CurrentRow.Cells("um").Value.ToString.Trim Then
                    If quant_paqbte(SolGrid1.CurrentRow.Index) <> 0 Then Updateinventaire(SolGrid1.CurrentRow.Cells("Produit").Value.ToString.PadRight(30), Tentrepot.Text.PadLeft(3), -1, 1, quant_paqbte(SolGrid1.CurrentRow.Index), um_old(SolGrid1.CurrentRow.Index), False, " ", 0, dscomma1.Rows(SolGrid1.CurrentRow.Index).Item("lot").ToString)
                    Updateinventaire(SolGrid1.CurrentRow.Cells("Produit").Value.ToString.PadRight(30), Tentrepot.Text.PadLeft(3), 1, 1, quantpb, SolGrid1.CurrentRow.Cells("um").Value.ToString, False, " ", 0, dscomma1.Rows(SolGrid1.CurrentRow.Index).Item("lot").ToString)
                    'quant_old(SolGrid1.CurrentRow.Index) = Val(SolGrid1.CurrentRow.Cells("quantite").Value)
                    quant_old(SolGrid1.CurrentRow.Index) = quant
                    quant_paqbte(SolGrid1.CurrentRow.Index) = quantpb
                    um_old(SolGrid1.CurrentRow.Index) = SolGrid1.CurrentRow.Cells("um").EditedFormattedValue.ToString

                End If
            Else
                If quant_old(SolGrid1.CurrentRow.Index) <> quant Or um_old(SolGrid1.CurrentRow.Index).Trim <> SolGrid1.CurrentRow.Cells("um").Value.ToString.Trim Then
                    If quant_old(SolGrid1.CurrentRow.Index) <> 0 Then Updateinventaire(SolGrid1.CurrentRow.Cells("Produit").Value.ToString.PadRight(30), Tentrepot.Text.PadLeft(3), -1, 1, quant_old(SolGrid1.CurrentRow.Index), um_old(SolGrid1.CurrentRow.Index), False, " ", 0, dscomma1.Rows(SolGrid1.CurrentRow.Index).Item("lot").ToString)
                    Updateinventaire(SolGrid1.CurrentRow.Cells("Produit").Value.ToString.PadRight(30), Tentrepot.Text.PadLeft(3), 1, 1, quant, SolGrid1.CurrentRow.Cells("um").Value.ToString, False, " ", 0, dscomma1.Rows(SolGrid1.CurrentRow.Index).Item("lot").ToString)
                    'quant_old(SolGrid1.CurrentRow.Index) = Val(SolGrid1.CurrentRow.Cells("quantite").Value)
                    quant_old(SolGrid1.CurrentRow.Index) = quant
                    'quant_paqbte(SolGrid1.CurrentRow.Index) = quant
                    um_old(SolGrid1.CurrentRow.Index) = SolGrid1.CurrentRow.Cells("um").EditedFormattedValue.ToString

                End If
            End If

           
        End If
        If SolGrid1.CurrentRow.Index = dscomma1.Rows.Count - 1 Then

            'gestion des cores ou rabattement
            Dim Sgcoreanc As String = AVBcs(AVBfiditemstub("GCORE", AVB + fInprix, 0))
            Dim Dquantanc As Double = Val(AVBcs(AVBfiditemstub("COREVALUE", AVB + fInprix, 0)))
            Dim Sstatutanc As String = SolGrid1.CurrentRow.Cells("status").EditedFormattedValue.ToString
            If (AVBcs(AVBfiditemstub("GCORE", AVB + fInprix, 0)) = oui10 _
            Or AVBcs(AVBfiditemstub("GCORE", AVB + fInprix, 0)) = "R" _
            Or AVBcs(AVBfiditemstub("GCORE", AVB + fInprix, 0)) = "V" _
            Or AVBcs(AVBfiditemstub("GCORE", AVB + fInprix, 0)) = "T" _
            Or AVBcs(AVBfiditemstub("GCORE", AVB + fInprix, 0)) = "E") _
            And gcore10 = "E" _
            And SolGrid1.CurrentRow.Index = SolGrid1.Rows.Count - 1 _
            And AVBcs(AVBfiditemstub("PRODCORE", AVB + fInprix, 0)).Trim <> "" Then
                Dim gp As String = AVBcs(AVBfiditemstub("GCORE", AVB + fInprix, 0))
                AVBSTAT = AVBPosn(AVB + fInprix, AVBcs(AVBfiditemstub("PRODCORE", AVB + fInprix, 0)).PadRight(30), 1, "", &H100)
                AVBSTAT = AVBread(AVB + fInprix, 1)
                If AVBSTAT = 0 Then
                    Dim quant As Double = SolGrid1.CurrentRow.Cells("quantite").Value
                    Dim prix As Double = SolGrid1.CurrentRow.Cells("montant").Value


                    'Dim prix As Double = SolGrid1.CurrentRow.Cells("unit").Value
                    Dim nvligne As Integer
                    Dim ligneor As Integer = SolGrid1.CurrentRow.Index

                    adligne()
                    nvligne = SolGrid1.Rows.Count - 1
                    AVBSTAT = AVBPosn(AVB + fInven, Tentrepot.Text.PadLeft(3) + AVBcs(AVBfiditemstub("PRODCORE", AVB + fInprix, 0)).PadRight(30), 1, "", &H100)
                    AVBSTAT = AVBread(AVB + fInven, 1)
                    SolGrid1.Rows(nvligne).Cells("produit").Value = AVBcs(AVBfiditemstub("CAT", AVB + fInprix, 0)).PadRight(30)
                    completeproduit(nvligne)
                    ' SolGrid1.Rows(nvligne).Cells("prix").Value = prixcollonne(Convert.ToString(0), SolGrid1.CurrentRow.Cells("UM").Value.ToString)

                    dscomma1.Rows(nvligne).Item("impk") = "O"
                    dscomma1.Rows(nvligne).Item("coreoui") = oui10

                    SolGrid1.Rows(nvligne).Cells("quantite").Value = quant


                    Prixspéciaux(SolGrid1.Rows(nvligne).Cells("UM").Value.ToString, Tclient.Text.PadRight(7), SolGrid1.Rows(nvligne).Cells("Produit").Value.ToString, 0, 0, False, False, SolGrid1.Rows(nvligne).Cells("quantite").Value, True, "")
                    If Bokprixspeciaux = True Then
                        SolGrid1.Rows(nvligne).DefaultCellStyle.BackColor = Color.LightGreen
                        SolGrid1.Rows(nvligne).Cells("sp").Value = "S"
                    End If
                    SolGrid1.Rows(nvligne).Cells("Prix").Value = Format(DresultPrixPS, Masque_Vendant)
                    SolGrid1.Rows(nvligne).Cells("Escompte").Value = 0
                    If Tclientliv.Text.Trim <> "" Then
                        Prixspéciaux(SolGrid1.CurrentRow.Cells("UM").Value.ToString, Tclientliv.Text.PadRight(7), SolGrid1.CurrentRow.Cells("Produit").Value.ToString, 0, 0, False, False, SolGrid1.CurrentRow.Cells("quantite").Value, True, "")
                        If DresultPrixPS <> 0 Then
                            SolGrid1.CurrentRow.Cells("Prix").Value = Format(DresultPrixPS, Masque_Vendant)
                            If Bokprixspeciaux = True Then
                                SolGrid1.CurrentRow.DefaultCellStyle.BackColor = Color.LightGreen
                                SolGrid1.CurrentRow.Cells("sp").Value = "S"
                            End If
                            SolGrid1.CurrentRow.Cells("Escompte").Value = DresultEscPs
                        End If
                    End If
                    If DresultPrixPS = 0 Then SolGrid1.Rows(nvligne).Cells("Prix").Value = Format(Val(AVBcs(AVBfiditemstub("PRIX1", AVB + fInprix, 0))), Masque_Vendant)
                    getstatusprodcore(nvligne, AVBcs(AVBfiditemstub("CAT", AVB + fInprix, 0)).PadRight(30), AVBcs(AVBfiditemstub("CAT", AVB + fInprix, 0)).PadRight(30))
                    If gp = "O" And gcore10 = "O" Then
                        SolGrid1.Rows(nvligne).Cells("status").Value = Sstatutanc




                    End If
                    If gp = "E" And gcore10 = "E" Then
                        SolGrid1.Rows(nvligne).Cells("UM").Value = SolGrid1.Rows(ligneor).Cells("UM").EditedFormattedValue
                        Dim umx As Integer = TrouveUm(SolGrid1.Rows(nvligne).Cells("produit").Value.ToString, SolGrid1.Rows(nvligne).Cells("UM").Value)
                        SolGrid1.Rows(nvligne).Cells("Prix").Value = Format(Val(AVBcs(AVBfiditemstub("PRIX1", AVB + fInprix, umx))), Masque_Vendant)
                        dscomma1.Rows(nvligne).Item("mult2") = AVBcs(AVBfiditemstub("MULT1", AVB + fInprix, umx))
                        dscomma1.Rows(nvligne).Item("div2") = AVBcs(AVBfiditemstub("DIV1", AVB + fInprix, umx))
                    End If
                    If Sgcoreanc = "T" Then
                        If quant <> 0 Then prix = prix / SolGrid1.Rows(nvligne).Cells("quantite").Value

                        SolGrid1.Rows(nvligne).Cells("Prix").Value = Format(Math.Round((prix * Dquantanc), 2, MidpointRounding.AwayFromZero), Masque_Vendant)
                        ' SolGrid1.Rows(nvligne).Cells("Prix").Value = Format(Math.Round((prix), 2), Masque_Vendant)
                    End If

                        If Sgcoreanc = "V" Then
                        SolGrid1.Rows(nvligne).Cells("Prix").Value = Format(Dquantanc, Masque_Vendant)
                        SolGrid1.Rows(nvligne).Cells("coutant").Value = Format(Dquantanc, Masque_Vendant)
                    End If

                    SolGrid1.RefreshEdit()
                    um_old(nvligne) = AVBcs(AVBfiditemstub("PAR", AVB + fInprix, 0))
                    quant_old(nvligne) = quant
                    prod_old(nvligne) = AVBcs(AVBfiditemstub("CAT", AVB + fInprix, 0)).PadRight(30)
                    Updateinventaire(AVBcs(AVBfiditemstub("CAT", AVB + fInprix, 0)).PadRight(30), Tentrepot.Text.PadLeft(3), 1, 1, Val(SolGrid1.Rows(nvligne).Cells("quantite").EditedFormattedValue.ToString), SolGrid1.Rows(nvligne).Cells("um").EditedFormattedValue.ToString, False, " ", 0, "")
                    SolGrid1.Rows(nvligne).Cells("escompte").Selected = True
                End If
            End If
            ' gestion des kits
            If Gkit10 = oui10 And AVBcs(AVBfiditemstub("TYPE1", AVB + fInprix, 0)) = "K" Then
                SysOpen(fkit)
                Dim nvligne As Integer
                Dim quant As Double = Val(SolGrid1.CurrentRow.Cells("quantite").Value)
                Dim prodtemp As String = SolGrid1.CurrentRow.Cells("produit").Value.ToString
                prodtemp = prodtemp.PadRight(30)
                AVBSTAT = AVBPosn(AVB + fkit, prodtemp, 1, "", 0)
                AVBSTAT = AVBread(AVB + fkit, 0)
                Dim tt As String = AVBcs(AVBfiditemstub("PRODUIT", AVB + fkit, 0))
                Do While AVBSTAT = 0 And Trim(prodtemp) = Trim(AVBcs(AVBfiditemstub("PRODUIT", AVB + fkit, 0)))
                    adligne()
                    nvligne = SolGrid1.Rows.Count - 1
                    Dim prodcompo As String = AVBcs(AVBfiditemstub("COMPO", AVB + fkit, 0)).PadRight(30)
                    AVBSTAT = AVBPosn(AVB + fInprix, prodcompo, 1, "", &H100)
                    AVBSTAT = AVBread(AVB + fInprix, 1)
                    SolGrid1.Rows(nvligne).Cells("produit").Value = prodcompo
                    dscomma1.Rows(nvligne).Item("client") = Tclient.Text
                    completeproduit(nvligne)
                    Dim dd As Double = (Val(AVBcs(AVBfiditemstub("QUANT", AVB + fkit, 0))) + Val(AVBcs(AVBfiditemstub("DIFSURP", AVB + fkit, 0)))) * quant
                    SolGrid1.Rows(nvligne).Cells("quantite").Value = dd
                    um_old(nvligne) = AVBcs(AVBfiditemstub("PAR", AVB + fInprix, 0))
                    SolGrid1.Rows(nvligne).Cells("UM").Value = AVBcs(AVBfiditemstub("PAR", AVB + fInprix, 0))
                    quant_old(nvligne) = dd
                    prod_old(nvligne) = prodcompo
                    Dim impk As String = AVBcs(AVBfiditemstub("IMPK", AVB + fkit, 0)).Trim
                    dscomma1.Rows(nvligne).Item("impk") = impk
                    dscomma1.Rows(nvligne).Item("datelivre") = Ddaterequis.Text
                    If impk <> "N" Then
                        If AVBcs(AVBfiditemstub("TYPE1", AVB + fkit, 0)) = "F" Then
                            SolGrid1.Rows(nvligne).Cells("prix").Value = Format(Val(AVBcs(AVBfiditemstub("PRIX", AVB + fkit, 0))), Masque_Vendant)
                        Else
                            Prixspéciaux(SolGrid1.Rows(nvligne).Cells("UM").Value.ToString, Tclient.Text.PadRight(7), SolGrid1.Rows(nvligne).Cells("Produit").Value.ToString, 0, 0, False, False, dd, False, "")
                            SolGrid1.Rows(nvligne).Cells("Prix").Value = Format(DresultPrixPS, Masque_Vendant)
                            If Bokprixspeciaux = True Then
                                SolGrid1.Rows(nvligne).DefaultCellStyle.BackColor = Color.LightGreen
                                SolGrid1.Rows(nvligne).Cells("sp").Value = "S"
                            End If
                            SolGrid1.Rows(nvligne).Cells("Escompte").Value = DresultEscPs
                            'cherche clientliv ??????????
                            If Tclientliv.Text.Trim <> "" Then
                                Prixspéciaux(SolGrid1.Rows(nvligne).Cells("UM").Value.ToString, Tclientliv.Text.PadRight(7), SolGrid1.Rows(nvligne).Cells("Produit").Value.ToString, 0, 0, False, False, SolGrid1.Rows(nvligne).Cells("quantite").Value, True, "")
                                If DresultPrixPS <> 0 Then
                                    SolGrid1.Rows(nvligne).Cells("Prix").Value = Format(DresultPrixPS, Masque_Vendant)
                                    If Bokprixspeciaux = True Then
                                        SolGrid1.Rows(nvligne).DefaultCellStyle.BackColor = Color.LightGreen
                                        SolGrid1.Rows(nvligne).Cells("sp").Value = "S"
                                    End If
                                    SolGrid1.Rows(nvligne).Cells("Escompte").Value = DresultEscPs
                                End If
                            End If
                        End If
                    Else
                        SolGrid1.Rows(nvligne).Cells("Prix").Value = 0
                        SolGrid1.Rows(nvligne).Cells("Escompte").Value = 0
                    End If

                    SolGrid1.RefreshEdit()
                    quant_old(nvligne) = Val(SolGrid1.Rows(nvligne).Cells("quantite").EditedFormattedValue)
                    Calculegrid(SolGrid1.Rows(nvligne).Index, True, SolGrid1)
                    Updateinventaire(SolGrid1.Rows(nvligne).Cells("Produit").EditedFormattedValue.ToString, Tentrepot.Text.PadLeft(3), 1, 1, Val(SolGrid1.Rows(nvligne).Cells("quantite").EditedFormattedValue.ToString), SolGrid1.Rows(nvligne).Cells("um").EditedFormattedValue.ToString, False, " ", 0, "")
                    AVBSTAT = AVBPosn(AVB + fInven, Tentrepot.Text.Trim.PadRight(3) & AVBcs(AVBfiditemstub("CAT", AVB + fInprix, 0)).PadRight(30), 1, "", &H100)
                    AVBSTAT = AVBread(AVB + fInven, 1)
                    SolGrid1.Rows(nvligne).Cells("status").Value = "S"
                    If getstatuskit(nvligne) = True Then
                        'If lang = "F" Then MsgBox("La quantité disponible de ce produit est insuffisante.")
                        'If lang <> "F" Then MsgBox("The quantity on hand is insufficient")
                        'SendKeys.Send("{TAB}")
                        'SendKeys.Send("{TAB}")
                    End If
                    AVBSTAT = AVBread(AVB + fkit, 0)
                Loop
                'CalculegridTotal()
                SysClose(fkit)
                'pour forcer a aller sur derniiere ligne pour creernouvelleligne
                SolGrid1.Rows(SolGrid1.Rows.Count - 1).Cells("produit").Selected = True
            End If
            creernouvligne(True)
            creer = False
        End If
        CalculegridTotal()
        barcodeauto = False
        inserelig = False
        insererfiche = -1
    End Sub
    Private Sub adligne()
        Try
            creernouvligne(False)
            Dim nvligne As Integer
            nvligne = SolGrid1.Rows.Count - 1
            For compteur As Integer = 0 To dscomma1.Columns.Count - 1
                If dscomma1.Columns("id").ColumnName <> dscomma1.Columns(compteur).ColumnName _
            And dscomma1.Columns("ligne").ColumnName <> dscomma1.Columns(compteur).ColumnName Then dscomma1.Rows(nvligne).Item(compteur) = dscomma1.Rows(nvligne - 1).Item(compteur)
            Next
        Catch ex As Exception

        End Try
        SolGrid1.RefreshEdit()
    End Sub
    Private Sub SolGrid1_Validated1(ByVal sender As Object, ByVal e As System.EventArgs) Handles SolGrid1.Validated
        If SolGrid1.Rows.Count - 1 < 0 Then Exit Sub
        If efflignevide = True Or pgup = True Or pgdn = True Or uparr = True Or dnarr = True Then Exit Sub
        If Bafficheseulement = True Then Exit Sub
        'quand on clique en dehors du grid et quon as juste modifier le no produit
        Dim prodtemp As String = SolGrid1.CurrentRow.Cells("produit").EditedFormattedValue.ToString
        prodtemp = prodtemp.PadRight(30)
        Dim noligne As Integer = SolGrid1.CurrentRow.Index
        's'ils ont change de ligne en plein milieu
        If Trim(prodtemp) <> prod_old(noligne).Trim Then
            SolGrid1.CurrentRow.Cells("Produit").Value = prod_old(noligne)
            SolGrid1.RefreshEdit()
        End If
        'fin 
        CalculegridTotal()
    End Sub
    Private Sub SolGrid1_DoubleClick1(ByVal sender As Object, ByVal e As System.EventArgs) Handles SolGrid1.DoubleClick
        recherche()
    End Sub
    Private Sub SolGrid1_GotFocus1(ByVal sender As Object, ByVal e As System.EventArgs) Handles SolGrid1.GotFocus
        If promener = True Or gridfocus = True Then Exit Sub
        If Bafficheseulement = True Then Exit Sub
        If Tnocom.Text.Trim = "" Then
            Tnocom.Focus()
            Exit Sub
        End If
        If SolGrid1.RowCount = 0 Then
            creernouvligne(True)
            Dim dd As Integer = SolGrid1.Rows.Count
            SolGrid1.CurrentCell = SolGrid1.Rows(0).Cells("produit")
        End If
        BTeffacer.Enabled = False
        SolGrid1.BeginEdit(True)
        gridfocus = True
        Trouvelignefocus()
    End Sub
    Private Sub SolGrid1_LostFocus1(ByVal sender As Object, ByVal e As System.EventArgs) Handles SolGrid1.LostFocus
        'CalculegridTotal()
        'gridfocus = False
        BTeffacer.Enabled = True
    End Sub
    'Private Sub SolGrid1_CellMouseUp(sender As Object, e As DataGridViewCellMouseEventArgs) Handles SolGrid1.CellMouseUp
    '    If e.RowIndex < 0 Or e.ColumnIndex < 0 Then Exit Sub
    '    If dscomma1.Rows.Count <> 0 Then
    '        If SolGrid1.Rows(e.RowIndex).Cells("status").EditedFormattedValue.ToString = "F" Then
    '            Dim strsql As String = "Commande fournisseur:  " & dscomma1.Rows(e.RowIndex).Item("ref") & "    No. Fournisseur:" & dscomma1.Rows(e.RowIndex).Item("fournisseur")
    '            If lang <> "F" Then strsql = "Supplier order:   " & dscomma1.Rows(e.RowIndex).Item("ref") & "    No. Fournisseur:" & dscomma1.Rows(e.RowIndex).Item("fournisseur")
    '            strsql = strsql & vbCrLf

    '            ToolTip2.SetToolTip(SolGrid1, strsql)
    '            ToolTip2.Show(strsql, FrmTip, 200)
    '        Else
    '            ToolTip2.SetToolTip(SolGrid1, "")
    '        End If
    '    End If
    'End Sub
    Private cellColumnIndex As Integer = -1, cellRowIndex As Integer = -1
    Private Sub solgrid1_CellMouseMove(ByVal sender As Object, ByVal e As DataGridViewCellMouseEventArgs) Handles SolGrid1.CellMouseMove
        If e.ColumnIndex <> Me.cellColumnIndex OrElse e.RowIndex <> Me.cellRowIndex Then
            Me.ToolTip2.Hide(Me.SolGrid1)
            Me.cellColumnIndex = e.ColumnIndex
            Me.cellRowIndex = e.RowIndex

            If Me.cellColumnIndex >= 0 AndAlso Me.cellRowIndex >= 0 Then
                If SolGrid1.Rows(e.RowIndex).Cells("status").EditedFormattedValue.ToString = "F" Then
                    Dim strsql As String = vbCrLf
                    strsql = strsql & "Commande fournisseur:  " & dscomma1.Rows(e.RowIndex).Item("ref") & "    No. Fournisseur:" & dscomma1.Rows(e.RowIndex).Item("fournisseur")
                    If lang <> "F" Then strsql = strsql & "Supplier order:   " & dscomma1.Rows(e.RowIndex).Item("ref") & "    No. Fournisseur:" & dscomma1.Rows(e.RowIndex).Item("fournisseur")
                    strsql = strsql & vbCrLf
                    Me.ToolTip1.SetToolTip(SolGrid1, "")
                    Me.ToolTip2.SetToolTip(Me.SolGrid1, strsql)
                    'ToolTip2.SetToolTip(SolGrid1, strsql)
                    'ToolTip2.Show(strsql, FrmTip, 20000)
                Else
                    ToolTip2.SetToolTip(SolGrid1, "")
                End If

            End If
        End If
    End Sub
    'Private Sub solgrid1_CellMouseMove(ByVal sender As Object, ByVal e As System.Windows.Forms.DataGridViewCellMouseEventArgs) Handles SolGrid1.CellMouseMove
    '    If e.RowIndex < 0 Or e.ColumnIndex < 0 Then Exit Sub
    '    If dscomma1.Rows.Count <> 0 Then
    '        If SolGrid1.Rows(e.RowIndex).Cells("status").EditedFormattedValue.ToString = "F" Then
    '            Dim strsql As String = "Commande fournisseur:  " & dscomma1.Rows(e.RowIndex).Item("ref") & "    No. Fournisseur:" & dscomma1.Rows(e.RowIndex).Item("fournisseur")
    '            If lang <> "F" Then strsql = "Supplier order:   " & dscomma1.Rows(e.RowIndex).Item("ref") & "    No. Fournisseur:" & dscomma1.Rows(e.RowIndex).Item("fournisseur")
    '            strsql = strsql & vbCrLf
    '            'ToolTip1.InitialDelay = 500
    '            'ToolTip1.ReshowDelay = 100
    '            ToolTip2.AutoPopDelay = 5000
    '            ToolTip2.SetToolTip(SolGrid1, strsql)
    '            ToolTip2.Show(strsql, FrmTip, 20000)
    '        Else
    '            ToolTip2.SetToolTip(SolGrid1, "")
    '        End If
    '    End If
    'End Sub
#End Region
#Region "Procédure bon de commande"
    Private Sub showinfoprod(ByVal um As String, ByVal prod As String)
        If prod.Trim = Rem10.Trim Then Exit Sub
        Bafficheseulement = True
        If lang = "F" Then LblQuantite.Text = "Quantités ( " + Tentrepot.Text + " )"
        If lang <> "F" Then LblQuantite.Text = "Quantities ( " + Tentrepot.Text + " )"
        TabTotal.SelectTab(0)
        TabTotal.TabPages(0).BringToFront()
        TabTotal.TabPages(0).Show()
        Dim umx As Integer = TrouveUm(prod, um)
        Dim mult As Decimal = Val(AVBcs(AVBfiditemstub("MULT1", AVB + fInprix, umx)))
        TxtCat.Text = AVBcs(AVBfiditemstub("CAT", AVB + fInprix, 0))
        Dim encom As Decimal = Val(AVBcs(AVBfiditemstub("ENCOM", AVB + fInven, 0)))
        TxtEncom.Text = CStr(encom / mult)
        Dim qcom As Decimal = Val(AVBcs(AVBfiditemstub("QCOM", AVB + fInven, 0)))
        TxtQcom.Text = CStr(qcom / mult)
        Dim qmain As Decimal = Val(AVBcs(AVBfiditemstub("QMAIN", AVB + fInven, 0)))
        TxtQmain.Text = CStr(qmain / mult)
        TxtAttendu.Text = AVBcs(AVBfiditemstub("DTA", AVB + fInven, 0))
        TxtPar1.Text = AVBcs(AVBfiditemstub("PAR", AVB + fInprix, umx))
        TxtPrix1.Text = AVBcs(AVBfiditemstub("PRIX1", AVB + fInprix, umx))
        TxtPrix2.Text = AVBcs(AVBfiditemstub("PRIX2", AVB + fInprix, umx))
        TxtPrix3.Text = AVBcs(AVBfiditemstub("PRIX3", AVB + fInprix, umx))
        TxtPrix4.Text = AVBcs(AVBfiditemstub("PRIX4", AVB + fInprix, umx))
        TxtPrix5.Text = AVBcs(AVBfiditemstub("PRIX5", AVB + fInprix, umx))
        Dim qtdispo As Decimal = qmain - qcom
        TxtLocat.Text = AVBcs(AVBfiditemstub("LOCAT", AVB + fInven, 0))
        TxtDispo.Text = qtdispo.ToString
        SolGrid1.Focus()
        SolGrid1.Select()
        'Try
        '    If qtdispo > 0 Then PctSourire.ImageLocation = app + "logo\sourire.gif"
        '    If qtdispo = 0 Then PctSourire.ImageLocation = app + "logo\neutre.gif"
        '    If qtdispo < 0 Then PctSourire.ImageLocation = app + "logo\pleur.gif"
        'Catch
        'End Try
        'Try
        '    PctSourire.Load()
        'Catch
        '    'PicLogo.ImageLocation = app + "logo\compagnie.jpg"
        '    'PicLogo.Load()
        'End Try
        Bafficheseulement = False
    End Sub
    Private Sub claireinfoproduit()
        If lang = "F" Then LblQuantite.Text = "Quantités"
        If lang <> "F" Then LblQuantite.Text = "Quantities"
        TxtCat.Text = ""
        TabTotal.TabPages(0).Show()
        TxtLocat.Text = ""
        TxtEncom.Text = ""
        TxtQcom.Text = ""
        TxtQmain.Text = ""
        TxtAttendu.Text = ""
        TxtPar1.Text = ""
        TxtPrix1.Text = ""
        TxtPrix2.Text = ""
        TxtPrix3.Text = ""
        TxtPrix4.Text = ""
        TxtPrix5.Text = ""
        TxtDispo.Text = ""
    End Sub
    Private Sub claireinfoclient()
        TabTotal.SelectTab(1)
        TabTotal.TabPages(1).Show()
        TxtA1.Text = ""
        TxtA2.Text = ""
        TxtA3.Text = ""
        TxtA4.Text = ""
        TxtA5.Text = ""
    End Sub
    Private Sub posproduit(ByVal prod As String, ByVal um As String)
        If prod.Trim = "" Then
            claireinfoproduit()
            Exit Sub
        End If
        AVBSTAT = AVBPosn(AVB + fInprix, prod, 1, "", &H100)
        AVBSTAT = AVBread(AVB + fInprix, 1)
        AVBSTAT = AVBPosn(AVB + fInven, Tentrepot.Text.PadLeft(3) + prod, 1, "", &H100)
        AVBSTAT = AVBread(AVB + fInven, 1)
        '     showinfoprod(SolGrid1.CurrentRow.Cells("um").EditedFormattedValue.ToString, prod)
        showinfoprod(um, prod)
    End Sub
    Sub Trouvelignefocus()



        Bafficheseulement = True
            gridfocus = False
            Dim trouver As Boolean
        Try
            For Each Row As DataGridViewRow In SolGrid1.Rows
                If Trim$(Convert.ToString(Row.Cells("Produit").Value)) = "" Then
                    Row.Cells("Produit").AccessibilityObject.Select(AccessibleSelection.AddSelection)
                    Row.Cells("Produit").AccessibilityObject.Select(AccessibleSelection.TakeSelection)
                    Row.Cells("Produit").AccessibilityObject.Select(AccessibleSelection.TakeFocus)
                    trouver = True
                    SolGrid1.Focus()
                    Row.Cells("Produit").Selected = True
                    SolGrid1.BeginEdit(True)
                    Exit For
                End If
            Next
        Catch ex As Exception

        End Try
        If trouver = False Then
                focusderniere()
            End If

            gridfocus = True
        Bafficheseulement = False
    End Sub
    Private Sub focusderniere()
        Dim derniere As Integer
        derniere = SolGrid1.Rows.Count - 1
        If derniere <> -1 Then
            SolGrid1.Rows(derniere).Cells("Produit").AccessibilityObject.Select(AccessibleSelection.AddSelection)
            SolGrid1.Rows(derniere).Cells("Produit").AccessibilityObject.Select(AccessibleSelection.TakeSelection)
            SolGrid1.Rows(derniere).Cells("Produit").AccessibilityObject.Select(AccessibleSelection.TakeFocus)
            SolGrid1.Rows(derniere).Cells("Produit").Selected = True
            sollignefocus = SolGrid1.Rows(derniere).Index
            solcelfocus = SolGrid1.Rows(derniere).Cells("produit").ColumnIndex
            SolGrid1.Focus()
        End If
    End Sub
    Private Sub Ecrantraiteur()
        'Inscription des valeurs traiteur
        STraiteur(0) = ""
        STraiteur(1) = ""
        STraiteur(2) = ""
        STraiteur(3) = ""
        STraiteur(4) = ""
        STraiteur(5) = ""
        STraiteur(6) = ""
        STraiteur(7) = ""
        STraiteur(8) = ""
        STraiteur(9) = ""
        SysOpen(fvalcli)
        Sfichierlire = fcotete
        AVBSTAT = AVBPosn(AVB + fcotete, Tnocom.Text.Trim.PadLeft(10), 1, "", &H100)
        AVBSTAT = AVBread(AVB + fcotete, 1)
        If dscotete1.Rows(bsourceenteteCom.Position).Item("NBPERS").ToString = "" _
And dscotete1.Rows(bsourceenteteCom.Position).Item("HEURES").ToString = "" _
And dscotete1.Rows(bsourceenteteCom.Position).Item("HEUREL").ToString = "" _
And dscotete1.Rows(bsourceenteteCom.Position).Item("ATTENTION").ToString = "" _
And dscotete1.Rows(bsourceenteteCom.Position).Item("REFE").ToString = "" _
And dscotete1.Rows(bsourceenteteCom.Position).Item("EVENEM").ToString = "" _
And dscotete1.Rows(bsourceenteteCom.Position).Item("REM1").ToString = "" _
And dscotete1.Rows(bsourceenteteCom.Position).Item("REM2").ToString = "" _
And dscotete1.Rows(bsourceenteteCom.Position).Item("REM3").ToString = "" _
And dscotete1.Rows(bsourceenteteCom.Position).Item("REM4").ToString = "" Then
            AVBSTAT = AVBPosn(AVB + fvalcli, Me.Tclient.Text.PadRight(7), 1, "", &H100)
            AVBSTAT = AVBread(AVB + fvalcli, 1)
            SvalClient = Tclient.Text
            If AVBSTAT = 0 Then
                Sfichierlire = fvalcli
            Else
                Sfichierlire = fcotete
            End If
            Sfichiersauve = fcotete
        Else
            STraiteur(0) = dscotete1.Rows(bsourceenteteCom.Position).Item("NBPERS")
            STraiteur(1) = dscotete1.Rows(bsourceenteteCom.Position).Item("HEURES")
            STraiteur(2) = dscotete1.Rows(bsourceenteteCom.Position).Item("HEUREL")
            STraiteur(3) = dscotete1.Rows(bsourceenteteCom.Position).Item("ATTENTION")
            STraiteur(4) = dscotete1.Rows(bsourceenteteCom.Position).Item("REFE")
            STraiteur(5) = dscotete1.Rows(bsourceenteteCom.Position).Item("EVENEM")
            STraiteur(6) = dscotete1.Rows(bsourceenteteCom.Position).Item("REM1")
            STraiteur(7) = dscotete1.Rows(bsourceenteteCom.Position).Item("REM2")
            STraiteur(8) = dscotete1.Rows(bsourceenteteCom.Position).Item("REM3")
            STraiteur(9) = dscotete1.Rows(bsourceenteteCom.Position).Item("REM4")
            Sfichierlire = fcotete
            Sfichiersauve = fcotete
        End If
        tbb = Me.ActiveControl
        Dim frmPTraiteur As New FrmPieceTraiteur
        frmPTraiteur.ShowDialog()
        If Sfichiersauve = fcotete Then
            dscotete1.Rows(bsourceenteteCom.Position).Item("NBPERS") = STraiteur(0)
            dscotete1.Rows(bsourceenteteCom.Position).Item("HEURES") = STraiteur(1)
            dscotete1.Rows(bsourceenteteCom.Position).Item("HEUREL") = STraiteur(2)
            dscotete1.Rows(bsourceenteteCom.Position).Item("ATTENTION") = STraiteur(3)
            dscotete1.Rows(bsourceenteteCom.Position).Item("REFE") = STraiteur(4)
            dscotete1.Rows(bsourceenteteCom.Position).Item("EVENEM") = STraiteur(5)
            dscotete1.Rows(bsourceenteteCom.Position).Item("REM1") = STraiteur(6)
            dscotete1.Rows(bsourceenteteCom.Position).Item("REM2") = STraiteur(7)
            dscotete1.Rows(bsourceenteteCom.Position).Item("REM3") = STraiteur(8)
            dscotete1.Rows(bsourceenteteCom.Position).Item("REM4") = STraiteur(9)
        End If
        Me.tbb.Focus()
        frmPTraiteur.Dispose()
        SysClose(fvalcli)
    End Sub
    Sub Affichebondecommande()
        Dim ok As Boolean
        Tclient.Text = AVBcs(AVBfiditemstub("NOCLI", AVB + fcotete, 0))
        Tnocom.Text = AVBcs(AVBfiditemstub("NOCOM", AVB + fcotete, 0))
        PosnReadAPG(Tclient.Text, fClient, 1, 1, 1, 0, "Client")
        If AVBSTAT <> 0 Then
            MsgBox("Le client de cette commande n'existe pas", MsgBoxStyle.OkOnly)
            Exit Sub
        Else
            Afficheclient(ok)
        End If
        CreateDataSourceLigneCom(Tnocom.Text.Trim.PadLeft(10), dscomma1, DsPoids)
        SolGrid1.DataSource = dscomma1
        ReDim quant_old(dscomma1.Rows.Count - 1)
        ReDim prod_old(dscomma1.Rows.Count - 1)
        ReDim um_old(dscomma1.Rows.Count - 1)
        ReDim quant_org(dscomma1.Rows.Count - 1)
        ReDim quant_paqbte(dscomma1.Rows.Count - 1)
        For compteur As Integer = 0 To dscomma1.Rows.Count - 1
            quant_old(compteur) = Val(dscomma1.Rows(compteur).Item("quantite"))
            quant_org(compteur) = Val(dscomma1.Rows(compteur).Item("quantite"))
            prod_old(compteur) = dscomma1.Rows(compteur).Item("produit")
            um_old(compteur) = dscomma1.Rows(compteur).Item("um")
            DCompteur = dscomma1.Rows(compteur).Item("ligne")
            quant_paqbte(compteur) = Val(dscomma1.Rows(compteur).Item("paq_bte"))
        Next
        'Definitionsolgrid1()
        CalculegridTotal()
    End Sub
    Sub Ouvrebondecommande()
        If Bafficheseulement = True Then Exit Sub
        'Dim Slongueur As Integer
        'SNocommande = Tnocom.Text.PadLeft(10)
        'If Trim(SNocommande) <> "" Then PosnReadAPG(SNocommande, fcotete, 1, 1, 1, 1, "Entete de commande")
        If AVBSTAT <> 0 Or Tnocom.Text.Trim = "" Or BnouveauBT = True Then
            If Tclient.Text.Trim = "" Then
                MsgBox("Le numéro de client ne peut pas être laissé vide", MsgBoxStyle.OkOnly)
                Tclient.Focus()
                Exit Sub
            End If
            If Tnocom.Text.Trim <> "" And BnouveauBT = True Then
                'verif si existe dans travail
                AVBSTAT = AVBPosn(AVB + fcotete, Tnocom.Text.Trim.PadLeft(10), 1, "", 0)
                AVBSTAT = AVBread(AVB + fcotete, 0)
                If AVBcs(AVBfiditemstub("NOCOM", AVB + fcotete, 0)).Trim = Tnocom.Text.Trim Then
                    If lang = "F" Then MsgBox("Cette commande existe déjà!")
                    If lang <> "F" Then MsgBox("This order already exist!")
                    Tnocom.Focus()
                    Exit Sub
                End If
            End If
            If Tnocom.Text.Trim = "" Then Donnernocom(1, fcotete, Tnocom.Text)
            Tnocom.Text = Tnocom.Text.Trim.PadLeft(10)
            'ouvrenombre(ftype)
            'If Trim(Txtvendeur.Text) = "" Then
            '    AVBSTAT = AVBPosn(AVB + 99, "VE", 1, "", 0)
            '    avbstat1 = AVBread(AVB + 99, 0)
            '    If Trim(AVBcs(AVBfiditemstub("CODE", AVB + 99, 0))) = "VE" Then Txtvendeur.Text = Trim(AVBcs(AVBfiditemstub("TYPE", AVB + 99, 0)))
            'End If
            'If Trim(Tcommis.Text) = "" Then
            '    AVBSTAT = AVBPosn(AVB + 99, "CM", 1, "", 0)
            '    avbstat1 = AVBread(AVB + 99, 0)
            '    If Trim(AVBcs(AVBfiditemstub("CODE", AVB + 99, 0))) = "CM" Then Tcommis.Text = Trim(AVBcs(AVBfiditemstub("TYPE", AVB + 99, 0)))
            'End If
            'AVBSTAT = AVBclose(AVB + 99)
            BtImpSoum.Enabled = True
            DCompteur = 10000
            NewLigneCom(DCompteur, Tnocom.Text, dscomma1, DsPoids)
            ReDim Preserve quant_old(dscomma1.Rows.Count - 1)
            ReDim Preserve quant_paqbte(dscomma1.Rows.Count - 1)
            ReDim Preserve prod_old(dscomma1.Rows.Count - 1)
            prod_old(UBound(prod_old)) = ""
            ReDim Preserve um_old(dscomma1.Rows.Count - 1)
            um_old(UBound(um_old)) = ""
            SolGrid1.DataSource = dscomma1
            'Definitionsolgrid1()
            Tnocom.ReadOnly = True
            If ent10 > 1 Then
                Tentrepot.Focus()
            Else
                Tnoachat.Focus()
            End If
            SolGrid1.ClearSelection()
            SolGrid1.Enabled = False
        Else
            PosnReadAPG(Tnocom.Text.Trim.PadLeft(10), fcotete, 1, 1, 1, 1, "Entete de commande")
            renouventetecom(bsourceenteteCom, dscotete1)
            Affichebondecommande()
            AVBSTAT = AVBPosn(AVB + fClient, Tclient.Text, 1, "", &H100S)
            AVBSTAT = AVBread(AVB + fClient, 1)
            If AVBSTAT <> 0 Then
                If lang = "F" Then MsgBox("Le client de ce bon a été effacé")
                If lang <> "F" Then MsgBox("This work order client has been erased")
            End If
            lang4 = AVBcs(AVBfiditemstub("LANGUE", AVB + fClient, 0))
            gettel()
            Me.Refresh()
            'replacer l'escompte en %
            'If TxtEscompte.Text.Trim <> "" And Val(Ttotal.Text) <> 0 Then
            '    TxtEscompte.Text = Math.Round(Val(TxtEscompte.Text) / Val(Tstotal.Text), 3)
            '    CalculegridTotal()
            'End If

            SolGrid1.Focus()
        End If
        '   Definitionsolgrid1()
    End Sub
    Sub Afficheclient(ByVal pasok As Boolean)

    End Sub
    Private Sub affichecdata()
        Me.Tnom.Enabled = True
        Me.Tadresse1.Enabled = True
        Me.Tadresse2.Enabled = True
        Tcodepostal.Enabled = True
        Tprovince.Enabled = True
        Me.Tville.Enabled = True
        Me.Ttelephone.Enabled = True
        Me.Tfax.Enabled = True

        Me.Tnomliv.Enabled = True
        Me.Tadresse1liv.Enabled = True
        Me.Tadresse2liv.Enabled = True
        Me.Tvilleliv.Enabled = True
        Tcodepostalliv.Enabled = True
        Tprovinceliv.Enabled = True
        Me.Ttelephoneliv.Enabled = True
        Me.Tfaxliv.Enabled = True

        Me.Tnom.Text = AVBcs(AVBfiditemstub("NOM", AVB + fClient, 0)).Trim
        Me.Tadresse1.Text = AVBcs(AVBfiditemstub("ADR1", AVB + fClient, 0)).Trim
        Me.Tadresse2.Text = AVBcs(AVBfiditemstub("ADR2", AVB + fClient, 0)).Trim
        Me.Tville.Text = AVBcs(AVBfiditemstub("VILLE", AVB + fClient, 0)).Trim
        Me.Tcodepostal.Text = AVBcs(AVBfiditemstub("CP1", AVB + fClient, 0))
        Tprovince.Text = AVBcs(AVBfiditemstub("PROV", AVB + fClient, 0))
        TxtTermes.Text = AVBcs(AVBfiditemstub("TERMES", AVB + fClient, 0))
        TxtExpediteur.Text = AVBcs(AVBfiditemstub("EXPEDIE", AVB + fClient, 0))
        Txtvendeur.Text = AVBcs(AVBfiditemstub("VENDEUR", AVB + fClient, 0))
        Tcommis.Text = AVBcs(AVBfiditemstub("COMIS", AVB + fClient, 0))
        affichemag()
        gettel()
        lang4 = AVBcs(AVBfiditemstub("LANGUE", AVB + fClient, 0))
        If Trim(Tclientliv.Text) = "" Then
            Me.Tnomliv.Text = AVBcs(AVBfiditemstub("NOM", AVB + fClient, 0)).Trim
            Me.Tadresse1liv.Text = AVBcs(AVBfiditemstub("ADR1", AVB + fClient, 0)).Trim
            Me.Tadresse2liv.Text = AVBcs(AVBfiditemstub("ADR2", AVB + fClient, 0)).Trim
            Me.Tvilleliv.Text = Tville.Text.Trim
            Tprovinceliv.Text = Tprovince.Text
            Tcodepostalliv.Text = Tcodepostal.Text
            Me.Ttelephoneliv.Text = Ttelephone.Text
            Me.Tfaxliv.Text = Tfax.Text

            If AVBcs(AVBfiditemstub("LIVRE", AVB + fClient, 0)) = "O" Then
                SysOpen(flivrea)
                AVBSTAT = AVBPosn(AVB + flivrea, Tclient.Text.Trim.PadRight(7), 1, "", 0)
                AVBSTAT = AVBread(AVB + flivrea, 1)
                If AVBcs(AVBfiditemstub("CLIENT", AVB + flivrea, 0)).Trim = Tclient.Text.Trim And AVBSTAT = 0 Then


                    Tclientliv.Text = AVBcs(AVBfiditemstub("LIVREA", AVB + flivrea, 0))

                    Me.Tnomliv.Text = AVBcs(AVBfiditemstub("NOM", AVB + flivrea, 0))
                    Me.Tadresse1liv.Text = AVBcs(AVBfiditemstub("ADR1", AVB + flivrea, 0))
                    Me.Tadresse2liv.Text = AVBcs(AVBfiditemstub("ADR2", AVB + flivrea, 0))
                    Me.Tvilleliv.Text = AVBcs(AVBfiditemstub("VILLE", AVB + flivrea, 0))
                    Me.Tprovinceliv.Text = AVBcs(AVBfiditemstub("PROV", AVB + flivrea, 0))
                    Me.Tcodepostalliv.Text = AVBcs(AVBfiditemstub("CP1", AVB + flivrea, 0))
                    Me.Ttelephoneliv.Text = AVBcs(AVBfiditemstub("TPHONE", AVB + flivrea, 0))
                    Me.Tfaxliv.Text = Tfax.Text
                End If
                SysClose(flivrea)
                'If Trim(Tprovinceliv.Text) = "" Then Tprovinceliv.Text = "QUE"
            End If
        End If
        TabTotal.SelectTab(1)
        TabTotal.TabPages(1).BringToFront()
        TabTotal.TabPages(1).Show()
        TxtA1.Text = AVBcs(AVBfiditemstub("A1", AVB + fClient, 0))
        TxtA2.Text = AVBcs(AVBfiditemstub("A2", AVB + fClient, 0))
        TxtA3.Text = AVBcs(AVBfiditemstub("A3", AVB + fClient, 0))
        TxtA4.Text = AVBcs(AVBfiditemstub("A4", AVB + fClient, 0))
        TxtA5.Text = AVBcs(AVBfiditemstub("A5", AVB + fClient, 0))
    End Sub
    Private Sub affichemag()
        If AVBcs(AVBfiditemstub("HOURS_C", AVB + fClient, 0)).Trim <> "1" _
And AVBcs(AVBfiditemstub("HOURS_C", AVB + fClient, 0)).Trim <> "0" _
And AVBcs(AVBfiditemstub("HOURS_C", AVB + fClient, 0)).Trim <> "" Then
            LblMag.Visible = True
            Dim str As String = "Magasin " + vbCrLf
            If lang <> "F" Then str = "Store " + vbCrLf
            LblMag.Text = str + AVBcs(AVBfiditemstub("HOURS_C", AVB + fClient, 0)).Trim
        Else
            LblMag.Visible = False
        End If

    End Sub
    Private Sub gettel()
        Me.Ttelephone.Text = AVBcs(AVBfiditemstub("TPHONE", AVB + fClient, 0))
        Me.Tfax.Text = AVBcs(AVBfiditemstub("FAX", AVB + fClient, 0))
    End Sub
    Private Sub redimquant()
        ReDim quant_old(0)
        ReDim quant_paqbte(0)
        ReDim prod_old(0)
        prod_old(0) = ""
        ReDim um_old(0)
        um_old(0) = ""
    End Sub
    Private Sub Imprime()
        If Imprimeouinon = False Then

            If impcom.Trim <> "" Then Tnocom.Text = impcom
            ImpSorte = "Bon de commande piece"
            ImpRapport = "repcom.rpt"
            reponse = "*"
            FormImp(Tnocom.Text.Trim.PadLeft(10))
            'Imprimeouinon = False
            impcom = ""
        Else
            impcom = ""
            Imprimeouinon = False
        End If
    End Sub
    Private Sub BindEnteteBT()
        Try
            bsourceenteteCom.Clear()
        Catch ex As Exception

        End Try
        CreateDataSourceEntetecomBinding("          ", dscotete1)
        bsourceenteteCom.DataSource = dscotete1
        BindingNavigator1.BindingSource = bsourceenteteCom
        Me.Tclient.DataBindings.Clear()
        Me.Tnocom.DataBindings.Clear()
        Me.Tadresse1.DataBindings.Clear()
        Me.Tnom.DataBindings.Clear()
        Me.Tadresse2.DataBindings.Clear()
        Me.Tville.DataBindings.Clear()
        Me.Tprovince.DataBindings.Clear()
        Me.Tnoachat.DataBindings.Clear()
        Me.Tentrepot.DataBindings.Clear()
        'Me.Ddateouverture.DataBindings.clear
        'Me.Ddaterequis.DataBindings.clear
        Me.Txtvendeur.DataBindings.Clear()
        Me.Tcommis.DataBindings.Clear()
        Me.Tcodepostal.DataBindings.Clear()
        Me.Tadresse1liv.DataBindings.Clear()
        Me.Tnomliv.DataBindings.Clear()
        Me.Tclientliv.DataBindings.Clear()
        Me.Tvilleliv.DataBindings.Clear()
        Me.Tprovinceliv.DataBindings.Clear()
        Me.Tadresse2liv.DataBindings.Clear()
        Me.Tcodepostalliv.DataBindings.Clear()
        Me.TxtTermes.DataBindings.Clear()
        Me.TxtEscompte.DataBindings.Clear()
        Txtcollect.DataBindings.Clear()
        TxtDivers.DataBindings.Clear()
        Txtstatus.DataBindings.Clear()
        TxtExpediteur.DataBindings.Clear()
        Me.Ttelephone.DataBindings.Clear()
        Me.Tfax.DataBindings.Clear()
        Me.Ttelephoneliv.DataBindings.Clear()
        Me.Tfaxliv.DataBindings.Clear()
        'Me..DataBindings.clear
        'Me..DataBindings.clear
        'Me..DataBindings.clear
        Me.Tdepot.DataBindings.Clear()
        Me.Tstotal.DataBindings.Clear()
        Me.Ttotal.DataBindings.Clear()
        Me.Ttps.DataBindings.Clear()
        Me.Ttvq.DataBindings.Clear()
        Me.Lblroute.DataBindings.Clear()
        Tgtotal.DataBindings.Clear()
        Ttransport.DataBindings.Clear()
        Lblroute.DataBindings.Add(New Binding("Text", bsourceenteteCom, "Route"))
        Tclient.DataBindings.Add(New Binding("Text", bsourceenteteCom, "Client"))
        Tnocom.DataBindings.Add(New Binding("Text", bsourceenteteCom, "NoCommande"))
        Tadresse1.DataBindings.Add(New Binding("Text", bsourceenteteCom, "Adresse"))
        Tnom.DataBindings.Add(New Binding("Text", bsourceenteteCom, "Nom"))
        Tadresse2.DataBindings.Add(New Binding("Text", bsourceenteteCom, "Adresse2"))
        Tville.DataBindings.Add(New Binding("Text", bsourceenteteCom, "Ville"))
        Tprovince.DataBindings.Add(New Binding("Text", bsourceenteteCom, "Province"))
        Tnoachat.DataBindings.Add(New Binding("Text", bsourceenteteCom, "Noachat"))
        Tentrepot.DataBindings.Add(New Binding("Text", bsourceenteteCom, "Entrepot"))
        'Me.Ddateouverture.DataBindings.Add(New Binding("Text", BsourceenteteCom, "Date Commandée"))
        'Me.Ddaterequis.DataBindings.Add(New Binding("Text", BsourceenteteCom, "Date Livrée"))
        Txtvendeur.DataBindings.Add(New Binding("Text", bsourceenteteCom, "Vendeur"))
        Tcommis.DataBindings.Add(New Binding("Text", bsourceenteteCom, "Commis"))
        Txtcollect.DataBindings.Add(New Binding("Text", bsourceenteteCom, "Collect"))
        Tcodepostal.DataBindings.Add(New Binding("Text", bsourceenteteCom, "CodePostal"))
        Tadresse1liv.DataBindings.Add(New Binding("Text", bsourceenteteCom, "AdresseLiv"))
        Tnomliv.DataBindings.Add(New Binding("Text", bsourceenteteCom, "NomLiv"))
        Tclientliv.DataBindings.Add(New Binding("Text", bsourceenteteCom, "ClientLiv"))
        Tvilleliv.DataBindings.Add(New Binding("Text", bsourceenteteCom, "VilleLiv"))
        Tprovinceliv.DataBindings.Add(New Binding("Text", bsourceenteteCom, "ProvinceLiv"))
        Tadresse2liv.DataBindings.Add(New Binding("Text", bsourceenteteCom, "Adresse2Liv"))
        Tcodepostalliv.DataBindings.Add(New Binding("Text", bsourceenteteCom, "CodePostalLiv"))
        TxtTermes.DataBindings.Add(New Binding("Text", bsourceenteteCom, "Termes"))
        TxtEscompte.DataBindings.Add(New Binding("Text", bsourceenteteCom, "Escompte"))
        TxtDivers.DataBindings.Add(New Binding("Text", bsourceenteteCom, "divers"))
        Txtstatus.DataBindings.Add(New Binding("Text", bsourceenteteCom, "status"))
        TxtExpediteur.DataBindings.Add(New Binding("Text", bsourceenteteCom, "expediteur"))
        Ttelephone.DataBindings.Add(New Binding("Text", bsourceenteteCom, "Telephone"))
        Tfax.DataBindings.Add(New Binding("Text", bsourceenteteCom, "fax"))
        Me.Ttelephoneliv.DataBindings.Add(New Binding("Text", bsourceenteteCom, "TelephoneLiv"))
        Me.Tfaxliv.DataBindings.Add(New Binding("Text", bsourceenteteCom, "faxliv"))
        Tdepot.DataBindings.Add(New Binding("Text", bsourceenteteCom, "Depot"))
        Tstotal.DataBindings.Add(New Binding("Text", bsourceenteteCom, "Total"))
        Ttps.DataBindings.Add(New Binding("Text", bsourceenteteCom, "Taxefederal"))
        Ttvq.DataBindings.Add(New Binding("Text", bsourceenteteCom, "Taxeprovincial"))
        Tgtotal.DataBindings.Add(New Binding("Text", bsourceenteteCom, "GrandTotal"))
        Ttransport.DataBindings.Add(New Binding("Text", bsourceenteteCom, "Transport"))
        Ttotal.Text = Val(Tstotal.Text) + Val(Ttps.Text) + Val(Ttvq.Text)
        lblnbimp.Text = "Nb d'impression :" & Val(AVBcs(AVBfiditemstub("IMP", AVB + fcotete, 0)))
    End Sub
    Sub affichebTbinding()
        Bafficheseulement = True
        Me.Refresh()
        Lblroutedef.Text = ""
        Me.btnroute.Visible = False
        AVBSTAT = AVBPosn(AVB + fClient, Tclient.Text.PadRight(7), 1, "", &H100)
        AVBSTAT = AVBread(AVB + fClient, 1)
        CreateDataSourceFicheClient()
        afficheinfoclient()
        affichemag()
        afficherestebon()
        ' affichecdata()
        If Lblroute.Text.Trim <> "" Then
            Lblroutedef.Text = "Route : "
            Me.btnroute.Visible = True
        End If
        CreateDataSourceLigneCom(Tnocom.Text.Trim.PadLeft(10), dscomma1, DsPoids)
        SolGrid1.DataSource = dscomma1
        If dscomma1.Rows.Count <> SolGrid1.Rows.Count Then
            MsgBox("ligne pas pareil")
        End If
        If dscomma1.Rows.Count > 0 Then DCompteur = Val(dscomma1.Rows(dscomma1.Rows.Count - 1).Item("Ligne"))
        ReDim quant_old(dscomma1.Rows.Count - 1)
        ReDim prod_old(dscomma1.Rows.Count - 1)
        ReDim um_old(dscomma1.Rows.Count - 1)
        ReDim quant_paqbte(dscomma1.Rows.Count - 1)
        For compteur As Integer = 0 To dscomma1.Rows.Count - 1
            quant_old(compteur) = Val(dscomma1.Rows(compteur).Item("quantite"))
            prod_old(compteur) = dscomma1.Rows(compteur).Item("produit")
            um_old(compteur) = dscomma1.Rows(compteur).Item("um")
            quant_paqbte(compteur) = Val(dscomma1.Rows(compteur).Item("paq_bte"))
        Next
        'ajout modif mb
        CalculegridTotal()

        'SolGrid1.Rows.Clear()
        '  Definitionsolgrid1()
        Bafficheseulement = False
    End Sub
    Private Sub afficheinfoclient()
        AVBSTAT = AVBPosn(AVB + fClient, Tclient.Text.PadRight(7), 1, "", &H100)
        AVBSTAT = AVBread(AVB + fClient, 1)

    End Sub
    Private Sub creernouvligne(ByVal sfocus As Boolean)
        If SolGrid1.Rows.Count = 0 Then
            creerligne()
        ElseIf SolGrid1.Rows(SolGrid1.Rows.Count - 1).Cells("produit").EditedFormattedValue.ToString.Trim <> "" Then
            creerligne()
        End If
        If sfocus = True Then Trouvelignefocus()
    End Sub
    Private Sub creerligne()
        Bafficheseulement = True
        If DCompteur <> Val(dscomma1.Rows(dscomma1.Rows.Count - 1).Item("Ligne")) Then
            If lang = "F" Then MsgBox("Les numéros ne balancent pas ( " + DCompteur.ToString + " ) ( " + dscomma1.Rows(dscomma1.Rows.Count - 1).Item("Ligne").ToString + " )")
            If lang <> "F" Then MsgBox("The lines do not balance ( " + DCompteur.ToString + " ) ( " + dscomma1.Rows(dscomma1.Rows.Count - 1).Item("Ligne").ToString + " )")
        End If
        DCompteur = DCompteur + 10
        NewLigneCom(DCompteur, Tnocom.Text, dscomma1, DsPoids)

        ReDim Preserve quant_paqbte(UBound(quant_paqbte) + 1)
        ReDim Preserve quant_old(UBound(quant_old) + 1)
        ReDim Preserve prod_old(UBound(prod_old) + 1)
        prod_old(UBound(prod_old)) = ""
        ReDim Preserve um_old(UBound(um_old) + 1)
        um_old(UBound(um_old)) = ""
        Bafficheseulement = False
    End Sub
    Private Sub afficherestebon()
        If dscotete1.Rows.Count <= 0 Then Exit Sub
        If DateTime.TryParse(dscotete1.Rows(bsourceenteteCom.Position).Item("DateCommande").ToString, Ddateouverture.Text) = True Then
            Ddateouverture.Text = dscotete1.Rows(bsourceenteteCom.Position).Item("DateCommande").ToString
        End If
        If DateTime.TryParse(dscotete1.Rows(bsourceenteteCom.Position).Item("Datelivraison").ToString, Ddaterequis.Text) = True Then
            Ddaterequis.Text = dscotete1.Rows(bsourceenteteCom.Position).Item("Datelivraison").ToString
        End If
    End Sub
#End Region
    Private Sub creerproduit()
        If SolGrid1.ContainsFocus = False Then Exit Sub
        If SolGrid1.CurrentCell.ColumnIndex <> SolGrid1.Columns("produit").Index Then Exit Sub
        Dim crprod As New FrmCreationProduit
        crprod.TxtEntrepot.Text = Tentrepot.Text
        crprod.ShowDialog()
        If crprod.TxtProduit.Text.Trim <> "" Then
            If SolGrid1.ContainsFocus = True Then
                SolGrid1.CurrentRow.Cells("produit").Value = crprod.TxtProduit.Text
                SolGrid1.RefreshEdit()
            End If
        End If
        crprod.Dispose()
    End Sub
#Region "ALT F1"

    Private Sub acces_add()
        If promener = True Then Exit Sub
        'au lieu de cliquer sur le bouton on fait ALT F1 pour créer ou voir
        tbb = Me.ActiveControl

        'Écran principal
        If tbb Is Tclient Then
            'Btn Client
            shclient()
        ElseIf tbb Is Tclientliv Then
            shclient()
            'ElseIf tbb Is TxtModele Then
            '    'Btn Modèle
            '    AVBType = "MO"
            '    entree_type()
            'ElseIf tbb Is TxtGroupe Then
            '    'Btn Groupe
            '    AVBType = "UT"
            '    Dim ntype As New FrmInstypeco
            '    ntype.ShowDialog()
            '    ntype.Dispose()
            'ElseIf tbb Is TxtStatut Then
            '    'Btn Statut
            '    AVBType = "CS"
            '    entree_type()
            'ElseIf tbb Is TxtCategorie Then
            '    'Btn Categorie
            '    AVBType = "CU"
            '    entree_type()
            'ElseIf tbb Is txtType Then
            '    'Btn Localisation
            '    AVBType = "TU"
            '    entree_type()
        ElseIf tbb Is TxtTermes Then
            Dim Nclic As New FrmTermes
            Nclic.ShowDialog()
            Nclic.Dispose()
        ElseIf tbb Is TxtExpediteur Then
            AVBType = "EX"
            entree_type()
        ElseIf tbb Is Tcommis Then
            'Échéance de la vignette
            AVBType = "CM"
            entree_type()
        ElseIf tbb Is Txtvendeur Then
            'Vendeur
            AVBType = "VE"
            entree_type()
        End If
    End Sub
    Private Sub entree_type()
        Dim ntype As New Frminstype
        ntype.ShowDialog()
    End Sub
#End Region
#Region "Annuller F2  "
    Sub ProcedureAnnule()
        If Bcommenceligne = True Then
            MsgBox("Vous devez terminer la ligne en cours")
            Exit Sub
        End If
        If promener = True Then Exit Sub
        If Val(Tdepot.Text) <> 0 Then
            If lang = "F" Then MsgBox("Vous ne pouvez annuler une commande ayant un dépot")
            If lang <> "F" Then MsgBox("You can not cancel an order with there is a deposit on it")
            Exit Sub
        End If
        Bencommandeclient = False
        Benmodification = False
        trclicom = False

        gridfocus = False
        SetEcran(Me)
        SNocommande = Tnocom.Text.PadLeft(10)
        If BnouveauBT = True Then
            effnocom(Tnocom.Text, fcotete)
        End If
        Bafficheseulement = True
        claireinfoproduit()
        claireinfoclient()
        For compteur As Integer = 0 To dscomma1.Rows.Count - 1
            Dim dd As DataRow = dscomma1.Rows(compteur)
            If dd.Item("Produit").ToString.Trim <> "" Then
                Dim ff As Double = Val(SolGrid1.Rows(compteur).Cells("quantite").EditedFormattedValue)
                If Val(DsPoids.Rows(compteur).Item("paq_bte")) <> 0 Then ff = Val(DsPoids.Rows(compteur).Item("paq_bte"))
                If quant_org Is Nothing And BnouveauBT = False Then
                    'rien a faire aucune valeur originale
                Else
                    Updateinventaire(dd.Item("Produit").ToString.PadRight(30), Tentrepot.Text.PadLeft(3), -1, 1, ff, dd.Item("um").ToString, False, " ", 0, dd.Item("lot").ToString)
                    If quant_org Is Nothing Then
                    Else
                        If compteur <= UBound(quant_org) And BnouveauBT = False Then Updateinventaire(dd.Item("Produit").ToString.PadRight(30), Tentrepot.Text.PadLeft(3), 1, 1, quant_org(compteur), dd.Item("um").ToString, False, " ", 0, dd.Item("lot").ToString)
                    End If
                End If
            End If
        Next
        If BnouveauBT = True Then
            effnocom(Tnocom.Text, fcotete)
            dscotete1.Rows(bsourceenteteCom.Position).Delete()
        Else
            CalculegridTotal()
            dscotete1.Rows(bsourceenteteCom.Position).EndEdit()
        End If
        BindEnteteBT()
        ' bsourceenteteCom.MoveLast()
        ' Me.Refresh()
        ReDim quant_org(0)
        ReDim quant_paqbte(0)
        SolGrid1.DataSource = ""
        dscomma1.Clear()
        DsPoids.Clear()
        Dim strmes As String = "Ligne de commande"
        If lang <> "F" Then strmes = "Order lines"
        DisableEcran()
        BnouveauBT = False
        affichebTbinding()
        ico_promener(True)
        Ttelephoneliv.Text = ""
        Tfaxliv.Text = ""
        btnconnaissement.Enabled = True
        BtImpSoum.Enabled = False
        AVBSTAT = AVBrunlock(AVB + fcotete)
        AVBSTAT = AVBrunlock(AVB + fcomma)
        AVBSTAT = AVBrunlock(AVB + fClient)
        SolGrid1.ClearSelection()
        LblMag.Visible = False
        promener = True
        frmcommod = False
        Tnocomrech.Focus()
    End Sub
#End Region
#Region "SF3 profit"
    Private Sub profit()
        If Bprofit.Visible = False Then Exit Sub
        afficheprofit(Pgrid, SolGrid1)
        'garder et replacer le focus dans la grille principale
        If Pgrid.Visible = False Then
            If promener = False And solrow <> -1 Then
                SolGrid1.Rows(solrow).Cells(solcol).AccessibilityObject.Select(AccessibleSelection.AddSelection)
                SolGrid1.Rows(solrow).Cells(solcol).AccessibilityObject.Select(AccessibleSelection.TakeSelection)
                SolGrid1.Rows(solrow).Cells(solcol).AccessibilityObject.Select(AccessibleSelection.TakeFocus)
                SolGrid1.Focus()
                SolGrid1.Rows(solrow).Cells(solcol).Selected = True
                SolGrid1.BeginEdit(True)
                solrow = -1
                solcol = -1
            End If
        Else
            If SolGrid1.ContainsFocus = True Then
                solrow = SolGrid1.CurrentRow.Index
                solcol = SolGrid1.CurrentCell.ColumnIndex
            End If
        End If
    End Sub
#End Region
#Region "Nouveau F4"
    Sub ProcedureNouveau()
        If promener = False And SolGrid1.ContainsFocus = False And btajoutcli = False Then
            If lang = "F" Then MsgBox("Vous êtes déjà en mode modification")
            If lang <> "F" Then MsgBox("You already are in edit mode")
            Exit Sub
        End If
        If troptit = False Then
            If peunouveau = False Then
                messagedroit()
                Exit Sub
            End If
        End If
        If Benmodification = True Then
            If lang = "F" Then MsgBox("Vous ne pouvez être en mode modification dans Bon de travail, commande fournisseur ou Réception fournisseur")
            If lang <> "F" Then MsgBox("You already are in edit mode")
            Exit Sub
        End If
        Tnocomrech.Text = ""
        If SolGrid1.ContainsFocus = False And btajoutcli = False Then
            If AVBisopen(AVB + fcomma) = 0 Then SysOpen(fcomma)
            If AVBisopen(AVB + fcotete) = 0 Then SysOpen(fcotete)
            If AVBisopen(AVB + fClient) = 0 Then SysOpen(fClient)
            Bencommandeclient = True
            Benmodification = True
            redimquant()
            Bafficheseulement = True
            EnableEcran()
            NewEntetecom("          ", dscotete1)
            BnouveauBT = True
            bsourceenteteCom.MoveLast()
            Me.Refresh()
            ico_promener(False)
            BTnouveau.Enabled = False
            BTmodifier.Enabled = False
            btnconnaissement.Enabled = False
            AVBSTAT = AVBrclear(AVB + fcotete)
            dscomma1.Clear()
            SolGrid1.DataSource = " "
            miseazero()
            entrepotold = ""
            DCompteur = 10000
            Ddateouverture.Value = Today
            Ddaterequis.Value = DateAdd(DateInterval.Day, My.Settings.MonInterval, Today).ToString
            Tnocom.ReadOnly = False
            DsPoids.Clear()
            promener = False
            If My.Settings.Monentrepot.Trim <> "" Then Tentrepot.Text = My.Settings.Monentrepot
            Tclient.Focus()
            SolGrid1.ClearSelection()
            Bafficheseulement = False
            LblMag.Visible = False
            frmcommod = True
            trclicom = False
            SolGrid1.Enabled = False
            ToolStrip1.Enabled = False
        Else
            '' If SolGrid1.Rows.Count - 1 < 0 Then Exit Sub
            'CalculegridTotal()
            'creernouvligne(True)
            'btajoutcli = False
        End If
    End Sub
#End Region
#Region "Sauve F5"
    Sub ProcedureSauve()
        If Tclient.Text.Trim = "" Then
            If lang = "F" Then MsgBox("Le N° de client ne peut être vide")
            If lang <> "F" Then MsgBox("The client N° can not be empty")
            Tclient.Focus()
            Exit Sub
        End If
        If Tclient.Text.Trim = "!" Then
            If lang = "F" Then MsgBox("Le N° de client ne peut être le client par défaut")
            If lang <> "F" Then MsgBox("The client N° can not be the default client")
            Tclient.Focus()
            Exit Sub
        End If
        If Txtvendeur.Text.Trim = "" Then
            If lang = "F" Then MsgBox("Le N° de vendeur ne peut être vide")
            If lang <> "F" Then MsgBox("The Salesman N° can not be empty")
            Txtvendeur.Focus()
            Exit Sub
        End If
        If SolGrid1.ContainsFocus = True Then
            If SolGrid1.CurrentCell.ColumnIndex = SolGrid1.Columns.Item("produit").Index _
            And SolGrid1.CurrentRow.Index = dscomma1.Rows.Count - 1 _
            And prod_old(SolGrid1.CurrentRow.Index).Trim = "" Then
                SolGrid1.CurrentRow.Cells("produit").Value = ""
                SolGrid1.RefreshEdit()
            End If
            If (Trim(SolGrid1.CurrentRow.Cells("produit").FormattedValue.ToString) <> _
             Trim(dscomma1.Rows(SolGrid1.CurrentRow.Index).Item("produit").ToString)) _
             Or Trim(SolGrid1.CurrentRow.Cells("produit").FormattedValue.ToString) <> "" _
             Or Trim(dscomma1.Rows(SolGrid1.CurrentRow.Index).Item("produit").ToString) <> "" Then
                If lang = "F" Then MsgBox("Complétez la ligne avant de sauver")
                If lang <> "F" Then MsgBox("You must be on an empty line to save")
                Exit Sub
            End If
            If SolGrid1.Rows(0).Cells("produit").EditedFormattedValue.ToString.Trim = "" Then
                If lang = "F" Then MsgBox("Vous ne pouvez pas sauver une commande sans ligne")
                If lang <> "F" Then MsgBox("You can not save an order without any lines")
                Exit Sub
            End If
        End If
        If dscomma1.Rows.Count = 0 Then
            If lang = "F" Then MsgBox("Vous ne pouvez pas sauver une commande sans ligne")
            If lang <> "F" Then MsgBox("You can not save an order without any lines")
            Exit Sub
        ElseIf dscomma1.Rows(0).Item("produit").ToString.Trim = "" Then
            If lang = "F" Then MsgBox("Vous ne pouvez pas sauver une commande sans ligne")
            If lang <> "F" Then MsgBox("You can not save an order without any lines")
            Exit Sub
        End If
        sauvage = True
        'Bafficheseulement = True
        TxtEscompte.Focus()
    End Sub
    Private Sub sauver()



        Tdepot.Text = recalculedepot(fdepotcf, Tnocom.Text, fcotete)
        Bencommandeclient = False
        Benmodification = False
        gridfocus = False
        CalculegridTotal()
        SNocommande = Tnocom.Text.PadLeft(10)
        dscotete1.Rows(bsourceenteteCom.Position).Item("DateCommande") = Ddateouverture.Text
        dscotete1.Rows(bsourceenteteCom.Position).Item("Datelivraison") = Ddaterequis.Text
        dscotete1.Rows(bsourceenteteCom.Position).Item("Entrepot") = Tentrepot.Text
        dscotete1.Rows(bsourceenteteCom.Position).Item("Route") = Lblroute.Text
        If dscotete1.Rows(bsourceenteteCom.Position).Item("ClientLiv").ToString.Trim = "" Then dscotete1.Rows(bsourceenteteCom.Position).Item("ClientLiv") = Tclient.Text

        dscotete1.Rows(bsourceenteteCom.Position).Item("territoire") = AVBcs(AVBfiditemstub("TER", AVB + fClient, 0))
        'Ecrantraiteur()
        'If BnouveauBT = False Then
        ' dscotete1.Rows(bsourceenteteCom.Position).EndEdit()
        '    dscotete1.Rows(bsourceenteteCom.Position).AcceptChanges()
        'End If

        '.EndEdit()
        If SolGrid1.Rows.Count > 0 Then dscotete1.Rows(bsourceenteteCom.Position).Item("Finligne") = SolGrid1.Rows(SolGrid1.Rows.Count - 1).Cells("ligne").EditedFormattedValue.ToString
        SaveEntetecom(bsourceenteteCom.Position, Tnocom.Text, bsourceenteteCom, dscotete1)
        For Each lig As DataRow In dscomma1.Rows
            lig.Item("Datelivre") = Ddaterequis.Text
            lig.Item("Datecommande") = Ddateouverture.Text
            lig.Item("territoire") = AVBcs(AVBfiditemstub("TER", AVB + fClient, 0))
        Next
        SaveLigneCom(Tnocom.Text, dscomma1, Tclient.Text)

        If My.Settings.triercmdum = "O" Then Trier_codeum(2)
        If My.Settings.Triercmdlocum = "O" Then Trier_codelocum(2)
        efflignevide = True
        'efface la ligne vide
        effacelaligne(SolGrid1, dscomma1)
        efflignevide = False
        DisableEcran()
        ico_promener(True)
        BnouveauBT = False
        promener = True
        Lblroute.Text = ""
        Lblroutedef.Text = ""
        Me.btnroute.Visible = False
        Ttelephoneliv.Text = ""
        Tfaxliv.Text = ""
        claireinfoclient()
        claireinfoproduit()
        SolGrid1.ClearSelection()
        AVBSTAT = AVBrunlock(AVB + fcotete)
        AVBSTAT = AVBrunlock(AVB + fcomma)
        AVBSTAT = AVBrunlock(AVB + fClient)
        Dim temps As String = Tnocom.Text
        BindEnteteBT()
        bsourceenteteCom.Position = bsourceenteteCom.Find("Nocommande", temps)
        affichebTbinding()
        CalculegridTotal()
        BtImpSoum.Enabled = False
        btnconnaissement.Enabled = True
        LblMag.Visible = False
        Btnnapa.Enabled = False
        BtCreation.Enabled = False
        entrepotold = "*"
        ancienclient = ""
        frmcommod = False
        trclicom = False
        Tnocomrech.Focus()
    End Sub
#End Region
#Region "SF6 info substitut"
    Private Sub BtnSubstitut_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles BtnSubstitut.Click
        infosubstitut()
    End Sub
    Private Sub infosubstitut()
        If promener = True Then Exit Sub
        If gridfocus = True Then
            sollignefocus = SolGrid1.CurrentRow.Index
            solcelfocus = SolGrid1.CurrentCell.ColumnIndex
        End If
        auclient = Me.Tclient.Text
        If dsrutilisateur.Item("tousacces") = True Then
            montreinfosubstitut(sollignefocus, SolGrid1, True, SolGrid1.CurrentRow.Cells("um").EditedFormattedValue.ToString)
            SolGrid1.Rows(sollignefocus).Cells(solcelfocus).Value = AVBproduit
        Else
            montreinfosubstitut(sollignefocus, SolGrid1, dsrutilisateurinv.Item("inprixn"), SolGrid1.CurrentRow.Cells("um").EditedFormattedValue.ToString)
            SolGrid1.Rows(sollignefocus).Cells(solcelfocus).Value = AVBproduit
        End If
        SolGrid1.RefreshEdit()
        SolGrid1.Rows(sollignefocus).Cells(solcelfocus).AccessibilityObject.Select(AccessibleSelection.AddSelection)
        SolGrid1.Rows(sollignefocus).Cells(solcelfocus).AccessibilityObject.Select(AccessibleSelection.TakeSelection)
        SolGrid1.Rows(sollignefocus).Cells(solcelfocus).AccessibilityObject.Select(AccessibleSelection.TakeFocus)
        SolGrid1.Rows(sollignefocus).Cells(solcelfocus).Selected = True
    End Sub
#End Region

#Region "F6 info produit"
    Private Sub infoproduit()
        If promener = True Then Exit Sub
        If gridfocus = True Then
            sollignefocus = SolGrid1.CurrentRow.Index
            solcelfocus = SolGrid1.CurrentCell.ColumnIndex
            Me.Cursor.Position = New System.Drawing.Point(Cursorx, Cursory)
        End If
        If dsrutilisateur.Item("tousacces") = True Then
            montreinfoprod(sollignefocus, SolGrid1, True, SolGrid1.CurrentRow.Cells("um").EditedFormattedValue.ToString)
        Else
            montreinfoprod(sollignefocus, SolGrid1, dsrutilisateurinv.Item("inprixn"), SolGrid1.CurrentRow.Cells("um").EditedFormattedValue.ToString)
        End If
        SolGrid1.Rows(sollignefocus).Cells(solcelfocus).Selected = True
        SolGrid1.Rows(sollignefocus).Cells(solcelfocus).AccessibilityObject.Select(AccessibleSelection.AddSelection)
        SolGrid1.Rows(sollignefocus).Cells(solcelfocus).AccessibilityObject.Select(AccessibleSelection.TakeSelection)
        SolGrid1.Rows(sollignefocus).Cells(solcelfocus).AccessibilityObject.Select(AccessibleSelection.TakeFocus)
    End Sub
#End Region
#Region "Inserer F7"
    Private Sub inserer()
        If promener = True Then Exit Sub
        If SolGrid1.CurrentRow.Index = SolGrid1.Rows.Count - 1 Then
            If lang = "F" Then MsgBox("Vous ne pouvez pas insérer une ligne à la fin")
            If lang <> "F" Then MsgBox("You can not insert a line at the end")
            Exit Sub
        End If
        If SolGrid1.CurrentRow.Index = 0 Then
            If lang = "F" Then MsgBox("Vous ne pouvez pas insérer une avant la première")
            If lang <> "F" Then MsgBox("You can not insert a line before the first one")
            Exit Sub
        End If
        'si fiche < 2 
        Dim ligneactuel As Integer = Int(SolGrid1.CurrentRow.Cells("ligne").EditedFormattedValue)
        Dim ligneprecedente As Integer = Int(SolGrid1.Rows(SolGrid1.CurrentRow.Index - 1).Cells("ligne").EditedFormattedValue)
        If ligneactuel - ligneprecedente < 2 Then
            If lang = "F" Then MsgBox("Vous ne pouvez pas insérer une autre ligne à cet endroit")
            If lang <> "F" Then MsgBox("You can not insert any more lines at this point")
            Exit Sub
        End If
        If inserelig = True Then
            If lang = "F" Then MsgBox("Vous ne pouvez pas faire une deuxième insertion" + vbCrLf + "Complétez la ligne et ensuite faites une autre insertion")
            If lang <> "F" Then MsgBox("You can not do a second insertion" + vbCrLf + "Complete the current line then do and insertion")
            Exit Sub
        End If
        BTannule.Enabled = False
        Bafficheseulement = True
        Dim nouvcompteur As Double = (ligneactuel - ligneprecedente) / 2 + ligneprecedente
        Dim dd As DataRow
        Dim ddp As DataRow
        InsertLignecom(nouvcompteur, Tnocom.Text, dscomma1, DsPoids, dd, ddp)
        dscomma1.Rows.InsertAt(dd, SolGrid1.CurrentRow.Index)
        DsPoids.Rows.InsertAt(ddp, SolGrid1.CurrentRow.Index)
        Dim nouvligne As Integer = SolGrid1.CurrentRow.Index - 1
        Dim ligne As DataGridViewRow = SolGrid1.Rows(nouvligne)
        ReDim Preserve quant_old(SolGrid1.Rows.Count - 1)
        ReDim Preserve quant_paqbte(SolGrid1.Rows.Count - 1)
        ReDim Preserve prod_old(SolGrid1.Rows.Count - 1)
        ReDim Preserve um_old(SolGrid1.Rows.Count - 1)
        For compteur As Integer = SolGrid1.Rows.Count - 2 To nouvligne Step -1
            quant_paqbte(compteur + 1) = quant_paqbte(compteur)
            quant_old(compteur + 1) = quant_old(compteur)
            prod_old(compteur + 1) = prod_old(compteur)
            um_old(compteur + 1) = um_old(compteur)
        Next
        quant_paqbte(nouvligne) = 0
        quant_old(nouvligne) = 0
        prod_old(nouvligne) = ""
        um_old(nouvligne) = ""
        ligne.Cells("Produit").Selected = True
        ligne.Cells("Produit").AccessibilityObject.Select(AccessibleSelection.AddSelection)
        ligne.Cells("Produit").AccessibilityObject.Select(AccessibleSelection.TakeSelection)
        ligne.Cells("Produit").AccessibilityObject.Select(AccessibleSelection.TakeFocus)
        sollignefocus = ligne.Index
        solcelfocus = ligne.Cells("produit").ColumnIndex
        inserelig = True
        insererfiche = ligne.Index
        Bafficheseulement = False
    End Sub
#End Region
#Region "Recherche F8"
    Private Sub recherchecata()
        Dim rechcat As New FrmRechercheCatalogueComplet
        rechcat.txtresult.Text = ""
        rechcat.ShowDialog()
        Dim lig As Integer = SolGrid1.CurrentRow.Index
        If rechcat.DialogResult = Windows.Forms.DialogResult.No Then
            SolGrid1.Rows(lig).Cells("produit").Selected = True
            Exit Sub
        End If
        If rechcat.DialogResult = System.Windows.Forms.DialogResult.OK Then
            dscomma1.Rows(SolGrid1.CurrentRow.Index).Item("Produit") = rechcat.txtresult.Text.PadRight(30)
            SolGrid1.RefreshEdit()
            AVBSTAT = AVBPosn(AVB + fInprix, rechcat.txtresult.Text.PadRight(30), 1, "", &H100)
            AVBSTAT = AVBread(AVB + fInprix, 1)
            If AVBSTAT = 0 Then
                If lang = "F" Then MsgBox("Produit existant")
                If lang <> "F" Then MsgBox("Existing product")
                Exit Sub
            Else
                Dim ok As Boolean
                Creerproduitcatalog(rechcat.txtresult.Text.PadRight(30), GIligne, ok, fInprix)
                If ok = False Then
                    Bcommenceligne = False
                Else
                    Sauve_sites(rechcat.txtresult.Text.PadRight(30), "   ")
                End If
                focusderniere()
            End If
        End If
        rechcat.Dispose()
    End Sub
    Sub Recherchercommande()
        If promener = True Then
            Dim NewMDIChildRcommande As New FrmRechercheCommande
            whichform = fcotete
            NewMDIChildRcommande.TxtResult.Text = Trim(Tnocomrech.Text)
            Dim result As System.Windows.Forms.DialogResult
            result = NewMDIChildRcommande.ShowDialog()
            If result = System.Windows.Forms.DialogResult.OK Then
                Tnocomrech.Text = NewMDIChildRcommande.TxtResult.Text
                If Tnocomrech.Text.Trim <> "" Then trouvcom()
            End If
            NewMDIChildRcommande.Dispose()
        Else
            If My.Settings.MonComshow = "O" Then
                Dim newrech As New FrmRecherchecommandeclient
                newrech.TxtResult.Text = Tclient.Text
                newrech.TxtWich.Text = "commande"
                newrech.ShowDialog()
                If newrech.DialogResult = Windows.Forms.DialogResult.OK Then
                    Dim nocomtemp As String = newrech.TxtResult.Text
                    AVBSTAT = AVBclose(AVB + 98)
                    'pour 2 écrans et que l'autre est encore dessus en modif
                    AVBSTAT = AVBPosn(AVB + fcotete, nocomtemp.PadLeft(10), 1, "", &H100)
                    AVBSTAT = AVBrlock(AVB + fcotete)
                    If AVBSTAT <> 0 Then
                        If lang = "F" Then MsgBox("Quelqu'un d'autre modifie ce bon. Je ne peux pas le réserver!")
                        If lang <> "F" Then MsgBox("Somebody else is using this order. Edit Mode not available !")
                        Exit Sub
                    End If
                    ProcedureAnnule()
                    Tnocom.Text = nocomtemp
                    newrech.Dispose()
                    bsourceenteteCom.Position = bsourceenteteCom.Find("NoCommande", Tnocom.Text.Trim.PadLeft(10))
                    ProcedureModifier()
                    trclicom = True
                    newrech.Dispose()
                End If
                newrech.Dispose()
            End If
        End If
    End Sub
    Private Sub recherche()
        Dim str As String
        Dim retype As Boolean
        str = Me.ActiveControl.Name
        tbb = Me.ActiveControl
        AVBType = ""
        AVBchercheType = ""
        If tbb Is Tclient Or tbb Is Tclientliv Then
            Dim rcclient As New FrmRechercheClient
            rcclient.TxtResult.Text = tbb.Text
            rcclient.ShowDialog()
            If rcclient.DialogResult = System.Windows.Forms.DialogResult.OK Then
                Me.tbb.Text = rcclient.TxtResult.Text
                Me.tbb.Focus()
                'repositionner sur client a l'ecran
                If tbb Is Tclientliv Then
                    AVBSTAT = AVBPosn(AVB + fClient, Tclient.Text.PadRight(7), 1, "", &H100)
                    AVBSTAT = AVBread(AVB + fClient, 1)
                End If
            End If
            rcclient.Dispose()
        ElseIf tbb Is Tnocomrech Then
            Recherchercommande()
        ElseIf Me.ActiveControl Is TxtTermes Then
            Dim rctermes As New FrmRechercheTermes
            rctermes.ShowDialog()
            If rctermes.DialogResult = System.Windows.Forms.DialogResult.OK Then
                Me.tbb.Text = AVBTermes
                Me.tbb.Focus()
            End If
            rctermes.Dispose()
        ElseIf Me.ActiveControl Is TxtExpediteur Then
            AVBType = "EX"
            retype = True
        ElseIf Me.ActiveControl Is Txtvendeur Then
            AVBType = "VE"
            retype = True
        ElseIf tbb Is Tentrepot Then
            AVBType = "EN"
            retype = True
        ElseIf Me.ActiveControl Is Tcommis Then
            AVBType = "CM"
            retype = True
        ElseIf SolGrid1.ContainsFocus = True Then
            If SolGrid1.CurrentCell.ColumnIndex = SolGrid1.Columns("produit").Index Then
                Dim col As Integer = SolGrid1.Columns("produit").Index
                Dim lig As Integer = SolGrid1.CurrentCell.RowIndex
                Dim NewMDIChildRproduit As New FrmRechercheProduit
                Dim result As System.Windows.Forms.DialogResult
                NewMDIChildRproduit.TxtResult.Text = SolGrid1.CurrentRow.Cells("produit").EditedFormattedValue.ToString.PadRight(30)
                result = NewMDIChildRproduit.ShowDialog()
                SolGrid1.Focus()
                If result = System.Windows.Forms.DialogResult.OK Then
                    dscomma1.Rows(SolGrid1.CurrentRow.Index).Item("Produit") = NewMDIChildRproduit.TxtResult.Text
                    'AVBSTAT = AVBPosn(AVB + fInprix, NewMDIChildRproduit.TxtResult.Text.PadRight(30), 1, "", &H100)
                    'AVBSTAT = AVBread(AVB + fInprix, 1)
                    'dscomma1.Rows(SolGrid1.CurrentRow.Index).Item("description") = AVBcs(AVBfiditemstub("DESCR", AVB + fInprix, 0))
                    'dscomma1.Rows(SolGrid1.CurrentRow.Index).Item("um") = AVBcs(AVBfiditemstub("PAR", AVB + fInprix, 0))
                    SolGrid1.RefreshEdit()
                End If
                NewMDIChildRproduit.Dispose()
                SolGrid1.CurrentCell.Selected = True
                SolGrid1.BeginEdit(True)
                AVBTrouveproduit = ""
            ElseIf SolGrid1.CurrentCell.ColumnIndex = SolGrid1.Columns("um").Index Then
                If Trim(AVBcs(AVBfiditemstub("PAR", AVB + fInprix, 1))) <> "" Then
                    Sposum = dscomma1.Rows(SolGrid1.CurrentRow.Index).Item("um")
                    Dim frmum As New FrmUmShow
                    frmum.ShowDialog()
                    If frmum.DialogResult = Windows.Forms.DialogResult.OK Then
                        If Trim(dscomma1.Rows(SolGrid1.CurrentRow.Index).Item("um")) <> Trim(AVBTrouveproduit) Then
                            SolGrid1.CurrentRow.Cells("prix").Value = ""
                            SolGrid1.CurrentRow.Cells("montant").Value = ""
                            SolGrid1.CurrentRow.Cells("escompte").Value = ""
                        End If
                        SolGrid1.CurrentRow.Cells("um").Value = AVBTrouveproduit
                        Dim noligne As Integer = SolGrid1.CurrentRow.Index
                        dscomma1.Rows(noligne).Item("um") = AVBTrouveproduit
                        Dim umx As Integer = TrouveUm(SolGrid1.CurrentRow.Cells("produit").Value.ToString, SolGrid1.CurrentRow.Cells("um").Value.ToString)
                        dscomma1.Rows(noligne).Item("umx") = umx
                        dscomma1.Rows(noligne).Item("mult2") = AVBcs(AVBfiditemstub("MULT1", AVB + fInprix, umx))
                        dscomma1.Rows(noligne).Item("div2") = AVBcs(AVBfiditemstub("DIV1", AVB + fInprix, umx))
                        Dim prodtemp As String = SolGrid1.Rows(noligne).Cells("produit").Value.ToString.PadRight(30)
                        'TrouveDispo(prodtemp, SolGrid1.CurrentRow.Index, Tentrepot.Text.PadLeft(3), SolGrid1.CurrentRow.Cells("um").Value.ToString)
                        showinfoprod(dscomma1.Rows(noligne).Item("um"), prodtemp)
                    End If
                    frmum.Dispose()
                End If
            End If
        End If
        If retype = True Then
            Dim rtype As New FrmRechercheType
            rtype.TxtResult.Text = tbb.Text
            rtype.ShowDialog()
            If rtype.DialogResult = System.Windows.Forms.DialogResult.OK Then
                Me.tbb.Text = AVBchercheType
                Me.tbb.Focus()
            End If
            rtype.Dispose()
        End If
        retype = False

    End Sub
    Private Sub rechercheentrepot()
        Dim rcprod As New FrmRechercheProduitEntrepot
        rcprod.TxtEntrepot.Text = Tentrepot.Text
        rcprod.TxtResult.Text = ""
        rcprod.ShowDialog()
        If rcprod.DialogResult = System.Windows.Forms.DialogResult.OK Then
            ''Me.tbb.Text = AVBTrouveproduit
            AVBSTAT = AVBkey(AVB + fInven, 1, 0)
            dscomma1.Rows(SolGrid1.CurrentRow.Index).Item("Produit") = rcprod.TxtResult.Text.Trim
            AVBSTAT = AVBPosn(AVB + fInprix, rcprod.TxtResult.Text.PadRight(30), 1, "", &H100)
            AVBSTAT = AVBread(AVB + fInprix, 1)
            dscomma1.Rows(SolGrid1.CurrentRow.Index).Item("description") = AVBcs(AVBfiditemstub("DESCR", AVB + fInprix, 0))
            dscomma1.Rows(SolGrid1.CurrentRow.Index).Item("um") = AVBcs(AVBfiditemstub("PAR", AVB + fInprix, 0))
            SolGrid1.RefreshEdit()
        End If
        rcprod.Dispose()
    End Sub

#End Region
#Region "Efface F9"

    Sub Effaceligne()
        If promener = True Then Exit Sub
        If SolGrid1.Rows.Count <= 0 Then Exit Sub
        If SolGrid1.CurrentCell.ColumnIndex <> SolGrid1.Columns("Produit").Index Then
            If lang = "F" Then MsgBox("Vous devez être sur le colonne numéro de produit")
            If lang <> "F" Then MsgBox("You must be on the product column")
            Exit Sub
        End If
        If dscomma1.Rows(SolGrid1.CurrentRow.Index) Is Nothing Then
            If lang = "F" Then MsgBox("Vous ne pouvez pas effacer une ligne vide")
            If lang <> "F" Then MsgBox("You can not delete an empty line")
            Exit Sub
        End If
        If Trim(SolGrid1.CurrentRow.Cells("produit").FormattedValue.ToString) = "" _
        Or Trim(dscomma1.Rows(SolGrid1.CurrentRow.Index).Item("produit").ToString) = "" Then
            If lang = "F" Then MsgBox("Vous ne pouvez pas effacer une ligne vide")
            If lang <> "F" Then MsgBox("You can not delete an empty line")
            Exit Sub
        End If
        If My.Settings.effproduitpbt.Trim = "O" Then
            If lang = "F" Then MsgBox("Vous n'avez pas le droit d'effacer une ligne")
            If lang <> "F" Then MsgBox("You do not have the right to delete a line")
            Exit Sub
        End If
        If Trim(SolGrid1.CurrentRow.Cells("status").FormattedValue.ToString) = "F" Then
            Dim question As String = ""
            If lang = "F" Then question = "Cette ligne a généré une commande fournisseur!"
            If lang <> "F" Then question = "This line has a supplier order!"
            If questioneffacer(question) = False Then
                If lang = "F" Then MsgBox("Annulé!")
                If lang <> "F" Then MsgBox("Canceled!")
                Exit Sub
            End If
        End If
        If SolGrid1.CurrentRow.Index = SolGrid1.Rows.Count - 1 Then
            For compteur1 As Integer = 0 To SolGrid1.Columns.Count - 1
                Dim str As String = SolGrid1.Columns(compteur1).Name
                If SolGrid1.Columns(compteur1).Name = "coutant" Or SolGrid1.Columns(compteur1).Name = "quantiteliv" _
                Or SolGrid1.Columns(compteur1).Name = "taxe provincial" _
                Or SolGrid1.Columns(compteur1).Name = "taxe fédéral" Then
                    SolGrid1.CurrentRow.Cells(compteur1).Value = 0
                ElseIf SolGrid1.Columns(compteur1).Name = "Ligne" Or SolGrid1.Columns(compteur1).Name = "no commande" Then

                Else
                    SolGrid1.CurrentRow.Cells(compteur1).Value = ""
                End If
            Next
            Bcommenceligne = False
            SolGrid1.RefreshEdit()
            Exit Sub
        End If
        '   If SolGrid1.Focused = False Then Exit Sub
        Dim index As Integer = SolGrid1.SelectedCells.Count
        If index = 0 Then Exit Sub
        index = SolGrid1.SelectedCells(0).RowIndex
        If SolGrid1.RowCount = 0 Then Exit Sub
        Bafficheseulement = True
        CausesValidation = False
        Dim strtemp As String
        'a checker l'inventaire
        Dim quant As Double = Val(SolGrid1.Rows(index).Cells("quantite").Value)
        If Val(dscomma1.Rows(SolGrid1.CurrentRow.Index).Item("paq_bte")) <> 0 Then quant = Val(dscomma1.Rows(index).Item("paq_bte"))
        Updateinventaire(SolGrid1.Rows(index).Cells("Produit").Value.ToString.PadRight(30), Tentrepot.Text.PadLeft(3), -1, 1, quant, SolGrid1.Rows(index).Cells("um").Value.ToString, False, " ", 0, dscomma1.Rows(index).Item("lot").ToString)
        'efface la ligne du work
        strtemp = dscomma1.Rows(index).Item("ligne").ToString
        strtemp = Tnocom.Text.PadLeft(10) + strtemp
        AVBSTAT = AVBPosn(AVB + fcomma, strtemp, 1, "", 0)
        Do
            AVBSTAT = AVBrlock(AVB + fcomma)
        Loop Until AVBSTAT = 0
        AVBSTAT = AVBread(AVB + fcomma, 0)
        If AVBSTAT = 0 And Trim(AVBcs(AVBfiditemstub("NOCOM", AVB + fcomma, 0))) = Trim(Tnocom.Text) _
         And Trim(AVBcs(AVBfiditemstub("FICHE", AVB + fcomma, 0))) = Trim(dscomma1.Rows(index).Item("ligne").ToString) Then
            AVBSTAT = AVBfree(AVB + fcomma)
            AVBSTAT = AVBsecure(AVB + fcomma)
        End If
        'avant d'effacer dans la grille checker si kit
        Dim prodtemp As String = SolGrid1.CurrentRow.Cells("produit").Value.ToString.PadRight(30)
        AVBSTAT = AVBPosn(AVB + fInprix, prodtemp, 1, "", &H100)
        AVBSTAT = AVBread(AVB + fInprix, 1)
        Dim compteur As Integer = index
        If AVBcs(AVBfiditemstub("TYPE1", AVB + fInprix, 0)) = "K" Then
            SysOpen(fkit)
            AVBSTAT = AVBPosn(AVB + fkit, prodtemp, 1, "", 0)
            AVBSTAT = AVBread(AVB + fkit, 0)
            Do While prodtemp = AVBcs(AVBfiditemstub("PRODUIT", AVB + fkit, 0)) And AVBSTAT = 0
                compteur = compteur + 1
                If compteur > SolGrid1.Rows.Count - 1 Then Exit Do
                Dim tt As String = SolGrid1.Rows(compteur).Cells("produit").Value.ToString.Trim
                Dim ff As String = AVBcs(AVBfiditemstub("COMPO", AVB + fkit, 0)).Trim
                If SolGrid1.Rows(compteur).Cells("produit").Value.ToString.Trim <> AVBcs(AVBfiditemstub("COMPO", AVB + fkit, 0)).Trim Then Exit Do
                Updateinventaire(SolGrid1.Rows(compteur).Cells("Produit").Value.ToString.PadRight(30), Tentrepot.Text.PadLeft(3), -1, 1, Val(SolGrid1.Rows(compteur).Cells("quantite").FormattedValue), SolGrid1.Rows(compteur).Cells("um").Value.ToString, False, " ", 0, "")



                strtemp = dscomma1.Rows(compteur).Item("ligne").ToString
                strtemp = Tnocom.Text.PadLeft(10) + strtemp
                AVBSTAT = AVBPosn(AVB + fcomma, strtemp, 1, "", 0)
                'Do
                '    AVBSTAT = AVBrlock(AVB + fcomma)
                'Loop Until AVBSTAT = 0
                AVBSTAT = AVBread(AVB + fcomma, 0)
                If AVBSTAT = 0 And Trim(AVBcs(AVBfiditemstub("NOCOM", AVB + fcomma, 0))) = Trim(Tnocom.Text) _
                 And Trim(AVBcs(AVBfiditemstub("FICHE", AVB + fcomma, 0))) = Trim(dscomma1.Rows(compteur).Item("ligne").ToString) Then
                    AVBSTAT = AVBfree(AVB + fcomma)
                    AVBSTAT = AVBsecure(AVB + fcomma)
                End If
                AVBSTAT = AVBread(AVB + fkit, 0)
            Loop
            SysClose(fkit)
        End If
        AVBSTAT = AVBrunlock(AVB + fcomma)
        'Effacer une ligne dans le grid
        For cc As Integer = index To compteur
            dscomma1.Rows.RemoveAt(index)
            DsPoids.Rows.RemoveAt(index)
        Next
        If SolGrid1.Rows.Count = 0 Then
            redimquant()
        Else
            ReDim quant_paqbte(SolGrid1.Rows.Count - 1)
            ReDim quant_old(SolGrid1.Rows.Count - 1)
            ReDim prod_old(SolGrid1.Rows.Count - 1)
            ReDim um_old(SolGrid1.Rows.Count - 1)
            For Each ligne As DataGridViewRow In SolGrid1.Rows
                If ligne.Cells("produit").Value Is DBNull.Value Then ligne.Cells("produit").Value = ""
                If ligne.Cells("um").Value Is DBNull.Value Then ligne.Cells("um").Value = ""
                quant_old(ligne.Index) = Val(ligne.Cells("quantite").Value)
                prod_old(ligne.Index) = ligne.Cells("produit").Value
                um_old(ligne.Index) = ligne.Cells("um").Value
                quant_paqbte(ligne.Index) = Val(ligne.Cells("paq_bte").Value)
            Next
        End If
        Dim fin As Integer = SolGrid1.Rows.Count - 1
        If fin = -1 Then
            creernouvligne(True)
        Else
            If Trim(SolGrid1.Rows(fin).Cells("produit").Value.ToString) = "" Then SolGrid1.Rows(fin).Cells("produit").Selected = True
        End If
        'recalcule totaux et coutant
        CalculegridTotal()
        claireinfoproduit()
        BTannule.Enabled = False
        CausesValidation = True
        Bafficheseulement = False
    End Sub
    Private Sub effaceentete()
        If promener = True Then Exit Sub
        If troptit = False Then
            If peueffacer = False Then
                messagedroit()
                Exit Sub
            End If
        End If
        If Val(Tdepot.Text) <> 0 Then
            If lang = "F" Then MsgBox("Il faut annuler le dépôt avant d'effacer")
            If lang <> "F" Then MsgBox("You must cancel the deposit before deleting")
            Tajoutdepot.Focus()
            Exit Sub
        End If
        If Bcommenceligne = True Then
            If lang = "F" Then MsgBox("Terminez la ligne avant d'effacer")
            If lang <> "F" Then MsgBox("Complete the line before deleting")
            Exit Sub
        End If
        If dscotete1.Rows.Count <= 0 Then
            If lang = "F" Then MsgBox("Il n'y a pas de commande a effacer")
            If lang <> "F" Then MsgBox("There are no orders to delete")
            Exit Sub
        End If
        Dim question As String = ""
        If lang = "F" Then question = "Le bon de commande " & Tnocom.Text & "?"
        If lang <> "F" Then question = "The order " & Tnocom.Text & "?"
        If questioneffacer(question) = False Then
            If lang = "F" Then MsgBox("Annulé!")
            If lang <> "F" Then MsgBox("Canceled!")
            Exit Sub
        Else
            If Checksilignefournisseur(fcomma, Tnocom.Text) = True Then
                If lang = "F" Then MsgBox("Il y a des produits reliés a une commande fournisseur")
                If lang <> "F" Then MsgBox("There are products related to a supplier order")
                Dim question2 As String = ""
                If lang = "F" Then question2 = "Le bon de commande " & Tnocom.Text & "?"
                If lang <> "F" Then question2 = "The order " & Tnocom.Text & "?"
                If questioneffacer(question2) = False Then
                    If lang = "F" Then MsgBox("Annulé!")
                    If lang <> "F" Then MsgBox("Canceled!")
                    Exit Sub
                End If
                ' Exit Sub
            End If
            'DisableEcran()
            'ico_promener(True)
            Erasecommande(fcotete, Tnocom.Text)
            'replace l'inventaire
            If SolGrid1.Rows.Count >= 0 Then
                For compteur As Integer = 0 To SolGrid1.Rows.Count - 1
                    If SolGrid1.Rows(compteur).Cells("Produit").Value.ToString.Trim <> "" Then
                        Dim quant As Double = Val(SolGrid1.Rows(compteur).Cells("quantite").Value)
                        If Val(dscomma1.Rows(compteur).Item("paq_bte")) <> 0 Then quant = Val(dscomma1.Rows(compteur).Item("paq_bte"))
                        Updateinventaire(SolGrid1.Rows(compteur).Cells("Produit").Value.ToString.PadRight(30), Tentrepot.Text.PadLeft(3), -1, 1, quant, SolGrid1.Rows(compteur).Cells("um").Value.ToString, False, " ", 0, dscomma1.Rows(compteur).Item("lot").ToString)
                    End If
                Next
            End If
            EraseLignecommande(fcomma, Tnocom.Text)
            dscotete1.Rows.RemoveAt(bsourceenteteCom.Position)
            DisableEcran()
            ico_promener(True)
            redimquant()
            bsourceenteteCom.MoveLast()
            dscomma1.Clear()
            DsPoids.Clear()
            SetEcran(Me)
            SolGrid1.DataSource = ""
            CreateDataSourceLigneCom(Tnocom.Text.Trim.PadLeft(10), dscomma1, DsPoids)
            promener = True
            SolGrid1.DataSource = dscomma1
            CalculegridTotal()
            'DisableEcran()
            'ico_promener(True)
            frmcommod = False
            Bafficheseulement = False
            Bencommandeclient = False
            Benmodification = False
            Tnocomrech.Focus()
        End If
    End Sub
#End Region
#Region "Modifier f11"
    Sub ProcedureModifier()
        If promener = False Then Exit Sub
        If dscotete1.Rows.Count <= 0 Then Exit Sub
        If troptit = False Then
            If peumodifier = False Then
                messagedroit()
                Exit Sub
            End If
        End If
        Bafficheseulement = True
        Btnnapa.Enabled = True
        Tnocomrech.Text = ""
        Bencommandeclient = True
        AVBSTAT = AVBPosn(AVB + fcotete, Tnocom.Text.PadLeft(10), 1, "", &H100)
        AVBSTAT = AVBrlock(AVB + fcotete)
        If AVBSTAT <> 0 Then
            If lang = "F" Then MsgBox("Quelqu'un d'autre modifie cette commande. Je ne peux pas la réserver!")
            If lang <> "F" Then MsgBox("Somebody else is using this order. Edit Mode not available !")
            Exit Sub
        End If
        AVBSTAT = AVBread(AVB + fcotete, 1)
        If AVBSTAT <> 0 Then
            If lang = "F" Then MsgBox("Cette commande n'existe plus!")
            If lang <> "F" Then MsgBox("This order does not exist!")
            AVBSTAT = AVBrunlock(AVB + fcotete)
            AVBSTAT = AVBrunlock(AVB + fcomma)
            AVBSTAT = AVBrunlock(AVB + fClient)
            BindEnteteBT()
            affichebTbinding()
            Exit Sub
        End If
        If Benmodification = True Then
            MsgBox("Vous ne pouvez être en mode modification dans Bon de travail, commande fournisseur ou Réception fournisseur")
            Exit Sub
        End If
        Benmodification = True


        entrepotold = AVBcs(AVBfiditemstub("ENTREPOT", AVB + fcotete, 0))
        EnableEcran()
        ico_promener(False)
        BTnouveau.Enabled = False
        BTmodifier.Enabled = False
        BtCreation.Enabled = True
        btnconnaissement.Enabled = False
        Dim pointeur As Integer = bsourceenteteCom.Position
        dscotete1.Rows(pointeur).BeginEdit()
        SNocommande = Tnocom.Text.PadLeft(10)
        renouventetecom(bsourceenteteCom, dscotete1)
        If dscotete1.Rows(pointeur).Item("Datecommande").ToString.Trim <> "" Then Ddateouverture.Text = dscotete1.Rows(pointeur).Item("Datecommande").ToString.Trim
        If dscotete1.Rows(pointeur).Item("Datelivraison").ToString.Trim <> "" Then Ddaterequis.Text = dscotete1.Rows(pointeur).Item("Datelivraison").ToString.Trim
        dscotete1.Rows(bsourceenteteCom.Position).EndEdit()
        Affichebondecommande()
        AVBSTAT = AVBPosn(AVB + fClient, Tclient.Text, 1, "", &H100S)
        AVBSTAT = AVBread(AVB + fClient, 1)
        If AVBSTAT <> 0 Then
            If lang = "F" Then MsgBox("Le client de ce bon a été effacé")
            If lang <> "F" Then MsgBox("The client on this work order has been erased")
        End If
        lang4 = AVBcs(AVBfiditemstub("LANGUE", AVB + fClient, 0))
        gettel()
        Me.Refresh()
        ancienclient = Tclient.Text
        SolGrid1.Focus()
        frmcommod = True
        Tnocom.ReadOnly = True
        promener = False
        SolGrid1.Focus()
        chkmemo("C", Tclient.Text.PadRight(7))
        If SolGrid1.Rows.Count <= 0 Then
            Bafficheseulement = True
            DCompteur = 10000
            NewLigneCom(DCompteur, Tnocom.Text, dscomma1, DsPoids)
            ReDim Preserve quant_old(UBound(quant_old) + 1)
            ReDim Preserve quant_paqbte(UBound(quant_paqbte) + 1)
            ReDim Preserve prod_old(UBound(prod_old) + 1)
            prod_old(UBound(prod_old)) = ""
            ReDim Preserve um_old(UBound(um_old) + 1)
            um_old(UBound(um_old)) = ""
            Trouvelignefocus()
            Bafficheseulement = False
        Else
            creernouvligne(True)
        End If
        Bafficheseulement = False
        BTprochain.Enabled = False
        BTfin.Enabled = False
        BTprecedent.Enabled = False
        BTdebut.Enabled = False
        If My.Settings.MonCommis.Trim = "O" Then
            Tcommis.Text = ""
            Tcommis.Focus()
        End If
    End Sub
#End Region
#Region "Imprimer F12 "
    Private Sub ProcedureImprime()
        'SNocommande = Tnocom.Text
        'SaveEnteteWo(BsourceenteteCom.Position)
        'Imprimeouinon = False
        If promener = False Then
            impcom = Tnocom.Text
            Imprimeouinon = True
            ProcedureSauve()

            TxtEscompte.Focus()
            Exit Sub
        End If
        Imprimeouinon = False
        Dim Inb As Integer = Val(AVBcs(AVBfiditemstub("IMP", AVB + fcotete, 0)))
        Inb = Inb + 1
        AVBfput(Inb.ToString, "IMP", AVB + fcotete, 0, 0)

        AVBSTAT = AVBwrite(AVB + fcotete, 0, 0)
        AVBSTAT = AVBsecure(AVB + fcotete)
        Imprime()
        promener = True
        Me.BTprochain.Enabled = True
        Me.BTprecedent.Enabled = True
        Me.BTdebut.Enabled = True
        Me.BTfin.Enabled = True
        Me.BTnouveau.Enabled = True
        Me.BTmodifier.Enabled = True
        Me.BTeffacer.Enabled = False
        Me.BTannule.Enabled = False
        Me.BTsauve.Enabled = False
        Me.BTimprime.Enabled = True
        ' affichebTbinding()
    End Sub
#End Region
#Region "CTRL F7 creer commande fournisseur"
    Private Sub crfournis(ByVal ext As Boolean)
        If promener = True Then Exit Sub
        If SolGrid1.ContainsFocus = False Then Exit Sub
        If SolGrid1.CurrentRow.Cells("produit").EditedFormattedValue.ToString.Trim = "" Then Exit Sub
        If SolGrid1.CurrentRow.Cells("status").EditedFormattedValue.ToString = "G" Then
            If lang = "F" Then MsgBox("Nous ne pouvons pas commander un status a G")
            If lang <> "F" Then MsgBox("We can not order a status G")
            Exit Sub
        End If
        If SolGrid1.CurrentRow.Cells("status").EditedFormattedValue.ToString <> "A" And SolGrid1.CurrentRow.Cells("status").EditedFormattedValue.ToString <> "S" And SolGrid1.CurrentRow.Cells("status").EditedFormattedValue.ToString <> "I" Then
            If lang = "F" Then MsgBox("La commande a déjà été placée")
            If lang <> "F" Then MsgBox("The order has already been passed")
            Exit Sub
        End If
        If Mid(SolGrid1.CurrentRow.Cells("produit").EditedFormattedValue.ToString, 1, 3) = Mid(Rem10, 1, 3) Then
            If lang = "F" Then MsgBox("Nous ne pouvons pas commander une remarque")
            If lang <> "F" Then MsgBox("We can not order a comment")
            Exit Sub
        End If
        Dim index As Integer = SolGrid1.CurrentCell.ColumnIndex
        If SolGrid1.Columns("Produit").Index <> index And ext = False Then
            If lang = "F" Then MsgBox("Il faut être sur la collonne produit")
            If lang <> "F" Then MsgBox("You must be on the product column")
            Exit Sub
        End If
        Dim prodtemp As String = SolGrid1.CurrentRow.Cells("produit").EditedFormattedValue.ToString.Trim.PadRight(30)
        AVBSTAT = AVBPosn(AVB + fInprix, prodtemp, 1, "", &H100)
        AVBSTAT = AVBread(AVB + fInprix, 1)

        If AVBcs(AVBfiditemstub("TYPE1", AVB + fInprix, 0)) = "D" Then
            If lang = "F" Then MsgBox("Nous ne pouvons pas commander un produit de dépense")
            If lang <> "F" Then MsgBox("e can not order a depense product")
            Exit Sub
        End If


        BTannule.Enabled = False
        Dim frcr As New FrmFournCommandeEXT
        frcr.TxtNocom.Text = Tnocom.Text
        frcr.TxtEntrepot.Text = Tentrepot.Text
        frcr.TxtAcheteur.Text = Txtvendeur.Text
        frcr.TxtLigne.Text = SolGrid1.CurrentRow.Cells("ligne").EditedFormattedValue.ToString
        frcr.TxtProduit.Text = SolGrid1.CurrentRow.Cells("produit").EditedFormattedValue.ToString
        frcr.TxtQuantite.Text = SolGrid1.CurrentRow.Cells("quantite").EditedFormattedValue.ToString
        frcr.txtcout.Text = SolGrid1.CurrentRow.Cells("coutant").EditedFormattedValue.ToString
        frcr.TxtUm.Text = SolGrid1.CurrentRow.Cells("UM").EditedFormattedValue.ToString
        frcr.TxtNocli.Text = Tclient.Text
        If Mid(SolGrid1.CurrentRow.Cells("produit").EditedFormattedValue.ToString, 1, 3) = Mid(Div10, 1, 3) Then frcr.TxtDesc.Text = SolGrid1.CurrentRow.Cells("description").EditedFormattedValue.ToString
        frcr.ChkRem.Checked = ext
        frcr.ShowDialog()
        If frcr.DialogResult = Windows.Forms.DialogResult.OK Then
            SolGrid1.CurrentRow.Cells("status").Value = "F"
            dscomma1.Rows(SolGrid1.CurrentRow.Index).Item("ref") = frcr.TxtFnocom.Text
            dscomma1.Rows(SolGrid1.CurrentRow.Index).Item("fournisseur") = frcr.TxtFournis.Text
            SolGrid1.RefreshEdit()
        End If
    End Sub
#End Region
#Region "recherche produit alt F11"
    Private Sub showhisto()
        'Qté vendue
        Dim varChamp As String = ""
        Dim varType As String = ""

        ''Choix à entrer => 1: ligne / 2:lignewo / 3: ligneve / 4: lignelo
        'Dim demandeChoix As New FrmQuantiteChoix
        'demandeChoix.ShowDialog()

        Dim rechQvendue As New FrmRechercheLigneProduit
        rechQvendue.TxtClient.Text = Tclient.Text
        rechQvendue.Txtcode.Text = SolGrid1.CurrentRow.Cells("produit").EditedFormattedValue.ToString
        rechQvendue.ShowDialog()
        If rechQvendue.DialogResult = Windows.Forms.DialogResult.OK Then
            'paramètres pour l'affichage de Crystal Reports
            SolGrid1.CurrentRow.Cells("produit").Value = rechQvendue.Txtcode.Text
            SolGrid1.RefreshEdit()

            varType = varCol.Trim
            'If (varChoixQte = "5" And varType = "F") Or varChoixQte = "1" Then
            '    SysOpen(ffactur)
            '    SysOpen(fligne)
            '    ImpSorte = "facture piece"              ' => FrmPrFacture
            '    reponse = "V"
            '    FormImp(SNocommande)
            '    SysClose(ffactur)
            '    SysClose(fligne)
            'End If
        End If
    End Sub
#End Region
#Region "Sortir esc ou X "
    Private Sub sortir()
        If promener = False Then
            If lang = "F" Then MsgBox("Vous êtes en mode modification, vous ne pouvez pas sortir")
            If lang <> "F" Then MsgBox("Save before leaving the Edit Mode")
            Exit Sub
        End If
        Tnocomrech.Text = ""
        Me.Close()
    End Sub

    Private Sub Frmoiececommande_FormClosing(ByVal sender As Object, ByVal e As System.Windows.Forms.FormClosingEventArgs) Handles Me.FormClosing
        'fermeture des fichiers Apogee
        If promener = False Then
            If lang = "F" Then MsgBox("Vous êtes en mode modification, vous ne pouvez pas sortir")
            If lang <> "F" Then MsgBox("Save before leaving the Edit Mode")
            e.Cancel = True
        End If
        If e.Cancel = False Then
            AVBSTAT = AVBrunlock(AVB + fClient)
            AVBSTAT = AVBrunlock(AVB + fcotete)
            AVBSTAT = AVBrunlock(AVB + fcomma)
            'SysClose(fcotete)
            'SysClose(fcomma)
        End If
    End Sub

#End Region
#Region "Textbox événement"
    Private Sub Tprovinceliv_Validated(ByVal sender As Object, ByVal e As System.EventArgs) Handles Tprovinceliv.Validated
        trouvtauxtaxeprov(Tprovinceliv.Text, prosufed, tauxtvqs)
    End Sub

    Private Sub Tclient_LostFocus(ByVal sender As Object, ByVal e As System.EventArgs) Handles Tclient.LostFocus
        If Tnocom.Text.Trim = "" Then
            'Ouvrebondecommande()
            Tnocom.Focus()
        Else
            Tnoachat.Focus()
        End If
    End Sub
    Private Sub Tclient_Validating(ByVal sender As Object, ByVal e As System.ComponentModel.CancelEventArgs) Handles Tclient.Validating
        If Bafficheseulement = True Then Exit Sub
        If clientclick = True Then Exit Sub
        If Trim(Tclient.Text) <> "" Then
            Tclient.Text = UCase(Tclient.Text).PadRight(7)
            If Tclient.Text.Trim = "!" Then
                If lang = "F" Then MsgBox("Vous ne pouvez pas utiliser le client par défaut")
                If lang <> "F" Then MsgBox("You can not use the default client")
                e.Cancel = True
                Exit Sub
            End If
            AVBSTAT = AVBPosn(AVB + fClient, Tclient.Text, 1, "", &H100S)
            AVBSTAT = AVBread(AVB + fClient, 1)
            If AVBSTAT <> 0 Then
                AVBSTAT = AVBPosn(AVB + fClient, Tclient.Text, 11, "", &H100S)
                AVBSTAT = AVBread(AVB + fClient, 1)
                If AVBSTAT <> 0 Then
                    AVBSTAT = AVBPosn(AVB + fClient, Tclient.Text, 12, "", &H100S)
                    AVBSTAT = AVBread(AVB + fClient, 1)
                    If AVBSTAT <> 0 Then
                        e.Cancel = True
                        If lang = "F" Then MsgBox("Ce client n'existe pas")
                        If lang <> "F" Then MsgBox("This client does not exist")
                    Else
                        chkclienttelplusmotcle2(AVBcs(AVBfiditemstub("MOTCLE2", AVB + fClient, 0)))
                        Tclient.Text = AVBcs(AVBfiditemstub("CLIENT", AVB + fClient, 0))
                    End If
                Else
                    'chkclienttelplus(AVBcs(AVBfiditemstub("CLIENT", AVB + fClient, 0)))
                    chkclienttelplus(AVBcs(AVBfiditemstub("MOTCLE1", AVB + fClient, 0)))
                    Tclient.Text = AVBcs(AVBfiditemstub("CLIENT", AVB + fClient, 0))
                End If
            End If
            If Trim(AVBcs(AVBfiditemstub("GROUPE", AVB + fClient, 0))) = "INTERNE" Then
                If lang = "F" Then MsgBox("Vous ne pouvez pas faire de commande pour un client ayant le groupe INTERNE")
                If lang <> "F" Then MsgBox("You can not make an order for a client in the INTERNAL group")
                e.Cancel = True
                Exit Sub
            End If
            If Trim(AVBcs(AVBfiditemstub("ARRET", AVB + fClient, 0))) = oui10 Then
                If lang = "F" Then MsgBox("Les transactions pour ce client sont arrêtées!" & vbCrLf & "Consultez le superviseur")
                If lang <> "F" Then MsgBox("The transactions with this client have been stopped!" & vbCrLf & "Consult your supervisor")
                e.Cancel = True
                Exit Sub
            End If
            If Trim(AVBcs(AVBfiditemstub("ACTIF", AVB + fClient, 0))) = "N" _
            Or Trim(AVBcs(AVBfiditemstub("ACTIF", AVB + fClient, 0))) = "CANCEL" _
            Or Mid(AVBcs(AVBfiditemstub("TERMES", AVB + fClient, 0)), 1, 1) = "F" Then
                If lang = "F" Then MsgBox("Ce client est inactif!" & vbCrLf & "Consultez le superviseur")
                If lang <> "F" Then MsgBox("This client is inactive!" & vbCrLf & "Consult your supervisor")
                e.Cancel = True
                Exit Sub
            End If
            If Mid(AVBcs(AVBfiditemstub("TERMES", AVB + fClient, 0)), 1, 1) = "S" Then
                If lang = "F" Then MsgBox("Attention payable sur livraison")
                If lang <> "F" Then MsgBox("Attention payable on delivery")
            End If
        Else
            Tclient.Text = cash10
            AVBSTAT = AVBPosn(AVB + fClient, Tclient.Text.PadRight(7), 1, "", &H100S)
            AVBSTAT = AVBread(AVB + fClient, 1)
            If Tclient.Text.Trim = "" Or AVBSTAT <> 0 Or AVBcs(AVBfiditemstub("CLIENT", AVB + fClient, 0)).Trim <> cash10.Trim _
            Or cash10.Trim = "" Then
                If lang = "F" Then MsgBox("Il faut entrer un client comptant dans le fichier de compagnie" & vbCrLf &
                "ou le client n'existe pas")
                If lang <> "F" Then MsgBox("You must enter a cash client in the company file " & vbCrLf & _
                "or enter a client number")
                e.Cancel = True
            End If
        End If
    End Sub
    Private Sub Tclient_Validated(ByVal sender As Object, ByVal e As System.EventArgs) Handles Tclient.Validated
        If Bafficheseulement = True Then Exit Sub
        If clientclick = True Then Exit Sub
        If Tclient.Text.Trim = "" Then
            Tclient.Text = cash10.PadRight(7)
            AVBSTAT = AVBPosn(AVB + fClient, Tclient.Text, 1, "", &H100S)
            AVBSTAT = AVBread(AVB + fClient, 1)
        End If
        chkmemo("C", Tclient.Text.PadRight(7))
        Dim Cancel As String = False
        If My.Settings.facturepassedu = "O" Then chkpasseduencomptabilite(Tclient.Text, Cancel, Tnocom.Text, Val(Ttotal.Text))
        If cancel = True Then
            ProcedureAnnule()
            Exit Sub
        End If
        If Trim(AVBcs(AVBfiditemstub("ROU1", AVB + fClient, 0))) <> "" Then
            Dim frmvr As New FrmVoirroute
            frmvr.ShowDialog()
            'If frmvr.DialogResult = Windows.Forms.DialogResult.Yes Then
            Lblroute.Text = Sroute
            Lblroutedef.Text = "Route : "
            Me.btnroute.Visible = True
            frmvr.Dispose()

        Else
            Me.btnroute.Visible = False
            Lblroute.Text = ""
            Lblroutedef.Text = ""
        End If
        affichecdata()
        'pour etre sur d'avoir le bon client
        If SolGrid1.RowCount > 0 Then
            For compteur As Integer = 0 To SolGrid1.RowCount - 1
                dscomma1.Rows(compteur).Item("client") = Tclient.Text
            Next
            Dim iposition As Integer = bsourceenteteCom.Position
            If BnouveauBT = False And ancienclient.Trim <> Tclient.Text.Trim And ancienclient.Trim <> "" Then
                dscotete1.Rows(iposition).Item("Adresse") = AVBcs(AVBfiditemstub("ADR1", AVB + fClient, 0)).Trim
                dscotete1.Rows(iposition).Item("Province") = AVBcs(AVBfiditemstub("PROV", AVB + fClient, 0))
                dscotete1.Rows(iposition).Item("CodePostal") = AVBcs(AVBfiditemstub("CP1", AVB + fClient, 0))
                dscotete1.Rows(iposition).Item("Adresse2") = AVBcs(AVBfiditemstub("ADR2", AVB + fClient, 0)).Trim
                dscotete1.Rows(iposition).Item("ville") = AVBcs(AVBfiditemstub("VILLE", AVB + fClient, 0)).Trim
                dscotete1.Rows(iposition).Item("AdresseLiv") = AVBcs(AVBfiditemstub("ADR1", AVB + fClient, 0)).Trim
                dscotete1.Rows(iposition).Item("NomLiv") = AVBcs(AVBfiditemstub("NOM", AVB + fClient, 0)).Trim
                dscotete1.Rows(iposition).Item("VilleLiv") = AVBcs(AVBfiditemstub("VILLE", AVB + fClient, 0)).Trim
                dscotete1.Rows(iposition).Item("ProvinceLiv") = AVBcs(AVBfiditemstub("PROV", AVB + fClient, 0))
                dscotete1.Rows(iposition).Item("Adresse2Liv") = AVBcs(AVBfiditemstub("ADR2", AVB + fClient, 0)).Trim
                dscotete1.Rows(iposition).Item("CodePostalLiv") = AVBcs(AVBfiditemstub("CP1", AVB + fClient, 0))
                dscotete1.Rows(iposition).Item("Telephone") = AVBcs(AVBfiditemstub("TPHONE", AVB + fClient, 0))
                dscotete1.Rows(iposition).Item("fax") = AVBcs(AVBfiditemstub("FAX", AVB + fClient, 0))
            End If
        End If
        lang4 = AVBcs(AVBfiditemstub("LANGUE", AVB + fClient, 0))
        If Trim(AVBcs(AVBfiditemstub("VENDEUR", AVB + fClient, 0))) <> "" Then Txtvendeur.Text = Trim(AVBcs(AVBfiditemstub("VENDEUR", AVB + fClient, 0)))
        If Trim(AVBcs(AVBfiditemstub("COMIS", AVB + fClient, 0))) <> "" Then Tcommis.Text = Trim(AVBcs(AVBfiditemstub("COMIS", AVB + fClient, 0)))
        If BnouveauBT = True Then TxtEscompte.Text = AVBcs(AVBfiditemstub("COOP", AVB + fClient, 0))
        If BnouveauBT = True And Val(AVBcs(AVBfiditemstub("TRANS", AVB + fClient, 0))) <> 0 Then Ttransport.Text = AVBcs(AVBfiditemstub("TRANS", AVB + fClient, 0))
        If Tclient.Text.Trim <> "" And Tclient.Text.Trim <> cash10.Trim Then
            Ouvrenombre(fcotete, 98)
            AVBSTAT = AVBPosn(AVB + 98, Tclient.Text.PadRight(7), 2, "", 0)
            AVBSTAT = AVBread(AVB + 98, 0)
            If AVBSTAT = 0 And Trim(Tclient.Text) = Trim(AVBcs(AVBfiditemstub("NOCLI", AVB + 98, 0))) _
            And Trim(AVBcs(AVBfiditemstub("NOCOM", AVB + 98, 0))) <> Tnocom.Text.Trim Then
                Recherchercommande()
                If trclicom = True Then
                    AVBSTAT = AVBclose(AVB + 98)
                    Exit Sub
                End If
            End If
            AVBSTAT = AVBclose(AVB + 98)
            Ouvrenombre(fqotete, 98)
            AVBSTAT = AVBPosn(AVB + 98, Tclient.Text.PadRight(7), 2, "", 0)
            AVBSTAT = AVBread(AVB + 98, 0)
            If AVBSTAT = 0 And Trim(Tclient.Text) = Trim(AVBcs(AVBfiditemstub("NOCLI", AVB + 98, 0))) Then
                If lang = "F" Then MsgBox("Il y a une soumission " & Trim(AVBcs(AVBfiditemstub("NOCOM", AVB + 98, 0))) & " pour ce client")
                If lang <> "F" Then MsgBox("There is a qote  " & Trim(AVBcs(AVBfiditemstub("NOCOM", AVB + 98, 0))) & " for this client")
            End If
            AVBSTAT = AVBclose(AVB + 98)
        End If
        If BnouveauBT = True And Gestionnocom10 <> "N" Then
            Ouvrebondecommande()
            EnableEcran()
            SolGrid1.Enabled = False
            'Tclient.ReadOnly = True
            'Tunite.ReadOnly = True
            Tnocom.ReadOnly = True
            If ent10 > 1 Then
                Tentrepot.Focus()
            Else
                Tnoachat.Focus()
            End If
            Exit Sub
        End If
        If Tnocom.Text.Trim = "" Then
            Tnocom.Focus()
        Else
            Tnoachat.Focus()
        End If
    End Sub

    Private Sub Tclientliv_Validating(ByVal sender As Object, ByVal e As System.ComponentModel.CancelEventArgs) Handles Tclientliv.Validating
        If Tclientliv.Text.Trim <> "" Then

            AVBSTAT = AVBclose(AVB + 99)
            Ouvrenombre(fClient, 99)
            AVBSTAT = AVBPosn(AVB + 99, Tclientliv.Text.PadRight(7), 1, "", &H100S)
            AVBSTAT = AVBread(AVB + 99, 1)
            If AVBSTAT <> 0 Then
                AVBSTAT = AVBPosn(AVB + 99, Tclientliv.Text, 11, "", &H100S)
                AVBSTAT = AVBread(AVB + 99, 1)
                If AVBSTAT <> 0 Then
                    e.Cancel = True
                    If lang = "F" Then MsgBox("Ce client n'existe pas")
                    If lang <> "F" Then MsgBox("This client does not exist")
                Else
                    'chkclienttelplus(AVBcs(AVBfiditemstub("CLIENT", AVB + fClient, 0)))
                    chkclienttelplusliv(AVBcs(AVBfiditemstub("MOTCLE1", AVB + 99, 0)))
                    Tclientliv.Text = AVBcs(AVBfiditemstub("CLIENT", AVB + 99, 0))
                End If
            End If
            Me.Tnomliv.Text = AVBcs(AVBfiditemstub("NOM", AVB + 99, 0)).Trim
            Me.Tadresse1liv.Text = AVBcs(AVBfiditemstub("ADR1", AVB + 99, 0)).Trim
            Me.Tadresse2liv.Text = AVBcs(AVBfiditemstub("ADR2", AVB + 99, 0)).Trim
            Me.Tvilleliv.Text = AVBcs(AVBfiditemstub("VILLE", AVB + 99, 0)).Trim
            Tprovinceliv.Text = AVBcs(AVBfiditemstub("PROV", AVB + 99, 0))
            Tcodepostalliv.Text = AVBcs(AVBfiditemstub("CP1", AVB + 99, 0))
            Me.Ttelephoneliv.Text = AVBcs(AVBfiditemstub("TPHONE", AVB + 99, 0))
            Me.Tfaxliv.Text = AVBcs(AVBfiditemstub("FAX", AVB + 99, 0))
            'If Trim(Tprovinceliv.Text) = "" Then Tprovinceliv.Text = "QUE"
        End If
        AVBSTAT = AVBclose(AVB + 99)
    End Sub
    Private Sub Tclientliv_Validated(ByVal sender As Object, ByVal e As System.EventArgs) Handles Tclientliv.Validated
        Tnomliv.Enabled = True
        Tadresse1liv.Enabled = True
        Tadresse2liv.Enabled = True
        Tvilleliv.Enabled = True
        Tprovinceliv.Enabled = True
        Tcodepostalliv.Enabled = True
        Tprovinceliv.Enabled = True
        Tnomliv.Focus()
    End Sub
    Private Sub TNoCom_Validating(ByVal sender As Object, ByVal e As System.ComponentModel.CancelEventArgs) Handles Tnocom.Validating
        e.Cancel = chktirait(Tnocom.Text)
    End Sub
    Private Sub Tnocom_TextChanged(ByVal sender As Object, ByVal e As System.EventArgs) Handles Tnocom.TextChanged
        If SolGrid1.Enabled = True Then Exit Sub
        If BTprochain.Pressed = True Then ProcedureProchain()
        If BTfin.Pressed = True Then ProcedureFin()
        If BTprecedent.Pressed = True Then ProcedurePrecedent()
        If BTdebut.Pressed = True Then ProcedureDebut()
    End Sub
    Private Sub Tnocom_Validated(ByVal sender As Object, ByVal e As System.EventArgs) Handles Tnocom.Validated
        If Tnocom.Focused = False Then Exit Sub
        If Tnocom.ReadOnly = False Then
            SNocommande = Tnocom.Text.PadLeft(10)
            Ouvrebondecommande()
        End If
        Me.BtImpSoum.Enabled = True
        If Trim(AVBcs(AVBfiditemstub("LIVRE", AVB + fClient, 0))) = oui10 Then
            Tclientliv.Enabled = True
            Tclientliv.Focus()
        End If

    End Sub
    Private Sub Tnocomrech_Validated(ByVal sender As Object, ByVal e As System.EventArgs) Handles Tnocomrech.Validated
        If Tnocomrech.Text.Trim = "" Then Exit Sub
        trouvcom()
    End Sub
    Private Sub trouvcom()
        If Tnocomrech.Text <> "" Then
            BindEnteteBT()
            Dim sposn As String = Tnocomrech.Text.Trim.PadLeft(10)
            AVBSTAT = AVBPosn(AVB + fcotete, sposn, 1, "", &H100)
            AVBSTAT = AVBread(AVB + fcotete, 1)
            If AVBSTAT <> 0 Then
                If lang = "F" Then MsgBox("Cette commande est inexistante")
                If lang <> "F" Then MsgBox("Can not find this order")
                Tnocomrech.Focus()
                Exit Sub
            End If
            Tnocomrech.Text = AVBcs(AVBfiditemstub("NOCOM", AVB + fcotete, 0)).Trim.PadLeft(10)
            dscomma1.Clear()
            Try
                Dim valeur As Object = Tnocomrech.Text
                bsourceenteteCom.Position = bsourceenteteCom.Find("Nocommande", valeur)
                If Tnocomrech.Text <> Tnocom.Text Then
                    DisableEcran()
                    BindEnteteBT()
                    bsourceenteteCom.Position = bsourceenteteCom.Find("Nocommande", valeur)
                    If Tnocomrech.Text <> Tnocom.Text Then
                        If lang = "F" Then MsgBox("Cette commande est inexistante")
                        If lang <> "F" Then MsgBox("Can not find this order")
                        Tnocomrech.Focus()
                        Exit Sub
                    End If
                End If
                affichebTbinding()
                Tnocomrech.Focus()
            Catch ex As Exception
                DisableEcran()
                MsgBox("Commande inexistante")
                Tnocomrech.Focus()
                Exit Sub
            End Try
            Tnocomrech.Text = ""
        End If
    End Sub
    Private Sub Tajoutdepot_Validated(ByVal sender As Object, ByVal e As System.EventArgs) Handles Tajoutdepot.Validated
        Ouvrenombre(fClient, 99)
        AVBSTAT = AVBPosn(AVB + 99, Tclient.Text.PadRight(7), 1, "", &H100S)
        AVBSTAT = AVBread(AVB + 99, 1)
        If AVBSTAT = 0 Then
            If AVBcs(AVBfiditemstub("TYPEE", AVB + 99, 0)).Trim <> "" Then
                If Mid(AVBcs(AVBfiditemstub("TYPEE", AVB + 99, 0)), 1, 1) = "Z" Then
                    If Val(Tajoutdepot.Text.Trim) <> 0 Then
                        If lang = "F" Then MsgBox("Vous ne pouvez pas ajouter un dépôt pour un client interne")
                        If lang <> "F" Then MsgBox("You can not add a deposit on a work that comes from internal customer")
                        Tajoutdepot.Text = ""
                        Tajoutdepot.Focus()
                        Exit Sub
                    End If
                End If
            End If

        End If
        'If AVBcs(AVBfiditemstub("TYPEE", AVB + fClient, 0)).Trim = "Z" And Val(Tajoutdepot.Text.Trim) <> 0 Then
        '    Tajoutdepot.Text = ""
        '    If lang = "F" Then MsgBox("Vous ne pouvez inscrire de valeur pour ce type de client !")
        '    If lang <> "F" Then MsgBox("You can not put any amount for this type of customer !")
        '    Tajoutdepot.Focus()
        '    Exit Sub
        'End If
        If Tajoutdepot.Text.Trim <> "" And Val(Tajoutdepot.Text) <> 0 Then
            Tajoutdepot.Text = Format((Val(Tajoutdepot.Text)), format8)


            Dim frmque As New FrmEffacer
            If lang = "F" Then frmque.LblMessage.Text = "Est-vous sur de vouloir ajouter un dépôt?"
            If lang <> "F" Then frmque.LblMessage.Text = "Are you sure you want to add a deposit?"
            frmque.ShowDialog()
            If frmque.DialogResult = Windows.Forms.DialogResult.Yes Then
                Dim cDepot As New FrmDepot
                bdepcom = False 'si depot sur bon de travail
                cDepot.TxtNocli.Text = Tclient.Text
                cDepot.TxtNomcli.Text = Tnom.Text
                SNocommande = Tnocom.Text
                cDepot.Tmontant.Text = Tajoutdepot.Text
                ' cDepot.TxtDate.Text = Ddateouverture.Text
                If Gcaisse10 = oui10 And My.Settings.MaCaisse.Trim = "" Then
                    Dim frmca As New FrmCaisseDemande
                    frmca.ShowDialog()
                    If frmca.DialogResult = Windows.Forms.DialogResult.OK Then
                        frmca.Dispose()
                        'frmfact.MdiParent = Me
                    Else
                        Tajoutdepot.Text = ""
                        Tajoutdepot.Focus()
                        Exit Sub
                    End If
                End If
                bdepot = True
                bdebours = False
                bencais = False
                sortedepot = "com"
                cDepot.ShowDialog()
                If cDepot.DialogResult = Windows.Forms.DialogResult.OK Then
                    Tajoutdepot.Text = Ddepotarrondi
                    If darrond <> 0 Then
                        TxtEscompte.Text = darrond * -1
                        LblEscompte.Text = "Escompte/Arrond"
                    End If

                    Dim Ddepot As Double = Val(Me.Tajoutdepot.Text)
                    Sdepot = Format(Ddepot, format10)
                    Tajoutdepot.Text = ""
                    Tdepot.Text = Format((Val(Tdepot.Text) + Ddepot), format8)
                Else
                    Tajoutdepot.Focus()
                End If
            Else
                Tajoutdepot.Text = ""
            End If
            frmque.Dispose()
            If sauvage = False Then
                SolGrid1.Focus()
                Trouvelignefocus()
            End If
        Else
            Tajoutdepot.Text = ""
        End If
        If sauvage = True Then
            Dim cancel As Boolean
            chklim(Tclient.Text, cancel, Tnocom.Text, Val(Ttotal.Text))
            '   If My.Settings.facturepassedu = "O" Then chkpasseduencomptabilite(Tclient.Text, cancel, Tnocom.Text, Val(Ttotal.Text))

            If cancel = True Then
                ProcedureAnnule()
                Exit Sub
            End If
            If reponse = "R" Then
                Tajoutdepot.Focus()
                Exit Sub
            End If
            sauver()
        Else
            If lang = "F" Then MsgBox("Si vous voulez sauver cette commande, faites F5 ou cliquez sur la disquette")
            If lang <> "F" Then MsgBox("If you want to save this order, press F5 or click on the floppy")
            Ttransport.Focus()
            Exit Sub
        End If
        sauvage = False
        If Imprimeouinon = True Then ProcedureImprime()
        Imprimeouinon = False
        Tnocomrech.Focus()
    End Sub

    Private Sub Tcommis_GotFocus(ByVal sender As Object, ByVal e As System.EventArgs) Handles Tentrepot.GotFocus, Tnoachat.GotFocus, Ddateouverture.GotFocus, Ddaterequis.GotFocus, Tcommis.GotFocus, Txtvendeur.GotFocus, TxtTermes.GotFocus, TxtExpediteur.GotFocus, Txtcollect.GotFocus, Txtstatus.GotFocus
        If Tnocom.Text.Trim = "" Then Tnocom.Focus()
    End Sub
    Private Sub Tcommis_Validating(ByVal sender As Object, ByVal e As System.ComponentModel.CancelEventArgs) Handles Tcommis.Validating
        If chkcommis(Tcommis.Text) = True Then
            e.Cancel = True
            Exit Sub
        End If
    End Sub
    Private Sub Tcommis_Validated(ByVal sender As Object, ByVal e As System.EventArgs) Handles Tcommis.Validated
        Btnnapa.Enabled = True
        BtCreation.Enabled = True
        If Bafficheseulement = True Then Exit Sub
        If Trim(Tcommis.Text) <> "" Then
            If chktype("CM", Tcommis.Text.PadRight(15)) = False Then
                Tcommis.Focus()
            Else
                SolGrid1.Enabled = True
                SolGrid1.Focus()
                gridfocus = True
                Trouvelignefocus()
                ToolStrip1.Enabled = True
                SolGrid1.BeginEdit(True)
            End If
        Else
            SolGrid1.Enabled = True
            SolGrid1.Focus()
            ToolStrip1.Enabled = True
            gridfocus = True
            Trouvelignefocus()
            SolGrid1.BeginEdit(True)
        End If
    End Sub
    Private Sub Txtvendeur_Validating(ByVal sender As Object, ByVal e As System.ComponentModel.CancelEventArgs) Handles Txtvendeur.Validating
        If Txtvendeur.Text.Trim = "" And arretvend10 = oui10 Then
            If validaut10 = oui10 Then
                cherchevendeur()
            Else
                If lang = "F" Then MsgBox("Il faut entrer un vendeur")
                If lang <> "F" Then MsgBox("You must enter a Salesman")
                e.Cancel = True
            End If
        End If
    End Sub
    Private Sub cherchevendeur()
        AVBType = "VE"
        Dim rtype As New FrmRechercheType
        rtype.ShowDialog()
        If rtype.DialogResult = System.Windows.Forms.DialogResult.OK Then
            'DSEntetewo.Rows(BSourceEnteteBT.Position).Item("vendeur") = AVBchercheType
            Txtvendeur.Text = Trim(AVBchercheType)
        End If
        rtype.Dispose()
    End Sub
    Private Sub Txtvendeur_Validated(ByVal sender As Object, ByVal e As System.EventArgs) Handles Txtvendeur.Validated
        If promener = True Or Bafficheseulement = True Then Exit Sub
        If Trim(Txtvendeur.Text) <> "" Then
            If chktype("VE", Txtvendeur.Text.PadRight(15)) = False Then Txtvendeur.Focus()
        Else
            If validaut10 = oui10 Then
                cherchevendeur()
                Txtvendeur.Focus()
            End If
        End If
    End Sub
    Private Sub Tentrepot_Validating(ByVal sender As Object, ByVal e As System.ComponentModel.CancelEventArgs) Handles Tentrepot.Validating
        Tentrepot.Text = Tentrepot.Text.Trim.PadLeft(3)
        If chktype("EN", Tentrepot.Text) = False Then
            Tentrepot.Focus()
            e.Cancel = True
        End If
    End Sub
    Private Sub Tentrepot_Validated(ByVal sender As Object, ByVal e As System.EventArgs) Handles Tentrepot.Validated
        'si on change d'entrepot
        If Tentrepot.Text.Trim <> entrepotold.Trim And entrepotold <> "*" And SolGrid1.Rows.Count <> 0 Then
            If SolGrid1.Rows.Count <> 0 And SolGrid1.Rows(0).Cells("produit").ToString.Trim <> "" Then
                For Each ligne As DataGridViewRow In SolGrid1.Rows
                    If ligne.Cells("Produit").EditedFormattedValue.ToString.Trim <> "" Then
                        Updateinventaire(ligne.Cells("Produit").EditedFormattedValue.ToString.PadRight(30), entrepotold.PadLeft(3), -1, 1, Val(ligne.Cells("quantite").EditedFormattedValue), ligne.Cells("um").EditedFormattedValue, False, " ", 0, "")
                        Updateinventaire(ligne.Cells("Produit").EditedFormattedValue.ToString.PadRight(30), Tentrepot.Text.PadLeft(3), 1, 1, Val(ligne.Cells("quantite").EditedFormattedValue), ligne.Cells("um").EditedFormattedValue.ToString, False, " ", 0, "")
                    End If
                Next
            End If
        End If
        entrepotold = Tentrepot.Text
    End Sub
    Private Sub TxtEscompte_Validated(ByVal sender As Object, ByVal e As System.EventArgs) Handles TxtEscompte.Validated
        If AVBcs(AVBfiditemstub("TYPEE", AVB + fClient, 0)).Trim = "Z" And Val(TxtEscompte.Text.Trim) <> 0 Then
            TxtEscompte.Text = ""
            If lang = "F" Then MsgBox("Vous ne pouvez inscrire de valeur pour ce type de client !")
            If lang <> "F" Then MsgBox("You can not put any amount for this type of customer !")
            TxtEscompte.Focus()
            Exit Sub
        End If
        Dim dd As Double = Val(TxtEscompte.Text)
        If Val(Tdepot.Text.Trim) > 0 Then
            If dd > 0.02 And dd < 1 Then
                Dim frmq As New FrmQuestion
                If lang = "F" Then frmq.LblMessage.Text = "Est-ce que la valeur inscrite est un taux d'escompte?"
                If lang <> "F" Then frmq.LblMessage.Text = "Is this a discount rate?"
                frmq.ShowDialog()
                If frmq.DialogResult = Windows.Forms.DialogResult.Yes Then
                    TxtEscompte.Text = Format(Math.Round(Val(Tstotal.Text) * dd, 2, MidpointRounding.AwayFromZero), format7)
                    'les taxes

                End If
            Else
                LblEscompte.Text = "Escompte/Arrond"
            End If

        Else

            If dd > 0 And dd < 1 Then
                Dim frmq As New FrmQuestion
                If lang = "F" Then frmq.LblMessage.Text = "Est-ce que la valeur inscrite est un taux d'escompte?"
                If lang <> "F" Then frmq.LblMessage.Text = "Is this a discount rate?"
                frmq.ShowDialog()
                If frmq.DialogResult = Windows.Forms.DialogResult.Yes Then
                    TxtEscompte.Text = Format(Math.Round(Val(Tstotal.Text) * dd, 2, MidpointRounding.AwayFromZero), format7)
                    'les taxes

                End If
            End If
        End If
        'If dd > 0 And dd < 1 Then
        '    Dim frmq As New FrmQuestion
        '    If lang = "F" Then frmq.LblMessage.Text = "Est-ce que la valeur inscrite est un taux d'escompte?"
        '    If lang <> "F" Then frmq.LblMessage.Text = "Is this a discount rate?"
        '    frmq.ShowDialog()
        '    If frmq.DialogResult = Windows.Forms.DialogResult.Yes Then
        '        TxtEscompte.Text = Format(Math.Round(Val(Tstotal.Text) * dd, 2), format7)
        '        'les taxes

        '    End If
        'End If
        If Val(TxtEscompte.Text) < 1 And Val(TxtEscompte.Text) > 1 Then
            TxtEscompte.Text = Format(Math.Round(Val(TxtEscompte.Text), 2, MidpointRounding.AwayFromZero), format7)
        End If

        CalculegridTotal()
    End Sub
    Private Sub Ttransport_Validated(ByVal sender As Object, ByVal e As System.EventArgs) Handles Ttransport.Validated
        If AVBcs(AVBfiditemstub("TYPEE", AVB + fClient, 0)).Trim = "Z" And Val(Ttransport.Text.Trim) <> 0 Then
            Ttransport.Text = ""
            If lang = "F" Then MsgBox("Vous ne pouvez inscrire de valeur pour ce type de client !")
            If lang <> "F" Then MsgBox("You can't put amount for this customer !")
            Ttransport.Focus()
            Exit Sub
        End If
        Ttransport.Text = (Format(Math.Round(Val(Ttransport.Text), 2, MidpointRounding.AwayFromZero), format7))
        CalculegridTotal()
    End Sub
    Private Sub Tnoachat_Validating(ByVal sender As Object, ByVal e As System.ComponentModel.CancelEventArgs) Handles Tnoachat.Validating
        If AVBcs(AVBfiditemstub("PO", AVB + fClient, 0)) = oui10 And Tnoachat.Text.Trim = "" Then

            If lang = "F" Then MsgBox("Il faut entrer un numéro d'achat")
            If lang <> "F" Then MsgBox("You must enter a purchase order number")
            e.Cancel = True
        ElseIf AVBcs(AVBfiditemstub("PO", AVB + fClient, 0)) = oui10 And Tnoachat.Text.Trim <> "" Then
            Ouvrenombre(fcotete, 98)
            AVBSTAT = AVBPosn(AVB + 98, Tnoachat.Text.Trim.PadRight(30), 9, "", 0)
            AVBSTAT = AVBread(AVB + 98, 0)
            Do While AVBSTAT = 0 And AVBcs(AVBfiditemstub("NOACHAT", AVB + 98, 0)).Trim = Tnoachat.Text.Trim
                If Tclient.Text.Trim = AVBcs(AVBfiditemstub("NOCLI", AVB + 98, 0)).Trim Then
                    If lang = "F" Then MsgBox("No d'achat déja existant pour une commande de ce client  " & AVBcs(AVBfiditemstub("NOCOM", AVB + 98, 0)).Trim)
                    If lang <> "F" Then MsgBox("Purchase Order already exist for this customer " & AVBcs(AVBfiditemstub("NOCOM", AVB + 98, 0)).Trim)
                End If
                AVBSTAT = AVBread(AVB + 98, 0)
            Loop
            AVBSTAT = AVBclose(AVB + 98)


            Ouvrenombre(ffactur, 98)
            AVBSTAT = AVBPosn(AVB + 98, Tnoachat.Text.Trim.PadRight(30), 11, "", 0)
            AVBSTAT = AVBread(AVB + 98, 0)
            Do While AVBSTAT = 0 And AVBcs(AVBfiditemstub("NOACHAT", AVB + 98, 0)).Trim = Tnoachat.Text.Trim
                If Tclient.Text.Trim = AVBcs(AVBfiditemstub("NOCLI", AVB + 98, 0)).Trim Then
                    If lang = "F" Then MsgBox("No d'achat déja existant pour une facture de ce client  " & AVBcs(AVBfiditemstub("NOFACT", AVB + 98, 0)).Trim)
                    If lang <> "F" Then MsgBox("Purchase order already invoice for this customer  " & AVBcs(AVBfiditemstub("NOFACT", AVB + 98, 0)).Trim)

                    Exit Do
                End If
                AVBSTAT = AVBread(AVB + 98, 0)
            Loop
            AVBSTAT = AVBclose(AVB + 98)


        End If
    End Sub
    Private Sub TxtDivers_Validated(ByVal sender As Object, ByVal e As System.EventArgs) Handles TxtDivers.Validated

    End Sub
    Private Sub Tfaxliv_Validated(ByVal sender As Object, ByVal e As System.EventArgs) Handles Tfaxliv.Validated
        If Trim(Tnocom.Text) <> "" Then
            If ent10 <> 0 Then
                Tentrepot.Focus()
            Else
                Tnoachat.Focus()
            End If
        Else
            Tnocom.Focus()
        End If

    End Sub

#End Region
#Region "Double click"
    Private Sub Tnocom_DoubleClick(ByVal sender As Object, ByVal e As System.EventArgs) Handles Tnocom.DoubleClick
        Recherchercommande()
    End Sub
    Private Sub Tentrepot_DoubleClick(ByVal sender As Object, ByVal e As System.EventArgs) Handles Tentrepot.DoubleClick
        If ent10 > 1 Then recherche()
    End Sub
    Private Sub Tclient_DoubleClick(ByVal sender As Object, ByVal e As System.EventArgs) Handles Tclient.DoubleClick
        recherche()
    End Sub
    Private Sub Tclientliv_DoubleClick(ByVal sender As Object, ByVal e As System.EventArgs) Handles Tclientliv.DoubleClick
        recherche()
    End Sub
    Private Sub Tnocomrech_DoubleClick(ByVal sender As Object, ByVal e As System.EventArgs) Handles Tnocomrech.DoubleClick
        Recherchercommande()
    End Sub
    Private Sub TVendeur_DoubleClick(ByVal sender As Object, ByVal e As System.EventArgs)
        recherche()
    End Sub
    Private Sub Tcommis_DoubleClick(ByVal sender As Object, ByVal e As System.EventArgs) Handles Tcommis.DoubleClick
        recherche()
    End Sub
    Private Sub TxtExpediteur_DoubleClick(ByVal sender As Object, ByVal e As System.EventArgs) Handles TxtExpediteur.DoubleClick
        recherche()
    End Sub
    Private Sub TxtTermes_DoubleClick(ByVal sender As Object, ByVal e As System.EventArgs) Handles TxtTermes.DoubleClick
        recherche()
    End Sub
#End Region
#Region "Calcule des montants et Grid"
    Private Sub miseazero()
        Ttotal.Text = "0.0"
        Tstotal.Text = "0.0"
        Ttps.Text = "0.0"
        Ttvq.Text = "0.0"
        Tgtotal.Text = "0.0"
        'Tdepot.Text = "0.0"
        'dscotete1.Rows(lig).Item("total") = 0
        'dscotete1.Rows(lig).Item("taxefederal") = 0
        'dscotete1.Rows(lig).Item("taxeprovincial") = 0
        'dscotete1.Rows(lig).Item("grandtotal") = 0
    End Sub
    Private Sub CalculegridTotal()
        If SolGrid1.Rows.Count <= 0 Then Exit Sub
        If dscotete1.Rows.Count <= 0 Then Exit Sub
        miseazero()
        Dim Itotal As Integer = SolGrid1.Rows.Count
        Dim pointeur As Integer = bsourceenteteCom.Position
        If pointeur = -1 Then
            bsourceenteteCom.Position = bsourceenteteCom.Find("Nocommande", Tnocom.Text)
            pointeur = bsourceenteteCom.Position
        End If
        Tdepot.Text = Format(getdepot(Tnocom.Text, fdepotcf), format9)
        dscotete1.Rows(pointeur).BeginEdit()
        Dim ligne As DataRow = dscotete1.Rows(pointeur)
        Dim Icompteur As Integer = 0
        Dim prod As String
        If SolGrid1.Rows.Count - 1 < 0 Then Exit Sub
        AVBSTAT = AVBPosn(AVB + fClient, Tclient.Text.PadRight(7), 1, "", &H100)
        AVBSTAT = AVBread(AVB + fClient, 1)
        'ligne.Item("COUTT") = 0
        dscotete1.Rows(pointeur).Item("poidt") = 0
        miseazero()
        Do While Icompteur < Itotal
            prod = SolGrid1.Rows(Icompteur).Cells("produit").EditedFormattedValue.ToString
            If Mid(prod, 1, 3) <> Mid(Rem10, 1, 3) _
                And Trim(prod) <> "" Then
                Calculegrid(Icompteur, True, SolGrid1)
                dscotete1.Rows(pointeur).Item("poidt") = Val(dscotete1.Rows(pointeur).Item("poidt").ToString) + Val(dscomma1.Rows(Icompteur).Item("poid").ToString)
                Tstotal.Text = (Val(Tstotal.Text) + Val(SolGrid1.Rows(Icompteur).Cells("Montant").EditedFormattedValue.ToString)).ToString
                Ttps.Text = (Val(Ttps.Text) + Val(SolGrid1.Rows(Icompteur).Cells("Taxe fédéral").EditedFormattedValue)).ToString
                Ttvq.Text = (Val(Ttvq.Text) + Val(SolGrid1.Rows(Icompteur).Cells("Taxe provincial").EditedFormattedValue)).ToString
                If dscotete1.Rows(pointeur).Item("coutt").ToString.Trim = "" Then dscotete1.Rows(pointeur).Item("coutt") = 0
                dscotete1.Rows(pointeur).Item("coutt") = dscotete1.Rows(pointeur).Item("coutt") + Calculecoutant(prod, SolGrid1.Rows(Icompteur).Cells("um").EditedFormattedValue.ToString, Val(SolGrid1.Rows(Icompteur).Cells("quantite").EditedFormattedValue))
            End If

            If SolGrid1.Rows(Icompteur).Cells("sp").Value.ToString.Trim = "S" Then
                SolGrid1.Rows(Icompteur).DefaultCellStyle.BackColor = Color.LightGreen
            End If


            Icompteur = Icompteur + 1
        Loop
        Dim taux As Integer
        'ligne.
        ' ligne.AcceptChanges()
        Dim ttot As Double = Val(Tstotal.Text)
        Dim pouresc As Double
        If ttot <> 0 Then pouresc = Val(TxtEscompte.Text) / ttot
        ttot = Math.Round(ttot, 2, MidpointRounding.AwayFromZero)
        Tstotal.Text = Format(ttot, format8)
        If Val(TxtEscompte.Text.Trim) >= -0.02 And Val(TxtEscompte.Text.Trim) <= 0.02 Then pouresc = 0
        Dim Dtvq As Double = Val(Ttvq.Text) * (1 - pouresc)
        Dim Dtps As Double = Val(Ttps.Text) * (1 - pouresc)

        Dim mtps As Double = Tps(Val(Ttransport.Text), False, taux, fClient, Tclient.Text, Tclientliv.Text)
        Dtps = Dtps + mtps
        Dtvq = Dtvq + Tvq(Val(Ttransport.Text), mtps, prosufed, tauxtvqs, False, fClient)
        'Ttvq.Text = Math.Round(Dtvq, 2)
        'Ttps.Text = Math.Round(Dtps, 2)
        'Ttvq.Text = Format(Val(Ttvq.Text), format7)

        Ttvq.Text = Format(Math.Round(Dtvq, 2, MidpointRounding.AwayFromZero), format7)
        Ttps.Text = Format(Math.Round(Dtps, 2, MidpointRounding.AwayFromZero), format7)



        Dim dtpstest As Double = 0.745
        dtpstest = Math.Round(dtpstest, 2, MidpointRounding.AwayFromZero)


        Dim dtpstest1 As Double = 0.7451
        dtpstest1 = Math.Round(dtpstest1, 2, MidpointRounding.AwayFromZero)

        dscotete1.Rows(pointeur).Item("Total") = Val(Tstotal.Text.Trim)
        Ttotal.Text = Format(Val(Tstotal.Text) + Val(Ttvq.Text) + Val(Ttransport.Text) + Val(Ttps.Text) - Val(TxtEscompte.Text), format11)
        Tgtotal.Text = Format(Val(Ttotal.Text) - Val(Tdepot.Text), format11)
        Dim Dgtot As Double = Val(Tgtotal.Text)
        Tgtotal.Text = Format(Math.Round(Dgtot, 2, MidpointRounding.AwayFromZero), format11)
        Tstotal.Text = Math.Round(Val(Tstotal.Text.Trim), 2, MidpointRounding.AwayFromZero)
        Ttotal.Text = Math.Round(Val(Ttotal.Text.Trim), 2, MidpointRounding.AwayFromZero)
        Tdepot.Text = Format(Val(Tdepot.Text), format11)
        TxtEscompte.Text = Format(Val(TxtEscompte.Text), format7)
        dscotete1.Rows(pointeur).Item("Taxefederal") = Val(Ttps.Text.Trim)
        dscotete1.Rows(pointeur).Item("Taxeprovincial") = Val(Ttvq.Text.Trim)
        dscotete1.Rows(pointeur).Item("GrandTotal") = Val(Tgtotal.Text.Trim)
        'dscotete1.Rows(pointeur).EndEdit()
        'fle SolGrid1.Refresh()
    End Sub
    Private Sub Calculegrid(ByVal Iligne As Integer, ByVal Bcalcule As Boolean, ByVal grid As DataGridView)
        'Bcalcule = true veut dire peut calculer le grid
        If SolGrid1.Rows.Count - 1 < 0 Then Exit Sub
        Dim produit As String = grid.Rows(Iligne).Cells("produit").EditedFormattedValue.ToString
        If Mid(produit, 1, 3) = Mid(Rem10.PadRight(30), 1, 3) Then Exit Sub
        AVBSTAT = AVBPosn(AVB + fInprix, produit, 1, "", 0)
        AVBSTAT = AVBread(AVB + fInprix, 0)
        trouvtauxtaxeprov(Tprovinceliv.Text, prosufed, tauxtvqs)
        If Tnocom.Text.Trim <> "" And Bcalcule = True And Iligne < grid.Rows.Count Then
            If Trim(produit) <> "" Then
                If Trim$(grid.Rows(Iligne).Cells("Prix").Value.ToString) = "" Then grid.Rows(Iligne).Cells("Prix").Value = 0.0
                If Trim$(grid.Rows(Iligne).Cells("quantite").Value.ToString) = "" Then grid.Rows(Iligne).Cells("quantite").Value = 0.0
                If Trim$(grid.Rows(Iligne).Cells("Escompte").Value.ToString) = "" Then grid.Rows(Iligne).Cells("Escompte").Value = 0.0
                Dim prix As Double = Val(grid.Rows(Iligne).Cells("Prix").Value)
                Dim Qte As Double = Val(grid.Rows(Iligne).Cells("quantite").Value)
                Dim facteur As Integer = 1
                If Qte < 0 Then facteur = -1
                If Val(dscomma1.Rows(Iligne).Item("paq_bte")) <> 0 Then Qte = Val(dscomma1.Rows(Iligne).Item("paq_bte")) * facteur
                'If Val(dscomma1.Rows(Iligne).Item("paq_bte")) <> 0 Then Qte = Val(dscomma1.Rows(Iligne).Item("paq_bte"))
                Dim Esc As Double = Val(grid.Rows(Iligne).Cells("Escompte").EditedFormattedValue.ToString)
                grid.Rows(Iligne).Cells("Montant").Value = Format(Calculemontant(produit, grid.Rows(Iligne).Cells("um").FormattedValue.ToString, Qte, prix, Esc), format9)
                Dim Dmontant As Double = Val(grid.Rows(Iligne).Cells("montant").EditedFormattedValue.ToString)
                'arrondissement montant 0412
                Dmontant = Math.Round(Dmontant, 2, MidpointRounding.AwayFromZero)
                grid.Rows(Iligne).Cells("Montant").Value = Dmontant

                Dim taux As Integer
                Dim Dtps As Double = Tps(Dmontant, True, taux, fClient, Tclient.Text, Tclientliv.Text)
                '                Dim Dtps As Double = Math.Round(Tps(Dmontant, True, taux, fClient, Tclient.Text, Tclientliv.Text), 2)

                grid.Rows(Iligne).Cells("Taxe fédéral").Value = Dtps
                Dim dtvq As Double = Tvq(Dmontant, Dtps, prosufed, tauxtvqs, True, fClient)
                grid.Rows(Iligne).Cells("Taxe provincial").Value = dtvq
                'fle Me.SolGrid1.Refresh()
            End If
        End If
    End Sub

#End Region
#Region "Bouton Click "
    Private Sub BTFournis_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles BTFournis.Click
        crfournis(True)
    End Sub
    Private Sub BAjout_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles BAjout.Click
        btajoutcli = True
        ProcedureNouveau()
        'DCompteur = DCompteur + 10
        'NewLigneWO(DCompteur, Tnocom.Text)
        'ReDim quant_old(dscomma1.Rows.Count - 1)
        'Trouvelignefocus()
    End Sub
    Private Sub Beffacer_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Beffacer.Click
        Effaceligne()
        Trouvelignefocus()
    End Sub
    Private Sub Bcatalog_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles BCatalog.Click
        recherchecata()
    End Sub
    Private Sub BInfo_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Binfo.Click
        If promener = True Then Exit Sub
        infoproduit()
    End Sub
    Private Sub BtClientliv_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Btclientliv.Click
        If promener = True Then Exit Sub
        Tclientliv.Focus()
        tbb = Btclientliv
        shclient()
    End Sub


    Private Sub BClient_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles BClient.Click
        If promener = True Then Exit Sub

        Tclient.Focus()
        AVBTrouveclient = Tclient.Text
        Dim frcli As New FrmClient
        frcli.ShowDialog()
        If AVBTrouveclient.Trim <> "!" Then Tclient.Text = AVBTrouveclient
        frcli.Dispose()
        Tclient.Focus()
        If Tnocom.Text.Trim <> "" Then Trouvelignefocus()
    End Sub
    Private Sub shclient()
        Dim frcli As New FrmClient
        frcli.ShowDialog()
        If tbb Is BClient Or tbb Is Tclient Then
            Tclient.Text = AVBTrouveclient
            Tclient.Focus()
        ElseIf tbb Is Btclientliv Or tbb Is Tclientliv Then
            Tclientliv.Text = AVBTrouveclient
            Tclientliv.Focus()
        End If
        AVBTrouveclient = ""
    End Sub
    Private Sub BCommis_Click(ByVal sender As Object, ByVal e As System.EventArgs) Handles BCommis.Click
        AVBType = "CM"
        entree_type()
    End Sub
    Private Sub Bvendeur_Click(ByVal sender As Object, ByVal e As System.EventArgs) Handles Bvendeur.Click
        AVBType = "VE"
        entree_type()
    End Sub
    Private Sub BtFacture_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles BtFacture.Click
        If promener = False Then
            If lang = "F" Then MsgBox("Terminez et sauvez ce bon avant de procéder!")
            If lang <> "F" Then MsgBox("Complete and save this work before proceeding!")
            Exit Sub
        End If
        ' If My.Settings.facturepassedu = "O" Then chkpasseduencomptabilite(Tclient.Text, False, Tnocom.Text, Val(Ttotal.Text))
        SNocommande = Tnocom.Text
        AVBSTAT = AVBPosn(AVB + fcotete, Tnocom.Text.PadLeft(10), 1, "", &H100)
        AVBSTAT = AVBread(AVB + fcotete, 1)
        If AVBSTAT <> 0 Or AVBcs(AVBfiditemstub("NOCOM", AVB + fcotete, 0)).Trim <> Tnocom.Text.Trim Then
            If lang = "F" Then MsgBox("Cette commande n'existe plus")
            If lang <> "F" Then MsgBox("This order does not exist any more")
            Exit Sub
        End If
        If Trim(AVBcs(AVBfiditemstub("GROUPE", AVB + fClient, 0))) = "INTERNE" Then
            If lang = "F" Then MsgBox("Vous ne pouvez pas facturer un client ayant le groupe INTERNE")
            If lang <> "F" Then MsgBox("You can not invoice a client in any INTERNAL groupe")
            Exit Sub
        End If
        If gserie10 = oui10 Then
            SysOpen(fserie)
            Dim str As String
            Dim pasassez As Boolean
            AVBSTAT = AVBPosn(AVB + fcomma, Tnocom.Text.PadLeft(10), 1, "", 0)
            AVBSTAT = AVBread(AVB + fcomma, 0)
            Do While AVBSTAT = 0 And Tnocom.Text.Trim = AVBcs(AVBfiditemstub("NOCOM", AVB + fcomma, 0)).Trim
                str = Tentrepot.Text + AVBcs(AVBfiditemstub("CODE", AVB + fcomma, 0)).PadRight(30)
                AVBSTAT = AVBPosn(AVB + fInven, str, 1, "", &H100)
                AVBSTAT = AVBread(AVB + fInven, 1)
                If AVBcs(AVBfiditemstub("TYPE1", AVB + fInprix, 0)).Trim <> "U" _
                And AVBcs(AVBfiditemstub("SERIAL", AVB + fInven, 0)).Trim = oui10 _
                And Val(AVBcs(AVBfiditemstub("QUANT", AVB + fcomma, 0))) > 0 Then
                    pasassez = verifquantserie(AVBcs(AVBfiditemstub("CODE", AVB + fcomma, 0)), Val(AVBcs(AVBfiditemstub("QUANT", AVB + fcomma, 0))))
                    If pasassez = True Then
                        SysClose(fserie)
                        Exit Sub
                    End If
                End If
                AVBSTAT = AVBread(AVB + fcomma, 0)
            Loop
            SysClose(fserie)
        End If
        Dim newfactwo As New FrmFactureComComplet
        If Gcaisse10 = oui10 And My.Settings.MaCaisse.Trim = "" Then
            Dim frmca As New FrmCaisseDemande
            frmca.ShowDialog()
            If frmca.DialogResult = Windows.Forms.DialogResult.OK Then
                frmca.Dispose()
                newfactwo.ShowDialog()
            End If
        Else
            newfactwo.ShowDialog()
        End If
        BindEnteteBT()
        ProcedureDebut()
    End Sub
    Private Sub BtCreation_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles BtCreation.Click
        creerproduit()
    End Sub
    Private Sub BTsauve_Click(ByVal sender As Object, ByVal e As System.EventArgs) Handles BTsauve.Click
        ProcedureSauve()
    End Sub
    Private Sub BTeffacer_Click(ByVal sender As Object, ByVal e As System.EventArgs) Handles BTeffacer.Click
        effaceentete()
    End Sub
    Private Sub BtIMpSoum_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles BtImpSoum.Click
        Dim trans As New FrmPieceImportExport
        trans.TxtNocom.Text = Tnocom.Text
        trans.TxtClient.Text = Tclient.Text
        trans.TxtSorte.Text = "S"
        trans.ShowDialog()
        If trans.DialogResult = Windows.Forms.DialogResult.OK Then
            Tclient.Text = trans.TxtClient.Text
            AVBSTAT = AVBPosn(AVB + fClient, Tclient.Text.PadRight(7), 1, "", &H100)
            AVBSTAT = AVBread(AVB + fClient, 1)

            affichecdata()
            affichebTbinding()
            Txtvendeur.Text = AVBcs(AVBfiditemstub("VENDEUR", AVB + fcotete, 0)).Trim
            SolGrid1.Focus()
            creernouvligne(True)
        End If
        trans.Dispose()
    End Sub
    Private Sub BtTermes_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles BtTermes.Click
        Dim Nclic As New FrmTermes
        Nclic.ShowDialog()
        Nclic.Dispose()
    End Sub
    Private Sub BtVia_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles BtVia.Click
        AVBType = "EX"
        entree_type()
    End Sub
    Private Sub Bhistorique_Click(ByVal sender As Object, ByVal e As System.EventArgs) Handles Bhistorique.Click
        showhisto()
    End Sub
    Private Sub Binsere_Click(ByVal sender As Object, ByVal e As System.EventArgs) Handles Binsere.Click
        inserer()
    End Sub
    Private Sub Bprofit_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Bprofit.Click
        profit()
    End Sub
    Private Sub btnroute_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles btnroute.Click
        If Trim(AVBcs(AVBfiditemstub("ROU1", AVB + fClient, 0))) <> "" Then
            Dim frmvr As New FrmVoirroute
            frmvr.ShowDialog()
            If frmvr.DialogResult = Windows.Forms.DialogResult.OK Then
                Lblroute.Text = Sroute
                Lblroutedef.Text = "Route : "
                frmvr.Dispose()

                Ouvrenombre(fcotete, 98)
                AVBSTAT = AVBPosn(AVB + 98, Tnocom.Text.PadLeft(10), 1, "", 0)
                AVBSTAT = AVBread(AVB + 98, 0)
                If AVBSTAT = 0 And Trim(AVBcs(AVBfiditemstub("NOCOM", AVB + 98, 0))) = Tnocom.Text.Trim Then
                    AVBfput(Sroute.Trim, "ROUTE", AVB + 98, 0, 0)
                    AVBSTAT = AVBwrite(AVB + 98, 0, 0)
                    AVBSTAT = AVBsecure(AVB + 98)
                End If
                AVBSTAT = AVBclose(AVB + 98)
            End If
        Else
                Lblroute.Text = ""
            Lblroutedef.Text = ""
        End If
    End Sub
    Private Sub BtDepot_Click(ByVal sender As Object, ByVal e As System.EventArgs) Handles BtDepot.Click
        'If Tdepot.Text.Trim = "" Or Val(Tdepot.Text) = 0 Then Exit Sub
        Dim frndp As New FrmShowdepot
        frndp.TxtContrat.Text = Tnocom.Text
        frndp.TxtSorte.Text = fdepotcf.ToString
        frndp.ShowDialog()
        frndp.Dispose()
    End Sub

#End Region
#Region "Bindingnavigator"


    Private Sub BindingNavigator1_ItemClicked(ByVal sender As Object, ByVal e As System.Windows.Forms.ToolStripItemClickedEventArgs) Handles BindingNavigator1.ItemClicked
        With BindingNavigator1
            If Tnocom.Enabled = False Then
                If BTmodifier.Pressed = True Then ProcedureModifier()
                If BTnouveau.Pressed = True Then ProcedureNouveau()
            End If
            If Tnocom.Enabled = True Then
                If BTsauve.Pressed = True Then ProcedureSauve()
                ' If BTeffacer.Pressed = True Then effaceentete()
                If BTannule.Pressed = True Then ProcedureAnnule()
            End If
            If BTimprime.Pressed = True Then ProcedureImprime()


        End With

    End Sub
    Sub ProcedureProchain()
        getentete()
        affichebTbinding()
        '   CalculegridTotal()
    End Sub
    Private Sub getentete()
        If DSCotete.Rows.Count > 0 Or 1 = 1 Then
            If dscotete1.Rows.Count > 0 Then
                Dim pointeur As Integer = bsourceenteteCom.Position
                dscotete1.Rows(pointeur).BeginEdit()
                AVBSTAT = AVBPosn(AVB + fcotete, Tnocom.Text.PadLeft(10), 1, "", &H100)
                AVBSTAT = AVBread(AVB + fcotete, 1)
                renouventetecom(bsourceenteteCom, dscotete1)
                dscotete1.Rows(bsourceenteteCom.Position).EndEdit()
            End If
        End If
    End Sub
    Private Sub BTfin_Click(ByVal sender As Object, ByVal e As System.EventArgs) Handles BTfin.Click
        ProcedureFin()
    End Sub
    Sub ProcedureFin()
        bsourceenteteCom.MoveLast()
        Tnocom.Text = dscotete1.Rows(bsourceenteteCom.Position).Item("nocommande").ToString
        getentete()
        affichebTbinding()
        'CalculegridTotal()
    End Sub
    Sub ProcedurePrecedent()
        getentete()
        affichebTbinding()
        CalculegridTotal()
    End Sub
    Sub ProcedureDebut()
        getentete()
        affichebTbinding()
        CalculegridTotal()
    End Sub

#End Region


    Private Sub BtnMultisite_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles BtnMultisite.Click

        ''If AVBcs(AVBfiditemstub("MAJAUT", AVB + fCompagni, 0)).Trim = "S" Then
        'If ChkInOut() = False Then Exit Sub
        'Dim compteur As Integer = chkform("FrmMultiSite")
        'If compteur <> -1 Then
        '    My.Application.OpenForms.Item(compteur).Select()
        'Else
        '    Dim FrmMultisiteE As New FrmMultiSite()
        '    If SolGrid1.Focused = True Then
        '        FrmMultisiteE.TxtResult.Text = SolGrid1.CurrentRow.Cells("produit").EditedFormattedValue
        '    End If
        '    'Set the Parent Form of the Child window.
        '    'Display the new form.
        '    ClefMemo = "*"
        '    FrmMultisiteE.ShowDialog()
        'End If


        If ChkInOut() = False Then Exit Sub
        Dim compteur As Integer = chkform("FrmMultiSite")
        If compteur <> -1 Then
            My.Application.OpenForms.Item(compteur).Select()
        Else

            Dim FrmMultisiteE As New FrmMultiSite()
            'If SolGrid1.Focused = True Then
            FrmMultisiteE.TxtResult.Text = SolGrid1.CurrentRow.Cells("produit").EditedFormattedValue
            'End If
            'Set the Parent Form of the Child window.
            'Display the new form.
            ClefMemo = "*"
            FrmMultisiteE.ShowDialog()
            If FrmMultisiteE.DialogResult = System.Windows.Forms.DialogResult.OK Then
                SolGrid1.CurrentRow.Cells("produit").Value = FrmMultisiteE.TxtResult.Text.Trim.ToString
                SolGrid1.RefreshEdit()
            End If

        End If



        'End If
    End Sub

    Private Sub btnconnaissement_Click(sender As System.Object, e As System.EventArgs) Handles btnconnaissement.Click
        If Imprimeouinon = False Then

            If impcom.Trim <> "" Then Tnocom.Text = impcom
            ImpSorte = "Bon de connaissement"
            ImpRapport = "connaissement.rpt"
            reponse = "*"
            FormImp(Tnocom.Text.Trim.PadLeft(10))
            'Imprimeouinon = False
            impcom = ""
        Else
            impcom = ""
            Imprimeouinon = False
        End If
    End Sub

   
    Private Sub Btncomfact_Click(sender As Object, e As EventArgs) Handles Btncomfact.Click
        If promener = False Then
            If lang = "F" Then MsgBox("Terminez et sauvez ce bon avant de procéder!")
            If lang <> "F" Then MsgBox("Complete and save this work before proceeding!")
            Exit Sub
        End If
        SNocommande = Tnocom.Text
        AVBSTAT = AVBrunlock(AVB + fcotete)
        AVBSTAT = AVBrunlock(AVB + 98)
        AVBSTAT = AVBPosn(AVB + fcotete, Tnocom.Text.PadLeft(10), 1, "", &H100)
        AVBSTAT = AVBread(AVB + fcotete, 1)
        If AVBSTAT <> 0 Or AVBcs(AVBfiditemstub("NOCOM", AVB + fcotete, 0)).Trim <> Tnocom.Text.Trim Then
            If lang = "F" Then MsgBox("Cette commande n'existe plus")
            If lang <> "F" Then MsgBox("This order does not exist any more")
            Exit Sub
        End If
        BcommandeFacture = True
        Snocommandefacture = Tnocom.Text.PadLeft(10)
        Dim commfact As New FrmFacturePiece
        commfact.ShowDialog()
        BindEnteteBT()
        ProcedureDebut()
    End Sub
    Private Sub Btenvoieoutlook_Click(sender As Object, e As EventArgs) Handles Btenvoieoutlook.Click
        If promener = False Then Exit Sub
        If Tnocom.Text.Trim = "" Then Exit Sub
        Dim frnenvo As New Frmenvoieoutlook
        frnenvo.lblfcommande.Text = fcotete
        frnenvo.Lblclient.Text = Tclient.Text
        frnenvo.ShowDialog()

    End Sub

    Private Sub Btnlocalisateurproduit_Click(sender As Object, e As EventArgs) Handles Btnlocalisateurproduit.Click
        If promener = True Then Exit Sub
        If Tnocom.Text.Trim = "" Then Exit Sub
        Dim frmlocalisateurproduit As New Frmlocalisateurproduit
        frmlocalisateurproduit.Txtprodlocatordeb.Text = SolGrid1.CurrentRow.Cells("produit").EditedFormattedValue
        frmlocalisateurproduit.ShowDialog()

    End Sub
    Private Sub InitializeConnection()
        'Dim DataProvider As IOlapDataProvider = Nothing
        'Dim basicHttpBinding As System.ServiceModel.Channels.Binding = New BasicHttpBinding(BasicHttpSecurityMode.None With {.MaxReceivedMessageSize = 2147483647})

        ''Address for Basic HTTP binding in corresponding Web configuration file

        'Dim address As EndpointAddress = New EndpointAddress(New Uri(app.Current.Host.Source & "../../../../OlapManager.svc/basic"))

        'Dim clientChannel As ChannelFactory(Of IOlapDataProvider) = New ChannelFactory(Of IOlapDataProvider)(basicHttpBinding, address)

        'DataProvider = clientChannel.CreateChannel()

    End Sub



    Private Sub Btnnapa_Click(sender As Object, e As EventArgs) Handles Btnnapa.Click
        If My.Settings.napaurl.Trim = "" Then Exit Sub

        Dim Frmnapa As New Frmcommandenapa
        Frmnapa.Svinnapa = ""
        Frmnapa.ShowDialog()
        Dim dgvPartsretour As DataGridView = New DataGridView
        dgvPartsretour.DataSource = partsretour

        If dgvPartsretour.Rows.Count < 0 Then Exit Sub

        For Each ligne As DataRow In partsretour.Rows
            If Trim(ligne.Item("PartNumber").ToString) <> "" Then


                Dim nvligne As Integer

                Dim prodtemp As String = ligne.Item("LineCode").ToString & ligne.Item("PartNumber").ToString
                prodtemp = prodtemp.Trim.PadRight(30)
                adligne()
                nvligne = SolGrid1.Rows.Count - 1

                AVBSTAT = AVBPosn(AVB + fInprix, prodtemp, 1, "", &H100)
                AVBSTAT = AVBread(AVB + fInprix, 1)
                If AVBSTAT <> 0 Then
                    'creer le produit
                    Creerproduitnapa(prodtemp, ligne.Item("Description").ToString.ToUpper, "PCS", ligne.Item("ListPrice").ToString, ligne.Item("Cost").ToString, "", ligne.Item("PartNumber").ToString.Trim, ligne.Item("LineCode").ToString)
                Else
                    Creerproduitnapaexistant(prodtemp, ligne.Item("Description").ToString.ToUpper, "PCS", ligne.Item("ListPrice").ToString, ligne.Item("Cost").ToString, "", ligne.Item("PartNumber").ToString.Trim, ligne.Item("LineCode").ToString)

                End If
                SolGrid1.Rows(nvligne).Cells("produit").Value = prodtemp
                dscomma1.Rows(nvligne).Item("client") = Tclient.Text
                completeproduit(nvligne)
                'SolGrid1.Rows(nvligne).Cells("quantite").Value = Val(ligne.Item("Quantity").ToString)
                SolGrid1.Rows(nvligne).Cells("quantite").Value = Val(ligne.Item("QACMD").ToString)
                um_old(nvligne) = AVBcs(AVBfiditemstub("PAR", AVB + fInprix, 0))
                SolGrid1.Rows(nvligne).Cells("UM").Value = AVBcs(AVBfiditemstub("PAR", AVB + fInprix, 0))
                'quant_old(nvligne) = Val(ligne.Item("Quantity").ToString)
                quant_old(nvligne) = Val(ligne.Item("QACMD").ToString)
                prod_old(nvligne) = prodtemp
                dscomma1.Rows(nvligne).Item("datelivre") = Ddaterequis.Text

                SolGrid1.Rows(nvligne).Cells("Description").Value = ligne.Item("Description").ToString.ToUpper


                SolGrid1.Rows(nvligne).Cells("Prix").Value = ligne.Item("ListPrice").ToString
                SolGrid1.Rows(nvligne).Cells("Escompte").Value = 0

                SolGrid1.RefreshEdit()
                ' quant_old(nvligne) = Val(ligne.Item("Quantity").ToString)
                quant_old(nvligne) = Val(ligne.Item("QACMD").ToString)
                Calculegrid(SolGrid1.Rows(nvligne).Index, True, SolGrid1)
                Updateinventaire(SolGrid1.Rows(nvligne).Cells("Produit").EditedFormattedValue.ToString, Tentrepot.Text.PadLeft(3), 1, 1, Val(SolGrid1.Rows(nvligne).Cells("quantite").EditedFormattedValue.ToString), SolGrid1.Rows(nvligne).Cells("um").EditedFormattedValue.ToString, False, " ", 0, "")
                SolGrid1.Rows(nvligne).Cells("status").Value = "A"

                AVBrclear(AVB + fcomma)
                AVBfput(Tnocom.Text.ToString.PadLeft(10), "NOCOM", AVB + fcomma, 0, 0)
                AVBfput(DCompteur, "FICHE", AVB + fcomma, 0, 0)

                AVBfput(prodtemp, "CODE", AVB + fcomma, 0, 0)
                AVBfput(ligne.Item("Description").ToString, "DESC", AVB + fcomma, 0, 0)
                AVBfput(AVBcs(AVBfiditemstub("PAR", AVB + fInprix, 0)), "TYPE", AVB + fcomma, 0, 0)
                AVBfput(SolGrid1.Rows(nvligne).Cells("Quantite").ToString, "QUANT", AVB + fcomma, 0, 0)

                AVBfput(SolGrid1.Rows(nvligne).Cells("Prix").ToString, "UNIT", AVB + fcomma, 0, 0)
                AVBfput(AVBcs(AVBfiditemstub("POSTC", AVB + fInprix, 0)), "DEPT", AVB + fcomma, 0, 0)
                AVBfput(Txtvendeur.Text.Trim, "VENDEUR", AVB + fcomma, 0, 0)
                AVBfput(SolGrid1.Rows(nvligne).Cells("Montant").Value, "MONTANT", AVB + fcomma, 0, 0)
                AVBfput(ligne.Item("Cost").ToString, "COUT", AVB + fcomma, 0, 0)
                AVBfput(SolGrid1.Rows(nvligne).Cells("Escompte").ToString, "ESC", AVB + fcomma, 0, 0)
                AVBfput(dscomma1.Rows(nvligne).Item("Taxeprovincial").ToString, "TAXEPR", AVB + fcomma, 0, 0)
                AVBfput(dscomma1.Rows(nvligne).Item("Taxefederal").ToString, "TAXEFE", AVB + fcomma, 0, 0)
                AVBfput(dscomma1.Rows(nvligne).Item("Taxff").ToString, "TAXFF", AVB + fcomma, 0, 0)
                AVBfput(dscomma1.Rows(nvligne).Item("Taxpp").ToString, "TAXPP", AVB + fcomma, 0, 0)

                AVBfput(Tclient.Text.Trim, "NOCLI", AVB + fcomma, 0, 0)
                AVBfput(SolGrid1.Rows(nvligne).Cells("UM").ToString, "PAR", AVB + fcomma, 0, 0)


                AVBfput(SolGrid1.Rows(nvligne).Cells("Quantite").ToString, "QUANTL", AVB + fcomma, 0, 0)
                AVBfput(dscomma1.Rows(nvligne).Item("Fournisseur").ToString, "FOURN", AVB + fcomma, 0, 0)
                AVBfput(dscomma1.Rows(nvligne).Item("Status").ToString, "STATUS", AVB + fcomma, 0, 0)
                AVBfput(dscomma1.Rows(nvligne).Item("ref").ToString, "REF", AVB + fcomma, 0, 0)
                AVBfput(dscomma1.Rows(nvligne).Item("lot").ToString, "LOT", AVB + fcomma, 0, 0)
                AVBfput(dscomma1.Rows(nvligne).Item("Datecommande").ToString, "DATEC", AVB + fcomma, 0, 0)
                AVBfput(dscomma1.Rows(nvligne).Item("Datelivre").ToString, "DATEL", AVB + fcomma, 0, 0)
                AVBfput(dscomma1.Rows(nvligne).Item("PosteVente").ToString, "POSTVTE", AVB + fcomma, 0, 0)
                AVBfput(ouinon(dscomma1.Rows(nvligne).Item("CoreOui").ToString), "OUICORE", AVB + fcomma, 0, 0)
                AVBfput(dscomma1.Rows(nvligne).Item("loc1").ToString, "LOC1", AVB + fcomma, 0, 0)
                AVBfput(dscomma1.Rows(nvligne).Item("poid").ToString, "POID", AVB + fcomma, 0, 0)
                AVBfput(dscomma1.Rows(nvligne).Item("taux").ToString, "TAUX", AVB + fcomma, 0, 0)
                AVBfput(dscomma1.Rows(nvligne).Item("umx").ToString, "UMX", AVB + fcomma, 0, 0)
                AVBfput(dscomma1.Rows(nvligne).Item("mult2").ToString, "MULT2", AVB + fcomma, 0, 0)
                AVBfput(dscomma1.Rows(nvligne).Item("div2").ToString, "DIV2", AVB + fcomma, 0, 0)
                AVBfput(dscomma1.Rows(nvligne).Item("territoire").ToString, "TER", AVB + fcomma, 0, 0)
                AVBfput(dscomma1.Rows(nvligne).Item("poidv").ToString, "POIDV", AVB + fcomma, 0, 0)
                AVBfput("", "PAQ_BTE", AVB + fcomma, 0, 0)
                AVBfput(dscomma1.Rows(nvligne).Item("couleur").ToString, "COULEUR", AVB + fcomma, 0, 0)
                AVBfput(dscomma1.Rows(nvligne).Item("sp").ToString, "SP", AVB + fcomma, 0, 0)
                AVBSTAT = AVBwrite(AVB + fcomma, 0, 0)
                AVBSTAT = AVBsecure(AVB + fcomma)
            End If

        Next
        creernouvligne(True)
        CalculegridTotal()
        'Exit Sub
        gencommande()
    End Sub

    Private Sub gencommande()
        'verification si existe deja une commande pour ce fournisseur
        Ouvrenombre(ffotete, 98)
        Ouvrenombre(ffomma, 99)
        Dim ajout As Boolean
        Dim prosufed As Boolean
        Dim tauxtvqs As Double
        Dim cout As Double = 0
        Dim dtps As Double
        Dim Dtvq As Double
        Dim dcompteur As Integer = 10000
        AVBSTAT = AVBPosn(AVB + fFournis, My.Settings.codefournapa.Trim.PadRight(7), 1, "", 0)
        AVBSTAT = AVBread(AVB + fFournis, 0)
        If AVBSTAT <> 0 Then
            MsgBox("Fournisseur napa inexistant- impossible de créer la commande fournisseur " & My.Settings.codefournapa.Trim.PadRight(7))
            Exit Sub
        End If
        Dim lang4 As String = AVBcs(AVBfiditemstub("LANGUE", AVB + fFournis, 0))
        Dim fnocom As String = ""

        If fnocom.Trim = "" Then
            Donnernocom(5, 98, fnocom)
        End If


        AVBSTAT = AVBrclear(AVB + 99)

        AVBSTAT = AVBrclear(AVB + 98)
        AVBfput(fnocom, "NOCOM", AVB + 98, 0, 0)
        AVBfput("   ", "ENTREPOT", AVB + 98, 0, 0)
        AVBfput("", "NOACHAT", AVB + 98, 0, 0)
        AVBfput(Mid(Today.Date, 1, 10), "DATEC", AVB + 98, 0, 0)
        AVBfput(Mid(Today.Date, 1, 10), "DATEL", AVB + 98, 0, 0)
        AVBfput(Mid(Today.Date, 1, 10), "DTA", AVB + 98, 0, 0)
        AVBfput(AVBcs(AVBfiditemstub("VENDEUR", AVB + fFournis, 0)), "VENDEUR", AVB + 98, 0, 0)
        'AVBfput(dsFotete.Rows(Iposition).Item("collect").ToString, "COLLECT", AVB + 98, 0, 0)
        AVBfput("R", "STAT", AVB + 98, 0, 0)
            AVBfput(AVBcs(AVBfiditemstub("COMIS", AVB + fFournis, 0)), "COMMIS", AVB + 98, 0, 0)
            AVBfput("0", "DEPOT", AVB + 98, 0, 0)
        AVBfput(My.Settings.codefournapa.Trim.PadRight(7), "NOCLI", AVB + 98, 0, 0)
        AVBfput(AVBcs(AVBfiditemstub("ADR1", AVB + fFournis, 0)), "ADR1", AVB + 98, 0, 0)
        AVBfput(AVBcs(AVBfiditemstub("PROV", AVB + fFournis, 0)), "PROV", AVB + 98, 0, 0)
            AVBfput(AVBcs(AVBfiditemstub("CP1", AVB + fFournis, 0)), "CP1", AVB + 98, 0, 0)
            AVBfput(AVBcs(AVBfiditemstub("ADR2", AVB + fFournis, 0)), "ADR2", AVB + 98, 0, 0)
            AVBfput(AVBcs(AVBfiditemstub("VILLE", AVB + fFournis, 0)), "VILLE", AVB + 98, 0, 0)
            AVBfput(AVBcs(AVBfiditemstub("ADR1", AVB + fCompagni, 0)), "ADR1L", AVB + 98, 0, 0)
            AVBfput(AVBcs(AVBfiditemstub("NOM", AVB + fFournis, 0)), "NOM", AVB + 98, 0, 0)
        AVBfput(AVBcs(AVBfiditemstub("COMPAGNIE", AVB + fCompagni, 0)), "NOML", AVB + 98, 0, 0)
        AVBfput(AVBcs(AVBfiditemstub("NOCLIF", AVB + fFournis, 0)), "NOCLIL", AVB + 98, 0, 0)
            AVBfput(AVBcs(AVBfiditemstub("VILLE", AVB + fCompagni, 0)), "VILLEL", AVB + 98, 0, 0)
            AVBfput(AVBcs(AVBfiditemstub("PROVINCE", AVB + fCompagni, 0)), "PROVL", AVB + 98, 0, 0)
        AVBfput(AVBcs(AVBfiditemstub("ADR2", AVB + fCompagni, 0)), "ADR2L", AVB + 98, 0, 0)
        AVBfput(AVBcs(AVBfiditemstub("CP", AVB + fCompagni, 0)), "CP1L", AVB + 98, 0, 0)
            AVBfput(AVBcs(AVBfiditemstub("EXPEDIE", AVB + fFournis, 0)), "EXPEDIE", AVB + 98, 0, 0)
        AVBfput(AVBcs(AVBfiditemstub("TERMES", AVB + fFournis, 0)), "TERMES", AVB + 98, 0, 0)
        AVBfput("1000", "FICHE", AVB + 98, 0, 0)
            AVBfput("1000", "FIN", AVB + 98, 0, 0)
            AVBfput(AVBcs(AVBfiditemstub("TPHONE", AVB + fCompagni, 0)), "TPHONECIE", AVB + 98, 0, 0)
            AVBfput(AVBcs(AVBfiditemstub("FAX", AVB + fCompagni, 0)), "FAXCIE", AVB + 98, 0, 0)
        AVBfput(Txtvendeur.Text, "VENDEUR", AVB + 98, 0, 0)
        'AVBfput(dsFotete.Rows(Iposition).Item("email").ToString, "EMAIL", AVB + 98, 0, 0)
        Dim montant As Double = 0
        Dim poids As Double = 0
        Dim depot As Double = 0
        Dim total As Double = 0
        Dim taxfed As Double = 0
        Dim taxprov As Double = 0
        Dim gtotal As Double = 0
        Dim poidt As Double = 0
        Dim couttt As Double = 0
        For Each ligne As DataRow In partsretour.Rows
            If Trim(ligne.Item("PartNumber").ToString) <> "" Then


                Dim prod As String = ligne.Item("LineCode").ToString & ligne.Item("PartNumber").ToString
                prod = prod.Trim.PadRight(30)
                AVBSTAT = AVBPosn(AVB + fInprix, prod, 1, "", &H100)
                AVBSTAT = AVBread(AVB + fInprix, 1)
                AVBSTAT = AVBPosn(AVB + fInven, Tentrepot.Text.PadLeft(3) + prod, 1, "", &H100)
                AVBSTAT = AVBread(AVB + fInven, 1)
                AVBfput(fnocom.PadLeft(10), "NOCOM", AVB + 99, 0, 0)
                AVBfput(dcompteur, "FICHE", AVB + 99, 0, 0)

                AVBfput(prod.PadRight(30), "CODE", AVB + 99, 0, 0)
                Dim indexfour As Integer = indicefournis(My.Settings.codefournapa.Trim.PadRight(7))
                Dim umx As Integer = TrouveUm(prod, "PCS")
                Dim dd As String = AVBcs(AVBfiditemstub("DESCR", AVB + fInprix, 0))
                If lang4 <> "F" And AVBcs(AVBfiditemstub("DESCR", AVB + fInprix, 0)).Trim <> "" Then dd = AVBcs(AVBfiditemstub("DESCA", AVB + fInprix, 0))
                If indexfour >= 0 Then
                    Dim descfo As String = AVBcs(AVBfiditemstub("DESCF0", AVB + fInprix, indexfour))
                    If descfo.Trim <> "" Then dd = descfo
                    Dim prfour As String = AVBcs(AVBfiditemstub("PRODFOUR", AVB + fInprix, indexfour))
                    If prfour.Trim <> "" Then AVBfput(prfour, "PRODFOUR", AVB + 99, 0, 0)
                End If
                dd = AVBcs(AVBfiditemstub("DESCR", AVB + fInprix, 0))
                AVBfput(dd, "DESC", AVB + 99, 0, 0)
                AVBfput(AVBcs(AVBfiditemstub("TYPE", AVB + fInprix, 0)), "TYPE", AVB + 99, 0, 0)
                Dim dept As String = "1"
                If AVBcs(AVBfiditemstub("DEPT", AVB + fCompagni, 0)) = oui10 Then
                    If Trim(AVBcs(AVBfiditemstub("POSTCA", AVB + fInprix, 0))) <> "" Then
                        dept = AVBcs(AVBfiditemstub("POSTCA", AVB + fInprix, 0))
                    End If
                    If Mid(AVBcs(AVBfiditemstub("MON", AVB + fFournis, 0)), 1, 1) <> "C" _
                    And Trim(AVBcs(AVBfiditemstub("POSTUA", AVB + fInprix, 0))) <> "" Then
                        dept = AVBcs(AVBfiditemstub("POSTUA", AVB + fInprix, 0))
                    End If
                End If
                AVBfput(dept, "DEPT", AVB + 99, 0, 0)
                AVBfput(Tnocom.Text, "REF", AVB + 99, 0, 0)
                AVBfput(dcompteur, "LIGNEREF", AVB + 99, 0, 0)
                AVBfput(AVBcs(AVBfiditemstub("COUT", AVB + fInprix, 0)), "COUT", AVB + 99, 0, 0)
                AVBfput("0", "ESC", AVB + 99, 0, 0)
                Dim taxff As String = "0"
                If Trim(AVBcs(AVBfiditemstub("TAXFED", AVB + fInprix, 0))) = "X" Then taxff = "2"
                If Trim(AVBcs(AVBfiditemstub("TAXFED", AVB + fInprix, 0))) = "N" Then taxff = "1"
                Dim taxpp As String = "0"
                If Trim(AVBcs(AVBfiditemstub("TAXPRO", AVB + fInprix, 0))) = oui10 _
                    Or Trim(AVBcs(AVBfiditemstub("TAXPRO", AVB + fInprix, 0))) = "P" Then taxpp = "1"
                If Trim(AVBcs(AVBfiditemstub("TAXPRO", AVB + fInprix, 0))) = "S" Then taxpp = "2"
                AVBfput(taxff, "TAXFF", AVB + 99, 0, 0)
                AVBfput(taxpp, "TAXPP", AVB + 99, 0, 0)
                AVBfput(My.Settings.codefournapa.Trim.PadRight(7), "NOCLI", AVB + 99, 0, 0)
                AVBfput("PCS", "PAR", AVB + 99, 0, 0)
                AVBfput("0", "QUANTL", AVB + 99, 0, 0)

                AVBfput(My.Settings.codefournapa.Trim.PadRight(7), "FOURN", AVB + 99, 0, 0)
                Dim stat As String = ""
                If Mid(AVBcs(AVBfiditemstub("TYPE", AVB + fInprix, 0)), 1, 3) = Mid(AVBcs(AVBfiditemstub("MO", AVB + fCompagni, 0)), 1, 3) Then
                    stat = "I"
                End If
                If stat.Trim = "" Then stat = "C"
                If Mid(AVBcs(AVBfiditemstub("INVENTAIRE", AVB + fInven, 0)), 1, 1) <> oui10 _
                 And stat <> "I" _
                 And stat <> "D" Then
                    stat = "S"
                End If
                AVBfput(stat, "STATUS", AVB + 99, 0, 0)
                AVBfput(Mid(Today.Date.ToString, 1, 10), "DATEC", AVB + 99, 0, 0)
                AVBfput(Mid(Today.Date, 1, 10), "DATEL", AVB + 99, 0, 0)
                AVBfput(dept, "POSTVTE", AVB + 99, 0, 0)
                AVBfput("N", "OUICORE", AVB + 99, 0, 0)
                AVBfput(AVBcs(AVBfiditemstub("LOCAT", AVB + fInven, 0)), "LOC1", AVB + 99, 0, 0)
                Dim taux As String = AVBcs(AVBfiditemstub("TXF", AVB + fInprix, 0))
                If Val(AVBcs(AVBfiditemstub("TAUX", AVB + fFournis, 0))) <> 0 Then
                    taux = AVBcs(AVBfiditemstub("TAUX", AVB + fFournis, 0))
                End If
                AVBfput(taux, "TAUX", AVB + 99, 0, 0)
                AVBfput(umx, "UMX", AVB + 99, 0, 0)
                AVBfput(AVBcs(AVBfiditemstub("MULT2", AVB + fInprix, umx)), "MULT2", AVB + 99, 0, 0)
                AVBfput(AVBcs(AVBfiditemstub("DIV2", AVB + fInprix, umx)), "DIV2", AVB + 99, 0, 0)
                Dim qt As Double = Val(ligne.Item("QACMD").ToString)
                'If Val(AVBcs(AVBfiditemstub("MULT2", AVB + fInprix, umx))) <> 1 Then qt = Int(Val(TxtQuantite.Text) / Val(AVBcs(AVBfiditemstub("MULT2", AVB + fInprix, umx))) + 0.5)
                AVBfput(Tclient.Text, "CLIECOM", AVB + 99, 0, 0)
                AVBfput(qt.ToString, "QUANT", AVB + 99, 0, 0)
                'Prixspéciaux(TxtUm.Text, TxtFournis.Text.PadRight(7), prod, 0, 0, False, True, 0, False, "")
                Dim prix As String = ""
                prix = Val(ligne.Item("Cost").ToString.Trim)
                AVBfput(prix, "UNIT", AVB + 99, 0, 0)

                montant = prix * (qt / Val(AVBcs(AVBfiditemstub("DIV2", AVB + fInprix, umx))))
                poids = Val(AVBcs(AVBfiditemstub("POID", AVB + fInprix, umx))) * qt
                AVBfput(poids.ToString, "POID", AVB + 99, 0, 0)
                Dim prov As String = AVBcs(AVBfiditemstub("PROVL", AVB + 98, 0))
                trouvtauxtaxeprov(prov, prosufed, tauxtvqs)
                dtps = Tps(montant, True, 1, fFournis, "", "")
                Dtvq = Tvq(montant, dtps, prosufed, tauxtvqs, True, fFournis)
                AVBfput(Format(montant, Masque_Coutant), "MONTANT", AVB + 99, 0, 0)
                total = total + montant
                AVBfput(Dtvq.ToString, "TAXEPR", AVB + 99, 0, 0)
                AVBfput(dtps.ToString, "TAXEFE", AVB + 99, 0, 0)
                Updateinventaire(prod, "   ", 1, 3, qt, "PCS", False, Mid(Today.Date, 1, 10), 0, "")
                AVBSTAT = AVBwrite(AVB + 99, 0, 0)
                AVBSTAT = AVBsecure(AVB + 99)
                dcompteur = dcompteur + 10
            End If
        Next

        'Dim coutt As Double = Calculecoutant(prod, TxtUm.Text, qt)
        '**********************************


        couttt = total
        AVBfput(couttt.ToString, "COUTT", AVB + 98, 0, 0)
        poidt = poidt + poids
        AVBfput(poidt.ToString, "POIDT", AVB + 98, 0, 0)
        total = total + montant
        AVBfput(Format(total, Masque_Coutant), "TOTAL", AVB + 98, 0, 0)
        taxfed = taxfed + dtps
        AVBfput(taxfed.ToString, "TAXEF", AVB + 98, 0, 0)
        taxprov = taxprov + Dtvq
        AVBfput(taxprov.ToString, "TAXE", AVB + 98, 0, 0)
        gtotal = total + taxprov + taxfed - depot
        AVBfput(gtotal.ToString, "GTOTAL", AVB + 98, 0, 0)

        AVBSTAT = AVBwrite(AVB + 98, 0, 0)
        AVBSTAT = AVBsecure(AVB + 98)
        AVBSTAT = AVBrunlock(AVB + 98)
        AVBSTAT = AVBclose(AVB + 99)
        AVBSTAT = AVBclose(AVB + 98)

        imprime(fnocom)
        If ajout = False Then
            If lang = "F" Then MsgBox("Création complétée")
            If lang <> "F" Then MsgBox("Created")
        Else
            If lang = "F" Then MsgBox("Ajout complété")
            If lang <> "F" Then MsgBox("Added")
        End If
    End Sub
    Private Sub imprime(ByVal commande As String)
        Dim frq As New FrmQuestion
        If lang = "F" Then frq.LblMessage.Text = "Voulez-vous imprimer cette commande fournisseur?"
        If lang <> "F" Then frq.LblMessage.Text = "Do you want to print this supplier order?"
        frq.ShowDialog()
        If frq.DialogResult = Windows.Forms.DialogResult.Yes Then
            SysOpen(ffotete)
            SysOpen(ffomma)
            ImpSorte = "Bon de commande fournisseur"
            ImpRapport = "repcomf.rpt"
            reponse = "*"
            FormImp(commande)
            SysClose(ffotete)
            SysClose(ffomma)
        End If
    End Sub

    Private Sub Btnmajdesprix_Click(sender As Object, e As EventArgs) Handles Btnmajdesprix.Click
        MajDesPrix()
        ProcedureModifier()
        'BindEnteteBT()
        'affichebTbinding()


        'trouvcom()
        'CalculegridTotal()
    End Sub
    Private Sub MajDesPrix()
        Ouvrenombre(fcomma, 502)
        Ouvrenombre(fcotete, 503)
        AVBSTAT = AVBPosn(AVB + 502, Tnocom.Text.PadLeft(10), 1, "", 0)
        AVBSTAT = AVBread(AVB + 502, 0)
        AVBSTAT = AVBPosn(AVB + 503, Tnocom.Text.PadLeft(10), 1, "", 0)
        AVBSTAT = AVBread(AVB + 503, 0)
        Dim Dqte As Double
        Do While AVBcs(AVBfiditemstub("NOCOM", AVB + 503, 0)) = AVBcs(AVBfiditemstub("NOCOM", AVB + 502, 0)) And AVBSTAT = 0
            Dim saffiche As String = AVBcs(AVBfiditemstub("CODE", AVB + 502, 0)) & AVBcs(AVBfiditemstub("NOCOM", AVB + 502, 0))
            'If Mid(AVBcs(AVBfiditemstub("CODE", AVB + 502, 0)), 1, 3) <> Mid(Rem10, 1, 3) And Mid(AVBcs(AVBfiditemstub("CODE", AVB + 502, 0)), 1, 3) <> Mid(AVBcs(AVBfiditemstub("D", AVB + fCompagni, 0)), 1, 3) Then
            If Mid(AVBcs(AVBfiditemstub("CODE", AVB + 502, 0)), 1, 3) <> Mid(Rem10, 1, 3) And Mid(AVBcs(AVBfiditemstub("CODE", AVB + 502, 0)), 1, 3) <> Mid(AVBcs(AVBfiditemstub("D", AVB + fCompagni, 0)), 1, 3) Then
                AVBSTAT = AVBPosn(AVB + fInprix, AVBcs(AVBfiditemstub("CODE", AVB + 502, 0)), 1, "", &H100)
                AVBSTAT = AVBread(AVB + fInprix, 0)
                If AVBcs(AVBfiditemstub("ACTIF", AVB + fInprix, 0)) <> AVBcs(AVBfiditemstub("OUI", AVB + fCompagni, 0)) Then
                    MsgBox("Attention, le produit " & AVBcs(AVBfiditemstub("CAT", AVB + fInprix, 0)).Trim)
                End If
                Dqte = Val(AVBcs(AVBfiditemstub("QUANT", AVB + 502, 0)))
                Dim jdate As String = ""
                If Ddateouverture.Text > AVBcs(AVBfiditemstub("DATE", AVB + fCompagni, 0)) Then jdate = Ddateouverture.Text
                If Tclientliv.Text.Trim <> Tclient.Text.Trim Then
                    Prixspéciaux(AVBcs(AVBfiditemstub("PAR", AVB + 502, 0)).ToString, Tclientliv.Text.PadRight(7), AVBcs(AVBfiditemstub("CODE", AVB + 502, 0)).ToString, 0, 0, False, False, Dqte, False, jdate)
                Else
                    Prixspéciaux(AVBcs(AVBfiditemstub("PAR", AVB + 502, 0)).ToString, Tclient.Text.PadRight(7), AVBcs(AVBfiditemstub("CODE", AVB + 502, 0)).ToString, 0, 0, False, False, Dqte, False, jdate)
                End If

                AVBfput(Format(DresultPrixPS, Masque_Vendant), "UNIT", AVB + 502, 0, 0)
                AVBfput(Format(DresultEscPs, Masque_Vendant), "ESC", AVB + 502, 0, 0)

            End If
            'preparation calcul  de taxe
            If Mid(AVBcs(AVBfiditemstub("CODE", AVB + 502, 0)), 1, 3) <> Mid(Rem10, 1, 3) Then

                Dim Dmontant As Double = DresultPrixPS * Dqte
                Dmontant = Format(Calculemontant(AVBcs(AVBfiditemstub("CODE", AVB + 502, 0)).ToString, AVBcs(AVBfiditemstub("PAR", AVB + 502, 0)).ToString, Dqte, DresultPrixPS, DresultEscPs), format9)
                AVBfput(Format(Dmontant, Masque_Vendant), "MONTANT", AVB + 502, 0, 0)
                Dim Dtaxefed As Double = 0
                Dim Dtaxeprov As Double = 0
                Dim Dtotal As Double = 0
                Dim Dgtotal As Double = 0
                Dim taux As Integer
                Dim Dtps As Double = Tps(Dmontant, True, taux, fClient, Tclient.Text, Tclientliv.Text)
                'la federale
                AVBfput(Dtps.ToString, "TAXEFE", AVB + 502, 0, 0)
                Dtaxefed = Dtaxefed + Dtps
                'la provinciale
                Dim Dtvq As Double
                Dtvq = Tvq(Dmontant, Dtps, prosufed, tauxtvqs, True, fClient)
                AVBfput(Dtvq.ToString, "TAXEPR", AVB + 502, 0, 0)
                Dtaxeprov = Dtaxeprov + Dtvq

                Dtotal = Dtotal + Val(AVBcs(AVBfiditemstub("MONTANT", AVB + 502, 0)))
                Dgtotal = Dtotal + Dtaxeprov + Dtaxefed
                AVBfput(Dtotal.ToString, "TAXEFE", AVB + 502, 0, 0)

            End If
            AVBwrite(AVB + 502, 0, 0)
            AVBsecure(AVB + 502)

            AVBSTAT = AVBread(AVB + 502, 0)
        Loop
        AVBSTAT = AVBclose(AVB + 502)
        AVBSTAT = AVBclose(AVB + 503)
    End Sub

    Private Sub Btnbarcodeauto_Click(sender As Object, e As EventArgs) Handles Btnbarcodeauto.Click
        scanauto()

    End Sub

    Sub scanauto()
        If ActiverBarcodeautomatique = False Then
            ActiverBarcodeautomatique = True
            Btnbarcodeauto.BackColor = Color.PaleGreen

        Else
            ActiverBarcodeautomatique = False
            Btnbarcodeauto.BackColor = Color.LightGray

        End If
        SolGrid1.Focus()
    End Sub

    Private Sub Txtvendeur_DoubleClick(sender As Object, e As EventArgs) Handles Txtvendeur.DoubleClick
        recherche()
    End Sub

    Private Sub TxtTermes_Validated(sender As Object, e As EventArgs) Handles TxtTermes.Validated
        Dim ok As Boolean
        If Trim(TxtTermes.Text) = "" Then
            If lang = "F" Then MsgBox("Ce champ ne peut être vide")
            If lang <> "F" Then MsgBox("This field can not be empty")
            TxtTermes.Focus()
            Exit Sub
        End If
        chktermes(ok)
    End Sub
    Private Sub chktermes(ByRef ok As Boolean)
        SysOpen(ftermes)
        Dim str As String
        Dim stat As Integer
        str = Mid(TxtTermes.Text + "  ", 1, 2)
        stat = AVBPosn(AVB + ftermes, str, 1, "", &H100S)
        If AVBread(AVB + ftermes, 0) <> 0 Or stat <> 0 Then
            If lang = "F" Then MsgBox("Ces termes n'existent pas")
            If lang <> "F" Then MsgBox("These terms do not exist")
            TxtTermes.Focus()
            ok = True
        End If
        SysClose(ftermes)
    End Sub
End Class