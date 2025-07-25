# 📋 Module Gestion Documents Commerciaux - SEILite

## 🎯 Vue d'Ensemble

Ce module de gestion des documents commerciaux permet de gérer le cycle de vie complet des transactions commerciales : **Soumissions → Commandes → Factures** pour quatre types de modules spécialisés.

## 🗂️ Structure du Module

### 📁 Fichiers Créés

#### **Templates HTML**
- `templates/documents/liste.html` - Interface de liste des documents avec filtres et actions
- `templates/documents/detail.html` - Vue détaillée d'un document avec onglets
- `templates/documents/formulaire.html` - Formulaire de saisie/édition des documents

#### **Routes et Logique Métier**
- `documents_routes.py` - Routes Flask et logique métier du module

#### **Assets (CSS/JS)**
- `static/css/documents.css` - Styles spécifiques au module documents
- `static/js/documents.js` - JavaScript pour interactions et calculs

#### **Documentation**
- `templates/documents/PRD_GESTION_DOCUMENTS_COMPLEXE.md` - Spécifications détaillées
- `README_DOCUMENTS.md` - Ce fichier de documentation

## 🔧 Modules Supportés

### **PI - Pièces détachées** 🔧
- **Soumission pièces** : Devis pour pièces de rechange
- **Commande pièces** : Commandes de pièces détachées
- **Facture pièces** : Facturation des pièces livrées

### **WO - Bons de travail** 🛠️
- **Soumission travail** : Devis pour interventions techniques
- **Ordre de travail** : Planification et suivi des interventions
- **Facture travail** : Facturation de la main d'œuvre et matériaux

### **LO - Location** 📅
- **Soumission location** : Devis pour location d'équipements
- **Contrat location** : Gestion des contrats de location
- **Facture location** : Facturation des périodes de location

### **VE - Vente équipement** 🤝
- **Soumission vente** : Propositions commerciales
- **Commande vente** : Commandes d'équipements neufs
- **Facture vente** : Facturation des ventes

## 🚀 Fonctionnalités Principales

### ✨ Gestion des Documents
- **Création** de nouveaux documents par module/type
- **Modification** des documents en brouillon
- **Consultation** détaillée avec navigation par onglets
- **Duplication** pour créer des documents similaires
- **Conversion** automatique (Soumission → Commande → Facture)

### 🔍 Recherche et Filtrage
- Filtres par **module**, **type**, **statut** et **période**
- Recherche par **numéro**, **client** ou **référence**
- **Pagination** et **tri** des résultats
- **Statistiques** en temps réel

### 💰 Calculs Automatiques
- **Totaux des lignes** avec remises individuelles
- **Remise globale** configurable
- **Calcul TVA** selon taux configuré
- **Totaux TTC** automatiques
- **Gestion multi-devises** (prévu)

### 👥 Gestion Clients
- **Recherche client** en temps réel
- **Auto-complétion** des coordonnées
- **Facturation/Livraison** séparées
- **Historique client** intégré

### 📦 Gestion Produits/Services
- **Catalogue produits** intégré
- **Recherche par code** avec auto-complétion
- **Prix automatiques** selon barème
- **Gestion stock** (si disponible)

## 🎨 Interface Utilisateur

### 🖥️ Page Liste
- **Tableau responsive** avec actions contextuelles
- **Sélecteur de module** avec compteurs
- **Filtres avancés** pliables
- **Actions groupées** (impression, export)
- **Modal de création** rapide

### 📋 Page Détail
- **En-tête informatif** avec badges de statut
- **Navigation par onglets** :
  - **Général** : Informations de base
  - **Lignes** : Détail des lignes du document
  - **Totaux** : Récapitulatif financier
  - **Planification** : Dates et ressources (WO/LO)
  - **Contrat** : Informations contractuelles (VE)
  - **Historique** : Timeline des modifications
- **Actions contextuelles** selon statut et type

### ✏️ Page Formulaire
- **Formulaire adaptatif** selon le module sélectionné
- **Sections spécialisées** :
  - Informations générales
  - Données module-spécifiques (WO/LO/VE)
  - Gestion des lignes avec tableau éditable
  - Informations client avec recherche
  - Calculs en temps réel
- **Validation côté client** et serveur
- **Sauvegarde automatique** (prévu)

## 📊 États et Workflow

### 🔄 Cycle de Vie
```
BROUILLON → CONFIRME → EN_COURS → TERMINE
     ↓         ↓          ↓         ↓
  [Modifier] [Convertir] [Suivre] [Facturer]
```

