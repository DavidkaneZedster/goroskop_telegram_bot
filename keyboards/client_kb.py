from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.types.base import T
from aiohttp.client import request

# from handlers.client import keyboard_delete

b1 = KeyboardButton('/Овен.')
b2 = KeyboardButton('/Стрелец.')
b3 = KeyboardButton('/Телец.')
b4 = KeyboardButton('/Близнецы.')
b5 = KeyboardButton('/Рак.')
b6 = KeyboardButton('/Лев.')
b7 = KeyboardButton('/Дева.')
b8 = KeyboardButton('/Весы.')
b9 = KeyboardButton('/Скорпион.')
b10 = KeyboardButton('/Козерог.')
b11 = KeyboardButton('/Водолей.')
b12 = KeyboardButton('/Рыбы.')
a1 = KeyboardButton('/Клавиатура.')
a2 = KeyboardButton('/Создатель.')
a3 = KeyboardButton('/help.')
a4 = KeyboardButton('/Убрать.')

markup_requests = ReplyKeyboardMarkup(resize_keyboard=True)  \
    .add(KeyboardButton('Отправить контакт', request_contact=True)).add(KeyboardButton('Отправить геолокацию.', request_location=True))

kb_client_second = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb_client_second.add(a1, a2, a3)

kb_client_third = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb_client_third.add(a1, a4, a2)

kb_client = ReplyKeyboardMarkup(resize_keyboard=True) # one_time_keyboard=True - скрытие клавиатуры после использования 

kb_client.row(b1, b2, b3, b4).row(b5, b6, b7, b8).row(b9, b10, b11, b12)

# add, row, insert