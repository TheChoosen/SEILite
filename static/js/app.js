// Gestion des Produits - JavaScript


document.addEventListener('DOMContentLoaded', function () {
  const settings = ['blur', 'opacity', 'radius'];
  settings.forEach(setting => {
    const input = document.getElementById(setting);
    if (input) {
      input.addEventListener('input', function () {
        document.documentElement.style.setProperty(`--client-${setting}`, input.value + (setting === 'opacity' ? '' : 'px'));
      });
    }
  });

  document.getElementById('theme')?.addEventListener('change', function (e) {
    const value = e.target.value;
    if (value === 'glass') {
      setTheme(8, 0.5, 16);
    } else if (value === 'clay-light') {
      setTheme(0, 1, 20);
    } else if (value === 'clay-dark') {
      setTheme(0, 0.9, 20);
    }
  });

  function setTheme(blur, opacity, radius) {
    document.documentElement.style.setProperty('--client-blur', blur + 'px');
    document.documentElement.style.setProperty('--client-opacity', opacity);
    document.documentElement.style.setProperty('--client-radius', radius + 'px');
  }
});


document.addEventListener('DOMContentLoaded', function() {
    // Auto-uppercase pour certains champs
    setupAutoUppercase();
    
    // Gestion des calculs automatiques
    setupAutoCalculations();
    
    // Prévisualisation des images
    setupImagePreview();
    
    // Validation des formulaires
    setupFormValidation();
    
    // Tooltips
    setupTooltips();
});

// Configuration de la mise en majuscules automatique
function setupAutoUppercase() {
    const upperCaseFields = document.querySelectorAll('input.bg-warning');
    upperCaseFields.forEach(field => {
        field.addEventListener('input', function() {
            const cursorPosition = this.selectionStart;
            const oldValue = this.value;
            const newValue = this.value.toUpperCase();
            
            if (oldValue !== newValue) {
                this.value = newValue;
                this.setSelectionRange(cursorPosition, cursorPosition);
            }
        });
    });
}

// Configuration des calculs automatiques
function setupAutoCalculations() {
    const coutRefField = document.querySelector('input[name="cout_reference"]');
    const coutTvfField = document.querySelector('input[name="cout_tvf"]');
    const prixRevientField = document.querySelector('input[name="prix_revient"]');
    const tvfSelect = document.querySelector('select[name="tvf"]');
    const tauxTvfField = document.querySelector('input[name="taux_taxe_fed"]');
    
    if (coutRefField && coutTvfField && prixRevientField) {
        // Calcul automatique du coût TVF
        function calculateCoutTvf() {
            const coutRef = parseFloat(coutRefField.value) || 0;
            const tvfActive = tvfSelect && tvfSelect.value === 'O';
            const tauxTvf = parseFloat(tauxTvfField?.value) || 0;
            
            if (tvfActive && tauxTvf > 0) {
                const coutTvf = coutRef * (1 + tauxTvf / 100);
                coutTvfField.value = coutTvf.toFixed(4);
            } else {
                coutTvfField.value = coutRef.toFixed(4);
            }
            
            calculatePrixRevient();
        }
        
        // Calcul automatique du prix de revient
        function calculatePrixRevient() {
            const coutTvf = parseFloat(coutTvfField.value) || 0;
            prixRevientField.value = coutTvf.toFixed(4);
        }
        
        // Attacher les événements
        coutRefField.addEventListener('input', calculateCoutTvf);
        if (tvfSelect) tvfSelect.addEventListener('change', calculateCoutTvf);
        if (tauxTvfField) tauxTvfField.addEventListener('input', calculateCoutTvf);
        coutTvfField.addEventListener('input', calculatePrixRevient);
    }
    
    // Calcul de la marge
    const coreValeurField = document.querySelector('input[name="core_valeur"]');
    const coreEscaladeField = document.querySelector('input[name="core_escalade"]');
    const margeField = document.querySelector('input[name="marge"]');
    
    if (coreValeurField && coreEscaladeField && margeField) {
        function calculateMarge() {
            const valeur = parseFloat(coreValeurField.value) || 0;
            const escalade = parseFloat(coreEscaladeField.value) || 0;
            const marge = valeur + escalade;
            margeField.value = marge.toFixed(4);
        }
        
        coreValeurField.addEventListener('input', calculateMarge);
        coreEscaladeField.addEventListener('input', calculateMarge);
    }
}

