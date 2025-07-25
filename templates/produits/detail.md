# Détail du Produit (`detail.html`)

1. Objectif du module "Détail du Produit"
Permettre l’affichage complet et dynamique de la fiche produit, incluant toutes les informations principales, secondaires et les mouvements de stock par entrepôt, en s’appuyant sur les tables INPRIX (produit) et INVEN (quantités).
---
2. Sources de données
- Table INPRIX : Informations principales du produit (identité, prix, statuts, descriptions, coûts, core/redevance, etc.).
- Table INVEN : Quantités et mouvements par entrepôt (stock, commandes, réservations, etc.).
- Table INPTECK : Fiche technique (description FR/EN, multi-lignes, mapping produit_id).
  (Source : Table INPTECK dans la base Apogee, mapping unifié sur produit_id)
---
3. Champs à afficher
A. Image du produit
•	image_path (INPRIX) : chemin de l’image, sinon icône par défaut.
B. Informations principales
•	numero (CAT), statut (ACTIF, DISCONT, INVENTAIRE), prix_revient (COUT)
C. Informations système
•	date_creation, date_modification
D. Description
•	description_fr (DESCR), description_en (DESCA)
•	code_barres (CODEBA)
•	groupe (TYPE)
•	format (FORMAT)
•	substitut (CODEAP)
•	mot_clef_1 (MOTCLE1), mot_clef_2 (MOTCLE2)
•	type (TYPEP)
•	categorie (CATP)
•	remarques_1 (DIMMET), remarques_2 (DIMIMP)
E. Gestion
•	escomptable (PROESCTAB)
•	etiquette (ETIQUETTE)
•	gestion_serie (SERIAL)
•	gestion_lot (LOT)
•	maj_auto (MAJCOUT)
F. Taxes & Comptabilité
•	tvp (TAXPRO)
•	tvf (TAXFED)
•	taux (TXF)
•	postes_comptables (POSTC, POSTU, POSTCA, POSTUA)
G. Coûts & Stocks
•	cout_reference (COUTL)
•	cout_tvf (COUTT)
•	prix_revient (COUT)
•	point_commande (REORP)
•	minimum_commander (MINCOM)
•	maximum_inventaire (MAXINV)
•	mode_calcul (CALMODE)
•	formule (FORM)
•	marge (MARGE)
H. Core/Redevance
•	produit_core (PRODCORE)
•	groupe_core (GRPCORE)
•	g_core (GCORE)
•	core_valeur (COREVALUE)
•	core_escalade (COREESCAL)
I. Autres informations
•	localisation (LOCAT)
•	famille (CONTENANT)
•	evaluation (EVALUATION)
J. Fiche technique (INPTECK)
- fiche_fr (FICHE1 à FICHE10, source inpteck.fiche1 à inpteck.fiche10)
- fiche_en (FICHE1A à FICHE10A, source inpteck.fiche1a à inpteck.fiche10a)
- Affichage dynamique dans le template : boucle Jinja2 sur inpteck.fiche1 à fiche10 et fiche1a à fiche10a
  Exemple d'intégration dans detail.html :
  ```jinja2
  <div class="row">
    <div class="col-md-6">
      <h6>Description technique (français)</h6>
      <pre class="bg-light p-2 border rounded">
      {% for i in range(1, 11) %}
        {{ attribute(inpteck, 'fiche' ~ i) or '' }}
      {% endfor %}
      </pre>
    </div>
    <div class="col-md-6">
      <h6>Description technique (anglais)</h6>
      <pre class="bg-light p-2 border rounded">
      {% for i in range(1, 11) %}
        {{ attribute(inpteck, 'fiche' ~ i ~ 'a') or '' }}
      {% endfor %}
      </pre>
    </div>
  </div>
  ```
K. Quantités par entrepôt (INVEN)
Pour chaque entrepôt lié au produit :
•	entrepot (ENTREPOT)
•	en_main (QMAIN)
•	commandé (QCOM)
•	disponible (calculé : QMAIN - QCOM - QNF)
•	attendue (ENCOM)
•	date_attendue (DTA)
•	localisation (LOCAT)
•	... et autres mouvements (QDEBUT, QRECU, QRESER, QVENDU, etc.)
---
4. Fonctionnement dynamique
•	Les routes Flask chargent le produit et ses quantités associées.
•	Les blocs Jinja affichent dynamiquement les données.
•	Les champs techniques (fiche, quantités) sont toujours à jour.
---
5. Points d’attention
• Vérifier la cohérence des noms de champs entre le modèle SQLAlchemy et la base Apogee (voir mapping ci-dessous).
• Gérer l’absence d’image ou de quantités par entrepôt (affichage d’un message).
• Les champs techniques (fiche) sont multi-lignes, à concaténer pour l’affichage (source inpteck, mapping produit_id).
• Pour les calculs dans Jinja2, toujours caster en float pour éviter les erreurs de type (ex : `{{ (q.qmain|float or 0) - (q.qcom|float or 0) - (q.qnf|float or 0) }}`)
• Pour l’affichage multi-lignes des fiches techniques, utiliser une boucle Jinja2 sur l’objet inpteck :
  ```jinja2
  {% for i in range(1, 11) %}
    {{ attribute(inpteck, 'fiche' ~ i) or '' }}
  {% endfor %}
  {% for i in range(1, 11) %}
    {{ attribute(inpteck, 'fiche' ~ i ~ 'a') or '' }}
  {% endfor %}
  ```
