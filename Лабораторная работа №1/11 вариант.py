print('''
Задание №11. Напишите генератор frange как аналог range() с дробным шагом.
              Пример вызова:

                for x in frange(1, 5, 0.1):
                print(x)
                # выводит 1 1.1 1.2 1.3 1.4 … 4.9
''')


def frange(start, end, step):
    while start + step < end:
        start = start + step
        yield start


gen = [float(s) for s in input('Введите начало, конец и шаг генератора через запятую без пробелов: ').split(',')]
for x in frange(gen[0], gen[1], gen[2]):
    print('{:.2f}'.format(x))