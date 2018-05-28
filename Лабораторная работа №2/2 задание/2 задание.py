import hashlib
import os
print('''
Задание 2. Напишите скрипт, позволяющий искать в заданной директории и в ее
           подпапках файлы-дубликаты на основе сравнения контрольных сумм
           (MD5). Файлы могут иметь одинаковое содержимое, но отличаться
           именами. Скрипт должен вывести группы имен обнаруженных файлов-
           дубликатов. 
''')


def check_hash(foldername):
    os.chdir(foldername) #Переходим в указанную директорию
    print("В папке "+os.getcwd()+":")
    folders = [file for file in os.listdir(os.path.abspath(os.getcwd())) if os.path.isdir(file)] #Читаем имена папок
    files = [file for file in os.listdir(os.path.abspath(os.getcwd())) if os.path.isdir(file)!= True] #Читаем имена файлов
    if len(files) == 0:  #Если папка пустая переходим в верхнюю папку и выводим "Нет дубликатов"
        print("Нет дубликатов")
    else:
        pre_filename = files[0]
        content = open(files[0], 'rb').read() #Считываем содержимое первого файла в бинарном виде
        checksum = hashlib.md5(content).hexdigest() #Получаем хеш содержимого первого файла
        duplicates = []
        for file in files[1:]:
            content = open(file, 'rb').read() #Читаем содержимое следующего файла
            if checksum == hashlib.md5(content).hexdigest(): #Если хеш прошлого файла совпал с хешем следующего
                duplicates.append(pre_filename+" = "+file)  #Добавляем в список дубликатов имена файлов через рзделитель " = "
            pre_filename = file
            checksum = hashlib.md5(content).hexdigest()
        if len(duplicates) == 0:
            print("Нет дубликатов")
        else:
            print(duplicates) #Выводим список дубликатов
    if len(folders) == 0:
        os.chdir("..")
    else:
        for folder in folders: #Далее проверяем все папки
            check_hash(folder)
        os.chdir("..") #После полной проверки переходим в верхнюю папку


check_hash(os.getcwd())
