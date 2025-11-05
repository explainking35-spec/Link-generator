from telegram import Bot
import asyncio
import datetime

# 🔹 अपने Bot Token और Channel Username यहाँ डालें
BOT_TOKEN = "8518610306:AAHnGSzN-_hzbsGkGICylmbr5-E1qHh_Wk0"
CHANNEL_USERNAME = "@Digitalindia8"  # चैनल का username (लिंक नहीं)

# 🔹 वह मैसेज जो भेजना है
MESSAGE_TEXT = """
💠 यह *Digital India Dev Bhai* का आधिकारिक चैनल है!
📢 नए अपडेट और मटेरियल के लिए अभी **सब्सक्राइब करें:**
👉 [Digital India 8](https://t.me/Digitalindia8)
"""

bot = Bot(token=BOT_TOKEN)

async def send_auto_message():
    while True:
        try:
            await bot.send_message(chat_id=CHANNEL_USERNAME, text=MESSAGE_TEXT, parse_mode="Markdown")
            print(f"✅ Message sent at {datetime.datetime.now()}")
        except Exception as e:
            print(f"❌ Error: {e}")
        await asyncio.sleep(3600)  # हर 1 घंटे (3600 सेकंड) बाद भेजेगा

if __name__ == "__main__":
    asyncio.run(send_auto_message())
