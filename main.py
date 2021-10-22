import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='>')




@bot.event
async def on_ready():
    print("Я запущен!")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('hello') :
        if message.author.id == 699253212011692073:
            await message.channel.send('АААА ЭТО ЖЕ МАААРК!')
        if message.author.id == 560791485071491082:
            await message.channel.send('Привет Гера, скоро я выучу новые слова от тебя и мы поговорим)')
        if message.author.id == 874657062917910580:
            await message.channel.send('РОМАААН! Привет! Я работаю Все огонь работаем дальше!)')
        if message.author.id == 495645748944175114:
            await message.channel.send('Создааааатель!!!!')
        if message.author.id == 573581266096488459:
            await message.channel.send('Привет Никита, я тебя знаю!')
        if message.author.id == 541541648153444354:
            await message.channel.send('Привет Данила, я тебя тоже знаю!')


@bot.command()
async def Hi(ctx):
    await ctx.send('Hi')

bot.run('OTAwNzQ5NjcwNTU1NDc2MDI5.YXF2gA.fQLP8iGemgQGI4jVAdjKIE5JM7o')