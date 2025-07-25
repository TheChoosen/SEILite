/**
 * JavaScript pour le module Documents commerciaux - SEILite
 * Gestion des interactions, calculs et validations
 */

// Configuration globale du module documents
const DocumentsModule = {
    // Configuration des modules et types
    modules: {
        'PI': { label: 'Pièces détachées', icon: 'fas fa-cog', color: '#17a2b8' },
        'WO': { label: 'Bon de travail', icon: 'fas fa-tools', color: '#fd7e14' },
        'LO': { label: 'Location', icon: 'fas fa-calendar-alt', color: '#20c997' },
        'VE': { label: 'Vente équipement', icon: 'fas fa-handshake', color: '#6f42c1' }
    },
    
    // Configuration des statuts
    statuts: {
        'BROUILLON': { label: 'Brouillon', color: 'secondary' },
        'CONFIRME': { label: 'Confirmé', color: 'info' },
        'EN_COURS': { label: 'En cours', color: 'warning' },
        'TERMINE': { label: 'Terminé', color: 'success' },
        'ANNULE': { label: 'Annulé', color: 'danger' },
        'FACTURE': { label: 'Facturé', color: 'primary' }
    },
    
    // Variables globales
    ligneIndex: 0,
    documentData: {},
    
    // Initialisation du module
    init: function() {
        this.initEventListeners();
        this.initTooltips();
        this.initDataTables();
        this.loadInitialData();
    },
    
    // Initialisation des écouteurs d'événements
    initEventListeners: function() {
        // Navigation et filtres
        $(document).on('change', '#moduleSelector', this.onModuleChange);
        $(document).on('change', '#typeSelector', this.onTypeChange);
        $(document).on('change', '#statutSelector', this.onStatutChange);
        $(document).on('click', '.btn-filter', this.applyFilters);
        $(document).on('click', '.btn-reset-filters', this.resetFilters);
        
        // Gestion des lignes de document
        $(document).on('click', '.btn-add-ligne', this.ajouterLigne);
        $(document).on('click', '.btn-remove-ligne', this.supprimerLigne);
        $(document).on('change', '.ligne-input', this.onLigneChange);
        $(document).on('blur', '.ligne-input', this.calculerLigne);
        
        // Recherche et sélection
        $(document).on('input', '#rechercheClientInput', this.rechercherClients);
        $(document).on('input', '#rechercheProduitInput', this.rechercherProduits);
        $(document).on('click', '.client-item', this.selectionnerClient);
        $(document).on('click', '.produit-item', this.selectionnerProduit);
        
        // Calculs automatiques
        $(document).on('change', '#remiseGlobale, #tauxTVA', this.calculerTotaux);
        $(document).on('change', '#date_debut, #date_fin', this.calculerDureeLocation);
        
        // Actions sur les documents
        $(document).on('click', '.btn-save-document', this.sauvegarderDocument);
        $(document).on('click', '.btn-confirm-document', this.confirmerDocument);
        $(document).on('click', '.btn-convert-document', this.convertirDocument);
        $(document).on('click', '.btn-duplicate-document', this.dupliquerDocument);
        $(document).on('click', '.btn-cancel-document', this.annulerDocument);
        
        // Prévisualisation et impression
        $(document).on('click', '.btn-preview', this.previsualiserDocument);
        $(document).on('click', '.btn-print', this.imprimerDocument);
        $(document).on('click', '.btn-email', this.envoyerEmail);
        $(document).on('click', '.btn-export-pdf', this.exporterPDF);
    },
    
    // Initialisation des tooltips
    initTooltips: function() {
        $('[data-bs-toggle="tooltip"]').tooltip();
    },
    
    // Initialisation des DataTables
    initDataTables: function() {
        if ($('#documentsTable').length) {
            $('#documentsTable').DataTable({
                language: {
                    url: '//cdn.datatables.net/plug-ins/1.13.4/i18n/fr-FR.json'
                },
                pageLength: 25,
                responsive: true,
                order: [[0, 'desc']], // Tri par défaut sur la première colonne (numéro)
                columnDefs: [
                    { targets: [-1], orderable: false } // Désactiver le tri sur la colonne Actions
                ]
            });
        }
    },
    
    // Chargement des données initiales
    loadInitialData: function() {
        this.chargerStatistiques();
        this.chargerDocumentsRecents();
    },
    
    // === Gestion des filtres ===
    onModuleChange: function() {
        const module = $(this).val();
        DocumentsModule.chargerTypesModule(module);
        DocumentsModule.applyFilters();
    },
    
    onTypeChange: function() {
        DocumentsModule.applyFilters();
    },
    
    onStatutChange: function() {
        DocumentsModule.applyFilters();
    },
    
    chargerTypesModule: function(module) {
        const types = {
            'PI': [
                { value: 'SOU', label: 'Soumission pièces' },
                { value: 'COM', label: 'Commande pièces' },
                { value: 'FAC', label: 'Facture pièces' }
            ],
            'WO': [
                { value: 'SOU', label: 'Soumission travail' },
                { value: 'COM', label: 'Ordre de travail' },
                { value: 'FAC', label: 'Facture travail' }
            ],
            'LO': [
                { value: 'SOU', label: 'Soumission location' },
                { value: 'COM', label: 'Contrat location' },
                { value: 'FAC', label: 'Facture location' }
            ],
            'VE': [
                { value: 'SOU', label: 'Soumission vente' },
                { value: 'COM', label: 'Commande vente' },
                { value: 'FAC', label: 'Facture vente' }
            ]
        };
        
        const typeSelector = $('#typeSelector');
        typeSelector.empty();
        typeSelector.append('<option value="">Tous les types</option>');
        
        if (types[module]) {
            types[module].forEach(type => {
                typeSelector.append(`<option value="${type.value}">${type.label}</option>`);
            });
        }
    },
    
    applyFilters: function() {
        const filters = {
            module: $('#moduleSelector').val(),
            type: $('#typeSelector').val(),
            statut: $('#statutSelector').val(),
            dateDebut: $('#dateDebutFilter').val(),
            dateFin: $('#dateFinFilter').val(),
            client: $('#clientFilter').val()
        };
        
        // Appliquer les filtres via AJAX
        $.get('/documents/liste', filters)
            .done(function(data) {
                $('#documentsContainer').html($(data).find('#documentsContainer').html());
                DocumentsModule.initDataTables();
            })
            .fail(function() {
                DocumentsModule.showAlert('danger', 'Erreur lors du filtrage des documents');
            });
    },
    
    resetFilters: function() {
        $('#moduleSelector, #typeSelector, #statutSelector').val('');
        $('#dateDebutFilter, #dateFinFilter, #clientFilter').val('');
        DocumentsModule.applyFilters();
    },
    
    // === Gestion des lignes de document ===
    ajouterLigne: function() {
        // Supprimer la ligne vide si elle existe
        $('.ligne-vide').remove();
        
        const html = `
            <tr data-ligne-index="${DocumentsModule.ligneIndex}">
                <td>${DocumentsModule.ligneIndex + 1}</td>
                <td>
                    <input type="text" class="form-control form-control-sm ligne-input" 
                           name="lignes[${DocumentsModule.ligneIndex}][code_produit]" 
                           data-field="code_produit">
                </td>
                <td>
                    <input type="text" class="form-control form-control-sm ligne-input" 
                           name="lignes[${DocumentsModule.ligneIndex}][designation]" 
                           data-field="designation" required>
                </td>
                <td>
                    <input type="number" class="form-control form-control-sm text-center ligne-input" 
                           name="lignes[${DocumentsModule.ligneIndex}][quantite]" 
                           data-field="quantite" value="1" step="0.01" min="0" required>
                </td>
                <td>
                    <input type="text" class="form-control form-control-sm ligne-input" 
                           name="lignes[${DocumentsModule.ligneIndex}][unite]" 
                           data-field="unite" value="unité">
                </td>
                <td>
                    <input type="number" class="form-control form-control-sm text-end ligne-input" 
                           name="lignes[${DocumentsModule.ligneIndex}][prix_unitaire]" 
                           data-field="prix_unitaire" value="0" step="0.01" min="0" required>
                </td>
                <td>
                    <input type="number" class="form-control form-control-sm text-center ligne-input" 
                           name="lignes[${DocumentsModule.ligneIndex}][remise_pourcentage]" 
                           data-field="remise_pourcentage" value="0" step="0.1" min="0" max="100">
                </td>
                <td class="text-end">
                    <span class="total-ligne">0.00</span> €
                </td>
                <td>
                    <button type="button" class="btn btn-sm btn-outline-danger btn-remove-ligne">
                        <i class="fas fa-trash"></i>
                    </button>
                </td>
            </tr>
        `;
        
        $('#lignesContainer').append(html);
        DocumentsModule.ligneIndex++;
        DocumentsModule.renumeroterLignes();
    },
    
    supprimerLigne: function() {
        $(this).closest('tr').remove();
        DocumentsModule.renumeroterLignes();
        DocumentsModule.calculerTotaux();
        
        // Ajouter ligne vide si aucune ligne
        if ($('#lignesContainer tr').length === 0) {
            $('#lignesContainer').html(`
                <tr class="ligne-vide">
                    <td colspan="9" class="text-center py-4">
                        <em>Aucune ligne. Cliquez sur "Ajouter une ligne" pour commencer.</em>
                    </td>
                </tr>
            `);
        }
    },
    
    renumeroterLignes: function() {
        $('#lignesContainer tr:not(.ligne-vide)').each(function(index) {
            $(this).find('td:first').text(index + 1);
            $(this).attr('data-ligne-index', index);
            
            // Mettre à jour les noms des champs
            $(this).find('input').each(function() {
                const name = $(this).attr('name');
                if (name) {
                    const newName = name.replace(/lignes\[\d+\]/, `lignes[${index}]`);
                    $(this).attr('name', newName);
                }
            });
        });
    },
    
    onLigneChange: function() {
        const field = $(this).data('field');
        
        // Recherche automatique de produit si code saisi
        if (field === 'code_produit') {
            DocumentsModule.rechercherProduitParCode($(this));
        }
        
        // Recalculer la ligne si c'est un champ numérique
        if (['quantite', 'prix_unitaire', 'remise_pourcentage'].includes(field)) {
            DocumentsModule.calculerLigne($(this));
        }
    },
    
    calculerLigne: function(input) {
        const row = $(input).closest('tr');
        const quantite = parseFloat(row.find('input[data-field="quantite"]').val()) || 0;
        const prixUnitaire = parseFloat(row.find('input[data-field="prix_unitaire"]').val()) || 0;
        const remisePourcentage = parseFloat(row.find('input[data-field="remise_pourcentage"]').val()) || 0;
        
        const sousTotal = quantite * prixUnitaire;
        const montantRemise = sousTotal * (remisePourcentage / 100);
        const total = sousTotal - montantRemise;
        
        row.find('.total-ligne').text(total.toFixed(2));
        DocumentsModule.calculerTotaux();
    },
    
    // === Calculs des totaux ===
    calculerTotaux: function() {
        let totalHT = 0;
        
        // Calculer le total HT
        $('#lignesContainer .total-ligne').each(function() {
            totalHT += parseFloat($(this).text()) || 0;
        });
        
        // Remise globale
        const remiseGlobalePourcentage = parseFloat($('#remiseGlobale').val()) || 0;
        const montantRemiseGlobale = totalHT * (remiseGlobalePourcentage / 100);
        const totalApresRemise = totalHT - montantRemiseGlobale;
        
        // TVA
        const tauxTVA = parseFloat($('#tauxTVA').val()) || 0;
        const montantTVA = totalApresRemise * (tauxTVA / 100);
        const totalTTC = totalApresRemise + montantTVA;
        
        // Mettre à jour l'affichage
        $('#totalHT').text(totalHT.toFixed(2));
        $('#montantRemise').text(montantRemiseGlobale.toFixed(2));
        $('#totalApresRemise').text(totalApresRemise.toFixed(2));
        $('#montantTVA').text(montantTVA.toFixed(2));
        $('#totalTTC').text(totalTTC.toFixed(2));
        
        // Sauvegarder les données
        DocumentsModule.documentData.totaux = {
            totalHT: totalHT,
            remiseGlobale: montantRemiseGlobale,
            totalApresRemise: totalApresRemise,
            montantTVA: montantTVA,
            totalTTC: totalTTC
        };
    },
    
    calculerDureeLocation: function() {
        const dateDebut = $('#date_debut').val();
        const dateFin = $('#date_fin').val();
        
        if (dateDebut && dateFin) {
            const debut = new Date(dateDebut);
            const fin = new Date(dateFin);
            const diffTime = Math.abs(fin - debut);
            const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));
            $('#duree_location').val(diffDays);
        }
    },
    
    // === Recherche et sélection ===
    rechercherClients: function() {
        const terme = $(this).val();
        
        if (terme.length >= 2) {
            $.get('/documents/api/clients/rechercher', { terme: terme })
                .done(function(clients) {
                    let html = '';
                    clients.forEach(client => {
                        html += `
                            <div class="list-group-item list-group-item-action client-item" 
                                 data-client-id="${client.id}"
                                 data-client-nom="${client.nom}"
                                 data-client-adresse="${client.adresse || ''}"
                                 data-client-ville="${client.ville || ''}"
                                 data-client-code-postal="${client.code_postal || ''}"
                                 data-client-telephone="${client.telephone || ''}"
                                 data-client-email="${client.email || ''}">
                                <h6 class="mb-1">${client.nom}</h6>
                                <p class="mb-1">${client.adresse || ''} ${client.ville || ''}</p>
                                <small>${client.telephone || ''} ${client.email || ''}</small>
                            </div>
                        `;
                    });
                    $('#resultatsClients').html(html);
                })
                .fail(function() {
                    DocumentsModule.showAlert('danger', 'Erreur lors de la recherche de clients');
                });
        }
    },
    
    selectionnerClient: function() {
        const clientData = $(this).data();
        
        $('#client_id').val(clientData.clientId);
        $('#client_nom').val(clientData.clientNom);
        $('#client_adresse').val(clientData.clientAdresse);
        $('#client_ville').val(clientData.clientVille);
        $('#client_code_postal').val(clientData.clientCodePostal);
        $('#client_telephone').val(clientData.clientTelephone);
        $('#client_email').val(clientData.clientEmail);
        
        $('#modalRechercheClient').modal('hide');
    },
    
    rechercherProduitParCode: function(input) {
        const code = input.val();
        
        if (code.length >= 2) {
            $.get('/documents/api/produits/rechercher', { code: code })
                .done(function(produit) {
                    if (produit) {
                        const row = input.closest('tr');
                        row.find('input[data-field="designation"]').val(produit.designation);
                        row.find('input[data-field="prix_unitaire"]').val(produit.prix_vente);
                        row.find('input[data-field="unite"]').val(produit.unite);
                        DocumentsModule.calculerLigne(row.find('input[data-field="quantite"]'));
                    }
                });
        }
    },
    
    // === Actions sur les documents ===
    sauvegarderDocument: function(confirmer = false) {
        const formData = new FormData($('#documentForm')[0]);
        
        if (confirmer) {
            formData.set('statut', 'CONFIRME');
        }
        
        $.ajax({
            url: $('#documentForm').attr('action'),
            method: 'POST',
            data: formData,
            processData: false,
            contentType: false,
            beforeSend: function() {
                $('.btn-save-document, .btn-confirm-document').prop('disabled', true);
            },
            success: function(response) {
                if (response.success) {
                    DocumentsModule.showAlert('success', 'Document sauvegardé avec succès !');
                    setTimeout(() => {
                        window.location.href = '/documents/detail/' + response.document_id;
                    }, 1500);
                } else {
                    DocumentsModule.showAlert('danger', 'Erreur lors de la sauvegarde : ' + response.message);
                }
            },
            error: function() {
                DocumentsModule.showAlert('danger', 'Erreur de communication avec le serveur.');
            },
            complete: function() {
                $('.btn-save-document, .btn-confirm-document').prop('disabled', false);
            }
        });
    },
    
    confirmerDocument: function() {
        if (confirm('Êtes-vous sûr de vouloir confirmer ce document ?')) {
            DocumentsModule.sauvegarderDocument(true);
        }
    },
    
    convertirDocument: function() {
        const documentId = $(this).data('document-id');
        $('#modalConversion').modal('show');
        window.currentDocumentId = documentId;
    },
    
    // === Utilitaires ===
    showAlert: function(type, message) {
        const alertHtml = `
            <div class="alert alert-${type} alert-dismissible fade show" role="alert">
                ${message}
                <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
            </div>
        `;
        
        $('.container-fluid').prepend(alertHtml);
        
        setTimeout(() => {
            $('.alert').alert('close');
        }, 5000);
    },
    
    formatMontant: function(montant) {
        return parseFloat(montant).toLocaleString('fr-FR', {
            minimumFractionDigits: 2,
            maximumFractionDigits: 2
        });
    },
    
    formatDate: function(date) {
        return new Date(date).toLocaleDateString('fr-FR');
    },
    
    // === Chargement des données ===
    chargerStatistiques: function() {
        $.get('/documents/api/statistiques')
            .done(function(stats) {
                $('#statsTotal').text(stats.total || 0);
                $('#statsBrouillons').text(stats.brouillons || 0);
                $('#statsConfirmes').text(stats.confirmes || 0);
                $('#statsEnCours').text(stats.en_cours || 0);
            });
    },
    
    chargerDocumentsRecents: function() {
        $.get('/documents/api/recents')
            .done(function(documents) {
                let html = '';
                documents.forEach(doc => {
                    html += `
                        <div class="list-group-item">
                            <div class="d-flex justify-content-between align-items-center">
                                <div>
                                    <h6 class="mb-1">${doc.numero}</h6>
                                    <p class="mb-1">${doc.client_nom}</p>
                                    <small>${DocumentsModule.formatDate(doc.date_document)}</small>
                                </div>
                                <div>
                                    <span class="badge bg-${doc.statut_color}">${doc.statut_label}</span>
                                </div>
                            </div>
                        </div>
                    `;
                });
                $('#documentsRecents').html(html);
            });
    }
};

// Initialisation au chargement du document
$(document).ready(function() {
    DocumentsModule.init();
});

// Export pour utilisation globale
window.DocumentsModule = DocumentsModule;
