import sqlite3 as sq
from create_bot import bot
import openpyxl

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
    filename = "feedbacks.xlsx"
    book = openpyxl.load_workbook(filename=filename)
    book.remove(book.active)
    sheet_1 = book.create_sheet("Отзывы")
    sheet_1.insert_rows(0)
    sheet_1["A1"].value = "Имя и фамилия"
    sheet_1["B1"].value = "Номер телефона"
    sheet_1["C1"].value = "Название МК и дата"
    sheet_1["D1"].value = "Оценка от 1 до 10"
    sheet_1["E1"].value = "Рисовали ли Вы ранее Нейрографику?"
    sheet_1["F1"].value = "На сегодняшнем МК что Вы получили, как начинающий в нейрографике"
    sheet_1["G1"].value = "Были ли объяснения и комментарии понятны? Если остались вопросы, пиши их сюда"
    sheet_1["H1"].value = "Какой результат вы ощутили сразу после МК?"
    sheet_1["I1"].value = "Какой отзыв о МК вы можете оставить?"
    sheet_1["J1"].value = "Хотели бы Вы получать приглашения на МК по другим темам?"
    sheet_1["K1"].value = "Хотели бы Вы записаться на индивидуальную сессию?"
    sheet_1["L1"].value = "Какой вопрос или сферу жизни Вы хотите проработать на индивидуальной сессии?"

    for sheet in book.worksheets:
        for ret in cur.execute('SELECT * FROM users').fetchall():
            sheet.append(ret)

    book.save(filename)
    await bot.send_document(msg.from_user.id, open("feedbacks.xlsx", 'rb'))
