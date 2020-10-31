import discord
from discord.ext import commands

def get_some_text():
    f = open(testText.txt, "r")
    return f

client= commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Bot is ready. ')

@client.command()
async def respond(ctx):
    await ctx.send('hello')

#client.run('NzU5NDYyMTM0NTc1NzkyMTI5.X292Ow.Q-4KaGUkST6Q_0S9xsw5o0WppYg')
