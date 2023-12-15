from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply
from pyrogram import Client, filters

@Client.on_message(filters.command('upgrade'))
async def upgrade(_, message):
    text = """ᴄᴏᴍɪɴɢ ꜱᴏᴏɴ 😀"""
    keyboard = InlineKeyboardMarkup([[  
        InlineKeyboardButton("🫰 Buy Premium 💸", url="https://t.me/leotgadmin_bot")],  
        [InlineKeyboardButton("Cancel Premium", callback_data="close_data")]])
    await update.message.edit(text=text, reply_markup=keyboard)


@Client.on_message(filters.command('upgrade'))
async def upgrade(_, message):
    text = """ᴄᴏᴍɪɴɢ ꜱᴏᴏɴ 😀"""
    keyboard = InlineKeyboardMarkup([[  
        InlineKeyboardButton("🫰 Buy Premium 💸", url="https://t.me/leotgadmin_bot")],  
        [InlineKeyboardButton("Cancel Premium", callback_data="close_data")]])
    await message.reply_text(text=text, reply_markup=keyboard)