### 🏷️ Statuts Disponibles
- **BROUILLON** : Document en cours de rédaction
- **CONFIRME** : Document validé et envoyé
- **EN_COURS** : Document en traitement (WO/LO)
- **TERMINE** : Document complètement traité
- **ANNULE** : Document annulé
- **FACTURE** : Document facturé (pour COM)

## 🔧 Configuration Technique

### 📋 Prérequis
- **Flask** 2.x avec blueprints
- **Bootstrap** 5.x pour l'interface
- **jQuery** 3.x pour les interactions
- **Font Awesome** 6.x pour les icônes
- **DataTables** pour les tableaux avancés

### 🗄️ Base de Données
Le module utilise la structure de tables existante du système legacy :
- Tables d'**en-têtes** : `QUOTETE[XX]`, `COTETE[XX]`, `FACTUR[XX]`
- Tables de **lignes** : `QOMMA[XX]`, `COMMA[XX]`, `LIGNE[XX]`
- Suffixes : *(vide)* = Standard, **WO** = Travail, **LO** = Location, **VE** = Vente

### 🔌 Intégration
Le module s'intègre dans l'application principale via :
```python
# Dans app.py
def init_documents_module():
    from documents_routes import register_documents_routes
    register_documents_routes(app)
```

## 🌐 URLs et Routes

### 📍 Routes Principales
- `/documents/` - Liste des documents
- `/documents/detail/<id>` - Détail d'un document
- `/documents/nouveau/<module>/<type>` - Nouveau document
- `/documents/modifier/<id>` - Modifier un document

### 🔄 Actions AJAX
- `/documents/sauvegarder` - Sauvegarde de document
- `/documents/convertir/<id>` - Conversion de document
- `/documents/api/clients/rechercher` - Recherche de clients
- `/documents/api/produits/rechercher` - Recherche de produits

## 🎯 Utilisation

### 🆕 Créer un Nouveau Document
1. Cliquer sur **"Documents"** dans le menu
2. Sélectionner le **module** et **type** souhaité
3. Cliquer sur **"Nouveau"** ou utiliser le dropdown
4. Remplir les informations requises
5. Ajouter les lignes de détail
6. **Sauvegarder** ou **Confirmer**

### 🔍 Rechercher un Document
1. Utiliser les **filtres** en haut de la liste
2. Sélectionner **module**, **type**, **statut**
3. Définir une **période** si nécessaire
4. Les résultats se mettent à jour automatiquement

### ✏️ Modifier un Document
1. Localiser le document dans la liste
2. Cliquer sur l'icône **"Modifier"** 
3. Effectuer les modifications nécessaires
4. **Sauvegarder** les changements

### 🔄 Convertir un Document
1. Ouvrir le **détail** du document
2. Cliquer sur **"Actions" → "Convertir"**
3. Confirmer la date de conversion
4. Le nouveau document est créé automatiquement

## 🐛 Dépannage

### ❌ Problèmes Courants

**Erreur de sauvegarde**
- Vérifier que tous les champs obligatoires sont remplis
- S'assurer que le client est sélectionné
- Contrôler que les lignes ont des quantités et prix valides

**Calculs incorrects**
- Actualiser la page et ressaisir les montants
- Vérifier le taux de TVA configuré
- Contrôler les pourcentages de remise

**Client non trouvé**
- Utiliser la recherche avec au moins 2 caractères
- Vérifier l'orthographe du nom
- Créer le client s'il n'existe pas

### 🔧 Support Technique
- Consulter la **console navigateur** pour les erreurs JavaScript
- Vérifier les **logs Flask** pour les erreurs serveur
- Tester avec les **données de démonstration** incluses

## 🚀 Améliorations Futures

### 📈 Version 2.0
- **Workflow d'approbation** configurable
- **Signatures électroniques** intégrées
- **Génération PDF** avancée avec modèles
- **Synchronisation mobile** hors ligne
- **API REST** complète pour intégrations

### 🔄 Intégrations Prévues
- **Module comptabilité** pour écritures automatiques
- **Module CRM** pour suivi commercial
- **Module stock** pour réservations
- **Module expédition** pour bons de livraison
- **Module achats** pour commandes fournisseurs

---

## 📞 Contact

Pour toute question ou suggestion concernant ce module :

**Développeur** : Assistant IA GitHub Copilot  
**Version** : 1.0.0  
**Date** : Janvier 2024  
**Licence** : SEILite Internal

---

*Ce module fait partie intégrante de la suite SEILite et respecte l'architecture et les standards de l'application principale.*
