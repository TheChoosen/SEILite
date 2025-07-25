# SEILite — Product Requirements Document (PRD)

## Objectif du projet
SEILite est une application de gestion de produits et de stocks, permettant de suivre les informations détaillées des articles, leurs mouvements et quantités par entrepôt, ainsi que la gestion complète des données associées (prix, fournisseurs, taxes, etc.).

## Fonctionnalités principales
- **Consultation des produits** : Fiche détaillée avec toutes les informations du produit et les quantités par entrepôt (INVEN).
- **Liste des produits** : Recherche, filtrage, pagination, actions (voir, modifier, supprimer).
- **Création/modification de produit** : Formulaire complet, gestion des images, validation, messages d’erreur/succès.
- **Gestion des stocks** : Suivi des quantités, mouvements, lots, séries, ajustements, etc.
- **Gestion des fournisseurs, prix, taxes, promotions, etc.**

## Architecture technique
- **Backend** : Flask, Flask-SQLAlchemy, MySQL.
- **Frontend** : Jinja2, Bootstrap, FontAwesome.
- **Templates** : Héritage via `base.html`, pages spécifiques pour la liste, le formulaire et le détail produit.
- **Modèles principaux** :
  - `Produit` (INPRIX) : Tous les champs principaux du produit, organisés par section (identification, prix, fournisseurs, gestion, etc.).
  - `Inven` (INVEN) : Champs principaux pour le suivi des quantités et mouvements par entrepôt.

## Fichiers clés
- `app.py` : Application Flask, modèles SQLAlchemy, routes principales, logique backend.
- `templates/base.html` : Structure HTML de base, héritage pour toutes les pages.
- `templates/produits/liste.html` : Liste paginée des produits, recherche, actions.
- `templates/produits/formulaire.html` : Formulaire de création/modification produit.
- `templates/produits/detail.html` : Fiche produit détaillée, tableau des quantités par entrepôt.
- `.md associés` : Documentation de chaque template pour faciliter la compréhension et la maintenance.

## Flux utilisateur
1. **Accueil** : Redirection vers la liste des produits.
2. **Liste** : Recherche, navigation, accès aux actions.
3. **Détail** : Consultation complète d’un produit, visualisation des stocks par entrepôt.
4. **Formulaire** : Création ou modification d’un produit, upload d’image, validation.

## Points d’intégration
- **Quantités par entrepôt** : Chargées dynamiquement depuis la table INVEN et affichées dans la fiche produit.
- **Gestion des images** : Upload sécurisé, affichage conditionnel.
- **Validation et messages** : Gestion des erreurs et succès côté serveur et client.

## Pour aller plus loin
- Ajouter des fonctionnalités avancées (statistiques, export, gestion multi-utilisateurs).
- Adapter les modèles selon l’évolution des besoins métier.
- Améliorer l’ergonomie et la personnalisation de l’interface.

---
Ce PRD synthétise tout ce qu’il faut savoir pour comprendre, maintenir et faire évoluer le projet SEILite.
