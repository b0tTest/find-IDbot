
from pyrogram import filters
from pyrogram import Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
from plugins.translation import Translation
from plugins.config import Config

UPDATE_CHANNEL=Config.UPDATE_CHANNEL # Update Channel Forces Subscribe
BOT_USERNAME=Config.BOT_USERNAME # ReStart Option 
JOIN=Translation.JOIN_TEXT # Button Text (Update Channel)
TRY=Translation.TRY_TEXT # Button Text (Update Channel)
SUB_TEXT=Translation.FSUB_TEXT # FSUB Information Text


@Client.on_message(filters.private & ~filters.forwarded & ~filters.command(["start", "help", "about", "info", "information", "json", "source", "id"]))
async def stickers(bot, msg):
    update_channel = UPDATE_CHANNEL
    if update_channel:
        try:
            user = await bot.get_chat_member(update_channel, msg.chat.id)
            if user.status == "kicked out":
               await update.reply_text("😔 Sorry Dude, You are **BANNED 😜**")
               return
        except UserNotParticipant:
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
@Client.on_message(filters.command(["stickerid"]))
async def stickerid(bot, message):   
    if message.reply_to_message.sticker:
       await message.reply(f"**Your Sticker ID is**  \n `{message.reply_to_message.sticker.file_id}` \n \n ** Unique ID is ** \n\n`{message.reply_to_message.sticker.file_unique_id}` \n\n **© @findTgIDbot**", quote=True)
    else: 
       await message.reply("Hmmm, it's not a Sticker...!!!")
    
