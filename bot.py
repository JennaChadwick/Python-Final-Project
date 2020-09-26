import discord
from discord.ext import commands

client= commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Bot is ready. ')

@client.command()
async def respond(ctx):
    await ctx.send('hello')

#client.run('NzU5NDYyMTM0NTc1NzkyMTI5.X292Ow.Q-4KaGUkST6Q_0S9xsw5o0WppYg')
