from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply
from pyrogram import Client, filters

@Client.on_message(filters.command('upgrade'))
async def upgrade(_, message):
    text = f"""<b>ʜᴀʏ {message.from_user.mention}..,👋
   ᴏᴜʀ ᴛʜɪꜱ ꜰʀᴇᴀᴛᴜʀᴇ ᴄᴏᴍɪɴɢ ꜱᴏᴏɴ . ᴀꜱ ꜱᴏᴏɴ ᴀꜱ ᴘᴏꜱꜱɪʙʟᴇ 😀</b>"""
    keyboard = InlineKeyboardMarkup([[  
        InlineKeyboardButton("♻️ ʙᴜʏ ᴘʀᴇᴍɪᴜᴍ ꜱᴜʙꜱᴄʀɪᴘᴛɪᴏɴ  / ꜱᴇɴᴅ ꜱᴄʀᴇᴇɴꜱʜᴏᴛ ♻️", url="https://t.me/PERSONAL_CHAT_ASSISTANT_BOT")],  
        [InlineKeyboardButton("❌ ᴄʟᴏꜱᴇ  ❌", callback_data="close_data")]])
    await update.message.edit(text=text, reply_markup=keyboard)


@Client.on_message(filters.command('upgrade'))
async def upgrade(_, message):
    text = f"""<b>ʜᴀʏ {message.from_user.mention}..,👋
   ᴏᴜʀ ᴛʜɪꜱ ꜰʀᴇᴀᴛᴜʀᴇ ᴄᴏᴍɪɴɢ ꜱᴏᴏɴ . ᴀꜱ ꜱᴏᴏɴ ᴀꜱ ᴘᴏꜱꜱɪʙʟᴇ 😀</b>"""
    keyboard = InlineKeyboardMarkup([[  
        InlineKeyboardButton("♻️ ʙᴜʏ ᴘʀᴇᴍɪᴜᴍ ꜱᴜʙꜱᴄʀɪᴘᴛɪᴏɴ / ꜱᴇɴᴅ ꜱᴄʀᴇᴇɴꜱʜᴏᴛ ♻️", url="https://t.me/PERSONAL_CHAT_ASSISTANT_BOT")],  
        [InlineKeyboardButton("❌ ᴄʟᴏꜱᴇ  ❌", callback_data="close_data")]])
    await message.reply_text(text=text, reply_markup=keyboard)
