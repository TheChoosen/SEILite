# Module Véhicules - Phase 1

## 📋 Description
Module de gestion des véhicules intégré à SEILite, permettant la gestion complète du cycle de vie des véhicules (interne, vendu, loué, financé, en réparation, désactivé).

## 🚀 Fonctionnalités implémentées (Phase 1)

### ✅ Liste des véhicules (`liste.html`)
- **Table responsive** avec colonnes personnalisables
- **Filtres dynamiques** par statut, type, marque, client
- **Recherche texte** par numéro d'unité, série, client, marque
- **Badges de statut** avec couleurs distinctives
- **Indicateurs d'entretien** avec alertes visuelles
- **Actions** : Voir, Modifier, Dupliquer, Désactiver
- **Statistiques rapides** en temps réel
- **Pagination** intégrée
- **Navigation vers produits** via bouton dédié

### ✅ Fiche détaillée (`detail.html`)
- **Informations générales** : N° unité, type, année, statut
- **Spécifications techniques** : Marque, modèle, cabine, poids, combustion
- **Client lié** : Code, nom, coordonnées complètes
- **Dates & historique** : Achat, vente, fournisseur, facture
- **Coûts & valeur** : Prix, coûts CAD/USD, profit calculé, taxes
- **Entretien** : Prochaine maintenance, garantie, historique (ENT1-ENT6)
- **Informations système** : Dates de création/modification

### ✅ Formulaire (`formulaire.html`)
- **Identification** : N° unité (unique), type, année, série, licence, statut
- **Spécifications** : Marque, modèle, spécifications techniques
- **Affectation client** : Recherche client intégrée
- **Coûts** : Prix, coûts, calcul automatique du profit
- **Dates** : Achat, vente, désactivation
- **Entretien** : Maintenance, garantie, historique complet
- **Validation** : Champs obligatoires, formats de données

## 🗃️ Base de données
- **Table principale** : `unit` (base `bdm`)
- **Champs mappés** : 50+ colonnes selon PRD
- **Clés** : ID auto-incrémenté, UNITE unique
- **Relations** : Client, fournisseur, entretien

## 🛣️ Routes implémentées
```
GET  /vehicules                    # Liste avec filtres
GET  /vehicules/<id>               # Détail véhicule
GET  /vehicules/nouveau            # Formulaire création
POST /vehicules/nouveau            # Traitement création
GET  /vehicules/<id>/modifier      # Formulaire modification
POST /vehicules/<id>/modifier      # Traitement modification
POST /vehicules/<id>/desactiver    # Désactivation
GET  /vehicules/<id>/dupliquer     # Duplication
GET  /vehicules/api/search         # API recherche
GET  /vehicules/api/stats          # API statistiques
```

## 🎨 Interface utilisateur
- **Design cohérent** avec le module produits
- **Bootstrap 5** pour la responsivité
- **Font Awesome** pour les icônes
- **Couleurs sémantiques** pour les statuts
- **Modales** pour confirmations
- **Navigation fluide** entre modules

## 🔗 Navigation inter-modules
- **Depuis véhicules** → **Produits** : Bouton "Produits" dans la liste
- **Depuis produits** → **Véhicules** : Lien "Véhicules" dans la navbar
- **Navigation principale** : Menu unifié dans `base.html`

## 📊 Statistiques affichées
- **Total véhicules**
- **Par statut** : Internes, Vendus, Loués, En réparation, Désactivés
- **Alertes entretien** : Maintenance urgente, planifiée
- **Valeurs moyennes** : Prix moyen via API

## 🔍 Recherche et filtres
- **Recherche textuelle** : Multi-champs (unité, série, client, marque)
- **Filtres** : Statut, type, marque, client
- **Tri** : Par date de modification (défaut)
- **Pagination** : 20 éléments par page

## 🛠️ Calculs automatiques
- **Profit** : Prix - Coût (temps réel)
- **Alertes entretien** : Basées sur DUREE
- **Statistiques** : Compteurs dynamiques

## 📁 Structure des fichiers
```
f:\SEILite\
├── templates\vehicules\
│   ├── liste.html          # Liste des véhicules
│   ├── detail.html         # Fiche détaillée
│   ├── formulaire.html     # Création/modification
│   └── vehicules.md        # PRD complet
├── vehicules_routes.py     # Routes Flask + modèle
└── app.py                  # Intégration blueprint
```

## 🎯 Phase 2 (à venir)
- **Documents associés** : Upload/téléchargement
- **Historique détaillé** : Bons de travail, locations, contrats
- **IA contextuelle** : Suggestions maintenance, alertes
- **Rapports** : Exports PDF, analyses
- **Intégration F&I** : Module financement
- **API étendue** : Intégrations externes

## 🚦 Tests recommandés
1. **Navigation** : Véhicules ↔ Produits
2. **CRUD** : Création, lecture, modification, désactivation
3. **Filtres** : Tous les filtres de recherche
4. **Calculs** : Profit automatique
5. **Responsive** : Mobile/tablette
6. **Données** : Validation des champs

## 📝 Notes techniques
- **Compatibilité** : Aucun conflit avec module produits
- **Performances** : Pagination et indexation
- **Sécurité** : Validation côté serveur
- **Maintenabilité** : Code modulaire et documenté
