from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

START_BUTTON = InlineKeyboardMarkup( [[
       InlineKeyboardButton("👨‍💻 Creator", url=f"https://telegram.me/MyTestBotZ"),
       InlineKeyboardButton("📝BotList", url=f"https://telegram.me/mybotzlist")
       ],[
       InlineKeyboardButton("🤔 How to Use meh", callback_data="help")
       ]]
       )

HELP_BUTTON = InlineKeyboardMarkup( [[
       InlineKeyboardButton("Telegram 🆔", callback_data="id"),
       InlineKeyboardButton("Telegram Info ℹ️", callback_data="info")
       ],[
       InlineKeyboardButton("🏠 Home", callback_data="start"),
       InlineKeyboardButton("💭 About", callback_data="about"),
       InlineKeyboardButton("⛔ Close", callback_data="close")
       ]]
       )

ABOUT_BUTTON = InlineKeyboardMarkup( [[
       InlineKeyboardButton("🔙 Back", callback_data="help"),
       InlineKeyboardButton("🏠 Home", callback_data="start"),
       InlineKeyboardButton("⛔ Close", callback_data="close")
       ]]
       )
