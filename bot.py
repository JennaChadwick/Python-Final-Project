import discord
from discord.ext import commands

client= commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Bot is ready. ')

@client.command()
async def respond(ctx):
    await ctx.send('hello')

client.run('NzU5NDYyMTM0NTc1NzkyMTI5.X292Ow.tNm-GHcYe5WOyh751_yisfL5B6M')
