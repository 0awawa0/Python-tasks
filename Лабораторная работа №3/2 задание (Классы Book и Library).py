import re

'''
Задание 2. Напишите классы «Книга» (с обязательными полями: название, автор, код), «Библиотека»
           (с обязательными полями: адрес, номер) и корректно свяжите их. Код книги должен назначаться
            автоматически при добавлении книги в библиотеку (используйте для этого статический член класса).
            Если в конструкторе книги указывается в параметре пустое название, необходимо сгенерировать
            исключение (например, ValueError). Книга должна реализовывать интерфейс Taggable с методом tag(),
            который создает на основе строки набор тегов (разбивает строку на слова и возвращает только те,
            которые начинаются с большой буквы). Например, tag() для книги с названием ‘War and Peace’
            вернет список тегов [‘War’, ‘Peace’]
'''


class Book(object):  # Описываем класс Book
    def __init__(self, author, title, code=None):  # Инициализация экземпляра класса
        if (title == '') or (type(title) != str):  # Если название книги - пустая строка
            raise ValueError  # Выбрасываем исключение
        else:
            self.__title = title  # Иначе сохраняем название
        if (author == '') or (type(author) != str):  # То же самое для автора
            self.__author = 'Unknown'
        else:
            self.__author = author
        self.__code = code

    def tag(self):  # Реализация Taggable интерфейса
        return re.compile('[A-Z][a-z]+').findall(self.__title)  # Ищем слова с большой буквы и возвращаем их список

    def set_code(self, code):  # Функция установки кода книги
        self.__code = code

    def __str__(self):  # Преобразование в тип string
        return "[%s] %s '%s'" % (str(self.__code), self.__author, self.__title)


class Library(object):  # Описание класса Library
    code = 1  # Статическая переменная класса, код книги

    def __init__(self, number, address):  # Инициализация экземпляра
        self.__number = number  # Номер библиотеки
        self.__address = address  # Адрес библиотеки
        self.__books = []  # Список книг, изначально пустой

    def __iadd__(self, b):  # Перегрузка оператора +=
        b.set_code(Library.code)  # Устанавливаем книге код
        Library.code += 1  # Увеличиваем код на 1
        self.__books.append(b)  # Дополняем список книг
        return self  # Возвращаем новую библиотеку

    def __iter__(self):  # Преобразование в итерируемый объект
        return iter(self.__books)  # Преобразуем список книг в итератор


if __name__ == "__main__":
    lib = Library(1, '51 Some str. NY')
    lib += Book('Leo Tolsoti', 'War and Peace')
    lib += Book('Charles Dickens', 'David Copperfield')
    for book in lib:
        print(book)
        print(book.tag())
