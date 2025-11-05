from telegram import Update, Bot
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import asyncio
import datetime

# 🔹 आपका Bot Token
BOT_TOKEN = "8518610306:AAHnGSzN-_hzbsGkGICylmbr5-E1qHh_Wk0"
# 🔹 आपका Channel username
CHANNEL_USERNAME = "@Digitalindia8"

# 🔹 Auto message text
MESSAGE_TEXT = """
💠 यह *Digital India Dev Bhai* का आधिकारिक चैनल है!
📢 नए अपडेट और मटेरियल के लिए अभी सब्सक्राइब करें:
👉 [Digital India 8](https://t.me/Digitalindia8)
"""

# 🔹 /start command पर चलने वाला फंक्शन
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🙏 नमस्ते! यह Digital India Dev Bhai का आधिकारिक बॉट है!\n\n"
        "📢 चैनल से जुड़ें ताज़ा अपडेट और मटेरियल के लिए 👇\n"
        "👉 https://t.me/Digitalindia8"
    )

# 🔹 Auto message sender (हर 1 घंटे में)
async def auto_message(bot: Bot):
    while True:
        try:
            await bot.send_message(
                chat_id=CHANNEL_USERNAME,
                text=MESSAGE_TEXT,
                parse_mode="Markdown"
            )
            print(f"✅ Message sent at {datetime.datetime.now()}")
        except Exception as e:
            print(f"❌ Error: {e}")
        await asyncio.sleep(3600)

# 🔹 मुख्य कोड
async def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # /start command
    app.add_handler(CommandHandler("start", start))

    # Auto message background task
    bot = Bot(BOT_TOKEN)
    asyncio.create_task(auto_message(bot))

    print("🚀 Bot started...")
    await app.run_polling()

if name == "main":
    asyncio.run(main())
