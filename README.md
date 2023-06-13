
# Twith-live !

Twith-live est un script qu'il vous permet d'envoyer un message sur votre serveur discord quand vous êtes en stream ou que votre streamer choisi est en stream avec un webhook discord,Il suffit s'implement de remplacer le nom du streamer ou si vous voulez le message envoyer par le webhook discord , Le script est souvent mis à jours.

## Utilisation du programme

### Configuration

Avant de lancer le programme, vous devez configurer les paramètres dans le fichier `main.py`. Les paramètres disponibles sont :

- `"webhooks"` : le webhooks dans la classe Start à remplacer par le votre pour recevoir le message embed
- `"name_twith "` : le nom twith dans la classe Start qui doit être remplacé par le nom de votre twith ou streamer 
- `"ur_message "` : le contenue de votre message , ce que vous voulez envoyer quand vous livez ou que le streamer live

Vous devez remplir les champs correspondants dans le fichier `main.py` avant d'exécuter le programme.

## ✔️Exigences

 - Python >= 3.10

## ⚙️Installation



```bash
# clone the repo
$ git clone https://github.com/Tokaref/Twith-live.git

# change the working directory to Toka-Master
$ cd Twith-live

# install the requirements
$ python3 -m pip install -r requirements.txt
```
    
## Usage

```bash
python3 main.py

```
