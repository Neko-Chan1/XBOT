import subprocess
from search_engine_parser import YahooSearch as GoogleSearch
from re import findall
from requests import get, post, exceptions
from telegram import Update, Bot
from telegram.ext import run_async, Filters

from xbotg import dispatcher
from xbotg.modules.disable import DisableAbleCommandHandler

def google(bot: Bot, update: Update):
         page = update.effective_message.text.split(" ", 1)
    try:
        page = page[0]
        page = page.replace("page=", "")
        match = match.replace("page=" + page[0], "")
    except IndexError:
        page = 1
    search_args = (str(match), int(page))
    gsearch = GoogleSearch()
    gresults = await gsearch.async_search(*search_args)
    msg = ""
    for i in range(10):
        try:
            title = gresults["titles"][i]
            link = gresults["links"][i]
            desc = gresults["descriptions"][i]
            msg += f"[{title}]({link})\n`{desc}`\n\n"
        except IndexError:
            break
    update.effective_message.reply_markdown(
        "**Search Query:**\n`" + match + "`\n\n**Results:**\n" + msg, link_preview=False
    )

__help__ = """
 - /google: Google search
 """

__mod_name__ = "Google"

GOOGLE_HANDLER = DisableAbleCommandHandler("google", google)

dispatcher.add_handler(GOOGLE_HANDLER)
