###################################################################################################
############################################# MODULES #############################################
###################################################################################################

from openai import OpenAI
from base64 import b64decode, b64encode
from tkinter.filedialog import askopenfilename

###################################################################################################
############################################ FONCTIONS ############################################
###################################################################################################

"""
    Fonction qui va encoder une image pour la rendre lisible par le programme

    Argument(s) :
        - image_path (String) => Le chemin de l'image à encoder

    Return(s) :
        - La version encodée de l'image en entrée
"""
def encode_image(image_path):
    # On ouvre l'image en entrée en mode lecture
    with open(image_path, "rb") as image_file:
        # On retourne la version encodée de l'image en entrée
        return b64encode(image_file.read()).decode('utf-8')

###################################################################################################
############################################ VARIABLES ############################################
###################################################################################################

# On initialise le client OpenAI avec la clé API
client = OpenAI(
    api_key="sk-proj-HwcgeNNTTg0PPl8bSE95T3BlbkFJgzf4uJqeh04rJtppKOHi",
)

# On ouvre un explorateur de fichier pour choisir l'image à modifier
image_path = askopenfilename(filetypes=[("Images files", ".png .jpg .jpeg")])
# On encode l'image pour qu'elle soit lisible par le programme
base64_image = encode_image(image_path)

# On demande une entrée à l'utilisateur pour qu'il décrive sa modification dans l'image
mod_text = input("Describe the modification you want on the image :\n")

###################################################################################################
############################################ PROGRAMME ############################################
###################################################################################################

# On crée un client de chat GPT-4 avec la fonction Vision pour pouvoir descrire l'image de base
response = client.chat.completions.create(
    model = "gpt-4o",
    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text", 
                    # On fait en sorte que GPT-4 nous fasse la description la plus détaillée de l'image afin d'avoir un meilleur résultat
                    "text": "Make an exaustive, verbose, description of the picture.\
                     One should be able to precisely paint picture without seeing it, just by reading your text.\
                     Don't forget to describe the style of the picture, if its realitic, drawn, etc."
                },
                {
                    "type": "image_url", 
                    # On envoie l'image à modifier dans le prompt
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{base64_image}"
                    }
                }
            ]
        }
    ],
    max_tokens=1000,
)

# On récupère la description de l'image faite par GPT-4
base_text = response.choices[0].message.content

# On crée un client de chat GPT-4 pour pouvoir descrire l'image avec la modification que l'on veut
response = client.chat.completions.create(
    model = "gpt-4o",
    messages = [
        {
            "role": "system", 
            # On fait en sorte que GPT-4 nous fasse la description la plus détaillée de l'image, sans perdre de précision avec la description précedente
            "content": "You must have the same precision on our output that in the base description of the image.\
             Make an exaustive, verbose, description of the picture. One should be able to precisely paint picture without seeing it, just by reading your text.\
             Don't forget to describe the style of the picture, if its realitic, drawn, etc.\
             You must repeat the base description of the image, adding the modification asked. DON'T LOSE any details on the descriptions."
        },
        {
            "role": "user", 
            # On demande à GPT-4 de fusionner la description de base avec la modification demandée par l'utilisateur
            "content": f"This is the description of an image : \"{base_text}\". Describe it again with the asked modification : \"{mod_text}\""
        }
    ]
)

# On récupère la nouvelle description de l'image avec les modification faites par GPT-4
new_image = response.choices[0].message.content

# On crée un client DALL-E pour pouvoir générer l'image modifiée
response = client.images.generate(
    model="dall-e-3",
    prompt=new_image,
    response_format="b64_json",
    quality="standard",
    size="1024x1024",
    n=1,
)

# On crée un fichier "output.png" où on va enresgistrer l'image générée par DALL-E
with open("output.png", "wb") as image:
    # On écrit dans le fichier l'image que l'on décode
    image.write(b64decode(response.data[0].b64_json))

# On affiche dans la console la description de l'image faite par DALL-E
print("\n" + response.data[0].revised_prompt)