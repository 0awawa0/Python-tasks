print('''
Задание №15. Напишите параметризированный декоратор pre_process, который
              осуществляет предварительную обработку (цифровую фильтрацию)
              списка по алгоритму: s[i] = s[i]–a∙s[i–1]. Параметр а можно задать в
              коде (по умолчанию равен 0.97). Пример кода:
                    @pre_process(a=0.93)
                    def plot_signal(s):
                        for sample in s:
                            print(sample)
''')
from functools import wraps
def pre_process(a=0.97):
    def decorator(func):
        @wraps(func)
        def decorator(s):
            for i in range(1, len(s)):
                s[i] = s[i]-a*s[i-1]
            func(s)
        return decorator
    return decorator


@pre_process(a=0.93)
def plot_signal(s):
    for sample in s:
        print(sample)

List=[1,2,3]
plot_signal(List)