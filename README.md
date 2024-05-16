# AlterImage

## Introduction
Notre équipe a développé un programme en Python qui offre à l'utilisateur la possibilité de personnaliser des images de son choix. Grâce à une série d'étapes coordonnées, le programme utilise des technologies de pointe telles que GPT-4 et DALL-E pour analyser, transformer et générer des images selon les préférences spécifiques de l'utilisateur. Ce processus méticuleux garantit une expérience de modification d'image précise et personnalisée.

## Méthodologie

### Technologies Utilisées
- Langage de programmation : Python
- Environnement de développement : Visual Studio Code
- API OpenAI Utilisée :
    - Dall-E
        - Model : Dall-E-3
    - GPT
        - GPT4

### Documentation de Référence
Nous nous sommes appuyés sur les documents suivants pour comprendre et implémenter notre solution :
- [Documentation sur la génération d'images via Dall-E](https://platform.openai.com/docs/guides/images)
- [Documentation sur l'utilisation de l'API d'OpenAI](https://platform.openai.com/docs/api-reference/images)
- [Documentation sur l'utilisation de GPT Vision](https://platform.openai.com/docs/guides/vision)
- Inspiration de retour utilisateurs sur Reddit

## Implémentation

### Développement du Programme
Notre équipe a développé un programme en langage Python qui permet à l'utilisateur de sélectionner une image de son choix et de saisir les modifications qu'il souhaite lui apporter. Ce processus s'articule en plusieurs étapes distinctes :

1. L'image sélectionnée est soumise à une analyse approfondie par le biais de l'API de GPT-4, permettant ainsi d'obtenir une description extrêmement détaillée de ses caractéristiques et de son contenu.

2. Les instructions de modification fournies par l'utilisateur sont renvoyées à GPT, accompagnées de la description détaillée de l'image obtenue à l'étape précédente. Ces éléments sont fusionnés pour former un prompt complet, combinant les détails spécifiques de l'image avec les demandes de modification de l'utilisateur.

3. Enfin, le prompt généré est transmis à DALL-E, déclenchant le processus de génération d'une nouvelle image. DALL-E utilise ce prompt pour créer une image personnalisée, intégrant les modifications spécifiées par l'utilisateur tout en conservant les caractéristiques fondamentales de l'image d'origine.


### Workflow
1. **Sélection de l'image et des modifications par l'utilisateur**
   - Avant de débuter le processus de modification, l'utilisateur est invité à choisir une image de son choix et à spécifier les modifications qu'il souhaite y apporter.

<div>
    <p align="center">
        <code>Add a hat on the cat and glasses on the dog</code>
    </p>
    <p align="center">
        <img src="/image/chien_chat_reference.png" alt="Image de référence" style="width:25%; height:auto;">
    </p>
</div>

2. **Soumission de l'Image et du Texte Descriptif**
   - Notre programme demande à GPT-4 via son API une description hyper détailler de l'image que nous avons publié.
  
3. **Traitement par GPT-4**

   - Après une analyse approfondie de notre image, nous recevons un retour détaillé comprenant une description exhaustive.

```
The picture is a very close-up, highly detailed, realistic photograph featuring the faces of a cat and a dog, placed side by side. Both animals are looking directly at the camera, creating a sense of intimacy and engagement with the viewer. The background is softly out of focus, consisting of warm, amber tones with a soft bokeh effect, highlighting the subjects and adding to the warm ambiance of the image.

**Description of the Cat:**
- **Fur and Coloring:** The cat has a dense, short to medium-length fur coat. The fur is primarily light brown with subtle, creamy white patches, particularly around the chest, lower face, and paws. The cat's facial fur, especially above the eyes, is slightly darker, giving it a slightly marked expression.
- **Eyes:** Its large eyes are deep, expressive, and slightly narrowed, suggesting a calm or curious demeanor. The irises are a striking gold or amber color, which stands out vividly against the fur.
- **Ears:** The cat’s ears are pointed and upright, with fur that is slightly lighter on the insides compared to the outer ear. One ear is slightly tilted forward, adding a sense of alertness.
- **Nose and Whiskers:** The cat’s nose is small and pink, positioned centrally on its face. Whiskers are long, thin, and white, extending outward from the cheeks in delicate curves.
- **Paw:** The cat’s raised paw, prominently in the foreground, is detailed. The paw pads are pink, which contrasts with the white fur covering the rest of the paw. The claws are retracted, giving a soft appearance.

**Description of the Dog:**
- **Breed and Fur:** The dog appears to be a breed with a thick, short to medium-length coat, such as a Corgi. The fur is primarily tricolored - black, white, and brown. The white fur covers the snout, chest, and parts of the face, while the brown fur highlights areas around the eyes, ears, and sides of the face.
- **Eyes:** The dog’s eyes are large, dark brown, and glossy, conveying a friendly and gentle expression. The eyes catch the light, adding a sparkle that increases the sense of realism.
- **Nose and Muzzle:** The dog has a black nose, positioned centrally on its face. Its muzzle is white, and the mouth is slightly open, hinting at either a relaxed or mildly curious disposition.
- **Ears:** The ears are large, upright, and pointy, typical of a Corgi, with the inner parts lighter in color compared to the outer fur. One ear slightly tilts, mirroring the expression of curiosity and attentiveness.       

**General Composition:**
- The lighting in the photograph is soft, warm, and natural, which enhances the colors of the animals' fur and eyes. The detailed textures of the fur, the glossiness of the eyes, and the subtlety of the background bokeh add a high level of realism.
- The overall mood of the photograph is one of warmth, comfort, and companionship, capturing a candid moment shared between two animals. The image's clarity and focus on the subjects' faces draw the viewer in, emphasizing the connection and tenderness between the cat and dog.

The photograph could be a cherished, spontaneous moment of interaction between pet companions, artistically captured with professional equipment to highlight their endearing traits and the subtle beauty in their expressions.
```

4. **Prompt de Modification**

   - La description de l'image est intégrée à un prompt personnalisé afin de créer une consigne détaillée à soumettre à Dall-E pour la génération d'une image modifiée.<br>
     &emsp;Rappel du prompt : ```Add a hat on the cat and glasses on the dog```

```
The picture is a very close-up, highly detailed, realistic photograph featuring the faces of a cat and a dog, placed side by side. Both animals are looking directly at the camera, creating a sense of intimacy and engagement with the viewer. The background is softly out of focus, consisting of warm, amber tones with a soft bokeh effect, highlighting the subjects and adding to the warm ambiance of the image.

**Description of the Cat:**
- **Fur and Coloring:** The cat has a dense, short to medium-length fur coat. The fur is primarily light brown with subtle, creamy white patches, particularly around the chest, lower face, and paws. The cat's facial fur, especially above the eyes, is slightly darker, giving it a slightly marked expression.
- **Eyes:** Its large eyes are deep, expressive, and slightly narrowed, suggesting a calm or curious demeanor. The irises are a striking gold or amber color, which stands out vividly against the fur.
- **Ears:** The cat's ears are pointed and upright, with fur that is slightly lighter on the insides compared to the outer ear. One ear is slightly tilted forward, adding a sense of alertness.
- **Nose and Whiskers:** The cat's nose is small and pink, positioned centrally on its face. Whiskers are long, thin, and white, extending outward from the cheeks in delicate curves.
- **Paw:** The cat's raised paw, prominently in the foreground, is detailed. The paw pads are pink, which contrasts with the white fur covering the rest of the paw. The claws are retracted, giving a soft appearance.
- **Hat:** Perched atop the cat's head is a stylish, miniature top hat. The hat is black with a small decorative band, adding a whimsical touch to the cat's appearance.

**Description of the Dog:**
- **Breed and Fur:** The dog appears to be a breed with a thick, short to medium-length coat, such as a Corgi. The fur is primarily tricolored - black, white, and brown. The white fur covers the snout, chest, and parts of the face, while the brown fur highlights areas around the eyes, ears, and sides of the face.
- **Eyes:** The dog's eyes are large, dark brown, and glossy, conveying a friendly and gentle expression. The eyes catch the light, adding a sparkle that increases the sense of realism.
- **Nose and Muzzle:** The dog has a black nose, positioned centrally on its face. Its muzzle is white, and the mouth is slightly open, hinting at either a relaxed or mildly curious disposition.
- **Ears:** The ears are large, upright, and pointy, typical of a Corgi, with the inner parts lighter in color compared to the outer fur. One ear slightly tilts, mirroring the expression of curiosity and attentiveness.       
- **Glasses:** The dog sports a pair of round, sleek glasses on its face. The glasses have thin frames and add a touch of charm and sophistication to the dog's already endearing features.

**General Composition:**
- The lighting in the photograph is soft, warm, and natural, which enhances the colors of the animals' fur and eyes. The detailed textures of the fur, the glossiness of the eyes, and the subtlety of the background bokeh add a high level of realism.
- The overall mood of the photograph is one of warmth, comfort, and companionship, capturing a candid moment shared between two animals. The image's clarity and focus on the subjects' faces draw the viewer in, emphasizing the connection and tenderness between the cat and dog.
- The photograph could be a cherished, spontaneous moment of interaction between pet companions, artistically captured with professional equipment to highlight their endearing traits and the subtle beauty in their expressions.
A highly detailed, close-up, realistic photograph features the faces of a light brown cat sporting a miniature black top hat and a Tricolored Corgi dog, both looking directly into the camera. The background consists of out of focus, warm, amber tones adding a soft bokeh effect. The cat's striking gold eyes contrast against its light brown and creamy white patched fur. The Corgi's large, glossy dark brown eyes look friendly and gentle against its black, white, and brown fur. The cat's one paw, with pink pads and white fur, is raised and the dog wears round sleek glasses. The image exudes a sense of warmth, comfort, and companionship.
```
 
5. **Traitement par DALL-E**

   - Dall-E reçoit le prompt final et procède à la génération d'une nouvelle image, s'appuyant sur l'image d'origine et tenant compte des modifications spécifiées.
    <p align="center"><br>
        <img src="/image/chien_chat_final.png" alt="Image de référence" style="width:25%; height:auto;">
    </p><br>



---

## Difficultés rencontré

    - Dall-E ne peut pas à lui seul faire de transfert de style, seulement de la génération via prompt ou une variation aléatoire (pas de possibilité de prompt), nous avons donc du rajouter des étapes en utilisant GPT-4 afin de pouvoir généré des images fidèle à celle d'origine.
