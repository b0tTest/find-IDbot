from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

START_BUTTON = InlineKeyboardMarkup( [[
       InlineKeyboardButton("π¨βπ» Creator", url=f"https://telegram.me/MyTestBotZ"),
       InlineKeyboardButton("πBotList", url=f"https://telegram.me/mybotzlist")
       ],[
       InlineKeyboardButton("π€ How to Use meh", callback_data="help")
       ]]
       )

HELP_BUTTON = InlineKeyboardMarkup( [[
       InlineKeyboardButton("Telegram π", callback_data="id"),
       InlineKeyboardButton("Telegram Info βΉοΈ", callback_data="info")
       ],[
       InlineKeyboardButton("π  Home", callback_data="start"),
       InlineKeyboardButton("π­ About", callback_data="about"),
       InlineKeyboardButton("β Close", callback_data="close")
       ]]
       )

ABOUT_BUTTON = InlineKeyboardMarkup( [[
       InlineKeyboardButton("π Back", callback_data="help"),
       InlineKeyboardButton("π  Home", callback_data="start"),
       InlineKeyboardButton("β Close", callback_data="close")
       ]]
       )
