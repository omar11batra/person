from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# ضع التوكن الخاص بك هنا
TOKEN = "7767534790:AAGHSlDN7fUQhZUMX8nWs7hTWpVl7w0ni90"

# إنشاء التطبيق باستخدام التوكن
app = Application.builder().token(TOKEN).build()

# دالة الرد على الأوامر
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("مرحبًا! أنا بوت المسافر عبر الزمن، لقد تم تطويري بواسطة م/ عمر عبدالعزيز، اسألني عن أي شخصية تاريخية")

# إضافة معالج للأوامر
app.add_handler(CommandHandler("start", start))

# تشغيل البوت
if __name__ == "__main__":
    print("البوت يعمل الآن...")
    app.run_polling()
