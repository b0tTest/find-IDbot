from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

ID_BUTTON = InlineKeyboardMarkup( [[
       InlineKeyboardButton("🍿 Join my Updates Channel 🍿", url="t.me/MyTestBotZ")
       ]]
       )
INFO_BUTTON = InlineKeyboardMarkup( [[
       InlineKeyboardButton("🍿 Join my Updates Channel 🍿", url="t.me/MyTestBotZ")
       ]]
       )
ID_BUTTONS = InlineKeyboardMarkup( [[
       InlineKeyboardButton("🧾 Information", callback_data="info")
       ],[
       InlineKeyboardButton("🔙 Back to Help", callback_data="help")
       ]]
       )
INFO_BUTTONS = InlineKeyboardMarkup( [[
       InlineKeyboardButton("🔍 Telegram 🆔", callback_data="id")
       ],[
       InlineKeyboardButton("🔙 Back to Help", callback_data="help")
       ]]
       )
JSON_BUTTON = InlineKeyboardMarkup( [[
       InlineKeyboardButton("🎭 Creator", url="t.me/OO7ROBOT")
       ]]
       )
