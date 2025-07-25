# 📋 PRD - Système de Gestion Intégré des Documents Commerciaux SEI Lite

## 🎯 **Vue d'Ensemble du Projet**

### **Objectif Principal**
Développer un système complet de gestion des documents commerciaux permettant de gérer le cycle de vie complet des transactions : Soumissions → Commandes → Factures pour quatre types de modules spécialisés.

### **Modules Cibles**
- **Standard** : Commandes/Factures normales (sans suffixe)
- **WO** : Bons de travail (Work Orders)
- **VE** : Contrats de vente (Vente)
- **LO** : Contrats de location (Location)

---

## 📊 **Architecture de Base de Données**

### **Structure des Tables par Module**

#### **1. Tables d'En-têtes (Headers)**
```sql
-- Tables principales d'en-tête par module
QUOTETE      -- Soumissions standard
QUOTETEWO    -- Soumissions bons de travail
QUOTETEVE    -- Soumissions contrats de vente
QUOTETELO    -- Soumissions location

COTETE       -- Commandes standard
COTETEWO     -- Commandes bons de travail
COTETEVE     -- Commandes contrats de vente
COTETELO     -- Commandes location

FACTUR       -- Factures standard
FACTWO     -- Factures bons de travail
FACTVE     -- Factures contrats de vente
FACTURLO     -- Factures location
```

#### **2. Tables de Lignes (Details)**
```sql
-- Tables de détails par module
QOMMA        -- Lignes soumissions standard
QOMMAWO      -- Lignes soumissions WO
QOMMAVE      -- Lignes soumissions VE
QOMMALO      -- Lignes soumissions LO

COMMA        -- Lignes commandes standard
COMMAWO      -- Lignes commandes WO
COMMAVE      -- Lignes commandes VE
COMMALO      -- Lignes commandes LO

LIGNE        -- Lignes factures standard
LIGNEWO      -- Lignes factures WO
LIGNEVE      -- Lignes factures VE
LIGNELO      -- Lignes factures LO
```

---

## 🗂️ **Modèles de Données Détaillés**

### **A. QUOTETE (En-tête Soumissions) - Toutes Variantes**

| Champ | Type | Taille | Description | Obligatoire |
|-------|------|--------|-------------|-------------|
| `id` | int | - | Clé primaire auto-incrémentée | ✅ |
| `NOSOUM` | varchar | 15 | Numéro de soumission unique | ✅ |
| `STAT` | varchar | 1 | Statut (A=Acceptée, R=Refusée, P=Pending) | ✅ |
| `NOCLI` | varchar | 7 | Code client | ✅ |
| `NOCLIL` | varchar | 7 | Code client livraison | ❌ |
| `NOM` | varchar | 80 | Nom client facturation | ✅ |
| `NOML` | varchar | 80 | Nom client livraison | ❌ |
| `ADR1` | varchar | 60 | Adresse 1 facturation | ❌ |
| `ADR2` | varchar | 60 | Adresse 2 facturation | ❌ |
| `ADR1L` | varchar | 60 | Adresse 1 livraison | ❌ |
| `ADR2L` | varchar | 60 | Adresse 2 livraison | ❌ |
| `VILLE` | varchar | 60 | Ville facturation | ❌ |
| `VILLEL` | varchar | 30 | Ville livraison | ❌ |
| `PROV` | varchar | 3 | Province facturation | ❌ |
| `PROVL` | varchar | 3 | Province livraison | ❌ |
| `CP1` | varchar | 15 | Code postal facturation | ❌ |
| `CP1L` | varchar | 15 | Code postal livraison | ❌ |
| `TELCON` | varchar | 20 | Téléphone contact | ❌ |
| `TPHONECIE` | varchar | 20 | Téléphone compagnie | ❌ |
| `FAXCIE` | varchar | 20 | Fax compagnie | ❌ |
| `DATEC` | varchar | 10 | Date création | ✅ |
| `DATEL` | varchar | 10 | Date livraison prévue | ❌ |
| `DATEEXP` | varchar | 10 | Date expiration soumission | ✅ |
| `VENDEUR` | varchar | 15 | Code vendeur | ✅ |
| `COMIS` | varchar | 15 | Commission vendeur | ❌ |
| `DEPOT` | varchar | 10 | Dépôt/Magasin | ✅ |
| `TERMES` | varchar | 15 | Termes de paiement | ❌ |
| `TRANS` | varchar | 10 | Transporteur | ❌ |
| `TOTAL` | decimal | 12,2 | Total avant taxes | ✅ |
| `TAXE` | decimal | 11,2 | Montant TPS | ❌ |
| `TAXEF` | decimal | 11,2 | Montant TVQ | ❌ |
| `ESC` | decimal | 8,2 | Escompte % | ❌ |
| `COUTT` | decimal | 10,2 | Coût total | ❌ |
| `POIDT` | decimal | 8,2 | Poids total | ❌ |
| `COLLECT` | varchar | 1 | Collecte (O/N) | ❌ |
| `BO` | varchar | 1 | Back order autorisé (O/N) | ❌ |
| `IMP` | varchar | 1 | Déjà imprimé (O/N) | ❌ |
| `FICHE` | varchar | 5 | Numéro de fiche | ❌ |
| `NOACHAT` | varchar | 30 | Numéro bon d'achat client | ❌ |
| `REMD` | varchar | 62 | Remarques/Notes | ❌ |
| `DIV` | varchar | 10 | Division | ❌ |
| `FIN` | decimal | 8,2 | Financement | ❌ |

