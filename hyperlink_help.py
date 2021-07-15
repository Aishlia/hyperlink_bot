from dotenv import load_dotenv
load_dotenv()

import os
import urllib.request
import asyncio
import datetime
import random
import time
import discord
from discord.ext import commands
import random

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'The bot has logged in as {bot.user} and is ready to serve requests of its human overlords.')

@bot.command(name='hello', help='Responds with a hello message to show bot is up. !hello')
async def greeting(context):
    await context.send('Hi bub! My name is Merle Ambrose, but you can call me Ear for short. I\'m the headmaster at Ravenwood. Have fun doing my bidding.')

@bot.command(name='link', help='<phrase> <link>')
async def finding_the_recipe(context, *phrase_link: str):
    phrase_link_list = phrase_link
    phrase = " ".join(phrase_link_list[:-1])
    link = phrase_link_list[-1]
    embed=discord.Embed(title=phrase, url = link, color=0xFF5733)
    await context.send(embed=embed)

bot.run(os.getenv('BOT_TOKEN'))
