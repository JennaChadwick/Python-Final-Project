import discord
from discord.ext import commands

client= commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Bot is ready. ')

@client.command()
async def respond(ctx):
    await ctx.send('hello, My name is Cat the Hat')

client.run('NzU5NDYyMTM0NTc1NzkyMTI5.X292Ow.ZBd5-ZmGLZd12g97GRSO6e-FWCM')
