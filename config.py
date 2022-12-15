import check_valid


def caesar_cipher_encoding():
    number_shift = int(input('На сколько букв сделать свдиг: '))
    language = input('Какой язык хотите использовать? ("ru"/"en"): ')
    # Кодировака на русском языке
    if language == 'ru':
        text = input('Введите текст: ').split(" ")
        res = ''
        if check_valid.Checking_for_the_correctness_of_the_language_is_valid(language, text):
            for full_element in text:
                result = ''
                for element in list(full_element):
                    number = number_shift
                    index_litters_ru = ord(element)
                    while number != 0:
                        # Првоерка числа на верхний регистр
                        if 1040 <= index_litters_ru <= 1071 or index_litters_ru == 1025:
                            if index_litters_ru != 1071:
                                if index_litters_ru == 1025:
                                    index_litters_ru = 1046
                                elif index_litters_ru == 1045:
                                    index_litters_ru = 1025
                                else:
                                    index_litters_ru += 1
                            else:
                                index_litters_ru = 1040
                        # Проверка на нижний регистр
                        elif 1072 <= index_litters_ru <= 1103 or index_litters_ru == 1105:
                            if index_litters_ru != 1103:
                                if index_litters_ru == 1105:
                                    index_litters_ru = 1078
                                elif index_litters_ru == 1077:
                                    index_litters_ru = 1105
                                else:
                                    index_litters_ru += 1
                            else:
                                index_litters_ru = 1072
                        number -= 1
                    # Сбор закодированного слова из перекодированных букв
                    result += chr(index_litters_ru)
                # Занесение закодированного слова в предложение
                res += result + " "
            print(res)
        else:
            print('Ошибка: неверный язык буквы. Все буквы должны быть русского алфавита')
    # Кодировка на английском языке
    elif language == 'en':
        text = input('Введите текст: ')
        res = ''
        if check_valid.Checking_for_the_correctness_of_the_language_is_valid(language, text):
            for full_element in text:
                result = ''
                for element in list(full_element):
                    number = number_shift
                    index_litters_ru = ord(element)
                    while number != 0:
                        # Проверка на верхний регистр
                        if 65 <= index_litters_ru <= 90:
                            if index_litters_ru != 90:
                                index_litters_ru += 1
                            else:
                                index_litters_ru = 65
                        # Проверка на нижний регистр
                        elif 97 <= index_litters_ru <= 122:
                            if index_litters_ru != 122:
                                index_litters_ru += 1
                            else:
                                index_litters_ru = 97
                        number -= 1
                    # Сбор закодированного слова из перекодированных букв
                    result += chr(index_litters_ru)
                # Занесение закодированного слова в предложение
                res += result
            print(res)
        else:
            print('Ошибка: неверный язык буквы. Все буквы должны быть английского алфавита')


def caesar_cipher_decoding():
    number_shift = int(input('На сколько букв сделать свдиг: '))
    language = input('Какой язык хотите использовать? ("ru"/"en"): ')
    # Декодировка русского текста
    if language == 'ru':
        text = input('Введите текст: ').split(" ")
        res = ''
        if check_valid.Checking_for_the_correctness_of_the_language_is_valid(language, text):
            for full_element in text:
                result = ''
                for element in list(full_element):
                    number = number_shift
                    index_litters_ru = ord(element)
                    # Првоерка числа на верхний регистр
                    while number != 0:
                        if 1040 <= index_litters_ru <= 1071 or index_litters_ru == 1025:
                            if index_litters_ru != 1040:
                                if index_litters_ru == 1046:
                                    index_litters_ru = 1025
                                elif index_litters_ru == 1025:
                                    index_litters_ru = 1046
                                else:
                                    index_litters_ru -= 1
                            else:
                                index_litters_ru = 1071
                        # Проверка на нижний регистр
                        elif 1072 <= index_litters_ru <= 1103 or index_litters_ru == 1105:
                            if index_litters_ru != 1072:
                                if index_litters_ru == 1078:
                                    index_litters_ru = 1105
                                elif index_litters_ru == 1105:
                                    index_litters_ru = 1077
                                else:
                                    index_litters_ru -= 1
                            else:
                                index_litters_ru = 1103
                        number -= 1
                    # Сбор закодированного слова из перекодированных букв
                    result += chr(index_litters_ru)
                # Занесение закодированного слова в предложение
                res += result + " "
            print(res)
        else:
            print('Ошибка: неверный язык буквы. Все буквы должны быть русского алфавита')
    # Декодировка англиского текста
    elif language == 'en':
        text = input('Введите текст: ').split(" ")
        res = ''
        if check_valid.Checking_for_the_correctness_of_the_language_is_valid(language, text):
            for full_element in text:
                result = ''
                for element in list(full_element):
                    number = number_shift
                    index_litters_ru = ord(element)
                    # Првоерка числа на верхний регистр
                    while number != 0:
                        # Проверка на верхний регистр
                        # Проверка на верхний регистр
                        if 65 <= index_litters_ru <= 90:
                            if index_litters_ru != 65:
                                index_litters_ru -= 1
                            else:
                                index_litters_ru = 90
                        # Проверка на нижний регистр
                        elif 97 <= index_litters_ru <= 122:
                            if index_litters_ru != 97:
                                index_litters_ru -= 1
                            else:
                                index_litters_ru = 122
                        number -= 1
                    # Сбор закодированного слова из перекодированных букв
                    result += chr(index_litters_ru)
                # Занесение закодированного слова в предложение
                res += result + " "
            print(res)
        else:
            print('Ошибка: неверный язык буквы. Все буквы должны быть английского алфавита')