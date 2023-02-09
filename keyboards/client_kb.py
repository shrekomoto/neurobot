from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton

b1 = KeyboardButton('/отзыв')
b2 = KeyboardButton('/отмена')


kb_client = ReplyKeyboardMarkup(resize_keyboard=True).row(b1,b2)