import random
import discord
from discord.ext import commands
import config

TOKEN = config.TOKEN
intents = discord.Intents.all()

bot = commands.Bot(command_prefix=commands.when_mentioned_or('?'), activity=discord.Activity(name='this server', type=discord.ActivityType.watching), intents=intents)

@bot.command(aliases=['random'])
@commands.guild_only()
async def randomise(ctx):
    """Randomly pairs up all members on the server"""
    members = [member for member in ctx.guild.members if not member.bot]
    if not members:
        return await ctx.send("Please enable privileged intents from the Discord developer portal")
    random.shuffle(members)
    lone = None
    if len(members) % 2 == 1:
        lone = members.pop()
    pairs = []
    while members:
        pairs.append((members.pop(), members.pop())
    text = '\n'.join([f"{num}. {pair[0].mention}, {pair[1].mention}" for num, pair in enumerate(pairs, 1)])
    if lone:
        text += f'\n\nLone: {lone}'
    await ctx.send(f"Randomised all server members into pairs:\n{text}")
@bot.command()
async def ping(ctx):
    """Returns bot latency"""
    await ctx.send(f"Pong! {round(bot.latency * 1000)}ms")

bot.run(TOKEN)
