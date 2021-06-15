import discord
from discord.ext import commands

description = 'A shitty python bot'

intents = discord.Intents.default()

client = commands.Bot(command_prefix='>', description=description, intents=intents)

@client.event
async def on_ready():
    print('Connected as {0.user}'.format(client))
    channel = client.get_channel(835732581399789630)
    await channel.send('Fuck you <@!384718506723115009>')
    await client.change_presence(activity=discord.Game(name="test"))

@client.command()
async def hello(ctx):
    await ctx.send('die')

@client.command()
async def die(ctx):
    await ctx.send('no')

@client.command()
async def frogfacts(ctx):
    await ctx.send('6 minutes remain.')

@client.command()
async def sally(ctx):
    await ctx.send('sally cute')

client.run(token)