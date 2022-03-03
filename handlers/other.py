# from aiogram import types, Dispatcher
# from create_bot import dp

# incorrect_words = ["блять", "сука", "хуй", "ебал", "чанда", "пидор", "уёбок", "хуйло", "гандон", "петушара", "соси", "нахуй", "пошел нахуй"]
# incorrect_words_dot = ["блять.", "сука.", "хуй.", "ебал.", "чанда.", "пидор.", "уёбок.", "хуйло.", "гандон.", "петушара.", "соси.", "нахуй.", "пошел нахуй."]

# # @dp.message_handler()
# async def find_mat(message: types.message):
#     if any(word in message.text.lower() for word in incorrect_words or incorrect_words_dot):
#         await message.reply('Не стоит использовать такие выражения, лучше посмотрите ещё один гороскоп!')
#         await message.delete()

# def register_handlers_other(dp : Dispatcher):
#     dp.register_message_handler(find_mat)