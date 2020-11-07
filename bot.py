import discord
from discord.ext import commands

# Imports
from dotenv import load_dotenv
import os
import re

# Credentials
load_dotenv('.env')

# Function for bot to open and read a text file
def get_some_text():
    f = open('testText.txt', "r")
    text = f.readlines()
    f.close()
    return text

# Function for bot to write to text file
def write_some_text():
    f = open('testText.txt', "a")
    f.write("\nExtra Line")
    f.close()

# Function to open and read userInfo text file and search and display the username
def read_user_profile(username):
    f = open('userInfo.txt', "r")
    text = f.readlines()
    f.close()
    userReg = re.compile(username)
    for l in text:
        if userReg.search(l):
            return l
    return 'No User Specified'




# . command line for running the bot
client= commands.Bot(command_prefix = '.')




# To turn on the Discord Bot
@client.event
async def on_ready():
    print('Bot is ready. ')

# To enter .respond command for bot to respond to USER
@client.command()
async def respond(ctx):
    await ctx.send('Never gonna give you up\nNever gonna let you donw\nNever gonna run around\nAnd hurt you')

# To enter a .test command for bot to write to load a text file
@client.command()
async def test(ctx):
    await ctx.send(get_some_text())

# To enter .testWrite command for bot to write to a text file
@client.command()
async def testWrite(ctx):
    write_some_text()


# To enter .userRead to read the Discord username from userInfo Text file
@client.command()
async def userRead(ctx):
    await ctx.send(read_user_profile(str(ctx.author.id)))


# To enter .userName to print one's username
@client.command()
async def userName(ctx):
    await ctx.send(str(ctx.author.id))








# Discord Bot token

client.run(os.getenv('TUTORIAL_BOT_TOKEN'))
