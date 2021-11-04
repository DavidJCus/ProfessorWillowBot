# RaidBot
Simple discord bot made for fun in Python. I created this bot for a Pokemon Go server. 
Features of this bot:
  - Achievement Database: memebers of the server can add when they catch a 3 Star or a shiny. They can also add when memebers of the server have completed a raid together.
    This data is then displayed in the achievements channel using the command $achievements
  - Pokedex: This bot uses an API call and JSON formatting so that memebers can type "-pokedex [name of pokemon]" and retrieve data about that pokemon all through discord.
  - Embeded messages: Using discord API documentation, messages like the achievements and pokedex entries are embedded and look nice.
  - Basic moderation: Every message sent in the server is first put into all lowercase checked for banned phrases then split to check for banned words
