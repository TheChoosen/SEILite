Voici un PRD structuré pour le module Gestion des Clients dans SEI Web, basé sur ta table MySQL client (bdm.client) et adapté aux trois vues frontales suivantes :

liste.html (tableau dynamique)

details.html (fiche complète)

formulaire.html (création/modification)

🧠 Module de gestion des clients
🎯 Fonction principale
Centraliser l’information client dans une fiche unifiée, intelligente et extensible — pour améliorer la gestion de la relation, les ventes, le service après-vente et les automatisations.

✅ Résultats concrets
Consultation rapide de l’état d’un client

Vue complète : coordonnées, historique, statut, activités

Automatisation des communications (courriel, relance, avis)

Intégration avec F&I, véhicules, commandes et punch

🔗 Table SQL principale
Base : bdm
Table : client

Champs clés pour l’UI :

Identification : CLIENT, client_index, NOM, PRENOM, COMPAGNY, LOYALID

Coordonnées : ADR1, ADR2, VILLE, CP1, PROV, PAYS, TPHONE, TELCEL, EMAIL

Contacts : CONTACT, TELCON, FAX

Statuts : ACTIF, ARRET, STAT, CAT, TYPE, TYPEE, LANGUE, VENDEUR, GROUPE

Fiscaux / Taxes : NOTAXFED, NOTAXPRO, TAUX, TERMES, LIMCRE

Données CRM : MOTCLE1, MOTCLE2, COMMENT, COMMENT2, REM1, REM2

Fichiers & autres : REPENVOIE, REPSORTIE, FTP, MOTPASSE, PERMIS, CARTE

📄 Pages concernées
1. liste.html – Tableau de clients
Élément	Détails
✅ Colonnes visibles	CLIENT, NOM, VILLE, VENDEUR, STAT, LOYALID
✅ Recherche globale	Par nom, code client, téléphone, vendeur
✅ Filtres dynamiques	ACTIF, TYPE, VENDEUR, PROV, GROUPE
✅ Actions rapides	Voir, Modifier, Archiver, Relancer
✅ Affichage enrichi	Badge de statut (actif / inactif), bouton "Appeler"
✅ Tri + pagination	Par nom, date création (DATECR), code client

2. details.html – Fiche client complète
Section	Champs SQL à exposer
👤 Informations générales	CLIENT, NOM, PRENOM, COMPAGNY, LOYALID, STAT, ACTIF
📞 Coordonnées	TPHONE, TELCEL, EMAIL, ADR1, ADR2, VILLE, CP1, PROV, PAYS
🔍 Données commerciales	VENDEUR, TERMES, TYPE, TYPEE, CAT, GROUPE, MON, LANGUE
🧾 Taxes / paiements	NOTAXFED, NOTAXPRO, TAUX, LIMCRE, DEPOT, TRANS
📎 Remarques & tags	MOTCLE1, MOTCLE2, REM1, REM2, COMMENT, COMMENT2
🔐 Sécurité & Fichiers	MOTPASSE, FTP, REPENVOIE, REPSORTIE
📅 Dates importantes	DATECR, DATENAIS, DATDVTE, DATEP
📁 Historique	Véhicules achetés, F&I, entretiens, factures (liens API unit, contrats_fi, bt)

3. formulaire.html – Création / modification
Section	Champs requis
🆔 Identité	CLIENT, NOM, PRENOM, COMPAGNY
📞 Contact	TPHONE, TELCEL, EMAIL, CONTACT, FAX
📍 Adresse	ADR1, ADR2, VILLE, CP1, PROV, PAYS
🧾 Commercial	TYPE, TYPEE, CAT, VENDEUR, GROUPE
💰 Facturation	TERMES, TAUX, LIMCRE, DEPOT
🔐 Sécurité	MOTPASSE, FTP, ACTIF, ARRET, STAT
🧠 CRM	MOTCLE1, MOTCLE2, REM1, REM2, COMMENT, COMMENT2
📆 Dates	DATECR, DATENAIS, DATEEXP

Fonctionnalités UI :

✅ Auto-remplissage des champs à partir d’un client existant (dupliquer)

✅ Menu déroulant dynamique pour les termes (TERMES), le vendeur (VENDEUR), etc.

✅ Validation d’unicité de CLIENT, EMAIL, TELCEL

🔗 API à prévoir
Endpoint	Description
GET /clients	Liste avec filtres
GET /client/{id}	Détail complet
POST /client/create	Création
POST /client/update/{id}	Modification
POST /client/disable/{id}	Archivage (champ ARRET ou ACTIF=0)
GET /client/{id}/historique	Interactions, véhicules, contrats, bons

📊 UX & IA contextuelle
Détection doublons sur NOM + VILLE + TELCON

Relance intelligente : si aucun contrat ou interaction dans les 6 mois

Badge fidélité (LOYALID) : afficher des badges en fonction de l'ancienneté ou de l'activité

Suggestions IA : "Proposer entretien", "Rappeler", "Offrir un rabais"