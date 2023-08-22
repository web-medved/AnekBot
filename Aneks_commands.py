from loader import dp

@dp.message_handler(commands=['Anek1'])
async def Anek1(message):
    file_path = 'Aneks/Anek1.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek2'])
async def Anek2(message):
    file_path = 'Aneks/Anek2.txt'
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        # bot.send_message(chat_id=message.chat.id, text=text)
    except Exception as e:
        text = f'Ошибка при открытии файла: {str(e)}'
    if len(text) > 4092:  # max = 4096
        for x in range(0, len(text), 4092):
            await message.answer('{}'.format(text[x:x + 4092]))
    else:
        await message.answer(text)

@dp.message_handler(commands=['Anek3'])
async def Anek3(message):
    file_path = 'Aneks/Anek3.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek4'])
async def Anek4(message):
    file_path = 'Aneks/Anek4.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek5_1'])
async def Anek5_1(message):
    file_path = 'Aneks/Anek5.1.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek5_2'])
async def Anek5_2(message):
    file_path = 'Aneks/Anek5.2.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek6'])
async def Anek6(message):
    file_path = 'Aneks/Anek6.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek7'])
async def Anek7(message):
    file_path = 'Aneks/Anek7.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek8'])
async def Anek8(message):
    file_path = 'Aneks/Anek8.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek9'])
async def Anek9(message):
    file_path = 'Aneks/Anek9.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek10'])
async def Anek10(message):
    file_path = 'Aneks/Anek10.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek11'])
async def Anek11(message):
    file_path = 'Aneks/Anek11.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek12'])
async def Anek12(message):
    file_path = 'Aneks/Anek12.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek13'])
async def Anek13(message):
    file_path = 'Aneks/Anek13.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek14_1'])
async def Anek14_1(message):
    file_path = 'Aneks/Anek14.1.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek14_2'])
async def Anek14_2(message):
    file_path = 'Aneks/Anek14.2.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek15'])
async def Anek15(message):
    file_path = 'Aneks/Anek15.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek16'])
async def Anek16(message):
    file_path = 'Aneks/Anek16.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek17'])
async def Anek17(message):
    file_path = 'Aneks/Anek17.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek18'])
async def Anek18(message):
    file_path = 'Aneks/Anek18.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek19'])
async def Anek19(message):
    file_path = 'Aneks/Anek19.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek20'])
async def Anek20(message):
    file_path = 'Aneks/Anek20.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek21'])
async def Anek21(message):
    file_path = 'Aneks/Anek21.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek22'])
async def Anek22(message):
    file_path = 'Aneks/Anek22.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek23'])
async def Anek23(message):
    file_path = 'Aneks/Anek23.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek24'])
async def Anek24(message):
    file_path = 'Aneks/Anek24.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek25'])
async def Anek25(message):
    file_path = 'Aneks/Anek25.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek26'])
async def Anek26(message):
    file_path = 'Aneks/Anek26.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek27'])
async def Anek27(message):
    file_path = 'Aneks/Anek27.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek28'])
async def Anek28(message):
    file_path = 'Aneks/Anek28.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek29'])
async def Anek29(message):
    file_path = 'Aneks/Anek29.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek30'])
async def Anek30(message):
    file_path = 'Aneks/Anek30.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek31'])
async def Anek31(message):
    file_path = 'Aneks/Anek31.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek32'])
async def Anek32(message):
    file_path = 'Aneks/Anek32.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek33'])
async def Anek33(message):
    file_path = 'Aneks/Anek33.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek34'])
async def Anek34(message):
    file_path = 'Aneks/Anek34.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek35'])
async def Anek35(message):
    file_path = 'Aneks/Anek35.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek36'])
async def Anek36(message):
    file_path = 'Aneks/Anek36.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek37'])
async def Anek37(message):
    file_path = 'Aneks/Anek37.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek38'])
async def Anek38(message):
    file_path = 'Aneks/Anek38.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek39'])
async def Anek39(message):
    file_path = 'Aneks/Anek39.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek40'])
async def Anek40(message):
    file_path = 'Aneks/Anek40.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek41'])
async def Anek41(message):
    file_path = 'Aneks/Anek41.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek42'])
async def Anek42(message):
    file_path = 'Aneks/Anek42.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek43'])
async def Anek43(message):
    file_path = 'Aneks/Anek43.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek44'])
async def Anek44(message):
    file_path = 'Aneks/Anek44.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek45'])
async def Anek45(message):
    file_path = 'Aneks/Anek45.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek46'])
async def Anek46(message):
    file_path = 'Aneks/Anek46.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek47_1'])
async def Anek47_1(message):
    file_path = 'Aneks/Anek47.1.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek47_2'])
async def Anek47_2(message):
    file_path = 'Aneks/Anek47.2.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek48_1'])
