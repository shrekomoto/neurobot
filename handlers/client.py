from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

class FSMUser(StatesGroup):
    name = State()
    phone = State()
    mark = State()


#@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply('Привет!\nЯ жду твой отзыв! Если нужна помощь, введи \'/help\'', reply_markup=kb_client)


# @dp.message_handler(commands=["отзыв"], state=None)
async def making_user(msg: types.Message, state: FSMContext):
    await bot.send_message(msg.from_user.id, 'Введите ваше имя и фамилию')


# @dp.message_handler(state=User.name)
async def name_taken(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = msg.text
    await FSMUser.next()
    await msg.reply('Введите ваш номер телефона')


# @dp.message_handler(state=User.phone)
async def phone_taken(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone'] = msg.text
    await FSMUser.next()
    await msg.reply('Оцените по десятибалльной шкале')

# @dp.message_handler(state=User.mark)
async def mark_taken(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['mark'] = msg.text
    async with state.proxy() as data:
        await msg.reply(str(data))
    await state.finish()


def register_handler_client(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_message_handler(making_user, commands=['отзыв'], state=None)
    dp.register_message_handler(name_taken, state=FSMUser.name)
    dp.register_message_handler(phone_taken, state=FSMUser.phone)
    dp.register_message_handler(mark_taken, state=FSMUser.mark)