// Configuration de la prévisualisation des images
function setupImagePreview() {
    const imageInput = document.querySelector('input[type="file"][name="image"]');
    if (imageInput) {
        imageInput.addEventListener('change', function(e) {
            const file = e.target.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = function(e) {
                    // Créer ou mettre à jour l'aperçu
                    let preview = document.getElementById('image-preview');
                    if (!preview) {
                        preview = document.createElement('div');
                        preview.id = 'image-preview';
                        preview.className = 'mt-3';
                        imageInput.parentNode.appendChild(preview);
                    }
                    
                    preview.innerHTML = `
                        <label class="form-label">Aperçu:</label><br>
                        <img src="${e.target.result}" class="img-thumbnail" style="max-width: 200px; max-height: 200px;" alt="Aperçu de l'image">
                    `;
                };
                reader.readAsDataURL(file);
            }
        });
    }
}

// Configuration de la validation des formulaires
function setupFormValidation() {
    const forms = document.querySelectorAll('form[method="POST"]');
    
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            let isValid = true;
            const requiredFields = form.querySelectorAll('input[required]');
            
            // Nettoyer les erreurs précédentes
            form.querySelectorAll('.is-invalid').forEach(field => {
                field.classList.remove('is-invalid');
            });
            form.querySelectorAll('.invalid-feedback').forEach(feedback => {
                feedback.remove();
            });
            
            // Valider les champs requis
            requiredFields.forEach(field => {
                if (!field.value.trim()) {
                    isValid = false;
                    field.classList.add('is-invalid');
                    
                    const feedback = document.createElement('div');
                    feedback.className = 'invalid-feedback';
                    feedback.textContent = 'Ce champ est requis.';
                    field.parentNode.appendChild(feedback);
                }
            });
            
            // Valider le numéro de produit (unique)
            const numeroProduitField = form.querySelector('input[name="numero_produit"]');
            if (numeroProduitField && numeroProduitField.value.trim()) {
                const numero = numeroProduitField.value.trim();
                if (numero.length < 1 || numero.length > 30) {
                    isValid = false;
                    numeroProduitField.classList.add('is-invalid');
                    
                    const feedback = document.createElement('div');
                    feedback.className = 'invalid-feedback';
                    feedback.textContent = 'Le numéro de produit doit contenir entre 1 et 30 caractères.';
                    numeroProduitField.parentNode.appendChild(feedback);
                }
            }
            
            // Valider les champs numériques
            const numericFields = form.querySelectorAll('input[type="number"]');
            numericFields.forEach(field => {
                if (field.value && isNaN(parseFloat(field.value))) {
                    isValid = false;
                    field.classList.add('is-invalid');
                    
                    const feedback = document.createElement('div');
                    feedback.className = 'invalid-feedback';
                    feedback.textContent = 'Veuillez entrer une valeur numérique valide.';
                    field.parentNode.appendChild(feedback);
                }
            });
            
            if (!isValid) {
                e.preventDefault();
                
                // Faire défiler vers le premier champ avec erreur
                const firstError = form.querySelector('.is-invalid');
                if (firstError) {
                    firstError.scrollIntoView({ behavior: 'smooth', block: 'center' });
                    firstError.focus();
                }
                
                // Afficher une alerte générale
                showAlert('Veuillez corriger les erreurs dans le formulaire.', 'danger');
            } else {
                // Désactiver le bouton de soumission pour éviter les double-clics
                const submitBtn = form.querySelector('button[type="submit"]');
                if (submitBtn) {
                    submitBtn.disabled = true;
                    submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Traitement...';
                }
            }
        });
    });
}

