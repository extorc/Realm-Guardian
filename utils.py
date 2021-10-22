import requests
from dotenv import load_dotenv,dotenv_values

temp = dotenv_values(".env")
TOKEN = temp["TOKEN"]

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