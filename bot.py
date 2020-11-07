import discord
from discord.ext import commands

# Imports
from dotenv import load_dotenv
import os
import re

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


def read_user_profile(username):
    f = open('userInfo.txt', "r")
    text = f.readlines()
    f.close()
    userReg = re.compile(username)
    for l in text:
        if userReg.search(l):
            return l
    return 'No User Specified'


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

@client.command()
async def testWrite(ctx):
    write_some_text()


@client.command()
async def userRead(ctx):
    await ctx.send(read_user_profile('Jeb'))

client.run(os.getenv('TUTORIAL_BOT_TOKEN'))
