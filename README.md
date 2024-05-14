# AlterImage

## Introduction
Dans le cadre de ce projet, notre équipe travaille sur l'utilisation de l'API Dall-E de OpenAI pour générer des images à partir de descriptions textuelles. L'objectif est de soumettre une image accompagnée d'un texte descriptif à l'API, qui retournera une image modifiée selon les spécifications fournies.

## Méthodologie

### Technologies Utilisées
- Langage de programmation : Python
- Environnement de développement : Visual Studio Code
- API Utilisée : OpenAI
    - Model : Dall-E-3

### Documentation de Référence
Nous nous sommes appuyés sur les documents suivants pour comprendre et implémenter notre solution :
- [Documentation sur la génération d'images via Dall-E](https://platform.openai.com/docs/guides/images)
- [Documentation sur l'utilisation de l'API d'OpenAI](https://platform.openai.com/docs/api-reference/images)

## Implémentation

### Développement du Programme
Nous avons développé un programme en Python qui interagit avec l'API Dall-E pour générer des images selon les spécifications fournies. Le programme utilise les bibliothèques Python nécessaires pour effectuer des requêtes HTTP et traiter les données JSON renvoyées par l'API.

### Workflow
1. **Soumission de l'Image et du Texte Descriptif**
   - Notre programme envoie une image ainsi qu'un texte descriptif à l'API Dall-E.
    <center>
        <img src="/image/chien_chat_reference.png" alt="Image de référence" style="width:25%; height:auto;">
    </center>



    
2. **Traitement par Dall-E**
   - L'API Dall-E traite la demande et génère une nouvelle image en fonction du texte descriptif.
3. **Réception de l'Image Modifiée**
   - Notre programme reçoit l'image générée par Dall-E et la stocke localement.

## Exemple d'Utilisation

```python
import requests

# URL de l'API Dall-E
api_url = "https://api.openai.com/v1/images/dalle-3/complete"

# Données d'entrée : image et texte descriptif
input_data = {
    "image": "chemin/vers/image.jpg",
    "prompt": "Un chat levant la patte et un chien sur un fond jaune dans un style osier. Je veux que le chat ait un chapeau."
}

# Clé d'API OpenAI
api_key = "YOUR_API_KEY"

# Envoi de la requête à l'API Dall-E
response = requests.post(api_url, json=input_data, headers={"Authorization": f"Bearer {api_key}"})

# Traitement de la réponse
if response.status_code == 200:
    # Récupération de l'image générée
    generated_image = response.json()["output"]["image"]
    # Affichage ou sauvegarde de l'image
else:
    print("Erreur lors de la requête à l'API Dall-E:", response.text)
