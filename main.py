from sys import argv
import requests
import json
import datetime
import discord
import sys

client = discord.Client()
TOKEN = sys.argv[1]

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == ('!mensa'):
        await message.channel.send('Choose A Caffeteria')
        await message.channel.send('!mensa1\n!foodtruck\n!mensa2')
    if message.content == ("!mensa1"):
        location = "101"
        await print_menu(message, location)
    if message.content == ("!foodtruck"):
        location = "194"
        await print_menu(message , location)
    if message.content == ("!mensa2"):
        location = "105"
        await print_menu(message ,location)
        

async def print_menu(message , location , date = None):
    date = datetime.datetime.now()
    str_date = str(date)
    str_date = str_date[:-16]
    url = "https://sls.api.stw-on.de/v1/location/"+location +"/menu/" + str_date
    response = requests.get(url)
    data = response.json()
    if len(data["meals"]) == 0:
        await message.channel.send("It looks like today there are no food in selected caffeteria")
        await message.channel.send("Showing the nearest day with food avaliable")
        print (len(data["meals"]))
        while(len(data["meals"]) == 0):
            date = date + datetime.timedelta(days=1)
            str_date = str(date)
            str_date = str_date[:-16]
            print(str_date)
            url = "https://sls.api.stw-on.de/v1/location/"+location +"/menu/" + str_date
            response = requests.get(url)
            data = response.json()
        await message.channel.send("Date: " + str_date)
        for i in data["meals"]:
            await message.channel.send(i["name"])
    else:
        for i in data["meals"]:
            await message.channel.send(i["name"])
    
    
client.run(TOKEN)
