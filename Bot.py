import discord
from discord.ext import commands
import requests
from dotenv import load_dotenv,dotenv_values
from utils import *

bot = commands.Bot(command_prefix="~")

@bot.event
async def on_ready():
    print("Yay")

@bot.command()
async def format(ctx):
    msg = await getReply(ctx)
    embed = discord.Embed(title = "Please Format your code in the Message",
    description = formattingMessage % msg.author.id)
    embed.set_image(url = formattedCodeImageLink)
    await ctx.send(embed = embed)    

@bot.command()
async def hs(ctx):
    msg = await getReply(ctx)
    embed = discord.Embed(title = "Please highlight your code syntax",
    description = codeHighlightMessage % msg.author.id)
    embed.set_image(url =highlightCodeSyntaxMessage)   
    await ctx.send(embed = embed) 

@bot.command()
async def rr(ctx):
    msg = await getReply(ctx)
    msgs = msg.content.split(" ")
    for link in msgs:
        anti_preview = link.replace("<","").replace(">","")
        if(check_if_url(anti_preview)):
            url = requests.get(anti_preview).url
            if("dQw4w9WgXcQ" in url):
                await ctx.send("This is a RickRoll")
            else:
                await ctx.send("You are Safe!")
        
bot.run(TOKEN)