---
6. Exemple de mapping (Python/SQLAlchemy → Apogee)
| SQLAlchemy           | Apogee (VB/DB) |
|----------------------|----------------|
| numero_produit       | CAT            |
| description_fr       | DESCR          |
| description_en       | DESCA          |
| barcode              | CODEBA         |
| groupe               | TYPE           |
| format               | FORMAT         |
| substitut            | CODEAP         |
| motclef1             | MOTCLE1        |
| motclef2             | MOTCLE2        |
| type_produit         | TYPEP          |
| categorie            | CATP           |
| remarques1           | DIMMET         |
| remarques2           | DIMIMP         |
| escomptable          | PROESCTAB      |
| etiquettes           | ETIQUETTE      |
| gestion_serie        | SERIAL         |
| gestion_lot          | LOT            |
| maj_auto             | MAJCOUT        |
| tvp                  | TAXPRO         |
| tvf                  | TAXFED         |
| taux_taxe_fed        | TXF            |
| poste_vente_can      | POSTC          |
| poste_vente_us       | POSTU          |
| poste_achat_can      | POSTCA         |
| poste_achat_us       | POSTUA         |
| cout_reference       | COUTL          |
| cout_tvf             | COUTT          |
| prix_revient         | COUT           |
| point_commande       | REORP          |
| minimum_commander    | MINCOM         |
| maximum_inventaire   | MAXINV         |
| mode_calcul          | CALMODE        |
| formule              | FORM           |
| marge                | MARGE          |
| produit_core         | PRODCORE       |
| groupe_core          | GRPCORE        |
| g_core               | GCORE          |
| core_valeur          | COREVALUE      |
| core_escalade        | COREESCAL      |
| localisation         | LOCAT          |
| famille              | CONTENANT      |
| evaluation           | EVALUATION     |
| fiche1 à fiche10     | FICHE1 à FICHE10 (INPTECK, mapping produit_id, modèle SQLAlchemy: Inpteck) |
| fiche1a à fiche10a   | FICHE1A à FICHE10A (INPTECK, mapping produit_id, modèle SQLAlchemy: Inpteck) |
| ...                  | ...            |
---
## Correspondance des champs caractéristiques (Apogee ↔ MySQL)

Cette section détaille le mapping des champs caractéristiques entre Apogee et MySQL pour la gestion des catégories et caractéristiques produit :

| Apogee (VB/DB) | MySQL (SQLAlchemy) | Description |
|----------------|-------------------|-------------|
| fliencate      | liencate          | Lien catégorie (catégorie principale du produit) |
| fliencpro      | liencpro          | Lien caractéristique produit (catégorie/produit) |
| ftype          | type              | Type de caractéristique (type produit) |

**Règle de synchronisation** :
- `Apogee.fliencate` doit être égal à `MySQL.liencate`
- `Apogee.fliencpro` doit être égal à `MySQL.liencpro`
- `Apogee.ftype` doit être égal à `MySQL.type`

Ce mapping garantit la cohérence des données entre l’interface Apogee (WinForms) et la base MySQL utilisée par SEILite.
---
## Ajout/Synchronisation des caractéristiques produit (Apogee ↔ MySQL)

Pour garantir la cohérence et permettre l’ajout ou la modification des caractéristiques produit, utilisez la correspondance suivante :

| Apogee (WinForms) | MySQL (SQLAlchemy) | Description |
|-------------------|-------------------|-------------|
| fliencate         | liencate          | Catégorie principale du produit |
| fliencpro         | liencpro          | Caractéristique liée au produit |
| ftype             | type              | Type de caractéristique |

**Synchronisation** :
- Lors de l’ajout ou modification d’une caractéristique dans l’interface Apogee, la valeur doit être répercutée dans la base MySQL (et inversement).
- Exemple d’utilisation : lors de la création d’une catégorie ou d’une caractéristique, vérifier que `fliencate == liencate`, `fliencpro == liencpro`, `ftype == type`.

**Exemple d’intégration Flask/Jinja** :
```jinja2
<!-- Affichage des caractéristiques synchronisées -->
<ul>
  <li>Catégorie (Apogee/MySQL) : {{ categorie_apogee }} / {{ produit.liencate }}</li>
  <li>Caractéristique (Apogee/MySQL) : {{ caracteristique_apogee }} / {{ produit.liencpro }}</li>
  <li>Type (Apogee/MySQL) : {{ type_apogee }} / {{ produit.type }}</li>
</ul>
```

Cette section doit être affichée dans la fiche produit pour garantir la traçabilité et la synchronisation des caractéristiques entre Apogee et MySQL.
---
7. Conclusion
Ce PRD doit servir de référence pour l’implémentation de la fiche produit dans SEILite, en garantissant l’exhaustivité des informations et la synchronisation avec la base Apogee.
---
Besoin d’un exemple de code Flask/Jinja pour l’affichage ou d’un mapping complet ? Indique la partie à détailler !