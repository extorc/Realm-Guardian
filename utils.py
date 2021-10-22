import requests
from dotenv import load_dotenv,dotenv_values

temp = dotenv_values(".env")
TOKEN = temp["TOKEN"]

formattingMessage = """Hey <@%s> \n
    A Message that you have sent contains code but is unformatted.\n
    This means that you message is difficult to be read by others in the server.\n
    Kindly suround your message in ` 3 times so that it could appear like ```this```"""

codeHighlightMessage =   """Hey <@%s> \n
    A Message that you have sent contains code but the syntax is not highlighted.\n
    This means that you message is difficult to be read by others in the server.\n
    Kindly add the name of your language in the first line and press enter to make it appear like \n"""

formattedCodeImageLink = "https://media.discordapp.net/attachments/877232296497905667/900783733987233792/unknown.png"
highlightCodeSyntaxMessage = "https://media.discordapp.net/attachments/877232296497905667/901028265760813067/unknown.png"
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