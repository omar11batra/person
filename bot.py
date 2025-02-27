from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.utils import executor
from pytube import YouTube
import os

# استبدل 'YOUR_BOT_TOKEN' بتوكن البوت الخاص بك
TOKEN = "7767534790:AAGHSlDN7fUQhZUMX8nWs7hTWpVl7w0ni90"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply(" ،مرحبًا! أرسل رابط فيديو من يوتيوب وسأقوم بتنزيله لك. مطور هذا البوت ( م/ عمر عبدالعزيز ) ، معرف التلجرام الخاص به هو : @omar11batra ")

@dp.message_handler()
async def download_video(message: types.Message):
    url = message.text
    if "youtube.com" not in url and "youtu.be" not in url:
        await message.reply("يرجى إرسال رابط يوتيوب صالح.")
        return
    
    await message.reply("جاري التنزيل، يرجى الانتظار...")
    
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        filename = stream.download()
        
        with open(filename, "rb") as video:
            await bot.send_video(message.chat.id, video, caption=f"📹 {yt.title}")
        
        os.remove(filename)  # حذف الملف بعد الإرسال
    except Exception as e:
        await message.reply(f"حدث خطأ أثناء التنزيل: {e}")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
