import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "👋 Welcome to GMAIL BUY&SELL BD\n\n"
        "🛒 /buy - পণ্য/সার্ভিস দেখুন\n"
        "📦 /sell - আপনার পণ্য/সার্ভিস তালিকাভুক্ত করুন\n"
        "💰 /balance - ব্যালেন্স দেখুন\n"
        "❓ /help - সাহায্য\n"
    )
    await update.message.reply_text(text)

async def buy(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🛒 Buy Section\n\nএখানে বৈধ ডিজিটাল পণ্য বা সার্ভিসের তালিকা দেখানো হবে।"
    )

async def sell(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📦 Sell Section\n\nআপনার বৈধ ডিজিটাল পণ্য/সার্ভিসের তথ্য পাঠান।"
    )

async def balance(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💰 আপনার বর্তমান ব্যালেন্স: 0"
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "❓ Help\n\n"
        "/start - Bot চালু করুন\n"
        "/buy - Buy Section\n"
        "/sell - Sell Section\n"
        "/balance - Balance\n"
        "/help - Help"
    )

def main():
    if not BOT_TOKEN:
        raise RuntimeError("BOT_TOKEN is not configured")

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("buy", buy))
    app.add_handler(CommandHandler("sell", sell))
    app.add_handler(CommandHandler("balance", balance))
    app.add_handler(CommandHandler("help", help_command))

    app.run_polling()

if __name__ == "__main__":
    main()