# Base Template (`base.html`)

Ce fichier définit la structure HTML de base pour toutes les pages de SEILite.

## Structure principale
- **Header** : Titre, navigation principale, logo.
- **Content Block** : Zone centrale où s’insèrent les contenus spécifiques via `{% block content %}`.
- **Footer** : Informations légales, liens utiles, copyright.
- **Inclusion CSS/JS** : Bootstrap, FontAwesome, fichiers personnalisés.

## Points clés
- Utilisation de Jinja2 pour l’héritage de template.
- Centralisation du style et des scripts.
- Facilite la cohérence visuelle et fonctionnelle de l’application.

---
Ce fichier est la base de tous les templates et garantit l’uniformité de l’interface.
