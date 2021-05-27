# embed.py

import os
import youtube_dl
import discord
from discord.ext import commands
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = commands.Bot(command_prefix="!")

@client.command()
async def play(ctx, url: str):
    song_path = './songs'
    song_there = os.path.isfile(song_path+"/song.mp3")
    try:
        if song_there:
            os.remove(song_path+"/song.mp3")
    except PermissionError:
        await ctx.send("Wait for the current playing music ot end or use the 'stop' commend.")
        return 

    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name="General")
    await voiceChannel.connect()
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    # if not voice.is_connected():
    
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'songs/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    for file in os.listdir(song_path):
        if file.endswith(".mp3"):
            os.rename(song_path+'/'+file, song_path+"/song.mp3")
    voice.play(discord.FFmpegPCMAudio(song_path+"/song.mp3"))



@client.command()
async def leave(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
    else:
        await voice.send("The bot is not connected to a voice channel.")

@client.command()
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await voice.send("Currenting no audio is playing.")

@client.command()
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await voice.send("The audio is not paused.")

@client.command()
async def stop(ctx):
   voice = discord.utils.get(client.voice_clients, guild=ctx.guild) 
   voice.stop()



client.run(TOKEN)