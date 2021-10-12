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
from plugins.translation import Translation
from plugins.config import Config
from plugins.commands.buttons import START_BUTTON, HELP_BUTTON, ABOUT_BUTTON
from plugins.commands.commands import developer, feed_back, source, support_chat, bot_channel
from plugins.modules.buttons import ID_BUTTONS, INFO_BUTTONS

BOT_USERNAME=Config.BOT_USERNAME # ReStart Option 

@ZauteKm.on_callback_query()
async def cb_handler(client, query):

    if query.data == "start":
        await query.answer()

        await query.message.edit_text(
            Translation.START_MSG.format(query.from_user.mention),
            reply_markup=START_BUTTON,
            disable_web_page_preview=True
        )
        return

    elif query.data == "help":
        await query.answer()

        await query.message.edit_text(
            Translation.HELP_MSG,
            reply_markup=HELP_BUTTON,
            disable_web_page_preview=True
        )
        return

    elif query.data == "about":
        await query.answer()

        await query.message.edit_text(
            Translation.ABOUT_MSG.format(BOT_USERNAME, developer, co_developer, mt_chat, mt_bot, source),
            reply_markup=ABOUT_BUTTON,
            disable_web_page_preview=True
        )
        return

    if query.data == "id":
        await query.answer()

        await query.message.edit_text(
            Translation.ID_TEXT.format(query.from_user.id),
            reply_markup=ID_BUTTONS,
            disable_web_page_preview=True
        )
        return

    elif query.data == "info":
        await query.answer()

        await query.message.edit_text(
            Translation.INFO_TEXT.format(query.from_user.first_name, query.from_user.last_name, query.from_user.username, query.from_user.id, query.from_user.mention, query.from_user.dc_id, query.from_user.language_code, query.from_user.status),
            reply_markup=INFO_BUTTONS,
            disable_web_page_preview=True
        )
        return

    elif query.data == "close":
        await query.message.delete()
        
