# Script de test pour créer un véhicule de test
$body = @{
    'unite' = 'TEST002'
    'type' = 'CAMION'
    'statut' = 'INTERNE'
    'annee' = '2020'
    'marque' = 'Ford'
    'modele' = 'F-150'
    'prix' = '25000.00'
    'cout' = '20000.00'
    'nom' = 'Client Test'
    'email' = 'test@example.com'
    'tphone' = '555-1234'
    'remarque' = 'Véhicule de test créé automatiquement'
}

try {
    $response = Invoke-WebRequest -Uri "http://127.0.0.1:5000/vehicules/nouveau" -Method POST -Body $body
    Write-Output "Status: $($response.StatusCode)"
    Write-Output "Création réussie!"
    
    # Teste aussi la liste
    $listResponse = Invoke-WebRequest -Uri "http://127.0.0.1:5000/vehicules/"
    Write-Output "Liste Status: $($listResponse.StatusCode)"
    
} catch {
    Write-Output "Erreur: $($_.Exception.Message)"
}
