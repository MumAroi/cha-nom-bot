# command.py

import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = commands.Bot(command_prefix="!")

@client.command()
async def hello(ctx, arg):
    await ctx.send(arg)

@client.command()
async def hello2(ctx, arg1, arg2):
    await ctx.send(arg1 +  ' : ' + arg2)

@client.command()
async def hello3(ctx, *args):
    for arg in args:
        await ctx.send(arg)

@client.command()
async def detail(ctx, arg):
    print(ctx.author)
    print(ctx.message)
    print(ctx.guild)

client.run(TOKEN)