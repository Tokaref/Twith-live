import os
from time import sleep
import colorama
import requests
from colorama import Fore
import threading
import sys

colorama.init(autoreset=True)

os.system("title No-Name")

ROOT_PATH = os.chdir(os.path.dirname(os.path.abspath(__file__)))

class start():
    def __init__(self):
        name_twith = f"jokaa45"
        ur_message = f"**@everyone live :) chill**"
        link = f"https://www.twitch.tv/{name_twith}"
        webhook = "https://discord.com/api/webhooks/1118105377565835284/M0OiPktamV8Ddq4jqOwO7WxZ7elBUwhX5XviFpDWYu3_y8LWJerdHmuJe5Yn7HYtSdTt"
        self.name_twith = name_twith
        self.ur_message = ur_message
        self.link = link
        self.webhook = webhook
h1 = start()

def webhook():
    data = {
    "avatar_url":"https://play-lh.googleusercontent.com/QLQzL-MXtxKEDlbhrQCDw-REiDsA9glUH4m16syfar_KVLRXlzOhN7tmAceiPerv4Jg",
    "username": "Twith",
    "content": '{}'.format(h1.ur_message),
    "embeds": [{
    "color": 9371903,
    "description": '{}'.format(h1.name_twith) + " vient de lancer son stream !!\n",
    "url":'{}'.format(h1.link),
    "author": {
    "name": "Twith " +'{}'.format(h1.name_twith),
    "url": '{}'.format(h1.link),
    "icon_url": "https://play-lh.googleusercontent.com/QLQzL-MXtxKEDlbhrQCDw-REiDsA9glUH4m16syfar_KVLRXlzOhN7tmAceiPerv4Jg",
    },
 }]}
    requests.post('{}'.format(h1.webhook),json=data)
    
def live_site():
    while True:
        sleep(2)
        res = requests.get("https://www.twitch.tv/" + '{}'.format(h1.name_twith))
        if res.status_code == 200:
            if "live_user" in str(res.content):
                webhook()
                a = "100"
                if a == "100":
                    verif_live_discord()
            else:
                print(Fore.LIGHTRED_EX + "L'utilisateur selectionné n'est pas en stream")
                live_site()
        else:
            print(Fore.LIGHTRED_EX + "Probleme au niveau de la requêtes 200 ")
            live_site()

def verif_live_discord():
    while True:
        sleep(2)
        res = requests.get("https://www.twitch.tv/" + '{}'.format(h1.name_twith))
        if res.status_code == 200:
            if "live_user" in str(res.content):
                verif_live_discord()
            else:
                if res.status_code == 200:
                    if "live_user" in str(res.content):
                        verif_live_discord()
                    else:
                        if res.status_code == 200:
                            if "live_user" in str(res.content):
                                verif_live_discord()
                        else:
                            print(Fore.LIGHTRED_EX + "Probleme au niveau de la requêtes 200 ")
                            live_site()
                else:  
                    print(Fore.LIGHTRED_EX + "Probleme au niveau de la requêtes 200 ")
                    live_site()

def bloque_site():
    while True:
        sleep(6)
        res = requests.get("https://www.twitch.tv")
        if res.status_code == 200:
            bloque_site()
        else:
           sleep(1)
           if res.status_code == 200:
                bloque_site()
           else:
                print(Fore.LIGHTRED_EX + "REQUETE BLOQUE, USE VPN")
                sys.exit()

class Threading:
    def __init__(self):
        threading.Thread(target=live_site).start()
        threading.Thread(target=bloque_site).start()
Threading()







