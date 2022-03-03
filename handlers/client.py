from aiogram.types import user
import requests
from bs4 import BeautifulSoup
from logging import info
from aiogram import types
from aiogram.dispatcher.dispatcher import Dispatcher
from aiohttp.client import request
from create_bot import dp, bot
from keyboards import kb_client, kb_client_second, kb_client_third, markup_requests
from aiogram.types import ReplyKeyboardRemove # reply_markup=ReplyKeyboardRemove()
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

# parol = ["это", 'Я.']


# async def compliment(message : types.message):
#     if any(word in message.text.lower() for word in parol):
#         await message.reply('Приветствую Вас!')


# @dp.message_handler(commands=['start'])
async def command_start(message : types.message):
    try:
        await bot.send_message(message.from_user.id, 'Здарова, зае6ал)\nЯ показываю и рассказываю все гороскопы на любой знак зодиака на сегодняшний день. Заранее говорю, что при написании команды не учитываются символы «<» и «>», их я использую для того, чтобы четко отделить команду от остального текста, команды бота пишутся строго с «/» и далее следует текст. Ставить ли точку в конце команды или нет - дело сугубо Ваше, команда отрабатывает как с точками в конце, так и без них.\n\nЧтобы узнать свой гороскоп на сегодня вопспользуйтесь следующей командой:\n< /Ваш знак зодиака >, например\n< /Стрелец > или < /Близнецы >.\n\nЕщё можно вспользоваться клавиатурой, чтобы не печатать ничего самостоятельно и ускорить процесс использования/получения информации, вызывается она командой:\n< /Клавиатура >.\n\nСоздатель бота: David Klorikyan, чуть больше информации по команде:\n< /Создатель >.\nИнформация о командах бота в - /help.', reply_markup=kb_client_second)
        # await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему:\nhttps://t.me/neZedsterbot')

# test1
async def test123(message: types.message):
    await bot.send_message(message.from_user.id, 'da', reply_markup=markup_requests)

# @dp.message.handler(commands=['help', 'help.'])
async def command_help(message : types.message):
    await bot.send_message(message.from_user.id, 'Вижу Вам нужна помощь с командами.\nВот список всех существующих команд бота neZedster!\n\n/start - приветствие с ботом, небольшой экскурс по командам.\n/help - та самая команда, которая дает тебе это прочитать.\n/Ваш знак зодиака - просмотр гороскопа для указанного знака зодиака на сегодняшний день, пример: /Овен.\n/Клавиатура - подключение клавиатуры для упрощения пользования командами бота, а именно для просмотра гороскопов по ЗЗ.\n/Убрать - команда, убирающая вызванную клавиатуру.\n/Создатель - информация и связь с создателем бота, а так же реквизиты для поддержки по Вашему желанию.\n\nУдачи в использовании бота neZedster!', reply_markup=kb_client_third)

# @dp.message_handler(commands=['Клавиатура'])
async def goroskop_bot_command(message : types.message):
    await bot.send_message(message.from_user.id, 'Вуаля, клавиатура запущена, выбирайте знак зодиака, гороскоп которого Вы хотите посмотреть!', reply_markup=kb_client)

# @dp.message_handler(commands=['Убрать', 'Убрать.'])
async def keyboard_delete_command(message : types.message):
    await bot.send_message(message.from_user.id, 'Вуаля, клавиатура убрана.\nДля повторного вызова клавиатуры используйте команду:\n< /Клавиатура. >', reply_markup=ReplyKeyboardRemove())

# @dp.message_handler(commands=['Создатель'])
async def info_creator_command(message : types.message):
    await bot.send_message(message.from_user.id, '~Luck love the reckless~\n Создатель бота - David Klorikyan.\n  VK: id309877578\n  Telegram: https://t.me/Davidka_neZedster\n  Почта: kdavid161262@yandex.ru\n  Свои идеи и предложения можете присылать куда Вам удобно, главное везде сверху пишите примечание:\n«Бот neZedster».\n   Принимаю вашу поддержку на карту.\n     Номер карты: 1234 5678 9101 1121')  

# @dp.message_handler(commands=['Овен', 'Овен.'])
async def oven_command(message : types.message):
    await bot.send_message(message.from_user.id, parse_ssr_oven())

# @dp.message_handler(commands=['Стрелец', 'Стрелец.'])
async def strelec_command(message : types.message):
    await bot.send_message(message.from_user.id, parse_ssr_strelec())

# @dp.message_handler(commands=['Телец', 'Телец.'])
async def telec_command(message : types.message):
    await bot.send_message(message.from_user.id, parse_ssr_telec())

# @dp.message_handler(commands=['Близнецы', 'Близнецы.'])
async def blizneci_command(message : types.message):
    await bot.send_message(message.from_user.id, parse_ssr_blizneci())

# @dp.message_handler(commands=['Рак', 'Рак.'])
async def rak_command(message : types.message):
    await bot.send_message(message.from_user.id, parse_ssr_rak())

# @dp.message_handler(commands=['Лев', 'Лев.'])
async def lev_command(message : types.message):
    await bot.send_message(message.from_user.id, parse_ssr_lev())

# @dp.message_handler(commands=['Дева', 'Дева.'])
async def deva_command(message : types.message):
    await bot.send_message(message.from_user.id, parse_ssr_deva())

# @dp.message_handler(commands=['Весы', 'Весы.'])
async def vesi_command(message : types.message):
    await bot.send_message(message.from_user.id, parse_ssr_vesi())

