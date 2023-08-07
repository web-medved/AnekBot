import telebot
import glob
import os
import random
from telebot import types

bot = telebot.TeleBot('6531315310:AAGcjLIrewkxVk9Ni8RM1-jWVZQLy8dwqSo')

@bot.message_handler(commands=['start'])
def start(massage):
    markup = types.ReplyKeyboardMarkup()
    btn_help = types.KeyboardButton('Помощь🆘')
    btn_restart = types.KeyboardButton('Перезапуск🔃')
    btn_list = types.KeyboardButton('Список анекдотов📋')
    btn_number = types.KeyboardButton('Поиск анекдота по номеру🔎')
    btn_name = types.KeyboardButton('Поиск анекдота по названию🔍')
    btn_random = types.KeyboardButton('Случайный анек🎲')

    markup.row(btn_list, btn_random)
    markup.row(btn_number, btn_name)
    markup.row(btn_help,btn_restart)

    if massage.from_user.last_name == None:
        last_name = 'Саныч'
    else:
        last_name = massage.from_user.last_name
    bot.send_message(massage.chat.id, f'Я вас категорически приветствую, {massage.from_user.first_name} {last_name}!',
                     reply_markup=markup)

@bot.message_handler(commands=['Anek1'])
def Anek1(message):
    file_path = 'Aneks/Anek1.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek2'])
def Anek2(message):
    file_path = 'Aneks/Anek2.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek3'])
def Anek3(message):
    file_path = 'Aneks/Anek3.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek4'])
def Anek4(message):
    file_path = 'Aneks/Anek4.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek5_1'])
def Anek5_1(message):
    file_path = 'Aneks/Anek5.1.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek5_2'])
def Anek5_2(message):
    file_path = 'Aneks/Anek5.2.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek6'])
def Anek6(message):
    file_path = 'Aneks/Anek6.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek7'])
def Anek7(message):
    file_path = 'Aneks/Anek7.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek8'])
def Anek8(message):
    file_path = 'Aneks/Anek8.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek9'])
def Anek9(message):
    file_path = 'Aneks/Anek9.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek10'])
def Anek10(message):
    file_path = 'Aneks/Anek10.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek11'])
def Anek11(message):
    file_path = 'Aneks/Anek11.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek12'])
def Anek12(message):
    file_path = 'Aneks/Anek12.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek13'])
def Anek13(message):
    file_path = 'Aneks/Anek13.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek14_1'])
def Anek14_1(message):
    file_path = 'Aneks/Anek14.1.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek14_2'])
def Anek14_2(message):
    file_path = 'Aneks/Anek14.2.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek15'])
def Anek15(message):
    file_path = 'Aneks/Anek15.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek16'])
def Anek16(message):
    file_path = 'Aneks/Anek16.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek17'])
def Anek17(message):
    file_path = 'Aneks/Anek17.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek18'])
def Anek18(message):
    file_path = 'Aneks/Anek18.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek19'])
def Anek19(message):
    file_path = 'Aneks/Anek19.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek20'])
def Anek20(message):
    file_path = 'Aneks/Anek20.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek21'])
def Anek21(message):
    file_path = 'Aneks/Anek21.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek22'])
def Anek22(message):
    file_path = 'Aneks/Anek22.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek23'])
def Anek23(message):
    file_path = 'Aneks/Anek23.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek24'])
def Anek24(message):
    file_path = 'Aneks/Anek24.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek25'])
def Anek25(message):
    file_path = 'Aneks/Anek25.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek26'])
def Anek26(message):
    file_path = 'Aneks/Anek26.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek27'])
def Anek27(message):
    file_path = 'Aneks/Anek27.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek28'])
def Anek28(message):
    file_path = 'Aneks/Anek28.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek29'])
def Anek29(message):
    file_path = 'Aneks/Anek29.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek30'])
def Anek30(message):
    file_path = 'Aneks/Anek30.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek31'])
def Anek31(message):
    file_path = 'Aneks/Anek31.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek32'])
