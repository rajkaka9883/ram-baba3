 from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply
from pyrogram import Client, filters

@Client.on_message(filters.command('buy_premium'))
async def buy_premium(_, message):
    text = """ENGLISH 👇👇👇

🎖️ PREMIUM MEMBERSHIP 🎖️

⚡ WE ARE HAPPY TO ANNOUNCE OUR BOT'S PREMIUM MEMBERSHIP FOR PREMIUM USERS IN CHEAP RATES ⚜️

🥶 BENEFITS OF IT:
👉 FREE MOVIES / SERIES
👉 NEW RELEASES ON SAME DAY
👉 WITHOUT ANY ADS
👉 DIRECT FILES
👉 WATCH ONLINE SUPPORT
👉 FAST DOWNLOAD SUPPORT
👉 EVERY LANGUAGE AVAILABLE

🥶 PRICE:
💸 ONLY 50₹ / Month

🚨 Contact @leotgadmin_bot to buy.


Tamil(தமிழில்) 👇👇👇

🎖️ பிரீமியம் உறுப்பினர் 🎖️

⚡ மலிவு விலையில் பிரீமியம் பயனர்களுக்கு எங்கள் போட்டின் பிரீமியம் உறுப்பினர்களை அறிவிப்பதில் நாங்கள் மகிழ்ச்சியடைகிறோம் ⚜️

இதன் நன்மைகள்:
👉 இலவச MOVIES / SERIES
👉 ஒரே நாளில் புதிய வெளியீடுகள்
👉 எந்த விளம்பரமும் இல்லாமல்
👉 DIRECT FILE
👉 WATCH ONLINE SUPPORT
👉 FAST DOWNLOAD SUPPORT
👉 ஒவ்வொரு மொழியும் கிடைக்கும்

விலை:
💸 மாதம் 50₹ மட்டுமே

🚨 வாங்க, @leotgadmin_bot ஐத் தொடர்பு கொள்ளவும்"""
    keyboard = InlineKeyboardMarkup([[  
        InlineKeyboardButton("🫰 Buy Premium 💸", url="https://t.me/leotgadmin_bot")],  
        [InlineKeyboardButton("Cancel Premium", callback_data="close_data")]])
    await update.message.edit(text=text, reply_markup=keyboard)


@Client.on_message(filters.command('buy_premium'))
async def buy_premium(_, message):
    text = """ENGLISH 👇👇👇

🎖️ PREMIUM MEMBERSHIP 🎖️

⚡ WE ARE HAPPY TO ANNOUNCE OUR BOT'S PREMIUM MEMBERSHIP FOR PREMIUM USERS IN CHEAP RATES ⚜️

🥶 BENEFITS OF IT:
👉 FREE MOVIES / SERIES
👉 NEW RELEASES ON SAME DAY
👉 WITHOUT ANY ADS
👉 DIRECT FILES
👉 WATCH ONLINE SUPPORT
👉 FAST DOWNLOAD SUPPORT
👉 EVERY LANGUAGE AVAILABLE

🥶 PRICE:
💸 ONLY 50₹ / Month
(only for the first 10 members)

🚨 Contact @leotgadmin_bot to buy.


Tamil(தமிழில்) 👇👇👇

🎖️ பிரீமியம் உறுப்பினர் 🎖️

⚡ மலிவு விலையில் பிரீமியம் பயனர்களுக்கு எங்கள் போட்டின் பிரீமியம் உறுப்பினர்களை அறிவிப்பதில் நாங்கள் மகிழ்ச்சியடைகிறோம் ⚜️

இதன் நன்மைகள்:
👉 இலவச MOVIES / SERIES
👉 ஒரே நாளில் புதிய வெளியீடுகள்
👉 எந்த விளம்பரமும் இல்லாமல்
👉 DIRECT FILE
👉 WATCH ONLINE SUPPORT
👉 FAST DOWNLOAD SUPPORT
👉 ஒவ்வொரு மொழியும் கிடைக்கும்

விலை:
💸 மாதம் 50₹ மட்டுமே

🚨 வாங்க, @leotgadmin_bot ஐத் தொடர்பு கொள்ளவும்"""
    keyboard = InlineKeyboardMarkup([[  
        InlineKeyboardButton("🫰 Buy Premium 💸", url="https://t.me/leotgadmin_bot")],  
        [InlineKeyboardButton("Cancel Premium", callback_data="close_data")]])
    await message.reply_text(text=text, reply_markup=keyboard)
