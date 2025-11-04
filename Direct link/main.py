from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes, CommandHandler
import os

BOT_TOKEN = "YOUR_BOT_TOKEN"  # <-- यहाँ नया BotFather token डालो
CHANNEL_USERNAME = "@Digitalindia8"  # <-- तुम्हारा चैनल
SERVER_URL = "https://your-domain.onrender.com"  # <-- Render URL डालना

UPLOAD_DIR = "static"
os.makedirs(UPLOAD_DIR, exist_ok=True)

async def is_subscribed(user_id, context):
    """Check user is member of your channel"""
    try:
        member = await context.bot.get_chat_member(CHANNEL_USERNAME, user_id)
        if member.status in ["member", "administrator", "creator"]:
            return True
    except:
        pass
    return False


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if not await is_subscribed(user_id, context):
        await update.message.reply_text(
            f"🚫 पहले हमारे चैनल को join करो ताकि bot use कर सको!\n\n👉 Join Here: {CHANNEL_USERNAME}"
        )
        return

    await update.message.reply_text("📤 कोई भी फ़ाइल भेजो — मैं तुम्हें direct download link दूँगा!")


async def handle_file(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if not await is_subscribed(user_id, context):
        await update.message.reply_text(f"❌ पहले चैनल join करो: {CHANNEL_USERNAME}")
        return

    file_obj = update.message.document or update.message.video or (
        update.message.photo[-1] if update.message.photo else None
    )
    if not file_obj:
        await update.message.reply_text("❌ कृपया कोई फ़ाइल भेजो।")
        return

    file_id = file_obj.file_id
    new_file = await context.bot.get_file(file_id)
    file_name = file_obj.file_name or f"file_{file_id}.bin"
    file_path = os.path.join(UPLOAD_DIR, file_name)
    await new_file.download_to_drive(file_path)

    file_url = f"{SERVER_URL}/static/{file_name}"
    await update.message.reply_text(
        f"✅ फ़ाइल save हो गई!\n📎 `{file_name}`\n\n🔗 Download Link:\n{file_url}",
        parse_mode="Markdown"
    )


app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.ALL, handle_file))
app.run_polling()
