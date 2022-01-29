import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import requests
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
#TOKEN
TOKEN = "TOKEN-GOES-HERE"

bbb = "4"
b = Bot(command_prefix = "yomama")

@b.event
async def on_ready():
    print("armed.")
#      _______ _ _     _____                            
#     |__   __(_) |   / ____|                           
#        | |   _| | _| (___  _ __   ___  ___  ___ _ __  
#        | |  | | |/ /\___ \| '_ \ / _ \/ __|/ _ \ '__| 
#        | |  | |   < ____) | |_) | (_) \__ \  __/ |    
#        |_|  |_|_|\_\_____/| .__/ \___/|___/\___|_|     v0.1
#                           | |                         
#                           |_|  coded by jmdevcz       

@b.event
async def on_message(message):
    if 'ts' in message.content.lower() and message.author.id == 858830987197546537:
        a = message.content.lower().replace("ts", "")
        
        aa,bb = map(int,a.split())
        await message.delete()
        for msg in await message.channel.history(limit=bb).flatten():
           if "https://vm.tiktok.com/" in msg.content and msg.author.id==aa:
                print(msg.author.name + " : " + msg.content)
                print("-----=====+++++=====-----")
                url = msg.content.split("https://vm.tiktok.com/")[1].split("/")[0]
                furl = "https://vm.tiktok.com/" + url + "/"
                response = requests.get(furl, headers=headers)
                aaaa = response.url.split("&user_id=")[1].split("&")[0]
                print("https://tiktok.com/@" + aaaa)
                print("-----=====+++++=====-----")


               
    elif 'stlkall' in message.content.lower() and message.author.id == 858830987197546537:
        aaa = message.content.lower().replace("stlkall","")
        await message.delete();
        for msga in await message.channel.history(limit=int(aaa)).flatten():
           if "https://vm.tiktok.com/" in msga.content:
                print(msga.author.name + " : " + msga.content)
                print(msga.author.name + " : " + msga.content)
                print("-----=====+++++=====-----")
                url = msga.content.split("https://vm.tiktok.com/")[1].split("/")[0]
                furl = "https://vm.tiktok.com/" + url + "/"
                response = requests.get(furl, headers=headers)
                aaaa = response.url.split("&user_id=")[1].split("&")[0]
                print("https://tiktok.com/@" + aaaa)
                print("-----=====+++++=====-----")


    else:
        #nothing
        bbb = "2"
b.run(TOKEN, bot = False)