async def Anek48_1(message):
    file_path = 'Aneks/Anek48.1.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek48_2'])
async def Anek48_2(message):
    file_path = 'Aneks/Anek48.2.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek49'])
async def Anek49(message):
    file_path = 'Aneks/Anek49.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek50'])
async def Anek50(message):
    file_path = 'Aneks/Anek50.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek51'])
async def Anek51(message):
    file_path = 'Aneks/Anek51.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek52'])
async def Anek52(message):
    file_path = 'Aneks/Anek52.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek53'])
async def Anek53(message):
    file_path = 'Aneks/Anek53.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek54'])
async def Anek54(message):
    file_path = 'Aneks/Anek54.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek55'])
async def Anek55(message):
    file_path = 'Aneks/Anek55.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek56'])
async def Anek56(message):
    file_path = 'Aneks/Anek56.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek57'])
async def Anek57(message):
    file_path = 'Aneks/Anek57.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek58'])
async def Anek58(message):
    file_path = 'Aneks/Anek58.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek59'])
async def Anek59(message):
    file_path = 'Aneks/Anek59.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek60'])
async def Anek60(message):
    file_path = 'Aneks/Anek60.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek61'])
async def Anek61(message):
    file_path = 'Aneks/Anek61.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek62'])
async def Anek62(message):
    file_path = 'Aneks/Anek62.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek63'])
async def Anek63(message):
    file_path = 'Aneks/Anek63.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek64'])
async def Anek64(message):
    file_path = 'Aneks/Anek64.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek65'])
async def Anek65(message):
    file_path = 'Aneks/Anek65.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek66'])
async def Anek66(message):
    file_path = 'Aneks/Anek66.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek67'])
async def Anek67(message):
    file_path = 'Aneks/Anek67.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek68'])
async def Anek68(message):
    file_path = 'Aneks/Anek68.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek69'])
async def Anek69(message):
    file_path = 'Aneks/Anek69.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek70'])
async def Anek70(message):
    file_path = 'Aneks/Anek70.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek71'])
async def Anek71(message):
    file_path = 'Aneks/Anek71.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek72'])
async def Anek72(message):
    file_path = 'Aneks/Anek72.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek73'])
async def Anek73(message):
    file_path = 'Aneks/Anek73.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek74'])
async def Anek74(message):
    file_path = 'Aneks/Anek74.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek75'])
async def Anek75(message):
    file_path = 'Aneks/Anek75.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek76'])
async def Anek76(message):
    file_path = 'Aneks/Anek76.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek77'])
async def Anek77(message):
    file_path = 'Aneks/Anek77.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek78'])
async def Anek78(message):
    file_path = 'Aneks/Anek78.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek79'])
async def Anek79(message):
    file_path = 'Aneks/Anek79.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek80'])
async def Anek80(message):
    file_path = 'Aneks/Anek80.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek81'])
async def Anek81(message):
    file_path = 'Aneks/Anek81.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek82'])
async def Anek82(message):
    file_path = 'Aneks/Anek82.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek83'])
async def Anek83(message):
    file_path = 'Aneks/Anek83.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek84'])
async def Anek84(message):
    file_path = 'Aneks/Anek84.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek85'])
async def Anek85(message):
    file_path = 'Aneks/Anek85.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek86'])
async def Anek86(message):
    file_path = 'Aneks/Anek86.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek87'])
async def Anek87(message):
    file_path = 'Aneks/Anek87.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek88'])
async def Anek88(message):
    file_path = 'Aneks/Anek88.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek89'])
async def Anek89(message):
    file_path = 'Aneks/Anek89.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek90'])
async def Anek90(message):
    file_path = 'Aneks/Anek90.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek91'])
async def Anek91(message):
    file_path = 'Aneks/Anek91.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek92_1'])
async def Anek92_1(message):
    file_path = 'Aneks/Anek92.1.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek92_2'])
async def Anek92_2(message):
    file_path = 'Aneks/Anek92.2.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek93'])
async def Anek93(message):
    file_path = 'Aneks/Anek93.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek94'])
async def Anek94(message):
    file_path = 'Aneks/Anek94.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek95'])
async def Anek95(message):
    file_path = 'Aneks/Anek95.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek96'])
async def Anek96(message):
    file_path = 'Aneks/Anek96.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek97'])
async def Anek97(message):
    file_path = 'Aneks/Anek97.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek98'])
async def Anek98(message):
    file_path = 'Aneks/Anek98.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek99'])
async def Anek99(message):
    file_path = 'Aneks/Anek99.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek100_1'])
async def Anek100_1(message):
    file_path = 'Aneks/Anek100.1.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek100_2'])
async def Anek100_2(message):
    file_path = 'Aneks/Anek100.2.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek101'])
