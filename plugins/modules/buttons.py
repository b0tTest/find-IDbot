from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

ID_BUTTON = InlineKeyboardMarkup( [[
       InlineKeyboardButton("๐ฟ Join my Updates Channel ๐ฟ", url="t.me/MyTestBotZ")
       ]]
       )
INFO_BUTTON = InlineKeyboardMarkup( [[
       InlineKeyboardButton("๐ฟ Join my Updates Channel ๐ฟ", url="t.me/MyTestBotZ")
       ]]
       )
ID_BUTTONS = InlineKeyboardMarkup( [[
       InlineKeyboardButton("๐งพ Information", callback_data="info")
       ],[
       InlineKeyboardButton("๐ Back to Help", callback_data="help")
       ]]
       )
INFO_BUTTONS = InlineKeyboardMarkup( [[
       InlineKeyboardButton("๐ Telegram ๐", callback_data="id")
       ],[
       InlineKeyboardButton("๐ Back to Help", callback_data="help")
       ]]
       )
JSON_BUTTON = InlineKeyboardMarkup( [[
       InlineKeyboardButton("๐ญ Creator", url="t.me/OO7ROBOT")
       ]]
       )
