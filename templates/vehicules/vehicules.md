🧠 Module de gestion des véhicules
🎯 Fonction principale
Gérer le cycle de vie complet des véhicules (interne, vendu, loué, financé, en réparation, désactivé) via une interface unifiée permettant la consultation, la modification, le suivi, et la prévision d’entretien.

✅ Résultats concrets
Accès rapide à l’état et à l’historique d’un véhicule

Vue centralisée : client, prix, statut, entretien, documents

Interface modulaire pour l’achat, la vente, l’entretien, la location

Réduction des erreurs et automatisation des statuts

Compatibilité native avec les autres modules (F&I, Entretien, Location)

🔗 Tables SQL principales
Base : bdm
Table : unit

Exemples de colonnes clés à exposer dans l’UI :

Identification : id, UNITE, SERIE, LICENCE

Spécifications : MARQUE, MODELE, ANNEE, TYPE, CABINE, POIDS, COMBUSTION

Client : CLIENT, NOM, TPHONE, ADR1, VILLE

État & Suivi : STATUT, DATE_ACH, DATE_VTE, DATE_CREE, DATE_MODIF, ETAT, REMARQUE

Valeur : PRIX, COUT, COUTU, PROFIT, DEVALUAT

Entretien : DUREE, ENTD, ENT1 à ENT6, DATE_DESAC

Financement : FOUR, COUTUS, NOFACTURE, TAXFED, TAXPRO, TOTALP, TOTALCO

📄 Pages concernées
1. liste.html – Vue de la liste des véhicules
Élément	Détails
✅ Table responsive	Colonnes visibles personnalisables (ex. : UNITE, MARQUE, MODELE, CLIENT, STATUT, PRIX)
✅ Filtres dynamiques	Par statut (INTERNE, VENDU, LOCATION, etc.), client, date, type
✅ Recherche texte	Par nom, numéro de série, client, vendeur
✅ Boutons d'action	Voir (modale ou lien), Modifier (inline ou modale), Dupliquer, Désactiver
✅ Tri + pagination	Composants DataTables.js ou équivalent Tailwind/Alpine.js
✅ Badges de statut	Couleurs pour INTERNE, VENDU, LOUE, DÉSACTIVÉ, À ENTRETENIR

2. detail.html – Fiche détaillée
Section	Champs extraits de unit
📋 Info générale	UNITE, SERIE, LICENCE, STATUT, TYPE, ANNEE
🔧 Spécifications techniques	MODELE, MARQUE, CABINE, POIDS, COMBUSTION, CAPACITE
📦 Achat & Coûts	PRIX, COUT, COUTU, DEVALUAT, PROFIT, NOFACTURE, FOUR
🧾 Dates & Historique	DATE_CREE, DATE_ACH, DATE_VTE, DATE_MODIF, DATE_DESAC
👤 Client lié	CLIENT, NOM, ADR1, VILLE, TPHONE, EMAIL
🛠 Entretien	ENT1 à ENT6, ENTDATEENT, REMUNIT, GARANTIE, REMGARANT
📄 Documents associés	Téléchargement auto à partir des NOFACTURE, fiche de vente, photos, etc.
📊 Historique	Liens vers bons_travail, locations, contrats_fi, punch_logs liés

3. formulaire.html – Création / modification d’un véhicule
Section	Champs SQL à mapper
Identification	UNITE, TYPE, ANNEE, SERIE, LICENCE
Spécifications	MODELE, MARQUE, CABINE, POIDS, CAPACITE, COMBUSTION
Affectation client	CLIENT, NOM, ADR1, TPHONE
Statut & Entretien	STATUT, DATE_ACH, DATE_VTE, ENT1 à ENT6, REMUNIT, GARANTIE
Coûts & Valeur	PRIX, COUT, COUTU, DEVALUAT, PROFIT
Données administratives	NOFACTURE, FOUR, DATE_CREE, DATE_MODIF, ETAT, DATE_DESAC

Fonctionnalités UI :

✅ Auto-complétion client et fournisseur

✅ Calcul dynamique du profit (PRIX - COUT)

✅ Sélecteur de date, menus déroulants pour STATUT, TYPE, etc.

✅ Champs de texte conditionnels selon le STATUT (ex : si "VENDU", afficher NOFACTURE)

🔗 API à prévoir
Endpoint	Description
GET /vehicules	Liste filtrée avec pagination
GET /vehicule/{id}	Récupérer tous les détails
POST /vehicule/create	Ajouter un véhicule
POST /vehicule/update/{id}	Mettre à jour les champs
POST /vehicule/disable/{id}	Archiver ou désactiver le véhicule
GET /vehicule/historique/{id}	Voir les entretiens, contrats, punchs associés

📊 UX & IA contextuelle à ajouter
Checklist automatique selon TYPE, ANNEE, GARANTIE

Suggestions IA : proposer une vente, un rappel, ou un entretien si inactivité prolongée

Badge IA sur fiche : “à risque de panne” (via maintenance prédictive)

Alertes intelligentes : si DATE_DESAC approche + GARANTIE expire