// Configuration des tooltips
function setupTooltips() {
    // Initialiser les tooltips Bootstrap si disponibles
    if (typeof bootstrap !== 'undefined' && bootstrap.Tooltip) {
        const tooltipTriggerList = [].slice.call(document.querySelectorAll('[title]'));
        tooltipTriggerList.map(function(tooltipTriggerEl) {
            return new bootstrap.Tooltip(tooltipTriggerEl);
        });
    }
}

// Fonction utilitaire pour afficher des alertes
function showAlert(message, type = 'info') {
    const alertContainer = document.querySelector('main .container-fluid');
    if (!alertContainer) return;
    
    const alertDiv = document.createElement('div');
    alertDiv.className = `alert alert-${type} alert-dismissible fade show`;
    alertDiv.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    
    // Insérer l'alerte au début du contenu principal
    const firstChild = alertContainer.firstElementChild;
    alertContainer.insertBefore(alertDiv, firstChild);
    
    // Supprimer automatiquement après 5 secondes
    setTimeout(() => {
        if (alertDiv && alertDiv.parentNode) {
            alertDiv.remove();
        }
    }, 5000);
}

// Fonction utilitaire pour confirmer une action
function confirmAction(message, callback) {
    if (confirm(message)) {
        callback();
    }
}

// Gestionnaire pour les liens de navigation avec données non sauvegardées
function setupUnsavedChangesWarning() {
    let formChanged = false;
    const form = document.querySelector('form[method="POST"]');
    
    if (form) {
        const inputs = form.querySelectorAll('input, select, textarea');
        inputs.forEach(input => {
            input.addEventListener('change', () => {
                formChanged = true;
            });
        });
        
        // Avertir l'utilisateur avant de quitter la page
        window.addEventListener('beforeunload', (e) => {
            if (formChanged) {
                e.preventDefault();
                e.returnValue = 'Vous avez des modifications non sauvegardées. Êtes-vous sûr de vouloir quitter cette page ?';
                return e.returnValue;
            }
        });
        
        // Désactiver l'avertissement lors de la soumission du formulaire
        form.addEventListener('submit', () => {
            formChanged = false;
        });
    }
}

// Fonction pour formater les nombres
function formatNumber(value, decimals = 2) {
    if (!value || isNaN(value)) return '0.00';
    return parseFloat(value).toFixed(decimals);
}

// Fonction pour formater la devise
function formatCurrency(value) {
    return formatNumber(value, 2) + ' $';
}

// Recherche en temps réel (debounced)
function setupLiveSearch() {
    const searchInput = document.querySelector('input[name="search"]');
    if (!searchInput) return;
    
    let timeout;
    searchInput.addEventListener('input', function() {
        clearTimeout(timeout);
        timeout = setTimeout(() => {
            // Auto-submit du formulaire de recherche après 500ms d'inactivité
            const form = this.closest('form');
            if (form && this.value.length >= 2) {
                form.submit();
            }
        }, 500);
    });
}

// Raccourcis clavier
function setupKeyboardShortcuts() {
    document.addEventListener('keydown', function(e) {
        // Ctrl+S pour sauvegarder
        if (e.ctrlKey && e.key === 's') {
            e.preventDefault();
            const saveBtn = document.querySelector('button[type="submit"]');
            if (saveBtn) {
                saveBtn.click();
            }
        }
        
        // Ctrl+N pour nouveau
        if (e.ctrlKey && e.key === 'n') {
            e.preventDefault();
            const newBtn = document.querySelector('a[href*="nouveau"]');
            if (newBtn) {
                window.location.href = newBtn.href;
            }
        }
        
        // Échap pour annuler/retour
        if (e.key === 'Escape') {
            const cancelBtn = document.querySelector('a[href*="liste"]');
            if (cancelBtn) {
                window.location.href = cancelBtn.href;
            }
        }
    });
}

// Initialiser les fonctionnalités avancées
document.addEventListener('DOMContentLoaded', function() {
    setupUnsavedChangesWarning();
    setupLiveSearch();
    setupKeyboardShortcuts();
});
