from aiogram.utils import executor
from create_bot import dp
from handlers import client


client.register_handler_client(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)







# @dp.message_handler(content_types=['poll'])
# async def msg_with_poll(message: types.Message):
#     if not user_database.get(str(message.from_user.id)):
#         user_database[str(message.from_user.id)] = []
