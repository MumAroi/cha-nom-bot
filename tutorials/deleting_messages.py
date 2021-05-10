# deleting_messages.py

import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_message(message):
    if str(message.channel) == 'general' and message.content != '':
        await message.channel.purge(limit=1)

client.run(TOKEN)