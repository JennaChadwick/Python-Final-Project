import discord
from discord.ext import commands

# Imports
from dotenv import load_dotenv
import os

# Credentials
load_dotenv('.env')

def get_some_text():
    f = open('testText.txt', "r")
    text = f.readlines()
    f.close()
    return text

def write_some_text():
    f = open('testText.txt', "a")
    f.write("\nExtra Line")
    f.close()

client= commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Bot is ready. ')

@client.command()
async def respond(ctx):
    await ctx.send('Never gonna give you up\nNever gonna let you donw\nNever gonna run around\nAnd hurt you')

@client.command()
async def test(ctx):
    await ctx.send(get_some_text())

client.run(os.getenv('TUTORIAL_BOT_TOKEN'))
