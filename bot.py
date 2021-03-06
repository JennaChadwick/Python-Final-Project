''' Imports '''
import discord
from discord.ext import commands
from dotenv import load_dotenv
import os, re, datetime, random

'''Credentials'''
load_dotenv('.env')


'''Function to open and read userInfo text file and search and display the username'''
def read_user_profile(username):
    f = open('userInfo.txt', "r")
    text = f.readlines()
    f.close()
    userReg = re.compile(username)
    for l in text:
        if userReg.search(l):
            return l
    return 'No User Specified'



'''Picks a random item from junk.txt'''
def rand_junk():
    f = open('junk.txt', "r")
    junk = f.readlines()
    x = random.randint(1, len(junk))
    f.close()
    return junk[x - 1]


'''Picks a random item from treasure.txt'''
def rand_treasure():
    f = open('treasure.txt', "r")
    treasure = f.readlines()
    x = random.randint(1, len(treasure))
    f.close()
    return treasure[x - 1]


'''Picks a random item from jackpot.txt'''
def rand_afamiliar():
    f = open('jackpot.txt', "r")
    afam = f.readlines()
    x = random.randint(1, len(afam))
    f.close()
    return afam[x - 1]


'''Checks to see if the user has called a function today. If not, allows and updates their time
If yes, blocks the attempt'''
def time_users(username, calltime):
    today = calltime[8:10]
    f = open('userInfo.txt', "r")
    text = f.readlines()
    f.close()
    userReg = re.compile(username)
    for (i, l) in enumerate(text):
        if userReg.search(l):
            if l[27:29] == today:
                return 'You have already called this function today'
            else:
                text[i] = l[:19] + calltime + l[45:] + '\n'
                f = open('userInfo.txt', "w")
                f.writelines(text)
                f.close()
                return 'Updated'
    return 'No User Specified'


'''
This function performs a simple calculation to determine if an item is junk or not
Then, it calls a function to pick a random item from junk or treasure
If the treasure item is the jackpot (Afamiliar), it calls a third random function for that table
'''
def decide_if_junk(luck):
    comp = random.randint(1, 110)
    if comp >= 70 - (luck * 3):
        res = str(rand_treasure())
        if res == 'Afamiliar':
            res = str(rand_afamiliar())
        return res
    else:
        return str(rand_treasure())


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


''' To edit a pet'''
def edit(petID, luck=0, owner=''):
    f = open('pets.txt', "r")
    text = f.readlines()
    f.close()
    petReg = re.compile(petID)
    for (i, l) in enumerate(text):
        if petReg.search(l):
            text[i] = str(petID) + ' ' + str(luck)
            f = open('pets.txt', "w")
            f.writelines(text)
            f.close()
            return str(text[i])
    f = open('pets.txt', 'a')
    f.write('\n' + str(petID) + ' ' + str(luck))
    f.close()
    if owner != '':
        f = open('userInfo.txt', "r")
        text = f.readlines()
        f.close()
        userReg = re.compile(owner)
        for (i, l) in enumerate(text):
            if userReg.search(l):
                if petReg.search(l):
                    return 'Owner is already correct'
                else:
                    text[i] = text[i] + str(petID)
                    f = open('userInfo.txt', 'w')
                    f.writelines(text)
                    f.close()
                    return 'Owner added'
    return 'Pet added'

'''To add a new user'''
def add_user(userID):
    f = open('userInfo.txt', "r")
    text = f.read()
    userReg = re.compile(userID)
    if userReg.search(text):
        return
    f = open('userInfo.txt', "a")
    f.write('\n' + str(userID))
    f.close()
    time_users(userID, datetime.datetime.utcnow())


''' a dot command syntax for the bot'''
catBot = commands.Bot(command_prefix='.')


'''
Bot Modular commands to check user command input to create channels
for users with an admin role on Discord. If user does not have an admin role,
it sends an error message
'''
@catBot.command(name='create-channel')
@commands.has_role('admin')
async def create_channel(ctx, channel_name='python-final-project'):
    guild = ctx.guild
    existing_channel = discord.utils.get(guild.channels, name=channel_name)
    if not existing_channel:
        print(f'Creating a new channel: {channel_name}')
        await guild.create_text_channel(channel_name)

@catBot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command.')



'''To turn on the Discord Bot'''
@catBot.event
async def on_ready():
    print('Bot is ready. ')


'''To enter .userRead to read the Discord username from userInfo Text file'''
@catBot.command()
async def userRead(ctx):
    await ctx.send(read_user_profile(str(ctx.author.id)))


'''To enter .userName to print one's username'''
@catBot.command()
async def userName(ctx):
    await ctx.send(str(ctx.author.id))


'''To enter .time to print the current time'''
@catBot.command()
async def time(ctx):
    await ctx.send(time_users(str(ctx.author.id), str(datetime.datetime.utcnow())))


'''
This .scavenge command takes one argument, in the format #xxxx
It then uses that as a pet ID, checks to make sure you own the pet,
and determines the luck of the pet. It then rolls to see if you get a junk
or treasure item
'''
@catBot.command()
async def scavenge(ctx, arg):
    # This will cause it to not accept the command if the channel is incorrect
    if ctx.channel.id != 747881675278516256:
        print('Improper channel')
        return
    # dest is the destination channel, where it will send the response
    dest = catBot.get_channel(782343771705704499)
    if time_users(str(ctx.author.id), str(datetime.datetime.utcnow())) == 'You have already called this function today':
        print('Improper time')
        await dest.send('You have already called this function today')
        return
    petID = checkOwner(str(ctx.author.id), str(arg))
    if petID == 'You do not own that pet.':
        print('Improper ID')
        await dest.send('You do not own that pet.')
    else:
        await dest.send(decide_if_junk(get_luck(petID)))
        await dest.send(str(petID))



''' To edit pets. Luck and Owner are optional arguments '''
@catBot.command()
async def editPet(ctx, pet, luck_val=0):
    await ctx.send(edit(pet, luck=luck_val, owner=str(ctx.author.id)))

''' To add an owner '''
@catBot.command()
async def start(ctx):
    await ctx.send(add_user(str(ctx.author.id)))




'''Discord Bot token'''
catBot.run(os.getenv('TUTORIAL_BOT_TOKEN'))
