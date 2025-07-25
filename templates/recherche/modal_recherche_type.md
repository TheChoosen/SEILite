# Documentation – Modale de recherche générique (`modal_recherche_type.html`)

## 1. Objectif et PRD (spécification)

La modale de recherche générique permet à l’utilisateur de rechercher et de sélectionner dynamiquement une valeur de référence (groupe, catégorie, entrepôt, etc.) dans un formulaire produit ou tout autre écran métier. Elle centralise la logique de recherche, d’affichage et de sélection, et renvoie la valeur choisie au champ cible du formulaire principal.

### Fonctionnalités principales
- **Recherche dynamique** sur différents types de référentiels (groupe, catégorie, entrepôt, etc.)
- **Affichage des résultats** sous forme de tableau (code, libellé, bouton de sélection)
- **Sélection d’une valeur** qui remplit automatiquement le champ cible du formulaire
- **Callback JS personnalisable** (id de champ ou fonction)
- **Pré-remplissage automatique** du champ de recherche avec la valeur du champ cible
- **Réutilisable** sur tous les écrans (inclusion globale dans `base.html`)
- **Extensible** à d’autres types de référentiels ou d’autres écrans

## 2. Structure HTML
- Modale Bootstrap (`modal-lg`) avec titre dynamique
- Formulaire de recherche :
  - Sélecteur du type de référence (`selectTypeRecherche`)
  - Champ texte de recherche (`inputRechercheType`)
  - Bouton de lancement de la recherche
- Tableau de résultats dynamique (`tableResultatsRechercheType`)
- Bouton de fermeture

## 3. API JS

### Ouvrir la modale
```js
ouvrirModalRechercheType(type, targetInputIdOrCallback)
```
- **type** : string, ex. 'groupe', 'categorie', 'entrepot' (doit correspondre à une valeur du select)
- **targetInputIdOrCallback** :
  - string : id du champ à remplir dans le formulaire principal (callback automatique)
  - function : callback personnalisée `(type, code, libelle) => { ... }`

### Recherche dynamique
- Lancement par bouton ou touche Entrée
- Appel AJAX `/recherche_type?type=...&q=...` (Flask)
- Affichage des résultats dans le tableau

### Sélection d’une valeur
- Bouton de sélection dans chaque ligne du tableau
- Appel du callback (remplissage du champ cible ou exécution de la fonction)
- Fermeture automatique de la modale

### Pré-remplissage
- À l’ouverture, le champ de recherche est pré-rempli avec la valeur du champ cible (si string)

## 4. API Flask

Route `/recherche_type` :
- **GET**
- Paramètres :
  - `type` : type de référence (groupe, catégorie, entrepôt, ...)
  - `q` : chaîne de recherche (optionnelle)
- Retour :
  - JSON : liste d’objets `{ code, libelle }` (ou colonnes dynamiques selon le type)

## 5. Cas d’usage
- Sélection d’un groupe, d’une catégorie, d’un entrepôt dans un formulaire produit
- Recherche de valeurs de référence dans d’autres écrans (fiche technique, attribut web, etc.)
- Peut être appelée depuis n’importe quel formulaire ou écran métier

## 6. Conventions d’intégration
- Inclure la modale une seule fois dans `base.html` (pour disponibilité globale)
- Utiliser le bouton de recherche avec :
  - `onclick="ouvrirModalRechercheType('groupe', 'idChampCible')"`
  - ou `onclick="ouvrirModalRechercheType('categorie', (type, code, libelle) => { ... })"`
- Le JS de la modale ne dépend que de Bootstrap et de fetch (pas de dépendance lourde)
- Extensible : ajouter d’autres types dans le select et le mapping côté Flask

## 7. Extensibilité et options avancées
- Ajout d’autres types de référentiels (ajouter dans le select et le mapping Flask)
- Colonnes dynamiques selon le type (adapter le JS et la route Flask)
- Gestion multilingue (adapter les labels et le mapping)
- Réutilisation sur d’autres écrans (fiche technique, attributs web, etc.)

## 8. Sécurité et bonnes pratiques
- Le mapping type/table/colonne côté Flask doit être strictement contrôlé (pas d’injection SQL)
- Les callbacks JS doivent être robustes (vérifier l’existence du champ cible)
- La modale ne stocke aucune donnée sensible

## 9. Exemple d’intégration
```html
<input type="text" id="champGroupe" ...>
<button type="button" onclick="ouvrirModalRechercheType('groupe', 'champGroupe')">Rechercher groupe</button>
```

## 10. Historique et évolutions
- Version initiale : centralisation de la recherche, callback JS, inclusion globale
- Améliorations : pré-remplissage, refactoring JS, extension à d’autres types
- À venir : colonnes dynamiques, multilingue, extension à d’autres écrans

---

**Auteur :** Automatique (Copilot) – Juillet 2025
