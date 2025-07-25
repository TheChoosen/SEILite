# Formulaire Produit (`formulaire.html`)

Ce fichier gère l'affichage et la soumission du formulaire de création ou modification d'un produit.

## Structure principale
- **Champs principaux** : Numéro, groupe, format, substitut, descriptions, code-barres, mots-clés, type, catégorie, remarques.
- **Gestion** : Statuts, escomptable, étiquettes, gestion série/lot, MAJ auto.
- **Taxes** : TVP, TVF, taux, postes comptables.
- **Localisation** : Localisation, famille.
- **Coûts et stocks** : Coût référence, coût TVF, prix de revient, point de commande, min/max stock.
- **Calculs** : Mode calcul, formule, maj auto.
- **Core** : Produit noyau, groupe, valeur, escalade, marge.
- **Évaluation** : Champ d’évaluation.
- **Image** : Upload et affichage de l’image produit.
- **Boutons** : Valider, annuler, retour.

## Points clés
- Validation côté client et serveur.
- Affichage des erreurs et messages de succès.
- Intégration complète avec le backend Flask pour la gestion des données.

## Caractéristiques synchronisées Apogee ↔ MySQL

- Champs CRUD : `liencate`, `liencpro`, `type`
- Saisie et modification via le formulaire produit.
- Mapping direct avec les champs Apogee (fliencate, fliencpro, ftype).
- Synchronisation automatique avec fliencate pour la table LIENCATE.
- Synchronisation automatique avec fliencpro pour la table LIENCPRO.
- Synchronisation automatique avec ftype pour la table TYPE.
- Toute modification est répercutée dans la fiche produit (detail.html).

## Quantités par entrepôt (INVEN)
- Saisie et modification des quantités pour chaque entrepôt lié au produit.
- Champs : entrepôt, en main, commandé, disponible, attendue, date attendue, localisation, mouvements (réception, réservation, vente, etc.).
- Interface dédiée dans le formulaire pour ajouter/modifier les stocks.

## Fiche technique (INPTECK)
- Saisie des fiches techniques en français et anglais (FICHE1 à FICHE10, FICHE1A à FICHE10A).
- Champs multi-lignes, affichage dynamique dans le formulaire.
- Mapping direct avec la table INPTECK (produit_id).

## Attributs web du produit (PRODUITWEB)
- Saisie et modification des attributs web : ligne, couleur, grandeur, dimensions, marque, modèle, groupe, famille, année, lien photo, statut web.
- Section dédiée dans le formulaire pour la gestion des informations web du produit.
- Synchronisation automatique avec la table PRODUITWEB.

---
Ce fichier est essentiel pour la gestion des produits (création et modification) dans SEILite.
