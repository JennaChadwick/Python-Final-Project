import discord
from discord.ext import commands

# Imports
from dotenv import load_dotenv
import os
import re
import datetime
import random

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


def write_id_time(userID, time):
    f = open('usertime.txt', "w")
    f.write(str(userID) + str(time))
    f.close()


def decide_if_junk(luck):
    comp = random.randint(1, 110)
    if comp >= 70 - (luck * 3):
        return 'treasure'
    else:
        return 'junk'




# . command line for running the bot
client= commands.Bot(command_prefix = '.')




# To turn on the Discord Bot
@client.event
async def on_ready():
    print('Bot is ready. ')

# To enter .respond command for bot to respond to USER
@client.command()
async def respond(ctx):
    await ctx.send('Welcome to the Cat Scavenger Game ! \n Please enter the .readUser and enter your name')

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


# To enter .time to print the current time
@client.command()
async def time(ctx):
    await ctx.send(str(datetime.datetime.utcnow()))
    await ctx.send(str(ctx.author.id))
    write_id_time(ctx.author.id, datetime.datetime.utcnow())


@client.command()
async def isJunk(ctx):
    await ctx.send(decide_if_junk(0))


# Discord Bot token

client.run(os.getenv('TUTORIAL_BOT_TOKEN'))
