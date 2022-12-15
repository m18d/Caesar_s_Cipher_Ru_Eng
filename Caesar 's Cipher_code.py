import check_valid
from config import caesar_cipher_decoding, caesar_cipher_encoding




print("Запущена программа по шифрования и дешифрованию 'Шифр Цезаря'")
while True:
    print('Шифровать пароль ( 1 ) или Дешифровать пароль ( 2 )')
    choice = input('Ввод: ')
    if check_valid.is_valid(choice):
        if int(choice) == 1:
            caesar_cipher_encoding()
        elif int(choice) == 2:
            caesar_cipher_decoding()