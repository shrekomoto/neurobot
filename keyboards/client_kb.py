from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.utils.emoji import emojize, demojize


# стартовые кнопки
b1 = KeyboardButton('/отзыв')
b2 = KeyboardButton('отмена')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(b1)

# структура кнопок вопросов - b24, где b - button, 2 - номер вопроса, 4 - номер варианта ответа на данный вопрос
b11 = KeyboardButton('Нет, сегодня впервые рисовала'+ demojize(':laughing:'))
b12 = KeyboardButton('Рисовала на бесплатном марафоне')
b13 = KeyboardButton('Рисовала другой алгоритм на очном МК')
b14 = KeyboardButton('Рисовала индивидуально со специалистом нейрографии')

first_q_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(b11).add(b12).add(b13).add(b14).add(b2)

b21 = KeyboardButton('просто получили удовольствие от процесса')
b22 = KeyboardButton('вошли в состояние медитации, появилось ощущение гармонии')
b23 = KeyboardButton('получили представление о методе и понимание, как работает нейрографика')
b24 = KeyboardButton('запомнили основные правила и технику безопасности для экологичного рисования')

second_q_kb = ReplyKeyboardMarkup(resize_keyboard=True).row(b21, b22).row(b23, b24).add(b2)
# second_q_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(b21).add(b22).add(b23).add(b24).add(b2)

# b31 = KeyboardButton('/Да')
# b32 = KeyboardButton('/Нет')
b33 = KeyboardButton('Всё понятно!')

third_q_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(b33).add(b2)

b41 = KeyboardButton('Хорошее настроение,вдохновение')
b42 = KeyboardButton('Воодушевление, уверенность, спокойствие')
b43 = KeyboardButton('Напряжение усилилось')
b44 = KeyboardButton('Раздражение')
b45 = KeyboardButton('Повысился уровень энергии, позитив, общий тонус, азарт')
b46 = KeyboardButton('Появилось много идей, возникли инсайты, прояснилась ситуация')

fourth_q_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(b41).add(b42).add(b43).add(b44).add(
    b45).add(b46).add(b2)

b61 = KeyboardButton('Да')
b62 = KeyboardButton('Нет')

sixth_q_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(b61).add(b62).add(b2)

b71 = KeyboardButton('Да')
b72 = KeyboardButton('Нет')

seventh_q_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(b71).add(b72).add(b2)

b81 = KeyboardButton('Самореализация')
b82 = KeyboardButton('Здоровье')
b83 = KeyboardButton('Отношения в семье')
b84 = KeyboardButton('Отношения с партнером')
b85 = KeyboardButton('Отношения с детьми')
b86 = KeyboardButton('Отдых и путешествия')
b87 = KeyboardButton('Переезд')
b88 = KeyboardButton('Увеличение дохода')
b89 = KeyboardButton('Рост в профессии')
b810 = KeyboardButton('Смена работы')
b811 = KeyboardButton('Другое')
#
# eighth_q_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(b81).add(b82).add(b83).add(b84).add(b85).add(b86).add(
#                                                             b87).add(b88).add(b89).add(b810).add(b811)

eighth_q_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(b81, b82).row(b83, b84).row(b85,
                                                                                                                b86).row(
    b87, b88).row(b89, b810, b811)
