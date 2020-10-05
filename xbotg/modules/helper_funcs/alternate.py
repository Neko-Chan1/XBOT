# UserindoBot
# Copyright (C) 2020  UserindoBot Team, <https://github.com/MoveAngel/UserIndoBot.git>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys
import traceback

from functools import wraps
from typing import Optional
from telegram import error, ChatAction
from xbotg.modules import languages

DUMP_CHAT = -1001188814263

def send_message(message, text, target_id=None, *args,**kwargs):
	if not target_id:
		try:
			return message.reply_text(text, *args,**kwargs)
		except error.BadRequest as err:
			if str(err) == "Reply message not found":
				try:
					return message.reply_text(text, quote=False, *args, **kwargs)
				except error.BadRequest as err:
					LOGGER.exception("ERROR: {}".format(err))
			elif str(err) == "Have no rights to send a message":
				try:
					dispatcher.bot.leaveChat(message.chat.id)
					dispatcher.bot.sendMessage(DUMP_CHAT, "I am leave chat `{}`\nBecause of: `Muted`".format(message.chat.title))

				except error.BadRequest as err:
					if str(err) == "Chat not found":
						pass
			else:
				LOGGER.exception("ERROR: {}".format(err))
	else:
		try:
			dispatcher.bot.send_message(target_id, text, *args, **kwarg)
		except error.BadRequest as err:
			LOGGER.exception("ERROR: {}".format(err))

def send_message_raw(chat_id, text, *args, **kwargs):
	try:
		return dispatcher.bot.sendMessage(chat_id, text, *args,**kwargs)
	except error.BadRequest as err:
		if str(err) == "Reply message not found":
				try:
					if kwargs.get('reply_to_message_id'):
						kwargs['reply_to_message_id'] = None
					return dispatcher.bot.sendMessage(chat_id, text, *args,**kwargs)
				except error.BadRequest as err:
					LOGGER.exception("ERROR: {}".format(err))
				'''elif str(err) == "Have no rights to send a message":
									try:
										dispatcher.bot.leaveChat(message.chat.id)
										dispatcher.bot.sendMessage(DUMP_CHAT, "I am leave chat `{}`\nBecause of: `Muted`".format(message.chat.title))
									except error.BadRequest as err:
										if str(err) == "Chat not found":
											pass'''
		else:
			LOGGER.exception("ERROR: {}".format(err))

def leave_chat(message):
	try:
		dispatcher.bot.leaveChat(message.chat.id)
		dispatcher.bot.sendMessage(DUMP_CHAT, "I am leave chat `{}`\nBecause of: `Muted`".format(message.chat.title))
	except error.BadRequest as err:
		if str(err) == "Chat not found":
			pass

def typing_action(func):
    """Sends typing action while processing func command."""

    @wraps(func)
    def command_func(update, context, *args, **kwargs):
        context.bot.send_chat_action(
            chat_id=update.effective_chat.id, action=ChatAction.TYPING
        )
        return func(update, context, *args, **kwargs)

    return command_func


def send_action(action):
    """Sends `action` while processing func command."""

    def decorator(func):
        @wraps(func)
        def command_func(update, context, *args, **kwargs):
            context.bot.send_chat_action(
                chat_id=update.effective_chat.id, action=action
            )
            return func(update, context, *args, **kwargs)

        return command_func

    return decorator
