
from pyrogram import filters
from pyrogram import Client
from plugins.translation import Translation
from plugins.config import Config
from plugins.commands.buttons import START_BUTTON, HELP_BUTTON, ABOUT_BUTTON
from plugins.commands.commands import developer, feed_back, source, support_chat, bot_channel
from plugins.modules.buttons import ID_BUTTONS, INFO_BUTTONS

BOT_USERNAME=Config.BOT_USERNAME # ReStart Option 

@Client.on_callback_query()
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
        
