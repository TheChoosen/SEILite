📘 PRD – Interface de Personnalisation du Style CLIENT (V2)
Nom du projet : SEI Web – Personnalisation du style client
Version : 2.0
Responsable produit : Adam Menard
Date : 2025-07-22
Contexte : Le style visuel est un facteur de différenciation clé dans la conversion des utilisateurs. L’objectif est de permettre à chaque entreprise ou client d’adapter visuellement son expérience via un panneau de style intelligent et dynamique.

🧭 1. Objectif du Module
Permettre à l’utilisateur de personnaliser l’apparence visuelle de tous les éléments UI de type “client” dans SEI Web (formulaires, tableaux, boutons, listes, cartes, modales) à l’aide d’un panneau de style interactif, basé sur des effets Claymorphism et Glassmorphism.

👥 2. Public Cible
Entreprises clientes (garages, vendeurs, techniciens)

Utilisateurs finaux (clients ayant accès à leur compte)

Responsables UX ou graphistes internes

🎨 3. Principes UX/UI
Style	Description	Applications
Claymorphism	Déformations douces, ombrage plastique, effets 3D doux	Boutons, cartes, sliders
Glassmorphism	Fond flou translucide, contours fins, surcouche brillante	Modales, formulaires, cartes de données

🧩 4. Fonctionnalités Clés
Fonction	Description
🎛️ Panneau glissant (offcanvas)	Interface latérale ou modale accessible en un clic
🌈 Thèmes prédéfinis	Clay clair, Clay foncé, Glass pur, Glass doux, Corporate
⚙️ Personnalisation avancée	Blurs, opacité, ombres, coins, couleurs, transitions
🧪 Aperçu instantané	Live Preview en zone .client-zone
💾 Sauvegarde par utilisateur	Via API REST (MySQL ou LocalStorage fallback)
🔄 Réinitialisation rapide	Bouton "Réinitialiser mon thème"
👀 Mode contrasté	Accessibilité élevée : haut contraste, couleurs AAA
🪞 Mode miroir	Affiche le style tel qu’un client le verrait (mode simulation)

🧱 5. Composants UI/UX à styliser
Gérés par Style Client (DOIVENT être surchargés) :

form, input, textarea, select, checkbox, radio

table, thead, tbody, td, th

list-group, list-group-item

card, modal, offcanvas, tooltip, popover

btn, btn-outline-*, btn-lg, btn-sm

progress, switch, accordion, dropdown, tab-pane

Restent en Bootstrap natif (utilitaires et layout) :

container, row, col, g-, text-*, bg-*

alert, badge, spinner, breadcrumb, pagination

🧱 6. Structure technique
a) HTML
html
Copier
Modifier
<div id="style-panel" class="offcanvas clay-card glassmorphic">
  <h5>🎨 Personnaliser l’apparence</h5>
  <label for="blur">Flou arrière-plan</label>
  <input type="range" id="blur" min="0" max="20" value="5" />

  <label for="opacity">Opacité</label>
  <input type="range" id="opacity" min="0.1" max="1" step="0.1" value="0.7" />

  <label for="theme">Thème</label>
  <select id="theme">
    <option value="glass">Glass Pur</option>
    <option value="clay-light">Clay Clair</option>
    <option value="clay-dark">Clay Foncé</option>
    <option value="custom">Personnalisé</option>
  </select>

  <button class="btn client-btn mt-3" onclick="applyStyle()">Appliquer</button>
</div>
b) CSS (extrait)
css
Copier
Modifier
:root {
  --client-blur: 8px;
  --client-opacity: 0.6;
  --client-radius: 16px;
  --client-shadow: 4px 4px 10px rgba(0,0,0,0.1);
}

.client-zone input,
.client-zone select,
.client-zone textarea {
  background: rgba(255,255,255,var(--client-opacity));
  border-radius: var(--client-radius);
  box-shadow: var(--client-shadow);
  backdrop-filter: blur(var(--client-blur));
  border: none;
}
🔗 7. API REST (exemples)
Endpoint	Méthode	Description
/api/user-style	GET	Récupère le style actuel
/api/user-style	POST	Sauvegarde les préférences
/api/themes	GET	Retourne les thèmes disponibles
/api/reset-style	POST	Réinitialise les styles utilisateur

📈 8. KPI et Suivi UX
Indicateur	Objectif
Taux d’activation du style	≥ 75% utilisateurs actifs
Temps de personnalisation moyen	< 60 sec
Satisfaction post-style (enquête)	≥ 90% positive
Revenir au thème par défaut	< 5% (indicateur d'efficacité du design par défaut)