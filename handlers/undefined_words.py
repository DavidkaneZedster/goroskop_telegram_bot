from aiogram import types, Dispatcher
from aiogram.utils import text_decorations
from create_bot import dp

dunno_words = [""]

# @dp.message_handler()
async def new_word(message : types.message):
    if any(word in message.text.lower() for word in incorrect_words or incorrect_words_dot):
        await message.reply('Не стоит использовать такие выражения, лучше посмотрите ещё один гороскоп!')
        await message.delete()
    # elif any(word in message.text.lower() for word in parol):
    #     await message.reply('Приветствую Вас!')
    elif any(word in message.text.lower() for word in dunno_words):
        f = open('new.txt', 'a+')
        f.write('\n')
        f.write(message.text)
        f.close()
        await message.answer('Что-то не то, я еще учусь отвечать на такие сообщения.\nПопробуйте воспользоваться командой:\n< /help >')

def register_handlers_undefined_words(dp : Dispatcher):
    # dp.register_message_handler(compliment)
    dp.register_message_handler(new_word)
