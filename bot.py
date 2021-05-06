# bot.py

import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_message(message):
    message.content.lower()
    if message.author == client.user:
        return
    if message.content.startswith('hello'):
        await message.channel.send('Hi ' + str(message.author) +  ', Im Robot' )

client.run(TOKEN)