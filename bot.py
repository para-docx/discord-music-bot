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