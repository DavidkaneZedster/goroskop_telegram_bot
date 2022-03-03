from aiogram.utils import executor
from create_bot import dp

async def on_startup(_):
    print('Bot online.')

from handlers import client, undefined_words #,other

client.register_handlers_client(dp)
# other.register_handlers_other(dp)
undefined_words.register_handlers_undefined_words(dp)


# @dp.message_handler()
# async def echo_send(message : types.message):
#     if {i.lower(). for i in message.text.split(' ')}
    
    # if message.text == 'Привет.':
    #     await message.answer('И тебе не хворать.')
    # # await message.reply(message.text)
    # # await bot.send_message(message.from_user.id, message.text)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

