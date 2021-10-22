import discord
from discord.ext import commands
import requests
from dotenv import load_dotenv,dotenv_values
from utils import check_if_url,getReply,TOKEN

bot = commands.Bot(command_prefix="~")

@bot.event
async def on_ready():
    print("Yay")

def check_if_url(link):
    try:
        site=requests.get(link)
        return True;
    except Exception:
        return False

@bot.command()
async def format(ctx):
    formattingMessage = """Hey <@%s> \n
    A Message that you have sent contains code but is unformatted.\n
    This means that you message is difficult to be read by others in the server.\n
    Kindly suround your message in ` 3 times so that it could appear like ```this```"""
    msg = await getReply(ctx)
    embed = discord.Embed(title = "Please Format your code in the Message"
    ,description = formattingMessage % msg.author.id)
    embed.set_image(url = "https://media.discordapp.net/attachments/877232296497905667/900783733987233792/unknown.png")
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