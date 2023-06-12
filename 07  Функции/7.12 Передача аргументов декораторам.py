#  7.12 Передача аргументов декораторам
""""""

# Декораторы функций с параметрами
import math


# Декорирование через @ с параметром
def df_decorator(dx=0.0001):
    def func_decorator(func):
        def wrapper(x, *args, **kwargs):
            res = (func(x + dx, *args, **kwargs) - func(x, *args, **kwargs)) / dx
            return res
        return wrapper
    return func_decorator


@df_decorator(dx=0.01)
def sin_df(x):
    return math.sin(x)


df = sin_df(math.pi / 3)
print(df)


# Декорирование стандартным способом (внешний декоратор)
def df_decorator2(dx=0.0001):
    def func_decorator(func):
        def wrapper(x, *args, **kwargs):
            res = (func(x + dx, *args, **kwargs) - func(x, *args, **kwargs)) / dx
            return res
        return wrapper
    return func_decorator


def sin_df2(x):
    return math.sin(x)


# Вариант полный
f = df_decorator2()
sin_df21 = f(sin_df2)
df = sin_df21(math.pi / 3)
print(df)

# Вариант сокращенный
sin_df22 = df_decorator2(dx=0.000001)(sin_df2)
df = sin_df22(math.pi / 3)
print(df)


# Проблема потери имени и описание декорируемой функции и варианты ее решения
# 1. Через __name__ и __doc__
def df_decorator3(dx=0.0001):
    def func_decorator(func):
        def wrapper(x, *args, **kwargs):
            res = (func(x + dx, *args, **kwargs) - func(x, *args, **kwargs)) / dx
            return res

        # хороший тон при декорировании функций
        wrapper.__name__ = func.__name__
        wrapper.__doc__ = func.__doc__
        return wrapper

    return func_decorator


@df_decorator3(dx=0.001)
def sin_df3(x):
    """Функция вычисления производной синуса"""
    return math.sin(x)


print(sin_df3.__name__)
print(sin_df3.__doc__)

# 2. Через functools и wraps
from functools import wraps


def df_decorator4(dx=0.0001):
    def func_decorator(func):
        @wraps(func)
        def wrapper(x, *args, **kwargs):
            res = (func(x + dx, *args, **kwargs) - func(x, *args, **kwargs)) / dx
            return res

        # хороший тон при декорировании функций
        # wrapper.__name__ = func.__name__
        # wrapper.__doc__ = func.__doc__
        return wrapper

    return func_decorator


@df_decorator4(dx=0.001)
def sin_df4(x):
    """Функция вычисления производной синуса"""
    return math.sin(x)


print(sin_df4.__name__)
print(sin_df4.__doc__)


#  *   *   *   *   *   TASK    *   *   *   *   *
#  *   *   *   *   *   TASK    *   *   *   *   *


"""
Вводится строка целых чисел через пробел. 
Напишите функцию, которая преобразовывает эту строку в список чисел и возвращает их сумму.
Определите декоратор для этой функции, который имеет один параметр start - начальное значение суммы.
Примените декоратор со значением start=5 к функции и вызовите декорированную функцию для введенной строки s:
s = input()
Input:  5 6 3 6 -4 6 -1
Output: 26
"""


def get_param(n=None):
    def increase_num(func):
        """increase in the number"""
        def wrapper(*args):
            res = func(*args)
            return res + n
        return wrapper
    return increase_num


@get_param(n=5)
def get_sum(st: str) -> int:
    """Convert string to summ of number"""
    ls = list(map(int, st.split()))
    res = sum(ls)
    return res


s = input()
print(get_sum(s))


"""
Объявите функцию, которая возвращает переданную ей строку в нижнем регистре (с малыми буквами). 
Определите декоратор для этой функции, который имеет один параметр tag, 
определяющий строку с названием тега и начальным значением "h1". 
Этот декоратор должен заключать возвращенную функцией строку в тег tag и возвращать результат.
Пример заключения строки "python" в тег h1: <h1>python</h1>
Примените декоратор со значением tag="div" к функции и вызовите декорированную функцию для введенной строки s:
s = input()
Input:  Декораторы - это классно!
Output: <div>декораторы - это классно!</div>
"""

def get_param(tag="h1"):
    def get_tag(func):
        def wrapper(*args):
            res = func(*args)
            return f'<{tag}>{res}</{tag}>'
        return wrapper
    return get_tag


@get_param('div')
def get_string(st: str):
    return st.lower()

s = input()
print(get_string(s))


"""
Объявите функцию, которая принимает строку на кириллице и преобразовывает ее в латиницу, 
используя следующий словарь для замены русских букв на соответствующее латинское написание.
Функция должна возвращать преобразованную строку. 
Замены делать без учета регистра (исходную строку перевести в нижний регистр - малые буквы). 
Определите декоратор с параметром chars и начальным значением " !?", 
который данные символы преобразует в символ "-" и, кроме того, 
все подряд идущие дефисы (например, "--" или "---") приводит к одному дефису. 
Полученный результат должен возвращаться в виде строки.
Примените декоратор с аргументом chars="?!:;,. " к функции и 
вызовите декорированную функцию для введенной строки s = input()
Input:  Декораторы - это круто!
Output: dekoratory-eto-kruto-
"""
t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}


def convert_not_letter(chars=' !?'):
    def get_func(fanc):
        def wrapper(*args):
            ls = fanc(*args)
            for el in chars:
                ls = ls.replace(el, '-')
            while '--' in ls:
                ls = ls.replace('--', '-')
            return ls
        return wrapper
    return get_func


@convert_not_letter(chars='?!:;,. ')
def make_convert(st: str):
    s = list(map(str, st.lower()))
    for idx, el in enumerate(s):
        if el in t.keys():
            s[idx] = t[el]
    return ''.join(s)

# Короче
# @convert_not_letter(chars='?!:;,. ')
# def make_convert(st: str):
#     return ''.join([t[el] if t.get(el) else el for el in st.lower()])

# s = 'Декораторы - это круто!'
s = input()
print(make_convert(s))


"""
Объявите функцию с именем get_list и следующим описанием в теле функции:
'''Функция для формирования списка целых значений'''
Сама функция должна формировать и возвращать список целых чисел, 
который поступает на ее вход в виде строки из целых чисел, записанных через пробел.
Определите декоратор, который выполняет суммирование значений из списка этой функции и возвращает результат.
Внутри декоратора декорируйте переданную функцию get_list 
с помощью команды @wraps (не забудьте сделать импорт: from functools import wraps). 
Такое декорирование необходимо, чтобы исходная функция get_list 
сохраняла свои локальные свойства: __name__ и __doc__.
Примените декоратор к функции get_list, но не вызывайте ее.
Input:  *
Output: *
"""
from functools import wraps


def get_sum(func):
    """Функция для получения суммы из списка целых значений"""
    @wraps(func)
    def wrapper(*args):
        """Декоратор для передачи аргументов во внутреннюю функцию"""
        res = func(*args)
        return sum(res)
    return wrapper


@get_sum
def get_list(st: str) -> list:
    """Функция для формирования списка целых значений"""
    res = list(map(int, st.split()))
    return res

# Для ответа это строки должны быть закомментированы
# s = input()
# print(get_list(s))
# print(get_list.__name__)
# print(get_list.__doc__)