def Anek32(message):
    file_path = 'Aneks/Anek32.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek33'])
def Anek33(message):
    file_path = 'Aneks/Anek33.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek34'])
def Anek34(message):
    file_path = 'Aneks/Anek34.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek35'])
def Anek35(message):
    file_path = 'Aneks/Anek35.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek36'])
def Anek36(message):
    file_path = 'Aneks/Anek36.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek37'])
def Anek37(message):
    file_path = 'Aneks/Anek37.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek38'])
def Anek38(message):
    file_path = 'Aneks/Anek38.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek39'])
def Anek39(message):
    file_path = 'Aneks/Anek39.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek40'])
def Anek40(message):
    file_path = 'Aneks/Anek40.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek41'])
def Anek41(message):
    file_path = 'Aneks/Anek41.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek42'])
def Anek42(message):
    file_path = 'Aneks/Anek42.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek43'])
def Anek43(message):
    file_path = 'Aneks/Anek43.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek44'])
def Anek44(message):
    file_path = 'Aneks/Anek44.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek45'])
def Anek45(message):
    file_path = 'Aneks/Anek45.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek46'])
def Anek46(message):
    file_path = 'Aneks/Anek46.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek47'])
def Anek47(message):
    file_path = 'Aneks/Anek47.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek48_1'])
def Anek48_1(message):
    file_path = 'Aneks/Anek48.1.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek48_2'])
def Anek48_2(message):
    file_path = 'Aneks/Anek48.2.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek49'])
def Anek49(message):
    file_path = 'Aneks/Anek49.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek50'])
def Anek50(message):
    file_path = 'Aneks/Anek50.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek51'])
def Anek51(message):
    file_path = 'Aneks/Anek51.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek52'])
def Anek52(message):
    file_path = 'Aneks/Anek52.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek53'])
def Anek53(message):
    file_path = 'Aneks/Anek53.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek54'])
def Anek54(message):
    file_path = 'Aneks/Anek54.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek55'])
def Anek55(message):
    file_path = 'Aneks/Anek55.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek56'])
def Anek56(message):
    file_path = 'Aneks/Anek56.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek57'])
def Anek57(message):
    file_path = 'Aneks/Anek57.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek58'])
def Anek58(message):
    file_path = 'Aneks/Anek58.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek59'])
def Anek59(message):
    file_path = 'Aneks/Anek59.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek60'])
def Anek60(message):
    file_path = 'Aneks/Anek60.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek61'])
def Anek61(message):
    file_path = 'Aneks/Anek61.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek62'])
def Anek62(message):
    file_path = 'Aneks/Anek62.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek63'])
def Anek63(message):
    file_path = 'Aneks/Anek63.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek64'])
def Anek64(message):
    file_path = 'Aneks/Anek64.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek65'])
def Anek65(message):
    file_path = 'Aneks/Anek65.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek66'])
def Anek66(message):
    file_path = 'Aneks/Anek66.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek67'])
def Anek67(message):
    file_path = 'Aneks/Anek67.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek68'])
def Anek68(message):
    file_path = 'Aneks/Anek68.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek69'])
def Anek69(message):
    file_path = 'Aneks/Anek69.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek70'])
def Anek70(message):
    file_path = 'Aneks/Anek70.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek71'])
def Anek71(message):
    file_path = 'Aneks/Anek71.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek72'])
def Anek72(message):
    file_path = 'Aneks/Anek72.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek73'])
def Anek73(message):
    file_path = 'Aneks/Anek73.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek74'])
def Anek74(message):
    file_path = 'Aneks/Anek74.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek75'])
def Anek75(message):
    file_path = 'Aneks/Anek75.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek76'])
def Anek76(message):
    file_path = 'Aneks/Anek76.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek77'])
def Anek77(message):
    file_path = 'Aneks/Anek77.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek78'])
def Anek78(message):
    file_path = 'Aneks/Anek78.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek79'])
