from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply
from pyrogram import Client, filters

@Client.on_message(filters.command('myplan'))
async def myplan(_, message):
    text = f"""<b>ʜᴀʏ {message.from_user.mention}.., 👋

ʏᴏᴜ ᴅᴏ ɴᴏᴛ ʜᴀᴠᴇ ᴀɴʏ ᴀᴄᴛɪᴠᴇ ᴘʀᴇᴍɪᴜᴍ ᴘʟᴀɴꜱ, ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴛᴀᴋᴇ ᴘʀᴇᴍɪᴜᴍ ᴛʜᴇɴ
ᴄʟɪᴄᴋ ᴏɴ /upgrade ᴛᴏ ᴋɴᴏᴡ ᴀʙᴏᴜᴛ ᴛʜᴇ ᴘʟᴀɴ</b>"""
    keyboard = InlineKeyboardMarkup([[  
        InlineKeyboardButton("🫰 Buy Premium 💸", url="https://t.me/leotgadmin_bot")],  
        [InlineKeyboardButton("Cancel Premium", callback_data="close_data")]])
    await update.message.edit(text=text, reply_markup=keyboard)


@Client.on_message(filters.command('myplan'))
async def myplan(_, message):
    text = f"""<b>ʜᴀʏ {message.from_user.mention}.., 👋

ʏᴏᴜ ᴅᴏ ɴᴏᴛ ʜᴀᴠᴇ ᴀɴʏ ᴀᴄᴛɪᴠᴇ ᴘʀᴇᴍɪᴜᴍ ᴘʟᴀɴꜱ, ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴛᴀᴋᴇ ᴘʀᴇᴍɪᴜᴍ ᴛʜᴇɴ
ᴄʟɪᴄᴋ ᴏɴ /upgrade ᴛᴏ ᴋɴᴏᴡ ᴀʙᴏᴜᴛ ᴛʜᴇ ᴘʟᴀɴ</b>"""
    keyboard = InlineKeyboardMarkup([[  
        InlineKeyboardButton("🫰 Buy Premium 💸", url="https://t.me/leotgadmin_bot")],  
        [InlineKeyboardButton("Cancel Premium", callback_data="close_data")]])
    await message.reply_text(text=text, reply_markup=keyboard)
