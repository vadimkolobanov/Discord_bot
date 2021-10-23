import os
import discord
from discord.ext import commands
import random
from dotenv import load_dotenv
import socket

from pythonping import ping

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

description = 'Hello from Something'


intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='-', description=description, intents=intents)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')



@bot.command()
async def status (ctx):
    async def check_status(self, status, hex, h_name):
        embedVar = discord.Embed(title=f"Статус сервера: {status} ", description="", color=hex)


        await self.send(embed=embedVar)
    try:



        h_name = socket.gethostbyname('minecraftshare.ru')
        print(ping(h_name))
        if ping(h_name):
           await check_status(ctx,'Online',0x00ff00,h_name)


    except Exception:
        await check_status(ctx,'Offline',0xF44336,'Не определен')





@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send('{0.name} joined in {0.joined_at}'.format(member))





bot.run(TOKEN)