### **Champs Spécifiques par Module**

#### **QUOTETEWO (Bons de Travail)**
| Champ Additionnel | Type | Description |
|-------------------|------|-------------|
| `TYPETRAV` | varchar(20) | Type de travail (Réparation, Maintenance, etc.) |
| `PRIORITE` | varchar(1) | Priorité (1=Urgent, 2=Normal, 3=Bas) |
| `DATEPREV` | varchar(10) | Date prévue début travaux |
| `DUREEEST` | decimal(5,2) | Durée estimée (heures) |
| `TECHNICIEN` | varchar(15) | Technicien assigné |
| `NOUNITE` | varchar(20) | Numéro d'unité/équipement |

#### **QUOTETEVE (Contrats de Vente)**
| Champ Additionnel | Type | Description |
|-------------------|------|-------------|
| `TYPECONTRAT` | varchar(20) | Type contrat (Vente, Lease-achat, etc.) |
| `DUREECONT` | int | Durée contrat (mois) |
| `TAUXFIN` | decimal(5,3) | Taux financement % |
| `ACOMPTE` | decimal(10,2) | Acompte requis |
| `MENSUALITE` | decimal(10,2) | Paiement mensuel |
| `DATELIVEST` | varchar(10) | Date livraison estimée |

#### **QUOTETELO (Location)**
| Champ Additionnel | Type | Description |
|-------------------|------|-------------|
| `TYPELOC` | varchar(20) | Type location (Court/Long terme) |
| `DATEDEB` | varchar(10) | Date début location |
| `DATEFIN` | varchar(10) | Date fin location |
| `TAUXJOUR` | decimal(8,2) | Taux journalier |
| `TAUXSEM` | decimal(8,2) | Taux hebdomadaire |
| `TAUXMOIS` | decimal(8,2) | Taux mensuel |
| `CAUTION` | decimal(10,2) | Dépôt de garantie |
| `KMINCL` | int | Kilomètres inclus |
| `TAUXKM` | decimal(4,2) | Taux par km additionnel |

---

### **B. QOMMA (Lignes Soumissions) - Toutes Variantes**

