import json
import requests
import os
from colorama import Fore



from colored import fg
b = Fore.RESET
d = Fore.RESET
w = fg('#400078')


def clear():
    print("\n" * 100)
    startmenu()



print(f"{d}Welcome To Discord Token Info")
print("")
request = requests.Session()
token = input(f"{w}[{d}Enter Token{w}] : {d}")
headers = {
    'Authorization': token,
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'
}


print(f'''
 {w}[{d}1{w}] {d}Token Info    , {w}[{d}2{w}] {d}Exit      
 
''')

def tokeninfo():
    src = request.get(
        'https://canary.discordapp.com/api/v6/users/@me', headers=headers, timeout=10)
    response = json.loads(src.content)

    if src.status_code == 403:
        print("[*] Token Is Invalid")
        startmenu()
    elif src.status_code == 401:
        print("[*] Token Is Invalid")
        startmenu()
    else:
        print(f"Token Is Valid")
        infotk = f'''\n   Name: {response['username']}#{response['discriminator']}   ID: {response['id']}\n   Email: {response['email']}   Phone: {response['phone']}\n   Verified: {response['verified']}          MFA: {response['nsfw_allowed']}\n   AvatarURL: https://cdn.discordapp.com/avatars/{response['id']}/{response['avatar']}.png?size=1024'''
        print(infotk)
        startmenu()


def startmenu():
    keywrd = input(f"{w}[{d}Command{w}] :{d} ")
    if keywrd == "2":
        print("Bye !")
        exit()
    elif keywrd == "clear":
        clear()
    elif keywrd == "1":
        tokeninfo()
        startmenu()
    else:
        print(f" {w}[{Fore.RED}!{w}] {Fore.RED}Command Not Found !")
        startmenu()


startmenu()
