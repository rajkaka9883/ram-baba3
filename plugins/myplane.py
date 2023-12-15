from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply
from pyrogram import Client, filters

@Client.on_message(filters.command('myplan'))
async def myplane(_, message):
    text = f"""<b>ʜᴀʏ {message.from_user.mention}.., 👋

ʏᴏᴜ ᴅᴏ ɴᴏᴛ ʜᴀᴠᴇ ᴀɴʏ ᴀᴄᴛɪᴠᴇ ᴘʀᴇᴍɪᴜᴍ ᴘʟᴀɴꜱ, ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴛᴀᴋᴇ ᴘʀᴇᴍɪᴜᴍ ᴛʜᴇɴ
ᴄʟɪᴄᴋ ᴏɴ /upgrade ᴛᴏ ᴋɴᴏᴡ ᴀʙᴏᴜᴛ ᴛʜᴇ ᴘʟᴀɴ</b>"""
    await update.message.edit(text=text)

   

@Client.on_message(filters.private & filters.command(["myplan"]))
async def myplane(_, message):
    text = f"""<b>ʜᴀʏ {message.from_user.mention}.., 👋

ʏᴏᴜ ᴅᴏ ɴᴏᴛ ʜᴀᴠᴇ ᴀɴʏ ᴀᴄᴛɪᴠᴇ ᴘʀᴇᴍɪᴜᴍ ᴘʟᴀɴꜱ, ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴛᴀᴋᴇ ᴘʀᴇᴍɪᴜᴍ ᴛʜᴇɴ
ᴄʟɪᴄᴋ ᴏɴ /upgrade ᴛᴏ ᴋɴᴏᴡ ᴀʙᴏᴜᴛ ᴛʜᴇ ᴘʟᴀɴ</b>"""   
    await update.message.edit(text=text)

