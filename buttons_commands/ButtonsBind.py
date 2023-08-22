from handlers.users.start_bot import restart, help
from loader import dp
from buttons_commands.make_kb import markup
from buttons_commands.RandomAnek import random_anek

markup_kb = markup()

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

class UnicCommands(StatesGroup):
    name = State()
    # address = State()

@dp.message_handler(content_types=['text'])
async def on_click(message):
    if message.text == 'Список анекдотов📋':
        file_path = 'Anek_list.txt'  # Здесь укажите путь до вашего .txt файла

        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read()
        except Exception as e:
            text = f'Ошибка при открытии файла: {str(e)}'
        if len(text) > 4084: #max = 4096
            for x in range(0, len(text), 4084):
                await message.answer('{}'.format(text[x:x + 4084]))
        else:
            await message.answer('{}'.format(text))
        # bot.send_message(chat_id=message.chat.id, text=text)

    elif message.text == 'Поиск анекдота🔎':
        await message.answer('Введите название или номер анекдота из списка')
        await UnicCommands.name.set()

    elif message.text == 'Перезапуск🔃':
        await restart(message)

    elif message.text == 'Случайный анек🎲':
        await random_anek(message)

    elif message.text == 'Помощь🆘':
        await help(message)