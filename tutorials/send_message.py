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

@client.event
async def on_error(event, *args, **kwargs):
    with open('logs/err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise

client.run(TOKEN)