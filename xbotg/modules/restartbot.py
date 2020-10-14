import datetime
import html
import os
import platform
import subprocess
import time
import sys
from time import sleep
from typing import List
from platform import python_version

import requests
import speedtest
from psutil import boot_time, cpu_percent, disk_usage, virtual_memory
from spamwatch import __version__ as __sw__
from telegram import Bot, Update, TelegramError, ParseMode, __version__
from telegram.error import BadRequest
from telegram.ext import CommandHandler, Filters, run_async
from telegram.utils.helpers import mention_html

from xbotg import MESSAGE_DUMP, OWNER_ID, dispatcher
from xbotg.modules.helper_funcs.alternate import typing_action
from xbotg.modules.helper_funcs.filters import CustomFilters
from xbotg.modules.helper_funcs.chat_status import dev_plus


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
            f"<b>Admin:</b> (°IᎷ▸ᷝᷟ͢ƒiηɇͥ ͫ། ℻)"
            f"<b>\nDate Bot Restart : </b><code>{current_time}</code>"
        )
        bot.send_message(
            chat_id=MESSAGE_DUMP,
            text=message,
            parse_mode=ParseMode.HTML,
            disable_web_page_preview=True,
        )

    os.system("bash start")


RESTART_HANDLER = CommandHandler("restart", restart)

dispatcher.add_handler(RESTART_HANDLER)

__mod_name__ = "Restarting"
__handlers__ = [RESTART_HANDLER]

