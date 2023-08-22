from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def markup():
    markup_kb = ReplyKeyboardMarkup()
    btn_help = KeyboardButton('Помощь🆘')
    btn_restart = KeyboardButton('Перезапуск🔃')
    btn_list = KeyboardButton('Список анекдотов📋')
    btn_name = KeyboardButton('Поиск анекдота🔎')
    btn_random = KeyboardButton('Случайный анек🎲')

    markup_kb.row(btn_list)
    markup_kb.row(btn_name, btn_random)
    markup_kb.row(btn_help, btn_restart)
    return markup_kb
