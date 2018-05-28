import re

print('''
Задание4. Напишите скрипт, который позволяет ввести с клавиатуры имя
          текстового файла, найти в нем с помощью регулярных выражений все
          подстроки определенного вида, в соответствии с вариантом. Например,
          для варианта № 1 скрипт должен вывести на экран следующее:
          Строка 3, позиция 10 : найдено '11-05-2014'
          Строка 12, позиция 2 : найдено '23-11-2014'
          Строка 12, позиция 17 : найдено '23-11-2014'
        ''')


#Эта функция ищет даты в формате 22-01-2018
def find_dates(file):
    text = [string.strip() for string in open(file, 'r', encoding="utf-8").readlines()]
    pattern = re.compile('\d\d-\d\d-\d\d\d\d')
    dates = {}
    for index, string in enumerate(text):
        matches = pattern.finditer(string)
        for match in matches:
            dates["Строка "+str(index+1)+", позиция "+str(match.start())]=" : найдено '"+match.group()+"'"
    for key in dates.keys():
        print(key+dates[key])


#Эта функция ищет время в формате 23:32:13
def find_time(file):
    text = [string.strip() for string in open(file, 'r', encoding="utf-8").readlines()]
    pattern = re.compile('\d\d:\d\d:\d\d')
    dates = {}
    for index, string in enumerate(text):
        matches = pattern.finditer(string)
        for match in matches:
            dates["Строка " + str(index + 1) + ", позиция " + str(match.start())] = " : найдено '" + match.group() + "'"
    for key in dates.keys():
        print(key + dates[key])


#Эта функция ищет объявления переменных вида "тип" "имя" = "значение"
def find_expression(file):
    text = [string.strip() for string in open(file, 'r', encoding="utf-8").readlines()]
    pattern = re.compile('(int|short|byte)[ ]\w+[ ][=][ ]\d+')
    dates = {}
    for index, string in enumerate(text):
        matches = pattern.finditer(string)
        for match in matches:
            dates["Строка "+str(index+1)+", позиция "+str(match.start())]=" : найдено '"+match.group()+"'"
    for key in dates.keys():
        print(key+dates[key])


#Эта функция ищет номера телефонов вида (000)1112233 или (000)111-22-33
def find_numbers(file):
    text = [string.strip() for string in open(file, 'r', encoding="utf-8").readlines()]
    pattern = re.compile('(\(\d\d\d\)\d{7,7})|(\(000\)\d\d\d-\d\d-\d\d)')
    dates = {}
    for index, string in enumerate(text):
        matches = pattern.finditer(string)
        for match in matches:
            dates["Строка " + str(index + 1) + ", позиция " + str(match.start())] = " : найдено '" + match.group() + "'"
    for key in dates.keys():
        print(key + dates[key])


#Эта функция ищет строки типа "слово": "тип" ["число"]
def find_arrays(file):
    text = [string.strip() for string in open(file, 'r', encoding="utf-8").readlines()]
    pattern = re.compile('\w*: (int|byte|short) \[\d*\]')
    dates = {}
    for index, string in enumerate(text):
        matches = pattern.finditer(string)
        for match in matches:
            dates["Строка " + str(index + 1) + ", позиция " + str(match.start())] = " : найдено '" + match.group() + "'"
    for key in dates.keys():
        print(key + dates[key])


#Эта функция ищет IP адреса
def find_ip(file):
    text = [string.strip() for string in open(file, 'r', encoding="utf-8").readlines()]
    pattern = re.compile('[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}')
    dates = {}
    for index, string in enumerate(text):
        matches = pattern.finditer(string)
        for match in matches:
            dates["Строка " + str(index + 1) + ", позиция " + str(match.start())] = " : найдено '" + match.group() + "'"
    for key in dates.keys():
        print(key + dates[key])


#Эта функция  ищет все смайлы вида :-) :) :)))
def find_smiles(file):
    text = [string.strip() for string in open(file, 'r', encoding="utf-8").readlines()]
    pattern = re.compile(':-{0,1}\)+')
    dates = {}
    for index, string in enumerate(text):
        matches = pattern.finditer(string)
        for match in matches:
            dates["Строка " + str(index + 1) + ", позиция " + str(match.start())] = " : найдено '" + match.group() + "'"
    for key in dates.keys():
        print(key + dates[key])


#Эта функция ищет логические выражения вида x&y или x&&y
def find_logic_and(file):
    text = [string.strip() for string in open(file, 'r', encoding="utf-8").readlines()]
    pattern = re.compile('\w+ *&{1,2} *\w+')
    dates = {}
    for index, string in enumerate(text):
        matches = pattern.finditer(string)
        for match in matches:
            dates["Строка " + str(index + 1) + ", позиция " + str(match.start())] = " : найдено '" + match.group() + "'"
    for key in dates.keys():
        print(key + dates[key])


#Эта функция ищет почтовые индексы вида 83000, Донецк (закреплены только 83)
def find_post(file):
    text = [string.strip() for string in open(file, 'r', encoding='utf-8').readlines()]
    pattern = re.compile('83\d{3}, \w{3,}')
    dates = {}
    for index, string in enumerate(text):
        matches = pattern.finditer(string)
        for match in matches:
            dates["Строка " + str(index + 1) + ", позиция " + str(match.start())] = " : найдено '" + match.group() + "'"
    for key in dates.keys():
        print(key + dates[key])


#Эта функция ищет полные пути к папкам в Windows - подстроки вида C:\Folder\folder
def find_paths(file):
    text = [string.strip() for string in open(file, 'r', encoding='utf-8').readlines()]
    pattern = re.compile(r'[A-Z]:(\\[^#%&*|\\:"<>?/]+)+')
    dates = {}
    for index, string in enumerate(text):
        matches = pattern.finditer(string)
        for match in matches:
            dates["Строка " + str(index + 1) + ", позиция " + str(match.start())] = " : найдено '" + match.group() + "'"
    for key in dates.keys():
        print(key + dates[key])


find_numbers("text.txt")
input()