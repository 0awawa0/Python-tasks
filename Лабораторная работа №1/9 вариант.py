print('''
Задание №9. Напишите программу, имитирующую работу банкомата. Выберите
             структуру данных для хранения купюр разного достоинства в заданном
             количестве. При вводе пользователем запрашиваемой суммы денег,
             скрипт должен вывести на консоль количество купюр подходящего
             достоинства. Если имеющихся денег не хватает, то необходимо
             напечатать сообщение «Операция не может быть выполнена!».
             Например, при сумме 5370 рублей на консоль должно быть выведено
             «5*1000 + 3*100 + 1*50 + 2*10».
''')

money = {"5000":2, "1000":3, "500":5, "100":1, "50":0, "10":6}
n = int(input("Введите сумму:"))
need = n
if n > sum(int(key)*money[key] for key in money.keys()):print('Операция не может быть выполнена!')
else:
    get = {}
    for key in money.keys():
        k = 0
        while(n>=int(key)) and (money[key]>0):
            n -= int(key)
            k += 1
            money[key]= money[key]-1
        get[key] = k
    if need > sum(int(key)*get[key] for key in get.keys()): print('Операция не может быть выполнена!')
    else: print('+'.join([("%s*%s"%(key, get[key])) for key in get.keys() if(get[key]!=0)]))