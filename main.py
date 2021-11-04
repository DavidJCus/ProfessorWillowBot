from __future__ import print_function
import discord
import os
import requests
import json
from replit import db
from keep_alive import keep_alive
from banned_word import banned_words
from banned_word import banned_phrases
from banned_word import smh_phrases
from banned_word import smh_words

token = os.environ['bot.token']
banword = os.environ['bannedwords']
client = discord.Client() 
raids_won = 0
threestar_caught = 0
shiny_caught = 0

db["Raids_won"]
db["star_caught"]
db["shiny_caught"] 

def pokedex(pokemon):
  url = "https://some-random-api.ml/pokedex"
  response = requests.get(url, params={'pokemon': pokemon})
  json_data = json.loads(response.text)
  return json_data

def add_raids():
  raids_won = db["Raids_won"]
  db["Raids_won"] = raids_won + 1

def raid_change(new_RaidNum):
  db["Raids_won"] = new_RaidNum

def add_3star():
  threestar_caught = db["star_caught"]
  db["star_caught"] = threestar_caught + 1

def star_change(new_threeStar):
  db["star_caught"] = new_threeStar

def add_shiny():
  shiny_caught = db["shiny_caught"]
  db["shiny_caught"] = shiny_caught + 1

def shiny_change(new_shiny):
  db["shiny_caught"] = new_shiny

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content.lower()
  msgsplit = msg.split()
  
  welcome = "This server has accomplished the following together:"
  #raid = "Raids together:  "+ str(db["Raids_won"])
  #star = "3-stars caught:  "+ str(db["star_caught"])
  #shiny = "Shinies caught:  "+ str(db["shiny_caught"])
  praise = "Awesome job everyone!!"
  command = "Commands can be found in #extra-resources"

  if msg.startswith("$test"):
    await message.channel.send("Bot online and active")

  if msg.startswith("$achievements"):
    embedVar = discord.Embed(title="Achievements", description = welcome, color=0x6cc3c4)
    embedVar.add_field(name="Raids together:", value=str(db["Raids_won"]), inline=True)
    embedVar.add_field(name="3-stars caught:", value=str(db["star_caught"]), inline=True)
    embedVar.add_field(name="Shinies caught:", value=str(db["shiny_caught"]), inline=True)
    embedVar.add_field(name="\u200b",value=praise+"\n"+command)
    #embedVar.set_footer(text=command)
    await message.channel.send(embed=embedVar)


  #if msg.startswith("$achievements"):
   # await message.channel.send(welcome + '\n' + raid + '\n' + star + '\n' + shiny + '\n' + praise + '\n' + command)

  if msg.startswith("$bannedwords"):
    await message.channel.send("**Current banned words: **" + str(banned_words) +'\n' + "**Current banned phrases: **"+ str(banned_phrases) + '\n' "**Unfunny words: **" + str(smh_words) + '\n' + "**Unfunny phrases: **" + str(smh_phrases))

  if '69' in msgsplit:
    await message.channel.send("Nice")

  if msg.startswith("-addraid"):
    add_raids()
    await message.channel.send("Raid added to the counter, congrats!")

  if msg.startswith("$manualraidchange"):
    new_raidNum = int(msg.split("$manualraidchange",1)[1])
    raid_change(new_raidNum)
    await message.channel.send("Raid number changed!")

  if msg.startswith("-add3star"):
    add_3star()
    await message.channel.send("3 star added to the counter, nice catch!")

  if msg.startswith("$manual3starchange"):
    new_threeStar = int(msg.split("$manual3starchange",1)[1])
    star_change(new_threeStar)
    await message.channel.send("3 star number changed!")
  
  if msg.startswith("-addshiny"):
    add_shiny()
    await message.channel.send("Shiny added to the counter, nice catch!")

  if msg.startswith("$manualshinychange"):
    new_shiny = int(msg.split("$manualshinychange", 1)[1])
    shiny_change(new_shiny)
    await message.channel.send("Shiny number change")

  if msg.startswith("-pokedex"):
    pokemon = (msg.split("-pokedex ",1)[1])
    pokedex(pokemon)
    json_data = pokedex(pokemon)
    #name = "**Name**: " + json_data["name"]
    pokeid = "**ID:** " + json_data["id"]
    generation = "**Generation:** " +json_data["generation"]
    poketype = "**Type:** " + ' & '.join(json_data["type"])
    abilities = "**Abilities:** " + ', '.join(json_data["abilities"])
    height = "**Height:** " + json_data["height"]
    sprites = json_data["sprites"]["animated"]
    weight = "**Weight:** " + json_data["weight"]
    #evolutionLine
    if json_data["family"]["evolutionStage"] == 0: 
      evolution = "**Evolution line:** No evolutions"
    else: 
      evolution = "**Evolution line:** " + ' -> '.join(json_data["family"]["evolutionLine"])
    
    description = json_data["description"]

    #await message.channel.send (sprites)
    #await message.channel.send(name + '\n' + pokeid + '\n' + generation + '\n' + poketype + '\n' + abilities + '\n' + height + '\n' + weight + '\n'+ evolution + '\n' + description)

    dex = discord.Embed(title=pokemon.upper(), description = description , color=0x6cc3c4)
    dex.set_thumbnail(url=sprites)
    dex.add_field(name="Details", value=pokeid + '\n' + generation + '\n' + poketype + '\n' + abilities + '\n' + height + '\n' + weight + '\n'+ evolution)
    await message.channel.send(embed = dex)

  if msg.startswith("-gif"):
    pokemon = (msg.split("-gif ",1)[1])
    pokedex(pokemon)
    json_data = pokedex(pokemon)
    sprites = json_data["sprites"]["animated"]
    await message.channel.send(sprites)

  
  if msg.startswith("$jsondatapk"):
    pk = (msg.split("$jsondatapk ",1)[1])
    pokedex(pk)
    json_data = pokedex(pk)
    await message.channel.send(json_data)

  if any(word in msgsplit for word in banned_words):
    await message.channel.send("I think you said something this server doesn't allow. I am just a bot though so I'll let <@&884234729128349706> and <@&885338785129300049> review it. Be sure to check out <#883557162029293568>.")
  elif any(word in msg for word in banned_phrases):
    await message.channel.send("I think you said something this server doesn't allow. I am just a bot though so I'll let <@&884234729128349706> and <@&885338785129300049> review it. Be sure to check out <#883557162029293568>.")

  if any(word in msgsplit for word in smh_words):
    await message.channel.send("Come on trainer, you can be funnier than that. I don't think <@&884234729128349706> or <@&885338785129300049> would be impressed")
  elif any(word in msg for word in smh_phrases):
    await message.channel.send("Come on trainer, you can be funnier than that. I don't think <@&884234729128349706> or <@&885338785129300049> would be impressed")
  
  if msg.startswith("$spanish"):
    await message.channel.send ("muy")
    await message.channel.send("https://download.logo.wine/logo/Microsoft_Excel/Microsoft_Excel-Logo.wine.png")
    await message.channel.send ("https://assets.pokemon.com/assets/cms2/img/pokedex/full/244.png")
    await message.channel.send ("lol")
    
keep_alive()
client.run(token) 