async def Anek101(message):
    file_path = 'Aneks/Anek101.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek102'])
async def Anek102(message):
    file_path = 'Aneks/Anek102.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek103'])
async def Anek103(message):
    file_path = 'Aneks/Anek103.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek104'])
async def Anek104(message):
    file_path = 'Aneks/Anek104.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek105'])
async def Anek105(message):
    file_path = 'Aneks/Anek105.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek106'])
async def Anek106(message):
    file_path = 'Aneks/Anek106.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek107'])
async def Anek107(message):
    file_path = 'Aneks/Anek107.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek108'])
async def Anek108(message):
    file_path = 'Aneks/Anek108.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek109'])
async def Anek109(message):
    file_path = 'Aneks/Anek109.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek110'])
async def Anek110(message):
    file_path = 'Aneks/Anek110.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek111_1'])
async def Anek111_1(message):
    file_path = 'Aneks/Anek111.1.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek111_2'])
async def Anek111_2(message):
    file_path = 'Aneks/Anek111.2.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek111_3'])
async def Anek111_3(message):
    file_path = 'Aneks/Anek111.3.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek112'])
async def Anek112(message):
    file_path = 'Aneks/Anek112.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek113'])
async def Anek113(message):
    file_path = 'Aneks/Anek113.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek114'])
async def Anek114(message):
    file_path = 'Aneks/Anek114.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek115'])
async def Anek115(message):
    file_path = 'Aneks/Anek115.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek116'])
async def Anek116(message):
    file_path = 'Aneks/Anek116.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek117'])
async def Anek117(message):
    file_path = 'Aneks/Anek117.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek118_1'])
async def Anek118_1(message):
    file_path = 'Aneks/Anek118.1.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek118_2'])
async def Anek118_2(message):
    file_path = 'Aneks/Anek118.2.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek119'])
async def Anek119(message):
    file_path = 'Aneks/Anek119.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek120_1'])
async def Anek120_1(message):
    file_path = 'Aneks/Anek120.1.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek120_2'])
async def Anek120_2(message):
    file_path = 'Aneks/Anek120.2.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek121'])
async def Anek121(message):
    file_path = 'Aneks/Anek121.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek122'])
async def Anek122(message):
    file_path = 'Aneks/Anek122.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek123_1'])
async def Anek123_1(message):
    file_path = 'Aneks/Anek123.1.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek123_2'])
async def Anek123_2(message):
    file_path = 'Aneks/Anek123.2.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek124'])
async def Anek124(message):
    file_path = 'Aneks/Anek124.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek125'])
async def Anek125(message):
    file_path = 'Aneks/Anek125.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek126'])
async def Anek126(message):
    file_path = 'Aneks/Anek126.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek127'])
async def Anek127(message):
    file_path = 'Aneks/Anek127.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek128'])
async def Anek128(message):
    file_path = 'Aneks/Anek128.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek129'])
async def Anek129(message):
    file_path = 'Aneks/Anek129.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek130'])
async def Anek130(message):
    file_path = 'Aneks/Anek130.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek131'])
async def Anek131(message):
    file_path = 'Aneks/Anek131.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek132'])
async def Anek132(message):
    file_path = 'Aneks/Anek132.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek133'])
async def Anek133(message):
    file_path = 'Aneks/Anek133.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek134'])
async def Anek134(message):
    file_path = 'Aneks/Anek134.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek135'])
async def Anek135(message):
    file_path = 'Aneks/Anek135.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek136'])
async def Anek136(message):
    file_path = 'Aneks/Anek136.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek137_1'])
async def Anek137_1(message):
    file_path = 'Aneks/Anek137.1.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek137_2'])
async def Anek137_2(message):
    file_path = 'Aneks/Anek137.2.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek138'])
async def Anek138(message):
    file_path = 'Aneks/Anek138.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek139'])
async def Anek139(message):
    file_path = 'Aneks/Anek139.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek140'])
async def Anek140(message):
    file_path = 'Aneks/Anek140.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek141'])
async def Anek141(message):
    file_path = 'Aneks/Anek141.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek142'])
async def Anek142(message):
    file_path = 'Aneks/Anek142.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek143'])
async def Anek143(message):
    file_path = 'Aneks/Anek143.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek144'])
async def Anek144(message):
    file_path = 'Aneks/Anek144.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek145'])
async def Anek145(message):
    file_path = 'Aneks/Anek145.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek146'])
async def Anek146(message):
    file_path = 'Aneks/Anek146.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek147'])
async def Anek147(message):
    file_path = 'Aneks/Anek147.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)

@dp.message_handler(commands=['Anek148'])
async def Anek148(message):
    file_path = 'Aneks/Anek148.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    await message.answer(text)