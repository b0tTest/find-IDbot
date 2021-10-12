from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

START_BUTTON = InlineKeyboardMarkup( [[
       InlineKeyboardButton("👨‍💻 Developer", url=f"t.me/ZauteKm"),
       InlineKeyboardButton("Open Source 💫", url=f"https://github.com/ZauteKm/tg_idsbot")
       ],[
       InlineKeyboardButton("⬇️ More Information ⬇️", callback_data="help")
       ]]
       )

HELP_BUTTON = InlineKeyboardMarkup( [[
       InlineKeyboardButton("🆔 Telegram ID", callback_data="id"),
       InlineKeyboardButton("Telegram Info ℹ️", callback_data="info")
       ],[
       InlineKeyboardButton("🏠 Home", callback_data="start"),
       InlineKeyboardButton("❌ Close", callback_data="close"),
       InlineKeyboardButton("About 🧐", callback_data="about")
       ]]
       )

ABOUT_BUTTON = InlineKeyboardMarkup( [[
       InlineKeyboardButton("🔙 Back", callback_data="help"),
       InlineKeyboardButton("🏠 Home", callback_data="start"),
       InlineKeyboardButton("Close ❌", callback_data="close")
       ]]
       )
