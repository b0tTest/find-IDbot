#!/usr/bin/env python3
# Copyright (C) @ZauteKm
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from pyrogram import filters
from pyrogram import Client as MT_ID_Bot
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
from plugins.translation import Translation
from plugins.config import Config

UPDATE_CHANNEL=Config.UPDATE_CHANNEL # Update Channel Forces Subscribe
BOT_USERNAME=Config.BOT_USERNAME # ReStart Option 
JOIN=Translation.JOIN_TEXT # Button Text (Update Channel)
TRY=Translation.TRY_TEXT # Button Text (Update Channel)
SUB_TEXT=Translation.FSUB_TEXT # FSUB Information Text

@ZauteKm.on_message(filters.private & filters.forwarded)
async def info(bot, msg):
    update_channel = UPDATE_CHANNEL
    if update_channel:
        try:
            user = await bot.get_chat_member(update_channel, msg.chat.id)
            if user.status == "kicked out":
               await update.reply_text("😔 Sorry Dude, You are **BANNNED 😜**")
               return
        except UserNotParticipant:
            #await update.reply_text(f"Join @{Channel User Name} To Use Me") From Bot.py
            await msg.reply_text(
                text=f"<b>{SUB_TEXT}</b>",
                reply_markup=InlineKeyboardMarkup([
                    [ InlineKeyboardButton(text=f"{JOIN}", url=f"t.me/{UPDATE_CHANNEL}")],
                    [ InlineKeyboardButton(text=f"{TRY}", url=f"https://t.me/{BOT_USERNAME}?start=try")]
              ])
            )
            return
        except Exception:
            await msg.reply_text(f"@{UPDATE_CHANNEL}")
            return
    if msg.forward_from:
        text = "<u>Forward Information 👀</u> \n\n"
        if msg.forward_from["is_bot"]:
            text += "<b><u>🤖 Bot Info</u></b>"
        else:
            text += "<b><u>👤 User Indo</u></b>"
        text += f'\n\n<b>👨‍💼 Name:</b> {msg.forward_from["first_name"]}'
        if msg.forward_from["username"]:
            text += f'\n\n<b>🔗 UserName:</b> @{msg.forward_from["username"]} \n\n🆔 ID : <code>{msg.forward_from["id"]}</code>'
        else:
            text += f'\n\n<b>🆔 ID:</b> `{msg.forward_from["id"]}`'
        await msg.reply(text, quote=True)
    else:
        hidden = msg.forward_sender_name
        if hidden:
            await msg.reply(
                f"❌️ Error <b><i>{hidden}</i></b> ❌️ Error",
                quote=True,
            )
        else:
            text = f"<b><u>Forward Information 👀</u></b>.\n\n"
            if msg.forward_from_chat["type"] == "channel":
                text += "<b><u>📢 Channel</u></b>"
            if msg.forward_from_chat["type"] == "supergroup":
                text += "<b><u>🗣️ Group</u></b>"
            text += f'\n\n<b>📃 Name</b> {msg.forward_from_chat["title"]}'
            if msg.forward_from_chat["username"]:
                text += f'\n\n<b>➡️ From:</b> @{msg.forward_from_chat["username"]}'
                text += f'\n\n<b>🆔 ID:</b> `{msg.forward_from_chat["id"]}`'
            else:
                text += f'\n\n<b>🆔 ID</b> `{msg.forward_from_chat["id"]}`\n\n'
            await msg.reply(text, quote=True)
