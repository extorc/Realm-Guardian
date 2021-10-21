from discord.ext import commands
import requests
from dotenv import load_dotenv,dotenv_values

temp = dotenv_values(".env")
TOKEN = temp["TOKEN"]

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
async def rr(ctx, *,link):
    anti_preview = link.replace("<","").replace(">","")
    if(check_if_url(anti_preview)):
        url = requests.get(anti_preview).url
        if("dQw4w9WgXcQ" in url):
            await ctx.send("This is a RickRoll")
        else:
            await ctx.send("You are Safe!")
        
bot.run(TOKEN)