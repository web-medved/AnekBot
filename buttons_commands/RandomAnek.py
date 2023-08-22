import os
import random
import os.path
async def random_anek(message):
    name = message.text
    if name == 'Помощь🆘' or name == 'Перезапуск🔃' or name == 'Список анекдотов📋' \
            or name == 'Поиск анекдота🔎' or name == 'Случайный анек🎲':

        # Указываем название нужной директории
        folder = "Aneks"

        # answer отвечает за выпадение из files
        def get_answer():
            files = os.listdir(folder)  # Получаем список элементов папки
            file = random.choice(files)  # Получение случайного файла из списка
            return file  # Возвращаем в значении функции - переменную file

        # read отвечает за открытие и чтение файла, который нам выпал
        def read(file):
            file = folder + "/" + file  # Создание пути к папке
            with open(file, 'r', encoding='utf-8') as f:  # Открытие файла
                text = f.read()  # Чтение файла
            return text  # Возвращаем в значении функции - переменную text

        text = read(get_answer())  # Получаем текст файла
        await message.answer(text)