# keyboard.py

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

drink_kb = ReplyKeyboardMarkup(resize_keyboard=True)
drink_kb.add(
    KeyboardButton("☕ Латте"),
    KeyboardButton("🍵 Матча"),
    KeyboardButton("🧋 Фраппе")
)


from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

drink_kb = ReplyKeyboardMarkup(resize_keyboard=True)
drink_kb.add(
    KeyboardButton("☕ Латте"),
    KeyboardButton("🍵 Матча"),
    KeyboardButton("🧋 Фраппе"),
    KeyboardButton("📝 Задание дня")
)
