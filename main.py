import random, string, requests, time
from colorama import Fore
import concurrent.futures
import os
Title = "MULTI-PLATFORM CHECKER"
print(Title)
print("v1 | oguse.rs/V")
time.sleep(.5)
K4 = int(input(Fore.WHITE+"""
        [1] Tiktok
        [2] SoundCloud
        [3] Steam
        [4] Twitch
        
        [5] Custom link
        Choose one : """+Fore.WHITE))
webss = ''
webs = ''
if K4 == 1 :
    webss = 'tiktok.com/@'
    webs = "Tiktok"
elif K4 == 2 :
    webss = 'soundcloud.com/'
    webs = "SoundCloud"
elif K4 == 3 :
    webss = 'https://steamcommunity.com/id/'
    webs = "Steam"
elif K4 == 4 :
    webss = 'm.twitch.tv/'
    webs = "Twitch"
elif K4 == 5 :
    webss = 'fortnitetracker.com/profile/search?q='
    webs = "Fortnite"
else:
    print('Error, please choose correct number.. ')
    time.sleep(3)
    quit()

def check(users): 
    try:
        r = requests.get(f'https://{webss}{users}')
        if r.status_code == 200:
            print(Fore.WHITE+"[+] "+Fore.WHITE + "Taken"+ Fore.WHITE+ f' {users}')
        else:
            print(Fore.WHITE + "[+] " + Fore.GREEN + "Available" + Fore.WHITE + f' {users}')
            f = open("Hits.txt", "a", encoding='utf-8')
            f.write(f"{users} | Available or Banned On => {webs} |\n")
    except:
        pass

with open('users.txt', 'r') as f:
    users = [line.strip() for line in f]
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(check,users)