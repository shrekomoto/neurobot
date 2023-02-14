import sqlite3 as sq
from create_bot import bot


def sql_start():
    global base, cur
    base = sq.connect('users')
    cur = base.cursor()
    if base:
        print('ok')
    base.execute('CREATE TABLE IF NOT EXISTS users(name TEXT PRIMARY KEY, phone TEXT, mk TEXT, mark TEXT, first_q TEXT, second_q TEXT, third_q TEXT, fourth_q TEXT, fifth_q TEXT, sixth_q TEXT, seventh_q TEXT, eighth_q TEXT)')
    base.commit()

async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', tuple(data.values()))
        base.commit()


async def sql_read(msg):
    for ret in cur.execute('SELECT * FROM users').fetchall():
        await bot.send_message(chat_id=msg.from_user.id, text=f'''Фамилия и имя - {ret[0]}, номер телефона - {ret[1]},
        был на мастер-классе {ret[2]}. Оценил этот мастер-класс в {ret[3]} баллов. Далее следуют ответы на все вопросы. 
        {ret[4]}, {ret[5]}, {ret[6]}, {ret[7]}, {ret[8]}, {ret[9]}, {ret[10]}, {ret[11]}''' )