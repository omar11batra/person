import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# الحصول على التوكن من متغيرات البيئة
TOKEN = os.getenv("7767534790:AAGHSlDN7fUQhZUMX8nWs7hTWpVl7w0ni90")

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("مرحبًا! أنا بوت المسافر عبر الزمن، لقد تم تطويري بواسطة م/ عمر عبدالعزيز، اسألني عن أي شخصية تاريخية.")

updater = Updater(TOKEN)
dp = updater.dispatcher

dp.add_handler(CommandHandler("start", start))

updater.start_polling()
updater.idle()
