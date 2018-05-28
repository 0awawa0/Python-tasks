import os
import sys
import datetime

print('''
Задание 6. Напишите скрипт reorganize.py, который в директории --source создает
           две директории: Archive и Small. В первую директорию помещаются
           файлы с датой изменения, отличающейся от текущей даты на
           количество дней более параметра --days (т.е. относительно старые
           файлы). Во вторую – все файлы размером меньше параметра --size байт.
           Каждая директория должна создаваться только в случае, если найден
           хотя бы один файл, который должен быть в нее помещен. Пример
           вызова:
            reorganize --source "C:\TestDir" --days 2 --size 4096
''')


def sort_files(source, days, size):
    if source[-1] != os.path.sep: #Если путь к папке не заканчивается разделителем
        source = source+os.path.sep #Добавляем разделитель
    today = datetime.date.today() #Получаем сегодняшнюю дату
    files = [file for file in os.listdir(source) if os.path.isfile(source+file)] #Получаем список файлов в папке
    for file in files: #Проходим по списку
        file_date = datetime.datetime.fromtimestamp(os.path.getmtime(source+file)).date() #Получаем дату изменения файла
        file_size = os.path.getsize(source+file) #Получаем размер файла
        delta = today - file_date #Получаем разницу во времени между сегодняшней и датой изменения файла
        if delta.days > days: #Если разница больше заданной
            folder_name = source+"Archive"+os.path.sep
            try:
                os.mkdir(folder_name) #Создаем папку "Archive"
                os.rename(source+file, folder_name+file) #Переносим в нее файл
            except FileExistsError: #Если папка уже существует
                os.rename(source+file, source+"Archive"+os.sep+file) #Просто переносим туда файл
            continue #Переходим к следующему файлу
        if file_size < size: #Если размер файла меньше заданного
            folder_name = source+"Small"+os.path.sep
            try:
                os.mkdir(folder_name) #Создаем папку "Small"
                os.rename(source + file, folder_name+file) #Переносим в нее файл
            except FileExistsError: #Если папка уже существует
                os.rename(source+file, folder_name+file) #Просто перносим туда файл


arguments = {sys.argv[1]: sys.argv[2], sys.argv[3]: sys.argv[4], sys.argv[5]: sys.argv[6]} #Создаем словарь переданных аргументов
source = arguments["--source"]
days = int(arguments["--days"])
size = int(arguments["--size"])
sort_files(source, days, size)