| Champ | Type | Taille | Description | Obligatoire |
|-------|------|--------|-------------|-------------|
| `id` | int | - | Clé primaire auto-incrémentée | ✅ |
| `NOSOUM` | varchar | 15 | Référence à l'en-tête | ✅ |
| `LIGNE` | int | - | Numéro de ligne | ✅ |
| `CODE` | varchar | 30 | Code produit/service | ✅ |
| `DESC` | varchar | 60 | Description détaillée | ✅ |
| `QUANT` | decimal | 8,3 | Quantité | ✅ |
| `UNIT` | varchar | 10 | Unité de mesure | ❌ |
| `COUT` | decimal | 10,4 | Coût unitaire | ❌ |
| `TAUX` | decimal | 8,4 | Prix de vente unitaire | ✅ |
| `MONTANT` | decimal | 13,2 | Montant ligne (Qté × Prix) | ✅ |
| `ESC` | decimal | 8,2 | Escompte ligne % | ❌ |
| `TAXPP` | varchar | 1 | Taxable TPS (O/N) | ❌ |
| `TAXFF` | varchar | 1 | Taxable TVQ (O/N) | ❌ |
| `TAXEPR` | decimal | 11,2 | Montant TPS calculé | ❌ |
| `TAXEFE` | decimal | 11,2 | Montant TVQ calculé | ❌ |
| `FOURN` | varchar | 7 | Code fournisseur | ❌ |
| `STATUS` | varchar | 1 | Statut ligne (A=Active, S=Suspendue) | ❌ |
| `TYPE` | varchar | 15 | Type d'item (Produit, Service, etc.) | ❌ |
| `PAR` | varchar | 20 | Paramètre/Unité packaging | ❌ |
| `DEPT` | varchar | 2 | Département | ❌ |
| `DIV2` | varchar | 12 | Division secondaire | ❌ |
| `MULT2` | decimal | 12,4 | Multiplicateur | ❌ |
| `UMX` | varchar | 1 | Unité de mesure étendue | ❌ |
| `QUANTL` | decimal | 7,3 | Quantité livrée | ❌ |
| `DATEL` | varchar | 10 | Date livraison prévue | ❌ |
| `LOC1` | varchar | 10 | Localisation/Rack | ❌ |
| `IMPK` | varchar | 1 | Impression spéciale (O/N) | ❌ |
| `SP` | varchar | 1 | Spécial (O/N) | ❌ |

### **Champs Spécifiques par Module - Lignes**

#### **QOMMAWO (Lignes Bons de Travail)**
| Champ Additionnel | Type | Description |
|-------------------|------|-------------|
| `HEUREEST` | decimal(5,2) | Heures estimées |
| `HEUREREEL` | decimal(5,2) | Heures réelles |
| `TAUXHEURE` | decimal(8,2) | Taux horaire |
| `COMPETENCE` | varchar(20) | Compétence requise |

#### **QOMMAVE (Lignes Contrats de Vente)**
| Champ Additionnel | Type | Description |
|-------------------|------|-------------|
| `GARANTIE` | int | Période garantie (mois) |
| `INSTALLATION` | varchar(1) | Installation incluse (O/N) |
| `FORMATION` | varchar(1) | Formation incluse (O/N) |

#### **QOMMALO (Lignes Location)**
| Champ Additionnel | Type | Description |
|-------------------|------|-------------|
| `DURELOC` | int | Durée location (jours) |
| `ETATDEPART` | varchar(50) | État équipement départ |
| `ETATRETOUR` | varchar(50) | État équipement retour |

---

## 🔄 **Workflow et États des Documents**

### **Cycle de Vie des Documents**
```
SOUMISSION → COMMANDE → FACTURE
     ↓           ↓         ↓
  [États]    [États]   [États]
```

### **États Soumissions (STAT)**
- `P` : En préparation
- `E` : Envoyée au client
- `A` : Acceptée par le client
- `R` : Refusée par le client
- `X` : Expirée
- `C` : Convertie en commande

### **États Commandes (STAT)**
- `O` : Ouverte
- `P` : En production/préparation
- `R` : Prête à expédier
- `L` : Livrée partiellement
- `F` : Fermée/Complétée
- `A` : Annulée
- `H` : En attente (Hold)

### **États Factures (STAT)**
- `O` : Ouverte
- `E` : Envoyée
- `P` : Payée partiellement
- `F` : Payée complètement
- `R` : En retard
- `C` : Annulée

---

## 🖥️ **Interface Utilisateur - Spécifications**

### **A. Fenêtre Principale**

#### **Toolbar Navigation (BindingNavigator)**
```
[Nouveau] [Modifier] | [Annuler] [Effacer] [Sauver] | [Imprimer] [Email] | 
[Premier] [Précédent] [Position] de [Total] [Suivant] [Dernier] | [Aide]
```

