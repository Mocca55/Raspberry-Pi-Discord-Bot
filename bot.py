# Import der Bibliotheken
import discord
import time
from discord.ext import commands
import datetime
import os
from time import sleep


#Startdaten anzeigen per Print ausgeben und in Logdatei schreiben
now = datetime.datetime.now()
print("Gestartet")
print(str(now))
datei = open('bot-log.txt','a')
datei.write("\r\n" + str(now) + "     Bot gestartet")
datei.close()


# Discord Token
TOKEN = 'Token hier einfügen'

#Command Prefix setzen hier -> -
client = commands.Bot(command_prefix='-')

# Information zum Bot mit Print Ausgaben
@client.event
async def on_ready():
    print('Connected to bot: {}'.format(client.user.name))
    print('Bot ID: {}'.format(client.user.id))

#Bot Commands
@client.command() 
async def netflix(ctx):
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='Netflix'))
    now = datetime.datetime.now()
    datei = open('bot-log.txt','a')
    print(str(now) + "     Wechsel auf -> schaut Netflix")
    datei.write("\r\n" + str(now) + "     Wechsel auf -> schaut Netflix")
    datei.close()

@client.command() 
async def rl(ctx):
    await client.change_presence(activity=discord.Game(name="Rocket League"))
    now = datetime.datetime.now()
    datei = open('bot-log.txt','a')
    print(str(now) + "     Wechsel auf -> spiel Rocket League")
    datei.write("\r\n" + str(now) + "     Wechsel auf -> spiel Rocket League")
    datei.close()
    

@client.command() 
async def mc(ctx):
    await client.change_presence(activity=discord.Game(name="Minecraft-Server"))
    now = datetime.datetime.now()
    datei = open('bot-log.txt','a')
    print(str(now) + "     Wechsel auf -> spielt Minecraft-Server")
    datei.write("\r\n" + str(now) + "     Wechsel auf -> spielt Minecraft-Server")
    datei.close()
    
@client.command() 
async def bf(ctx):
    await client.change_presence(activity=discord.Game(name="Star Wars Battlefront II"))
    print(str(now) + "     Game BF2")
    now = datetime.datetime.now()
    datei = open('bot-log.txt','a')
    print(str(now) + "     Wechsel auf -> spielt BF2")
    datei.write("\r\n" + str(now) + "     Wechsel auf -> spielt BF2")
    datei.close()
    
@client.command() 
async def minecraft(ctx):
    await ctx.send('GameON Minecraft Server XX.XX.XXX.XXX')
    now = datetime.datetime.now()
    datei = open('bot-log.txt','a')
    print(str(now) + "     Mincraft Server Abfrage")
    datei.write("\r\n" + str(now) + "     Mincraft Server Abfrage")
    datei.close()
    
@client.command() 
async def temp(ctx):
    tempData = "/sys/class/thermal/thermal_zone0/temp"
    dateilesen = open(tempData, "r")
    temperatur = dateilesen.readline(2)
    dateilesen.close()
    now = datetime.datetime.now()
    datei = open('bot-log.txt','a')
    print(str(now) + "     Deine CPU hat " + temperatur + " Grad")
    datei.write("\r\n" + str(now) + "     Deine CPU hat " + temperatur + " Grad")
    await ctx.send("Meine CPU Temperatur ist gerade " +  temperatur +  " Grad.")
    datei.close()


@client.command() 
async def serverrestart(ctx):
    now = datetime.datetime.now()
    datei = open('bot-log.txt','a')
    print(str(now) + "     Minecraft Server Restart")
    datei.write("\r\n" + str(now) + "     Minecraft Server Restart")
    await ctx.send("Einen moment der Minecraft Server wird jetzt neu gestartet.")
    stop = os.system("~/minecraft/stop.sh")
    start = os.system("~/minecraft/start.sh")
    sleep (47)
    await ctx.send("Minecraft Server ist neu gestartet und bereit.")
    datei.close()
        
@client.command() 
async def serverbackup(ctx):
    now = datetime.datetime.now()
    datei = open('bot-log.txt','a')
    print(str(now) + "     Minecraft Server Backup auf USB-Stick")
    datei.write("\r\n" + str(now) + "     Minecraft Server Backup auf USB-Stick")
    await ctx.send("Einen moment Backup wird jetzt erstellt.")
    backup = os.system("cp /home/pi/minecraft /media/pi/USB-Backup -r -u -v")
    await ctx.send("Server Backup wurde auf dem USB-Stick erstellt.")
    datei.close()

client.run(TOKEN)
