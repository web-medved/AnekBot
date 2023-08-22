from Aneks_commands import *
from buttons_commands.ButtonsBind import *


@dp.message_handler(state=UnicCommands.name)
async def find_name(message: types.Message, state: FSMContext):
    try:
        file_path = 'Anek_list.txt'
        name = message.text
        if name == '/Anek1':
            await Anek1(message)
        elif name == '/Anek2':
            await Anek2(message)
        elif name == '/Anek3':
            await Anek3(message)
        elif name == '/Anek4':
            await Anek4(message)
        elif name == '/Anek5_1':
            await Anek5_1(message)
        elif name == '/Anek5_2':
            await Anek5_2(message)
        elif name == '/Anek6':
            await Anek6(message)
        elif name == '/Anek7':
            await Anek7(message)
        elif name == '/Anek8':
            await Anek8(message)
        elif name == '/Anek9':
            await Anek9(message)
        elif name == '/Anek10':
            await Anek10(message)
        elif name == '/Anek11':
            await Anek11(message)
        elif name == '/Anek12':
            await Anek12(message)
        elif name == '/Anek13':
            await Anek13(message)
        elif name == '/Anek14_1':
            await Anek14_1(message)
        elif name == '/Anek14_2':
            await Anek14_2(message)
        elif name == '/Anek15':
            await Anek15(message)
        elif name == '/Anek16':
            await Anek16(message)
        elif name == '/Anek17':
            await Anek17(message)
        elif name == '/Anek18':
            await Anek18(message)
        elif name == '/Anek19':
            await Anek19(message)
        elif name == '/Anek20':
            await Anek20(message)
        elif name == '/Anek21':
            await Anek21(message)
        elif name == '/Anek22':
            await Anek22(message)
        elif name == '/Anek23':
            await Anek23(message)
        elif name == '/Anek24':
            await Anek24(message)
        elif name == '/Anek25':
            await Anek25(message)
        elif name == '/Anek26':
            await Anek26(message)
        elif name == '/Anek27':
            await Anek27(message)
        elif name == '/Anek28':
            await Anek28(message)
        elif name == '/Anek29':
            await Anek29(message)
        elif name == '/Anek30':
            await Anek30(message)
        elif name == '/Anek31':
            await Anek31(message)
        elif name == '/Anek32':
            await Anek32(message)
        elif name == '/Anek33':
            await Anek33(message)
        elif name == '/Anek34':
            await Anek34(message)
        elif name == '/Anek35':
            await Anek35(message)
        elif name == '/Anek36':
            await Anek36(message)
        elif name == '/Anek37':
            await Anek37(message)
        elif name == '/Anek38':
            await Anek38(message)
        elif name == '/Anek39':
            await Anek39(message)
        elif name == '/Anek40':
            await Anek40(message)
        elif name == '/Anek41':
            await Anek41(message)
        elif name == '/Anek42':
            await Anek42(message)
        elif name == '/Anek43':
            await Anek43(message)
        elif name == '/Anek44':
            await Anek44(message)
        elif name == '/Anek45':
            await Anek45(message)
        elif name == '/Anek46':
            await Anek46(message)
        elif name == '/Anek47_1':
            await Anek47_1(message)
        elif name == '/Anek47_2':
            await Anek47_2(message)
        elif name == '/Anek48_1':
            await Anek48_1(message)
        elif name == '/Anek48_2':
            await Anek48_2(message)
        elif name == '/Anek49':
            await Anek49(message)
        elif name == '/Anek50':
            await Anek50(message)
        elif name == '/Anek51':
            await Anek51(message)
        elif name == '/Anek52':
            await Anek52(message)
        elif name == '/Anek53':
            await Anek53(message)
        elif name == '/Anek54':
            await Anek54(message)
        elif name == '/Anek55':
            await Anek55(message)
        elif name == '/Anek56':
            await Anek56(message)
        elif name == '/Anek57':
            await Anek57(message)
        elif name == '/Anek58':
            await Anek58(message)
        elif name == '/Anek59':
            await Anek59(message)
        elif name == '/Anek60':
            await Anek60(message)
        elif name == '/Anek61':
            await Anek61(message)
        elif name == '/Anek62':
            await Anek62(message)
        elif name == '/Anek63':
            await Anek63(message)
        elif name == '/Anek64':
            await Anek64(message)
        elif name == '/Anek65':
            await Anek65(message)
        elif name == '/Anek66':
            await Anek66(message)
        elif name == '/Anek67':
            await Anek67(message)
        elif name == '/Anek68':
            await Anek68(message)
        elif name == '/Anek69':
            await Anek69(message)
        elif name == '/Anek70':
            await Anek70(message)
        elif name == '/Anek71':
            await Anek71(message)
        elif name == '/Anek72':
            await Anek72(message)
        elif name == '/Anek73':
            await Anek73(message)
        elif name == '/Anek74':
            await Anek74(message)
        elif name == '/Anek75':
            await Anek75(message)
        elif name == '/Anek76':
            await Anek76(message)
        elif name == '/Anek77':
            await Anek77(message)
        elif name == '/Anek78':
            await Anek78(message)
        elif name == '/Anek79':
            await Anek79(message)
        elif name == '/Anek80':
            await Anek80(message)
        elif name == '/Anek81':
            await Anek81(message)
        elif name == '/Anek82':
            await Anek82(message)
        elif name == '/Anek83':
            await Anek83(message)
        elif name == '/Anek84':
            await Anek84(message)
        elif name == '/Anek85':
            await Anek85(message)
        elif name == '/Anek86':
            await Anek86(message)
        elif name == '/Anek87':
            await Anek87(message)
        elif name == '/Anek88':
            await Anek88(message)
        elif name == '/Anek89':
            await Anek89(message)
        elif name == '/Anek90':
            await Anek90(message)
        elif name == '/Anek91':
            await Anek91(message)
        elif name == '/Anek92_1':
            await Anek92_1(message)
        elif name == '/Anek92_2':
            await Anek92_2(message)
        elif name == '/Anek93':
            await Anek93(message)
        elif name == '/Anek94':
            await Anek94(message)
        elif name == '/Anek95':
            await Anek95(message)
        elif name == '/Anek96':
            await Anek96(message)
        elif name == '/Anek97':
            await Anek97(message)
        elif name == '/Anek98':
            await Anek98(message)
        elif name == '/Anek99':
            await Anek99(message)
        elif name == '/Anek100_1':
            await Anek100_1(message)
        elif name == '/Anek100_1':
            await Anek100_2(message)
        elif name == '/Anek101':
            await Anek101(message)
        elif name == '/Anek102':
            await Anek102(message)
        elif name == '/Anek103':
            await Anek103(message)
        elif name == '/Anek104':
            await Anek104(message)
        elif name == '/Anek105':
            await Anek105(message)
        elif name == '/Anek106':
            await Anek106(message)
        elif name == '/Anek107':
            await Anek107(message)
        elif name == '/Anek108':
            await Anek108(message)
        elif name == '/Anek109':
            await Anek109(message)
        elif name == '/Anek110':
            await Anek110(message)
        elif name == '/Anek111_1':
            await Anek111_1(message)
        elif name == '/Anek111_2':
            await Anek111_2(message)
        elif name == '/Anek111_3':
            await Anek111_3(message)
        elif name == '/Anek112':
            await Anek112(message)
        elif name == '/Anek113':
            await Anek113(message)
        elif name == '/Anek114':
            await Anek114(message)
        elif name == '/Anek115':
            await Anek115(message)
        elif name == '/Anek116':
            await Anek116(message)
        elif name == '/Anek117':
            await Anek117(message)
        elif name == '/Anek118_1':
            await Anek118_1(message)
        elif name == '/Anek118_2':
            await Anek118_2(message)
        elif name == '/Anek119':
            await Anek119(message)
        elif name == '/Anek120_1':
            await Anek120_1(message)
        elif name == '/Anek120_2':
            await Anek120_2(message)
        elif name == '/Anek121':
            await Anek121(message)
        elif name == '/Anek122':
            await Anek122(message)
        elif name == '/Anek123_1':
            await Anek123_1(message)
        elif name == '/Anek123_2':
            await Anek123_2(message)
        elif name == '/Anek124':
            await Anek124(message)
        elif name == '/Anek125':
            await Anek125(message)
        elif name == '/Anek126':
            await Anek126(message)
        elif name == '/Anek127':
            await Anek127(message)
        elif name == '/Anek128':
            await Anek128(message)
        elif name == '/Anek129':
            await Anek129(message)
        elif name == '/Anek130':
            await Anek130(message)
        elif name == '/Anek131':
            await Anek131(message)
        elif name == '/Anek132':
            await Anek132(message)
        elif name == '/Anek133':
            await Anek133(message)
        elif name == '/Anek134':
            await Anek134(message)
        elif name == '/Anek135':
            await Anek135(message)
        elif name == '/Anek136':
            await Anek136(message)
        elif name == '/Anek137_1':
            await Anek137_1(message)
        elif name == '/Anek137_2':
            await Anek137_2(message)
        elif name == '/Anek138':
            await Anek138(message)
        elif name == '/Anek139':
            await Anek139(message)
        elif name == '/Anek140':
            await Anek140(message)
        elif name == '/Anek141':
            await Anek141(message)
        elif name == '/Anek142':
            await Anek142(message)
        elif name == '/Anek143':
            await Anek143(message)
        elif name == '/Anek144':
            await Anek144(message)
        elif name == '/Anek145':
            await Anek145(message)
        elif name == '/Anek146':
            await Anek146(message)
        elif name == '/Anek147':
            await Anek147(message)
        elif name == '/Anek148':
            await Anek148(message)

        else:
            await state.update_data(username=message.text)
            k = 0
            with open(file_path, 'r', encoding='utf-8') as file:
                for line in file:
                    if name.lower() in line.lower():
                        k = k + 1
                        text = line
                        await message.answer(text)

            if name == 'Помощь🆘' or name == 'Перезапуск🔃' or name == 'Список анекдотов📋' \
                    or name == 'Поиск анекдота🔎' or name == 'Случайный анек🎲':
                await on_click(message)
            else:
                if k == 0:
                    await message.answer(f'В списке нет такого анека \n'
                                         'Введи другое название')
    except:
        await message.answer('Хз, что произошло. Пиши админу.')
        await on_click(message)