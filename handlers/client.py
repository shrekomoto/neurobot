import emoji
from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import client_kb
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from database import neuro_db
from aiogram.utils.markdown import bold
from aiogram.dispatcher.filters import Text
from aiogram.types import ParseMode, ReplyKeyboardRemove


class FSMUser(StatesGroup):
    name = State()
    phone = State()
    mk = State()
    mark = State()
    first_q = State()
    second_q = State()
    third_q = State()
    fourth_q = State()
    fifth_q = State()
    sixth_q = State()
    # seventh_q = State()
    eighth_q = State()
    gift = State()


# @dp.message_handler(commands=['start'])
async def start_command(msg: types.Message):
    with open('/Users/Admin/PycharmProjects/neurobot/database/greet.jpeg', 'rb') as photo:
        await bot.send_photo(chat_id=msg.from_user.id, photo=photo)
    await msg.reply('''Привет! Я – НейроБот от Юлии Дедовой!
Я задам вам несколько вопросов по поводу прошедшего Мастер-класса,
А в конце вас ждет подарок от Юлии!''', reply_markup=client_kb.kb_client)


# @dp.message_handler(commands=["отзыв"], state=None)
async def making_user(msg: types.Message, state: FSMContext):
    await FSMUser.name.set()
    await msg.answer('Введите ваше имя и фамилию')


# @dp.message_handler(state=User.name)
async def name_taken(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = msg.text
    await FSMUser.next()
    await msg.answer('Введите ваш номер телефона')


# @dp.message_handler(state=User.phone)
async def phone_taken(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone'] = msg.text
    await FSMUser.next()
    await msg.answer('Напишите название мастер-класса и дату его посещения (например, 22.02.2023)')


async def mk_date(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['mk'] = msg.text
    await FSMUser.next()
    await msg.answer('Оцените мероприятие по десятибалльной шкале')


# @dp.message_handler(state=User.mark)
async def mark_taken(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['mark'] = msg.text
    await FSMUser.next()
    await msg.answer('Рисовали ли Вы ранее Нейрографику?', reply_markup=client_kb.first_q_kb)


async def first_q(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['first_q'] = msg.text
    await FSMUser.next()
    await msg.answer('На сегодняшнем МК что Вы получили, как начинающий в нейрографике:',
                     reply_markup=client_kb.second_q_kb)


async def second_q(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['second_q'] = msg.text
    await FSMUser.next()
    await msg.answer('Были ли объяснения и комментарии понятны? Если остались вопросы, пиши их сюда',
                     reply_markup=client_kb.third_q_kb)


async def third_q(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['third_q'] = msg.text
    await FSMUser.next()
    await msg.answer('Какой результат вы ощутили сразу после МК?', reply_markup=client_kb.fourth_q_kb)


async def fourth_q(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['fourth_q'] = msg.text
    await FSMUser.next()
    await msg.answer('Какой отзыв о МК вы можете оставить?')


async def fifth_q(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['fifth_q'] = msg.text
    await FSMUser.next()
    await msg.answer(
        'Хотели бы Вы получать приглашения на МК по другим темам?',
        reply_markup=client_kb.sixth_q_kb)


async def sixth_q(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['sixth_q'] = msg.text
    await  FSMUser.next()
    #     await msg.answer('Хотели бы Вы записаться на индивидуальную сессию?', reply_markup=client_kb.seventh_q_kb)
    #
    #
    # async def seventh_q(msg: types.Message, state: FSMContext):
    #     async with state.proxy() as data:
    #         data['seventh_q'] = msg.text
    #     await FSMUser.next()
    await msg.answer('Какой вопрос или сферу жизни Вы хотите проработать на индивидуальной сессии?',
                     reply_markup=client_kb.eighth_q_kb)


async def eighth_q(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['eighth_q'] = msg.text
    await neuro_db.sql_add_command(state)
    await FSMUser.next()
    await msg.answer('''Благодарю за ответы!
Выбирайте подарок:''', reply_markup=client_kb.gift_kb)


async def gift(msg: types.Message, state: FSMContext):
    if msg.text == 'Скидка на индивидуальную сессию':
        with open('/Users/Admin/PycharmProjects/neurobot/database/gift1.jpg', 'rb') as photo:
            await bot.send_photo(chat_id=msg.from_user.id, photo=photo, reply_markup=ReplyKeyboardRemove())
        await state.finish()
    elif msg.text == 'Скидка на Мастер-класс в группе':
        with open('/Users/Admin/PycharmProjects/neurobot/database/gift2.jpg', 'rb') as photo:
            await bot.send_photo(chat_id=msg.from_user.id, photo=photo, reply_markup=ReplyKeyboardRemove())
        await state.finish()
    else:
        await msg.reply('Нажмите верную кнопку')

    await msg.answer(bold("""Индивидуальные сессии проходят дистанционно по видеосвязи в удобное для Вас время""") +
                     '\nСпециалист по нейрографике порекомендует, какой именно алгоритм нарисовать, чтобы получить результат, который нужен вам.', parse_mode=ParseMode.MARKDOWN)
    with open('/Users/Admin/PycharmProjects/neurobot/database/final.jpeg', 'rb') as photo:
        await bot.send_photo(chat_id=msg.from_user.id, photo=photo)
    await msg.answer('''        
        Проработка вашей темы под руководством профессионального инструктора – это:
    · безопасно и экологично для вас с соблюдением всех шагов и правил психологического алгоритма
    · обратная связь и рекомендации специалиста
    · возможность задать все интересующие вопросы для дальнейшей самостоятельной работы
    · получение результата за один или несколько рисунков''', reply_markup=client_kb.url_kb)



@dp.message_handler(state='*', commands=['stop'])
@dp.message_handler(Text(equals='stop', ignore_case=True), state='*')
async def cancel_handler(msg: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await msg.reply(
        'Заполнение отзыва отменено. Если захотите вернуться и оставить отзыв, воспользуйтесь командой /start', reply_markup=ReplyKeyboardRemove())


@dp.message_handler(commands=['admin'])
async def check_db(msg: types.Message):
    if msg.from_user.id in [369716486, 869657610]:
        await neuro_db.sql_read(msg)
    else:
        await msg.reply('У вас нет прав администратора')


def register_handler_client(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_message_handler(making_user, commands=['begin'], state=None)
    dp.register_message_handler(name_taken, state=FSMUser.name)
    dp.register_message_handler(phone_taken, state=FSMUser.phone)
    dp.register_message_handler(mk_date, state=FSMUser.mk)
    dp.register_message_handler(mark_taken, state=FSMUser.mark)
    dp.register_message_handler(first_q, state=FSMUser.first_q)
    dp.register_message_handler(second_q, state=FSMUser.second_q)
    dp.register_message_handler(third_q, state=FSMUser.third_q)
    dp.register_message_handler(fourth_q, state=FSMUser.fourth_q)
    dp.register_message_handler(fifth_q, state=FSMUser.fifth_q)
    dp.register_message_handler(sixth_q, state=FSMUser.sixth_q)
    # dp.register_message_handler(seventh_q, state=FSMUser.seventh_q)
    dp.register_message_handler(eighth_q, state=FSMUser.eighth_q)
    dp.register_message_handler(check_db, commands=['admin'])
    dp.register_message_handler(gift, state=FSMUser.gift)
