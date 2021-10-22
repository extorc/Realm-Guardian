import requests
from dotenv import load_dotenv,dotenv_values

temp = dotenv_values(".env")
TOKEN = temp["TOKEN"]

formattingMessage = """Hey <@%s> \n
    A Message that you have sent contains code but is unformatted.\n
    This means that you message is difficult to be read by others in the server.\n
    Kindly suround your message in ` 3 times so that it could appear like ```this```"""

formattedCodeImageLink = "https://media.discordapp.net/attachments/877232296497905667/900783733987233792/unknown.png"

def check_if_url(link):
    try:
        site=requests.get(link)
        return True;
    except Exception:
        return False
    
async def getReply(ctx):
    r = ctx.message.reference
    msg = await ctx.fetch_message(r.message_id)
    return msg