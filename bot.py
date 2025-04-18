# bot.py
from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import random
from predictions import predictions
from keyboard import drink_kb
from tasks import get_random_task


API_TOKEN = '7925334331:AAFjfKpuKvGT8fCFOgjPGfW7pt_gjjvb5lQ'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])

async def send_welcome(message: types.Message):
    await message.reply("🍪 Добро пожаловать в нашу уютную кофейню!\n\nЧто будете пить сегодня?", reply_markup=drink_kb)

@dp.message_handler(lambda message: message.text in ["☕ Латте", "🍵 Матча", "🧋 Фраппе"])
async def serve_fortune(message: types.Message):
    phrase = random.choice(predictions)
    await message.reply(f"Отличный выбор! {message.text} уже готов.\n\nВот твоя печенька дня: \U0001F960\n\n\"{phrase}\"", reply_markup=drink_kb)


@dp.message_handler(lambda message: message.text == "📝 Задание дня")
async def send_task(message: types.Message):
    task = get_random_task()
    await message.reply(f"🌍 Твое доброе дело на сегодня:\n\n📝 {task}")



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)


