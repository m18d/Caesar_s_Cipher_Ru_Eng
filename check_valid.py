def is_valid(choice):
    if choice.isdigit():
        if 0 < int(choice) < 3:
            return True
        else:
            print("Диапазон от 1 до 2")
            return False
    else:
        print('Некорректные данные')
        return False


def Checking_for_the_correctness_of_the_language_is_valid(language, text):
    if language == 'ru':
        for full_element in text:
            for element_in_text in list(full_element):
                if 1040 <= ord(element_in_text) <= 1071 or 1025 == ord(element_in_text) or 1072 <= ord(element_in_text) <= 1103 or ord(element_in_text) == 1105:
                    continue
                else:
                    return False
    elif language == 'en':
        for full_element in text:
            for element_in_text in list(full_element):
                if 65 <= ord(element_in_text) <= 90 or 97 <= ord(element_in_text) <= 122:
                    continue
                else:
                    return False
    return True
