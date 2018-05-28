class Fraction(object):

    def __init__(self, num, den):  # Инициализация экземпляра класса
        self.__num = num  # Это числитель
        self.__den = den  # Это знаменатель
        self.reduce()  # Объявление метода сокращения дроби

    def __str__(self):  # Преборазования объекта в строку
        if (self.__num < 0 and self.__den < 0) or (self.__num > 0 and self.__den > 0):  # Если числитель и знаменатель одного знака
            return "%d/%d" % (abs(self.__num), abs(self.__den))  # Выводим дробь без минуса
        else:
            return "-%d/%d" % (abs(self.__num), abs(self.__den))  # Иначе с минусом

    def reduce(self):  # Метод сокращения дроби
        g = Fraction.gcd(self.__num, self.__den)  # Вычисляем найименьший общий делитель по алгоритму Евклида
        self.__num /= g  # Делим числитель
        self.__den /= g  # Делим знаменатель

    @staticmethod  # Статический метод
    def gcd(n, m):  # Алгоритм Евклида
        if m == 0:  # Если второе число ноль
            return n  # Возвращаем первое число
        else:
            return Fraction.gcd(m, n % m)  # Иначе вызываем эту же функцию, но меняем местами аргументы и первое число
            #  делится по модулю на второе

    def __neg__(self):  # Перегрузка унарного оператора -
        return Fraction(-self.__num, self.__den)  # Возвращаем новый объект с обращенным знаком числителя

    def __invert__(self):  # Перегрузка унарного оператора бинарного инвертирования
        return Fraction(self.__den, self.__num)  # Меняем местами числитель и знаменатель

    def __pow__(self, power):  # Перегрузка оператора возведения в степень
        return Fraction(self.__num ** power, self.__den ** power)  # Возводим в степень числитель и знаменатель

    def __float__(self):  # Преобразование объекта в десятичную дробь
        return self.__num/self.__den  # Делим числитель на знаменатель

    def __int__(self):  # Преобразование объекта в целое число
        return int(self.__num/self.__den)  # Делим числитель и знаменатель и преобразовываем в целое


if __name__ == "__main__":
    frac = Fraction(7, 2)
    print(-frac)
    print(~frac)
    print(frac**2)
    print(float(frac))
    print(int(frac))
