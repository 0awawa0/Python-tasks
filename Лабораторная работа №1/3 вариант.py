print('''
Задание №3. Напишите скрипт, который позволяет ввести с клавиатуры номер
             дебетовой карты (16 цифр) и выводит номер в скрытом виде: первые и
             последние 4 цифры отображены нормально, а между ними – символы
             «*» (например, 5123 **** **** 1212).
''')

try:
    num = input('Введите номер карты: ')
    if len(num) != 16:
        raise ValueError
except ValueError:
    print('Неверный формат!')
else:
    print('{} **** **** {}'.format(num[0:4], num[-4:len(num) + 1]))
finally:
    input()
