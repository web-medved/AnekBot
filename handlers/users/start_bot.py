from aiogram import types
from aiogram.dispatcher.filters import CommandStart

from loader import dp
from utils.sql_commands import register_user
from buttons_commands.make_kb import markup

markup_kb = markup()

@dp.message_handler(CommandStart(), state='*')
async def start_bot(message: types.Message):
    register_user(message.from_user.id)

    last_name = 'Саныч'
    await message.answer(
        f'Я вас категорически приветствую, {message.from_user.first_name} {last_name}!',
    reply_markup=markup_kb)

@dp.message_handler(commands=['help'])
async def help(message):
    file_path = 'help.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)
    await message.answer_document(document=open('Живой сборник анекдотов.pdf', 'rb'))

@dp.message_handler(commands=['restart'])
async def restart(message):
    await message.answer('Перезапуск выполнен')
    await start_bot(message)