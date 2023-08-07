import telebot
from telebot import types

bot = telebot.TeleBot('')


@bot.message_handler(commands=['start'])
def start(massage):
    markup = types.ReplyKeyboardMarkup()
    btn_help = types.KeyboardButton('Помощь')
    btn_restart = types.KeyboardButton('Перезапуск')
    btn_list = types.KeyboardButton('Список анекдотов')
    btn_number = types.KeyboardButton('Поиск анекдота по номеру')
    btn_name = types.KeyboardButton('Поиск анекдота по названию')

    markup.add(btn_list)
    markup.add(btn_number)
    markup.add(btn_name)
    markup.add(btn_help)
    markup.add(btn_restart)

    if massage.from_user.last_name == None:
        last_name = 'Саныч'
    else:
        last_name = massage.from_user.last_name
    bot.send_message(massage.chat.id, f'Я вас категорически приветствую, {massage.from_user.first_name} {last_name}!', reply_markup=markup)

    bot.register_next_step_handler(massage, on_click)

def on_click(message):

    if message.text == 'Список анекдотов':
        file_path = 'Anek_list.txt'  # Здесь укажите путь до вашего .txt файла

        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read()
        except Exception as e:
            text = f'Ошибка при открытии файла: {str(e)}'
        bot.send_message(chat_id=message.chat.id, text=text)

    if message.text == 'Перезапуск':
        bot.send_message(chat_id=message.chat.id, text='Перезапуск выполнен')
        start(message)

@bot.message_handler(commands=['Anek1'])
def Anek1(message):
    file_path = 'Anek1.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek2'])
def Anek2(message):
    file_path = 'Anek2.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek3'])
def Anek3(message):
    file_path = 'Anek3.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek4'])
def Anek4(message):
    file_path = 'Anek4.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek5_1'])
def Anek5_1(message):
    file_path = 'Anek5_1.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek5_2'])
def Anek5_2(message):
    file_path = 'Anek5_2.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek6'])
def Anek6(message):
    file_path = 'Anek6.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek7'])
def Anek7(message):
    file_path = 'Anek7.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek8'])
def Anek8(message):
    file_path = 'Anek8.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek9'])
def Anek9(message):
    file_path = 'Anek9.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek10'])
def Anek10(message):
    file_path = 'Anek10.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek11'])
def Anek11(message):
    file_path = 'Anek11.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek12'])
def Anek12(message):
    file_path = 'Anek12.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek13'])
def Anek13(message):
    file_path = 'Anek13.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek14_1'])
def Anek14_1(message):
    file_path = 'Anek14_1.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek14_2'])
def Anek14_2(message):
    file_path = 'Anek14_2.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek15'])
def Anek15(message):
    file_path = 'Anek15.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek16'])
def Anek16(message):
    file_path = 'Anek16.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek17'])
def Anek17(message):
    file_path = 'Anek17.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek18'])
def Anek18(message):
    file_path = 'Anek18.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek19'])
def Anek19(message):
    file_path = 'Anek19.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek20'])
def Anek20(message):
    file_path = 'Anek20.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek21'])
def Anek21(message):
    file_path = 'Anek21.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek22'])
def Anek22(message):
    file_path = 'Anek22.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek23'])
def Anek23(message):
    file_path = 'Anek23.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek24'])
def Anek24(message):
    file_path = 'Anek24.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek25'])
def Anek25(message):
    file_path = 'Anek25.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek26'])
def Anek26(message):
    file_path = 'Anek26.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek27'])
def Anek27(message):
    file_path = 'Anek27.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek28'])
def Anek28(message):
    file_path = 'Anek28.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek29'])
def Anek29(message):
    file_path = 'Anek29.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek30'])
def Anek30(message):
    file_path = 'Anek30.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek31'])
def Anek31(message):
    file_path = 'Anek31.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek32'])
def Anek32(message):
    file_path = 'Anek32.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek33'])
def Anek33(message):
    file_path = 'Anek33.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek34'])
def Anek34(message):
    file_path = 'Anek34.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek35'])
def Anek35(message):
    file_path = 'Anek35.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek36'])
def Anek36(message):
    file_path = 'Anek36.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek37'])
def Anek37(message):
    file_path = 'Anek37.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek38'])
def Anek38(message):
    file_path = 'Anek38.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek39'])
def Anek39(message):
    file_path = 'Anek39.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek40'])
def Anek40(message):
    file_path = 'Anek40.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek41'])
def Anek41(message):
    file_path = 'Anek41.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek42'])
def Anek42(message):
    file_path = 'Anek42.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek43'])
def Anek43(message):
    file_path = 'Anek43.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek44'])
def Anek44(message):
    file_path = 'Anek44.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek45'])