#### **Toolbar Actions Spécialisées**
```
ToolStrip1: [Ajouter Ligne] [Insérer] [Effacer Ligne] [Info Produit] [Catalogue] [Historique] [Substituts]
ToolStrip2: [Impr. Soumission] [Convertir Facture] [Trier Produits] [Connaissement] [Feuille Route]
ToolStrip3: [Termes Paiement]
ToolStrip4: [Via/Transporteur]
ToolStrip5: [Client]
ToolStripProfit: [Calcul Profit] [Multi-sites] [Fournisseurs] [Création Produit] [Localisateur] [NAPA]
ToolStrip9: [Dépôt/Magasin]
```

### **B. Sections de l'Interface**

#### **1. Section En-tête (Header)**
```
┌─ Informations Document ─────────────────────────────┐
│ N° Document: [_______] Date: [__/__/____]           │
│ Statut: [____] Type: [____]                         │
│ Vendeur: [_______] Commission: [____] Dépôt: [____] │
│ Date Requise: [__/__/____] N° Achat Client: [____]  │
└─────────────────────────────────────────────────────┘
```

#### **2. Section Client**
```
┌─ Client Facturation ──────────┬─ Client Livraison ──────────┐
│ Client: [_____] [Recherche]   │ Client: [_____] [Recherche]  │
│ Nom: [________________]       │ Nom: [________________]      │
│ Adresse 1: [______________]   │ Adresse 1: [______________]  │
│ Adresse 2: [______________]   │ Adresse 2: [______________]  │
│ Ville: [____________]         │ Ville: [____________]        │
│ Province: [__] CP: [______]   │ Province: [__] CP: [______]  │
│ Tél: [____________]           │ Tél: [____________]          │
│ Fax: [____________]           │ Fax: [____________]          │
└───────────────────────────────┴──────────────────────────────┘
```

#### **3. Section Lignes (Grid)**
```
┌─ Détails des Lignes ────────────────────────────────────────────────┐
│ Code│Description    │Qté │U/M│Prix Unit│Esc%│Montant │Taxes│Statut  │
├─────┼───────────────┼────┼───┼─────────┼────┼────────┼─────┼────────┤
│     │               │    │   │         │    │        │     │        │
│     │               │    │   │         │    │        │     │        │
└─────────────────────────────────────────────────────────────────────┘
```

#### **4. Onglets Informationnels**
```
[Produit] [Client/Totaux]

Onglet Produit:
- Localisation, Disponible
- Quantités: En main, En commande, Attendu
- Prix par niveau (1-5)
- Fournisseur, Département

Onglet Totaux:
- Sous-total, Escompte, Transport
- TPS, TVQ, Total
- Termes, Collecte, Statut
```

### **C. Sections Spécialisées par Module**

#### **Module WO (Bons de Travail)**
```
┌─ Informations Travail ──────────────────────────────┐
│ Type Travail: [____________] Priorité: [_]          │
│ N° Unité: [__________] Technicien: [__________]     │
│ Date Prévue: [__/__/____] Durée Est.: [____] hrs   │
│ État: [En cours] [Complété] [En attente]            │
└─────────────────────────────────────────────────────┘
```

#### **Module VE (Contrats de Vente)**
```
┌─ Informations Financement ──────────────────────────┐
│ Type Contrat: [____________] Durée: [__] mois       │
│ Taux: [___._]% Acompte: [_______] $                 │
│ Mensualité: [_______] $ Date Livraison: [__/__/__] │
│ Approbation Crédit: [Pending] [Approuvé] [Refusé]  │
└─────────────────────────────────────────────────────┘
```

#### **Module LO (Location)**
```
┌─ Informations Location ─────────────────────────────┐
│ Type: [_____________] Début: [__/__/____]           │
│ Fin: [__/__/____] Caution: [_______] $             │
│ Taux: Jour[____] Semaine[____] Mois[____] $        │
│ KM Inclus: [_____] Taux/KM: [____] $/km            │
└─────────────────────────────────────────────────────┘
```

---

## ⚙️ **Fonctionnalités Avancées**

### **A. Gestion des Conversions**
```
SOUMISSION --[Accepter]--> COMMANDE --[Livrer]--> FACTURE
     │                          │                     │
     └─[Dupliquer]              └─[Back Order]        └─[Crédit Note]
```