# @dp.message_handler(commands=['Скорпион', 'Скорпион.'])
async def scorpion_command(message : types.message):
    await bot.send_message(message.from_user.id, parse_ssr_scorpion())

# @dp.message_handler(commands=['Козерог', 'Козерог.'])
async def kozerog_command(message : types.message):
    await bot.send_message(message.from_user.id, parse_ssr_kozerog())

# @dp.message_handler(commands=['Водолей', 'Водолей.'])
async def vodoley_command(message : types.message):
    await bot.send_message(message.from_user.id, parse_ssr_vodoley())

# @dp.message_handler(commands=['Рыбы', 'Рыбы.'])
async def ribi_command(message : types.message):
    await bot.send_message(message.from_user.id, parse_ssr_ribi())

# @dp.message_handler(commands=['Хочу', 'Хочу.'])
# async def compliment(message : types.message):
#     await bot.send_message(message.from_user.id, 'Введите пароль.')
#     if any(word in message.text.lower() for word in parol):
#         await message.reply('Приветствую Вас!')

# ****************************************PARSERS START****************************************

def parse_ssr_oven():
    response = requests.get('https://www.astrostar.ru/horoscopes/main/oven/day.html')
    soup = BeautifulSoup(response.content, 'html.parser')
    data = soup.find('p').text
    return data

def parse_ssr_strelec():
    response = requests.get('https://www.astrostar.ru/horoscopes/main/strelets/day.html')
    soup = BeautifulSoup(response.content, 'html.parser')
    data = soup.find('p').text
    return data

def parse_ssr_telec():
    response = requests.get('https://www.astrostar.ru/horoscopes/main/telets/day.html')
    soup = BeautifulSoup(response.content, 'html.parser')
    data = soup.find('p').text
    return data

def parse_ssr_blizneci():
    response = requests.get('https://www.astrostar.ru/horoscopes/main/bliznetsi/day.html')
    soup = BeautifulSoup(response.content, 'html.parser')
    data = soup.find('p').text
    return data

def parse_ssr_rak():
    response = requests.get('https://www.astrostar.ru/horoscopes/main/rac/day.html')
    soup = BeautifulSoup(response.content, 'html.parser')
    data = soup.find('p').text
    return data

def parse_ssr_lev():
    response = requests.get('https://www.astrostar.ru/horoscopes/main/lev/day.html')
    soup = BeautifulSoup(response.content, 'html.parser')
    data = soup.find('p').text
    return data

def parse_ssr_deva():
    response = requests.get('https://www.astrostar.ru/horoscopes/main/deva/day.html')
    soup = BeautifulSoup(response.content, 'html.parser')
    data = soup.find('p').text
    return data

def parse_ssr_vesi():
    response = requests.get('https://www.astrostar.ru/horoscopes/main/vesy/day.html')
    soup = BeautifulSoup(response.content, 'html.parser')
    data = soup.find('p').text
    return data

def parse_ssr_scorpion():
    response = requests.get('https://www.astrostar.ru/horoscopes/main/scorpion/day.html')
    soup = BeautifulSoup(response.content, 'html.parser')
    data = soup.find('p').text
    return data

def parse_ssr_kozerog():
    response = requests.get('https://www.astrostar.ru/horoscopes/main/kozerog/day.html')
    soup = BeautifulSoup(response.content, 'html.parser')
    data = soup.find('p').text
    return data

def parse_ssr_vodoley():
    response = requests.get('https://www.astrostar.ru/horoscopes/main/vodoley/day.html')
    soup = BeautifulSoup(response.content, 'html.parser')
    data = soup.find('p').text
    return data

def parse_ssr_ribi():
    response = requests.get('https://www.astrostar.ru/horoscopes/main/riby/day.html')
    soup = BeautifulSoup(response.content, 'html.parser')
    data = soup.find('p').text
    return data

#, {'horoscope-text'}
# *****************************************PARSERS END******************************************


def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'start.'])
    dp.register_message_handler(command_help, commands=['help', 'help.'])
    dp.register_message_handler(test123, commands=['Test', 'Test.'])
    dp.register_message_handler(goroskop_bot_command, commands=['Клавиатура', 'Клавиатура.'])
    dp.register_message_handler(keyboard_delete_command, commands=['Убрать', 'Убрать.'])
    dp.register_message_handler(info_creator_command, commands=['Создатель', 'Создатель.'])
    dp.register_message_handler(oven_command, commands=['Овен', 'Овен.'])
    dp.register_message_handler(strelec_command, commands=['Стрелец', 'Стрелец.'])
    dp.register_message_handler(telec_command, commands=['Телец', 'Телец.'])
    dp.register_message_handler(blizneci_command, commands=['Близнецы', 'Близнецы.'])
    dp.register_message_handler(rak_command, commands=['Рак', 'Рак.'])
    dp.register_message_handler(lev_command, commands=['Лев', 'Лев.'])
    dp.register_message_handler(deva_command, commands=['Дева', 'Дева.'])
    dp.register_message_handler(vesi_command, commands=['Весы', 'Весы.'])
    dp.register_message_handler(scorpion_command, commands=['Скорпион', 'Скорпион.'])
    dp.register_message_handler(kozerog_command, commands=['Козерог', 'Козерог.'])
    dp.register_message_handler(vodoley_command, commands=['Водолей', 'Водолей.'])
    dp.register_message_handler(ribi_command, commands=['Рыбы', 'Рыбы.'])
    # dp.register_message_handler(compliment, commands=['Хочу', 'Хочу.'])
