import re

print('''
Задание 5. Введите с клавиатуры текст. Программно найдите в нем и выведите
           отдельно все слова, которые начинаются с большого латинского
           символа (от A до Z) и заканчиваются 2 или 4 цифрами, например
           «Petr93», «Johnny70», «Service2002». Используйте регулярные
           выражения.
''')


def find_nicks(text):
    pattern = re.compile(r"[A-Z][A-Za-z]*(\d{2}|\d{4})\b")
    for found in pattern.finditer(text):
        match = found.group()
        if (str.isdigit(match[-1])):
            print(match)
        else:
            print(match[:-1])


find_nicks(input("Введите текст: "))