def Anek79(message):
    file_path = 'Aneks/Anek79.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek80'])
def Anek80(message):
    file_path = 'Aneks/Anek80.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek81'])
def Anek81(message):
    file_path = 'Aneks/Anek81.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek82'])
def Anek82(message):
    file_path = 'Aneks/Anek82.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek83'])
def Anek83(message):
    file_path = 'Aneks/Anek83.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek84'])
def Anek84(message):
    file_path = 'Aneks/Anek84.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek85'])
def Anek85(message):
    file_path = 'Aneks/Anek85.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek86'])
def Anek86(message):
    file_path = 'Aneks/Anek86.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek87'])
def Anek87(message):
    file_path = 'Aneks/Anek87.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek88'])
def Anek88(message):
    file_path = 'Aneks/Anek88.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek89'])
def Anek89(message):
    file_path = 'Aneks/Anek89.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek90'])
def Anek90(message):
    file_path = 'Aneks/Anek90.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek91'])
def Anek91(message):
    file_path = 'Aneks/Anek91.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek92'])
def Anek92(message):
    file_path = 'Aneks/Anek92.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek93'])
def Anek93(message):
    file_path = 'Aneks/Anek93.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek94'])
def Anek94(message):
    file_path = 'Aneks/Anek94.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek95'])
def Anek95(message):
    file_path = 'Aneks/Anek95.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek96'])
def Anek96(message):
    file_path = 'Aneks/Anek96.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek97'])
def Anek97(message):
    file_path = 'Aneks/Anek97.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek98'])
def Anek98(message):
    file_path = 'Aneks/Anek98.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek99'])
def Anek99(message):
    file_path = 'Aneks/Anek99.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek100_1'])
def Anek100_1(message):
    file_path = 'Aneks/Anek100.1.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek100_2'])
def Anek100_2(message):
    file_path = 'Aneks/Anek100.2.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek101'])
def Anek101(message):
    file_path = 'Aneks/Anek101.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek102'])
def Anek102(message):
    file_path = 'Aneks/Anek102.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek103'])
def Anek103(message):
    file_path = 'Aneks/Anek103.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek104'])
def Anek104(message):
    file_path = 'Aneks/Anek104.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['Anek105'])
def Anek105(message):
    file_path = 'Aneks/Anek105.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(content_types=['text'])
def on_click(message):
    if message.text == 'Список анекдотов📋':
        file_path = 'Anek_list.txt'  # Здесь укажите путь до вашего .txt файла

        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read()
        except Exception as e:
            text = f'Ошибка при открытии файла: {str(e)}'
        bot.send_message(chat_id=message.chat.id, text=text)

    elif message.text == 'Поиск анекдота по номеру🔎':
        bot.send_message(chat_id=message.chat.id, text='Введите номер анекдота в списке')
        bot.register_next_step_handler(message, find_number)

    elif message.text == 'Поиск анекдота по названию🔍':
        bot.send_message(chat_id=message.chat.id, text='Введите название анекдота в списке')
        bot.register_next_step_handler(message, find_name)

    elif message.text == 'Перезапуск🔃':
        restart_text(message)

    elif message.text == 'Случайный анек🎲':
        random_anek(message)

    elif message.text == 'Помощь🆘':
        help_text(message)

@bot.message_handler(commands=['help'])
def help(message):
    file_path = 'help.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(commands=['restart'])
def restart(message):
    start(message)

@bot.message_handler()
def help_text(message):
    if message.text == 'Помощь🆘':
        help(message)

def restart_text(message):
    if message.text == 'Перезапуск🔃':
        bot.send_message(chat_id=message.chat.id, text='Перезапуск выполнен')
        start(message)