### **B. Calculs Automatiques**
1. **Montants Lignes** : Quantité × Prix × (1 - Escompte%)
2. **Taxes** : Selon configuration par province
3. **Totaux** : Somme + Transport + Taxes
4. **Profits** : Prix vente - Coût × Quantité
5. **Commissions** : Total × Taux commission vendeur

### **C. Validations Métier**
1. **Stock Disponible** : Vérification avant confirmation
2. **Limites Crédit** : Contrôle crédit client
3. **Prix Minimums** : Respect des prix coûtants
4. **Approbations** : Workflow selon montants
5. **Séquencement** : Numérotation automatique

### **D. Intégrations**
1. **Inventaire** : Réservation/Allocation stock
2. **Comptabilité** : Écritures automatiques
3. **CRM** : Historique client complet
4. **Expédition** : Génération docs transport
5. **Achats** : Commandes fournisseurs automatiques

---

## 📊 **Rapports et Analyses**

### **A. Rapports Standard**
1. **Soumissions**
   - En attente de réponse
   - Taux de conversion
   - Analyse par vendeur/période

2. **Commandes**
   - En cours de traitement
   - Retards de livraison
   - Back orders

3. **Factures**
   - Comptes receivables
   - Analyses de vente
   - Marges et profits

### **B. Rapports Spécialisés par Module**

#### **WO (Bons de Travail)**
- Temps réel vs estimé
- Rentabilité par type travail
- Performance techniciens
- Équipements les plus réparés

#### **VE (Contrats de Vente)**
- Portfolio de contrats
- Échéanciers de paiements
- Analyses de financement
- Taux d'approbation crédit

#### **LO (Location)**
- Utilisation de la flotte
- Revenus par équipement
- Analyses saisonnières
- Retours et damages

---

## 🔐 **Sécurité et Permissions**

### **Niveaux d'Accès**
1. **Lecture Seule** : Consultation uniquement
2. **Commis** : Création/modification limitée
3. **Vendeur** : Gestion documents clients assignés
4. **Superviseur** : Approbations et overrides
5. **Manager** : Accès complet + configuration
6. **Admin** : Accès système + maintenance

### **Contrôles Spécifiques**
- **Modification prix** : Selon niveau utilisateur
- **Annulation documents** : Approbation requise
- **Accès autres vendeurs** : Restriction possible
- **Escomptes maximums** : Limites par rôle
- **Impression duplicatas** : Traçabilité

---

## 🚀 **Phases d'Implémentation**

### **Phase 1 : Foundation (2-3 mois)**
- Modèles de données et migrations
- Interface de base (CRUD)
- Module standard (sans suffixe)
- Validations essentielles

### **Phase 2 : Modules Spécialisés (2 mois)**
- Implémentation WO, VE, LO
- Interfaces spécialisées
- Workflows spécifiques
- Tests d'intégration

### **Phase 3 : Avancées (2 mois)**
- Conversions automatiques
- Rapports et analyses
- Intégrations externes
- Optimisations performance

### **Phase 4 : Production (1 mois)**
- Migration données legacy
- Formation utilisateurs
- Support et maintenance
- Améliorations continues

---

## 📝 **Critères d'Acceptation**

### **Fonctionnels**
- ✅ Gestion complète des 4 modules
- ✅ Conversions Soumission→Commande→Facture
- ✅ Calculs automatiques corrects
- ✅ Interfaces intuitives et ergonomiques
- ✅ Rapports complets et précis

### **Techniques**
- ✅ Performance < 2 sec pour operations courantes
- ✅ Support 100+ utilisateurs concurrents
- ✅ Sauvegardes automatiques
- ✅ Compatibilité multi-navigateurs
- ✅ Responsive design mobile

### **Métier**
- ✅ Respect règles d'affaires
- ✅ Intégration systèmes existants
- ✅ Formation équipe complétée
- ✅ Migration données validée
- ✅ Support utilisateur opérationnel

---

**🎯 Résultat Attendu** : Un système complet, robuste et évolutif permettant de gérer efficacement tous les types de documents commerciaux avec des interfaces adaptées aux besoins spécifiques de chaque module métier.