def Anek45(message):
    file_path = 'Anek45.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek46'])
def Anek46(message):
    file_path = 'Anek46.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek47'])
def Anek47(message):
    file_path = 'Anek47.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek48_1'])
def Anek48_1(message):
    file_path = 'Anek48_1.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek48_2'])
def Anek48_2(message):
    file_path = 'Anek48_2.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek49'])
def Anek49(message):
    file_path = 'Anek49.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek50'])
def Anek50(message):
    file_path = 'Anek50.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek51'])
def Anek51(message):
    file_path = 'Anek51.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek52'])
def Anek52(message):
    file_path = 'Anek52.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek53'])
def Anek53(message):
    file_path = 'Anek53.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek54'])
def Anek54(message):
    file_path = 'Anek54.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek55'])
def Anek55(message):
    file_path = 'Anek55.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek56'])
def Anek56(message):
    file_path = 'Anek56.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek57'])
def Anek57(message):
    file_path = 'Anek57.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek58'])
def Anek58(message):
    file_path = 'Anek58.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek59'])
def Anek59(message):
    file_path = 'Anek59.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek60'])
def Anek60(message):
    file_path = 'Anek60.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek61'])
def Anek61(message):
    file_path = 'Anek61.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek62'])
def Anek62(message):
    file_path = 'Anek62.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek63'])
def Anek63(message):
    file_path = 'Anek63.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek64'])
def Anek64(message):
    file_path = 'Anek64.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek65'])
def Anek65(message):
    file_path = 'Anek65.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek66'])
def Anek66(message):
    file_path = 'Anek66.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek67'])
def Anek67(message):
    file_path = 'Anek67.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek68'])
def Anek68(message):
    file_path = 'Anek68.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek69'])
def Anek69(message):
    file_path = 'Anek69.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek70'])
def Anek70(message):
    file_path = 'Anek70.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek71'])
def Anek71(message):
    file_path = 'Anek71.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek72'])
def Anek72(message):
    file_path = 'Anek72.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek73'])
def Anek73(message):
    file_path = 'Anek73.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek74'])
def Anek74(message):
    file_path = 'Anek74.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek75'])
def Anek75(message):
    file_path = 'Anek75.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek76'])
def Anek76(message):
    file_path = 'Anek76.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek77'])
def Anek77(message):
    file_path = 'Anek77.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek78'])
def Anek78(message):
    file_path = 'Anek78.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek79'])
def Anek79(message):
    file_path = 'Anek79.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek80'])
def Anek80(message):
    file_path = 'Anek80.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek81'])
def Anek81(message):
    file_path = 'Anek81.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek82'])
def Anek82(message):
    file_path = 'Anek82.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek83'])
def Anek83(message):
    file_path = 'Anek83.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek84'])
def Anek84(message):
    file_path = 'Anek84.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek85'])
def Anek85(message):
    file_path = 'Anek85.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek86'])
def Anek86(message):
    file_path = 'Anek86.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek87'])
def Anek87(message):
    file_path = 'Anek87.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek88'])
def Anek88(message):
    file_path = 'Anek88.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek89'])
def Anek89(message):
    file_path = 'Anek89.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek90'])
def Anek90(message):
    file_path = 'Anek90.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek91'])
def Anek91(message):
    file_path = 'Anek91.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek92'])
def Anek92(message):
    file_path = 'Anek92.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek93'])
def Anek93(message):
    file_path = 'Anek93.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek94'])
def Anek94(message):
    file_path = 'Anek94.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek95'])
def Anek95(message):
    file_path = 'Anek95.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek96'])
def Ane96(message):
    file_path = 'Anek96.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek97'])
def Anek97(message):
    file_path = 'Anek97.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek98'])
def Anek98(message):
    file_path = 'Anek98.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek99'])
def Anek99(message):
    file_path = 'Anek99.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek100_1'])
def Anek100_1(message):
    file_path = 'Anek100_1.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek100_2'])
def Anek100_2(message):
    file_path = 'Anek100_2.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek101'])
def Anek101(message):
    file_path = 'Anek101.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek102'])
def Anek102(message):
    file_path = 'Anek102.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek103'])
def Anek103(message):
    file_path = 'Anek103.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek104'])
def Anek104(message):
    file_path = 'Anek104.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek105'])
def Anek105(message):
    file_path = 'Anek105.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)



@bot.message_handler(commands=['restart'])
def restart(message):
    start(message)

@bot.message_handler()
def restart_text(message):
    if message.text == 'Перезапуск':
        bot.send_message(chat_id=message.chat.id, text='Перезапуск выполнен')
        start(message)

bot.polling(none_stop=True)