def find_number(message):
    try:
        num = message.text
        if num == 'Помощь🆘' or num == 'Перезапуск🔃' or num == 'Список анекдотов📋' \
                or num == 'Поиск анекдота по номеру🔎' or num == 'Поиск анекдота по названию🔍'\
                or num == 'Случайный анек🎲':
            on_click(message)
        else:
            num_int = float(num)
            if num_int < 106:
                for file_path in sorted(glob.glob(f'Aneks/Anek{num}.txt')):
                    with open(file_path, 'r', encoding='utf-8') as file:
                        text = file.read()
                    bot.send_message(chat_id=message.chat.id, text=text)
            else:
                bot.send_message(chat_id=message.chat.id, text='В списке нет такого анека')
            bot.register_next_step_handler(message, find_number)
    except:
        bot.send_message(chat_id=message.chat.id, text='Мне нужнен номер, а не этот бред')

def find_name(message):
    try:
        file_path = 'Anek_list.txt'
        name = message.text
        if name == '/Anek1':
            Anek1(message)
        elif name == '/Anek2':
            Anek2(message)
        elif name == '/Anek3':
            Anek3(message)
        elif name == '/Anek4':
            Anek4(message)
        elif name == '/Anek5_1':
            Anek5_1(message)
        elif name == '/Anek5_2':
            Anek5_2(message)
        elif name == '/Anek6':
            Anek6(message)
        elif name == '/Anek7':
            Anek7(message)
        elif name == '/Anek8':
            Anek8(message)
        elif name == '/Anek9':
            Anek9(message)
        elif name == '/Anek10':
            Anek10(message)
        elif name == '/Anek11':
            Anek11(message)
        elif name == '/Anek12':
            Anek12(message)
        elif name == '/Anek13':
            Anek13(message)
        elif name == '/Anek14_1':
            Anek14_1(message)
        elif name == '/Anek14_2':
            Anek14_2(message)
        elif name == '/Anek15':
            Anek15(message)
        elif name == '/Anek16':
            Anek16(message)
        elif name == '/Anek17':
            Anek17(message)
        elif name == '/Anek18':
            Anek18(message)
        elif name == '/Anek19':
            Anek19(message)
        elif name == '/Anek20':
            Anek20(message)
        elif name == '/Anek21':
            Anek21(message)
        elif name == '/Anek22':
            Anek22(message)
        elif name == '/Anek23':
            Anek23(message)
        elif name == '/Anek24':
            Anek24(message)
        elif name == '/Anek25':
            Anek25(message)
        elif name == '/Anek26':
            Anek26(message)
        elif name == '/Anek27':
            Anek27(message)
        elif name == '/Anek28':
            Anek28(message)
        elif name == '/Anek29':
            Anek29(message)
        elif name == '/Anek30':
            Anek30(message)
        elif name == '/Anek31':
            Anek31(message)
        elif name == '/Anek32':
            Anek32(message)
        elif name == '/Anek33':
            Anek33(message)
        elif name == '/Anek34':
            Anek34(message)
        elif name == '/Anek35':
            Anek35(message)
        elif name == '/Anek36':
            Anek36(message)
        elif name == '/Anek37':
            Anek37(message)
        elif name == '/Anek38':
            Anek38(message)
        elif name == '/Anek39':
            Anek39(message)
        elif name == '/Anek40':
            Anek40(message)
        elif name == '/Anek41':
            Anek41(message)
        elif name == '/Anek42':
            Anek42(message)
        elif name == '/Anek43':
            Anek43(message)
        elif name == '/Anek44':
            Anek44(message)
        elif name == '/Anek45':
            Anek45(message)
        elif name == '/Anek46':
            Anek46(message)
        elif name == '/Anek47':
            Anek47(message)
        elif name == '/Anek48_1':
            Anek48_1(message)
        elif name == '/Anek48_2':
            Anek48_2(message)
        elif name == '/Anek49':
            Anek49(message)
        elif name == '/Anek50':
            Anek50(message)
        elif name == '/Anek51':
            Anek51(message)
        elif name == '/Anek52':
            Anek52(message)
        elif name == '/Anek53':
            Anek53(message)
        elif name == '/Anek54':
            Anek54(message)
        elif name == '/Anek55':
            Anek55(message)
        elif name == '/Anek56':
            Anek56(message)
        elif name == '/Anek57':
            Anek57(message)
        elif name == '/Anek58':
            Anek58(message)
        elif name == '/Anek59':
            Anek59(message)
        elif name == '/Anek60':
            Anek60(message)
        elif name == '/Anek61':
            Anek61(message)
        elif name == '/Anek62':
            Anek62(message)
        elif name == '/Anek63':
            Anek63(message)
        elif name == '/Anek64':
            Anek64(message)
        elif name == '/Anek65':
            Anek65(message)
        elif name == '/Anek66':
            Anek66(message)
        elif name == '/Anek67':
            Anek67(message)
        elif name == '/Anek68':
            Anek68(message)
        elif name == '/Anek69':
            Anek69(message)
        elif name == '/Anek70':
            Anek70(message)
        elif name == '/Anek71':
            Anek71(message)
        elif name == '/Anek72':
            Anek72(message)
        elif name == '/Anek73':
            Anek73(message)
        elif name == '/Anek74':
            Anek74(message)
        elif name == '/Anek75':
            Anek75(message)
        elif name == '/Anek76':
            Anek76(message)
        elif name == '/Anek77':
            Anek77(message)
        elif name == '/Anek78':
            Anek78(message)
        elif name == '/Anek79':
            Anek79(message)
        elif name == '/Anek80':
            Anek80(message)
        elif name == '/Anek81':
            Anek81(message)
        elif name == '/Anek82':
            Anek82(message)
        elif name == '/Anek83':
            Anek83(message)
        elif name == '/Anek84':
            Anek84(message)
        elif name == '/Anek85':
            Anek85(message)
        elif name == '/Anek86':
            Anek86(message)
        elif name == '/Anek87':
            Anek87(message)
        elif name == '/Anek88':
            Anek88(message)
        elif name == '/Anek89':
            Anek89(message)
        elif name == '/Anek90':
            Anek90(message)
        elif name == '/Anek91':
            Anek91(message)
        elif name == '/Anek92':
            Anek92(message)
        elif name == '/Anek93':
            Anek93(message)
        elif name == '/Anek94':
            Anek94(message)
        elif name == '/Anek95':
            Anek95(message)
        elif name == '/Anek96':
            Anek96(message)
        elif name == '/Anek97':
            Anek97(message)
        elif name == '/Anek98':
            Anek98(message)
        elif name == '/Anek99':
            Anek99(message)
        elif name == '/Anek100_1':
            Anek100_1(message)
        elif name == '/Anek100_1':
            Anek100_2(message)
        elif name == '/Anek101':
            Anek101(message)
        elif name == '/Anek102':
            Anek102(message)
        elif name == '/Anek103':
            Anek103(message)
        elif name == '/Anek104':
            Anek104(message)
        elif name == '/Anek105':
            Anek105(message)

        else:
            k = 0
            with open(file_path, 'r', encoding='utf-8') as file:
                for line in file:
                    if name in line:
                        k = k + 1
                        text = line
                        bot.send_message(chat_id=message.chat.id, text=text)

            if name == 'Помощь🆘' or name == 'Перезапуск🔃' or name == 'Список анекдотов📋' \
                or name == 'Поиск анекдота по номеру🔎' or name == 'Поиск анекдота по названию🔍'\
                or name == 'Случайный анек🎲':
                on_click(message)
            else:
                if k == 0:
                    bot.send_message(chat_id=message.chat.id, text=f'В списке нет такого анека \n'
                                                                   'Попробуй написать с большой буквы или введи другое название')
                bot.register_next_step_handler(message, find_name)
    except:
        on_click(message)

def random_anek(message):
    name = message.text
    if name == 'Помощь🆘' or name == 'Перезапуск🔃' or name == 'Список анекдотов📋' \
            or name == 'Поиск анекдота по номеру🔎' or name == 'Поиск анекдота по названию🔍' \
            or name == 'Случайный анек🎲':

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
        bot.send_message(chat_id=message.chat.id, text=text)


bot.polling(none_stop=True)