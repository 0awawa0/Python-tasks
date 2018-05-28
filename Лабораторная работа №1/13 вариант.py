print ('''
Задание №13. Напишите собственную версию генератора enumerate под названием
              extra_enumerate. Пример вызова:
                for i, elem, cum, frac in extra_enumerate(x):
                    print(elem, cum, frac)
              В переменной cum хранится накопленная сумма на момент текущей
              итерации, в переменной frac – доля накопленной суммы от общей
              суммы на момент текущей итерации. Например, для списка x=[1,3,4,2]
              вывод будет таким:
                (1, 1, 0.1) (3, 4, 0.4) (4, 8, 0.8) (2, 10, 1)
''')

def extra_enumerate(L):
    curr_cum = 0
    cum = sum(L)
    for i in range(len(L)):
        curr_cum += L[i]
        frac = curr_cum/cum
        yield (i, L[i], curr_cum, frac)


List = [int(x) for x in input('Введите список: ').split(' ')]
print(List)
for i, elem, cum, frac in extra_enumerate(List):
    print(elem, cum, "{:.2f}".format(frac))