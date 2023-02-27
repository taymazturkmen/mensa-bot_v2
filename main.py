from sys import argv
import requests
import datetime
import discord
import os
from discord.ext import commands;

#client = discord.Client()
client = commands.Bot(command_prefix="!",intents=discord.Intents.all())
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    synced = await client.tree.sync()
    print(len(synced))

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
        location = "106"
        await print_menu(message ,location)
        
@client.tree.command(name="print" ,description="prints the menu for the day")
async def print_menu(message: discord.Interaction):
    Mensa1 = discord.SelectOption(label="Mensa 1" , value="101")
    Mensa2 = discord.SelectOption(label="Mensa 2" , value="106")
    Foodtruck = discord.SelectOption(label="Foodtruck" , value="194")
    selection = discord.ui.Select(options=[Mensa1,Mensa2,Foodtruck])
    view = discord.ui.View()
    view.add_item(selection)
    await message.response.send_message("Choose Your Caffeteria" , view=view)
    async def mycallback(message):
        date = datetime.datetime.now()
        str_date = str(date)
        str_date = str_date[:-16]
        location = selection.values[0]
        url = "https://sls.api.stw-on.de/v1/location/"+location +"/menu/" + str_date
        response = requests.get(url)
        data = response.json()
        if len(data["meals"]) == 0:
            await message.response.send_message("It looks like today there are no food in selected caffeteria")
            await message.response.send_message("Showing the nearest day with food avaliable")
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
        
    selection.callback = mycallback
   
client.run(TOKEN)
