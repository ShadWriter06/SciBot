import requests
import discord
from discord.ext import commands
import json

TOKEN = 'MTA4NTM2NTc0NzAzNjk4MzQyNg.Gr8WNi.fqPpihoJis5CXwLwLUSNNGYnQsYbFxXOpyGcEE'
bot = commands.Bot(command_prefix='!',intents=discord.Intents.all())


questionData = ""

@bot.command(name="q")
async def question(ctx):
    question = requests.get("https://scibowldb.com/api/questions/random")
    global questionData
    questionData = question.json()
    print(questionData)
    toBeSent = (questionData["question"]["tossup_question"])
    await ctx.send(toBeSent)

@bot.command(name="a")
async def answer(ctx):
    if str(questionData["question"]["tossup_format"]).startswith("S") == True:
        print("sa")
    else:
        print("mc")
    toBeSent = (questionData["question"]["tossup_answer"])
    await ctx.send(toBeSent)


@bot.command(name="tellmethetruth")
async def answer(ctx):
    await ctx.send("burt is a blurter")

bot.run(TOKEN)