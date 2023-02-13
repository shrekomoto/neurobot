import sqlite3 as sq


def sql_start():
    global base, cur
    base = sq.connect()
    cur = base.cursor()
    if base:
        print('ok')
    base.execute(
        'CREATE TABLE IF NOT EXISTS users(name TEXT, phone TEXT, mk TEXT, mark TEXT, first_q TEXT, second_q TEXT, third_q TEXT, fourth_q TEXT, fifth_q TEXT, sixth_q TEXT, seventh_q TEXT, eighth_q TEXT)')
    base.commit()

async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', tuple(data.values()))
        base.commit()