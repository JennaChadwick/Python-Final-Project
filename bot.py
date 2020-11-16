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

# Function that writes junk items to a text file
def write_junk():
    f=open("junk.txt","a")
    f.write("junk 1\njunk 2\njunk 3\njunk 4")
    f.close()

    f=open("junk.txt","r")
    print(f.readlines())


# Function that writes junk items to a text file
def write_treasure():
    f=open("treasure.txt","a")
    f.write("treasure 1\ntreasure 2\ntreasure 3\ntreasure 4")
    f.close()

    f=open("treasure .txt","r")
    print(f.readlines())

  

"""
Everything after this section, I am actively working on. Please do not change these
"""
'''
This function performs a simple calculation to determine if an item is junk or not
Eventually, it will call other functions to get actual items
'''
def decide_if_junk(luck):
    comp = random.randint(1, 110)
    if comp >= 70 - (luck * 3):
        return 'treasure'
    else:
        return 'junk'


'''
This function reads the luck value of the pet with the provided id
'''
def get_luck(petID):
    f = open('pets.txt', "r")
    text = f.readlines()
    f.close()
    petReg = re.compile(petID)
    for l in text:
        if petReg.search(l):
            return int(l[5:7])
    return 'No Pet Specified'


'''
This function checks if the petID provided is found on the same line 
as the userID provided, indicating ownership
'''
def checkOwner(userID, petID):
    f = open('userInfo.txt', "r")
    text = f.readlines()
    f.close()
    userReg = re.compile(userID)
    petReg = re.compile(petID)
    for l in text:
        if userReg.search(l):
            if petReg.search(l):
                return petID
            else:
                return 'You do not own that pet.'

    return 'No User Specified'


"""
End active section
"""


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
    # write_id_time(ctx.author.id, datetime.datetime.utcnow())


'''
This command takes one argument, in the format #xxxx
It then uses that as a pet ID, checks to make sure you own the pet,
and determines the luck of the pet. It then rolls to see if you get a junk
or treasure item
'''
@client.command()
async def isJunk(ctx, arg):
    petID = checkOwner(str(ctx.author.id), str(arg))
    if petID == 'You do not own that pet.':
        await ctx.send('You do not own that pet.')
    else:
        await ctx.send(decide_if_junk(get_luck(petID)))
        await ctx.send(str(petID))


@client.command()
async def Junk(ctx):
    write_junk()

@client.command()
async def Treasure(ctx):
    write_treasure()



# Discord Bot token

client.run(os.getenv('TUTORIAL_BOT_TOKEN'))
