print('''
Задание №14. Напишите декоратор non_empty, который дополнительно проверяет
              списковый результат любой функции: если в нем содержатся пустые
              строки или значение None, то они удаляются. Пример кода:
              @non_empty
              def get_pages():
                return ['chapter1', '', 'contents', '', 'line1'] 
''')


def non_empty(function):
    def decorator():
        pages = function()
        for page in pages:
            if page == '' or page==None:
             pages.remove(page)
        return pages
    return decorator


@non_empty
def get_pages():
    return ['chapter1', '', 'contents', '', 'line1']


print(get_pages())