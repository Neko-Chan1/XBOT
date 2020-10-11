import io
import os
import subprocess
import platform
import datetime
import html
import time
import sys
import requests
from time import sleep
from typing import List
from random import randint
from telegram import Bot, Update, TelegramError
from telegram.ext import CommandHandler, run_async, Filters
from telegram import ParseMode
from telegram.error import BadRequest

from xbotg import dispatcher, MESSAGE_DUMP, OWNER_ID
from xbotg.modules.helper_funcs.chat_status import dev_plus
from xbotg.modules.helper_funcs.alternate import typing_action
from xbotg.modules.helper_funcs.filters import CustomFilters


@run_async
@dev_plus
def leave(bot: Bot, update: Update, args: List[str]):
    message = update.effective_message
    if args:
        chat_id = str(args[0])
        try:
            bot.leave_chat(int(chat_id))
            message.reply_text(
                "Beep boop, I left that soup!.")
        except TelegramError:
            message.reply_text(
                "Beep boop, I could not leave that group(dunno why tho).")
    else:
        message.reply_text("Send a valid chat ID")

@run_async
@dev_plus
def gitpull(bot: Bot, update: Update):
    sent_msg = update.effective_message.reply_text(
        "Pulling all changes from remote and then attempting to restart."
    )
    subprocess.Popen("git pull", stdout=subprocess.PIPE, shell=True)

    sent_msg_text = sent_msg.text + "\n\nChanges pulled...I guess.. Restarting in "

    for i in reversed(range(5)):
        sent_msg.edit_text(sent_msg_text + str(i + 1))
        sleep(1)

    sent_msg.edit_text("Restarted.")

    os.system("restart.bat")
    os.execv("start.bat", sys.argv)

@run_async
@dev_plus
def restart(bot: Bot, update: Update):
    update.effective_message.reply_text(
        "Starting a new instance and shutting down this one"
    )
    if MESSAGE_DUMP:
        datetime_fmt = "%H:%M - %d-%m-%Y"
        current_time = datetime.datetime.utcnow().strftime(datetime_fmt)
        message = (
            f"<b>Bot Restarted </b>"
            f"<b>\nDate Bot Restart : </b><code>{current_time}</code>"
        )
        bot.send_message(
            chat_id=MESSAGE_DUMP,
            text=message,
            parse_mode=ParseMode.HTML,
            disable_web_page_preview=True,
        )
      os.system("bash start")
    


LEAVE_HANDLER = CommandHandler("leave", leave, pass_args=True)
GITPULL_HANDLER = CommandHandler("gitpull", gitpull)
RESTART_HANDLER = CommandHandler("restart", restart)

dispatcher.add_handler(LEAVE_HANDLER)
dispatcher.add_handler(GITPULL_HANDLER)
dispatcher.add_handler(RESTART_HANDLER)

__mod_name__ = "DEV"
__handlers__ = [LEAVE_HANDLER, GITPULL_HANDLER, RESTART_HANDLER]
