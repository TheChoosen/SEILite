# SEILite

## Description
Application de gestion commerciale pour SEI (Système d'Équipement Industriel).

## Structure du projet

```
SEILite/
├── app.py                 # Application Flask principale
├── requirements.txt       # Dépendances Python
├── routes/               # Modules de routes
│   ├── clients_routes.py
│   ├── documents_routes.py
│   ├── vehicules_routes.py
│   └── ...
├── templates/            # Templates Jinja2
├── static/              # Fichiers statiques (CSS, JS)
├── instance/            # Base de données
└── documents/           # Documentation du projet
```

## Installation

1. Créer un environnement virtuel :
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# ou
.venv\Scripts\activate     # Windows
```

2. Installer les dépendances :
```bash
pip install -r requirements.txt
```

3. Lancer l'application :
```bash
python app.py
```

## Accès
L'application sera accessible sur : http://127.0.0.1:5000

## Documentation
Consultez le répertoire `documents/` pour la documentation complète du projet.
