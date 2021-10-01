import discord
from discord.ext import commands
from discord.utils import get
import youtube_dl
import os
import shutil
from os import system


TOKEN = ''
BOT_PREFIX = '.'

bot = commands.Bot(command_prefix=BOT_PREFIX)
bot.remove_command('help')


@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('type .help to get started'))
    print(f'Logged in as: {bot.user.name}\n')

# Bot commands

@bot.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author

    help_embed = discord.Embed(colour=discord.Colour.green(
    ), title='Bot commands', description='Commands for the music bot')
    help_embed.set_author(
        name='Music 24/7', icon_url='https://cdn.discordapp.com/attachments/738729159685308487/738752162091499640/02mtFJaU_400x400.jpg')
    help_embed.add_field(
        name=".join", value="Bot will join the voice channel that you're currently in", inline=False)
    help_embed.add_field(
        name=".leave", value="Bot will leave the voice channel", inline=False)
    help_embed.add_field(
        name=".play", value="This will play the music that you pass in here. Works like youtube search. This also works with youtube/spotify links. Example: .play song name", inline=False)
    help_embed.add_field(name=".pause", value="Pauses the music", inline=False)
    help_embed.add_field(
        name=".resume", value="Resumes the music", inline=False)
    help_embed.add_field(
        name=".next", value="Skips the current on and plays next music", inline=False)
    help_embed.add_field(
        name=".stop", value="Stops playing music", inline=False)
    help_embed.add_field(
        name=".queue", value="Adds song to the queue. Example: .queue song name", inline=False)
    help_embed.add_field(
        name=".volume", value="Changes the volume. Default is 23. Volume limit = 1-100. Example: .volume 30", inline=False)

    await author.send(embed=help_embed)