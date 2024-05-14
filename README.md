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
   - Notre programme demande à GPT-4 via son API une description hyper détailler de l'image que nous avons publié.

    <p align="center"><br>
        <img src="/image/chien_chat_reference.png" alt="Image de référence" style="width:25%; height:auto;">
    </p><br>
   
2. **Traitement par GPT-4**

   - Après une analyse approfondie de notre image, nous recevons un retour détaillé comprenant une description exhaustive.

3. **Prompt de Modification**

   - La description de l'image est intégrée à un prompt personnalisé afin de créer une consigne détaillée à soumettre à Dall-E pour la génération d'une image modifiée.
    > Add a hat on the cat and glasses on the dog
4. **Traitement par DALL-E**

   - Dall-E reçoit le prompt final et procède à la génération d'une nouvelle image, s'appuyant sur l'image d'origine et tenant compte des modifications spécifiées.
    <p align="center"><br>
        <img src="/image/chien_chat_reference.png" alt="Image de référence" style="width:25%; height:auto;">
    </p><br>
