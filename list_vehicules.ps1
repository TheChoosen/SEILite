# Script pour lister les véhicules et leurs IDs
try {
    $response = Invoke-WebRequest -Uri "http://127.0.0.1:5000/vehicules/api"
    Write-Output "API Response Status: $($response.StatusCode)"
    Write-Output "Content: $($response.Content)"
} catch {
    Write-Output "Erreur API: $($_.Exception.Message)"
    Write-Output "Essayons la page normale..."
    
    # Essayons la page normale et cherchons des liens vers des véhicules
    $listResponse = Invoke-WebRequest -Uri "http://127.0.0.1:5000/vehicules/"
    $links = $listResponse.Links | Where-Object { $_.href -match "/vehicules/\d+" }
    if ($links) {
        Write-Output "Véhicules trouvés:"
        $links | ForEach-Object { 
            Write-Output "ID: $($_.href.Split('/')[-1])"
        }
    } else {
        Write-Output "Aucun véhicule trouvé dans la liste"
    }
}
