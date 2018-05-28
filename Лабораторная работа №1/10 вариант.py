print('''
Задание №10. Напишите скрипт, позволяющий определить надежность вводимого
              пользователем пароля. Это задание является творческим: алгоритм
              определения надежности разработайте самостоятельно.
''')

password = input('Введите пароль:')
if len(password) < 8:
    print('Ненадежный пароль!')
else:
    check_dict = {"upper": 0, "lower": 0, "digit": 0, "sign": 0}
    for letter in password:
        if letter.isupper():
            check_dict["upper"] += 1
        else:
            if letter.islower():
                check_dict["lower"] += 1
            else:
                if letter.isdigit():
                    check_dict["digit"] += 1
                else:
                    if letter.isprintable():
                        check_dict["sign"] += 1
    print(check_dict)
    if 0 in check_dict.values():
        print("Ненадежный пароль!")
    else:
        print("Надежный пароль")