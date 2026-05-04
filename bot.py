from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
    ApplicationBuilder,
    CallbackQueryHandler,
)
from data_collection.jobvision import jobvision
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_text = """
job finding bot
"""

    keyboard = [
        [
            InlineKeyboardButton("راهنما 📘", callback_data="help"),
            InlineKeyboardButton("شروع 🚀", callback_data="begin"),
        ],
        [
            InlineKeyboardButton("درباره ربات 🤖", callback_data="about"),
        ],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        welcome_text,
        reply_markup=reply_markup
    )


async def handle_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "begin":
        context.user_data["step"] = "waiting_for_name"
        await query.message.reply_text("جست و جوی شغل")


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if context.user_data.get("step") == "waiting_for_name":
        keyword = text
        context.user_data["step"] = None

        data = jobvision(keyword)

        if not data:
            await update.message.reply_text("چیزی پیدا نشد ")
            return

        message = ""

        for job in data:
            message += f"""
💼 {job['job title']}
🔗 {job['link']}

"""

        await update.message.reply_text(message)


app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(handle_button))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

app.run_polling()