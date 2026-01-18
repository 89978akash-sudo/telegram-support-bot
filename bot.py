from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

BOT_TOKEN = "8572936002:AAH9OVyfUKLhj7Wb1gDf hmKdy_RieQgvpVY"
ADMIN_ID = 7160389642  # aapki Telegram ID

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    text = update.message.text

    if user.id != ADMIN_ID:
        await context.bot.send_message(
            chat_id=ADMIN_ID,
            text=f"📩 Message from @{user.username} ({user.id}):\n{text}"
        )
    else:
        if update.message.reply_to_message:
            user_id = int(update.message.reply_to_message.text.split("(")[-1].replace("):", ""))
            await context.bot.send_message(chat_id=user_id, text=update.message.text)

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
app.run_polling()
