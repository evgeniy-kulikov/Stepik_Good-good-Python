# 7.11 Декораторы функций
""""""


def func_decorator(func):  # Параметр func ссылка на функцию func()
    def wrapper():
        print("--- что-то делаем перед вызовом функции ---")
        func()
        print("--- что-то делаем перед вызовом функции ---")

    return wrapper


def some_func():
    print("Тут вызов функции some_func")


some_func()
# Тут вызов функции some_func

f = func_decorator(some_func)
f()
"""
--- что-то делаем перед вызовом функции ---
Тут вызов функции some_func
--- что-то делаем перед вызовом функции ---
"""

some_func = func_decorator(some_func)
some_func()
"""
--- что-то делаем перед вызовом функции ---
Тут вызов функции some_func
--- что-то делаем перед вызовом функции ---
"""


# добавление аргументов

def func_decorator1(func):
    def wrapper(title):
        print("--- что-то делаем перед вызовом функции ---")
        func(title)
        print("--- что-то делаем перед вызовом функции ---")

    return wrapper


def some_funk1(title):
    print(f"Вызов функции some_func, title =", title)


some_funk1 = func_decorator1(some_funk1)
some_funk1('Тоже неплохо')


# универсальный метод для любых функций

def func_decorator2(func):
    def wrapper(*args, **kwargs):
        print("--- что-то делаем перед вызовом функции ---")
        res = func(*args, **kwargs)
        print("--- что-то делаем перед вызовом функции ---")
        return res

    return wrapper


def some_funk2(title, tag):
    print(f"Вызов функции some_func, title = {title}, tag = {tag}")
    return f"<{tag}>{title}</{tag}>"


some_funk2 = func_decorator2(some_funk2)
res1 = some_funk2('Python навсегда', 'h1')
"""
--- что-то делаем перед вызовом функции ---
Вызов функции some_func, title = Python навсегда, tag = h1
--- что-то делаем перед вызовом функции ---
"""

print(res1)
# <h1>Python навсегда</h1>


# пример применения - тестировщик времени хода (универсальный)

import time


def test_time(func):
    """Тестирование скорости выполнения функции"""
    def wrapper(*args, **kwargs):
        st = time.time()  # Временная отметка старта
        res = func(*args, **kwargs)
        et = time.time()  # Временная отметка финиша
        dt = et - st  # Промежуток времени
        print(f"Время работы: {dt} сек")
        # print(f"Время работы {func}: {dt} сек")
        return res  # результат работы функции

    return wrapper


@test_time  # Применение декоратора
def get_nod(a,b):
    """Медленный алгоритм Евклида"""
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return f'НОД: {a}'


@test_time  # Применение декоратора
def get_fast_nod(a, b):
    """Быстрый алгоритм Евклида"""
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a % b

    return f'НОД: {a}'


get_nod = test_time(get_nod)  # Вариант декорирования функции (для примера) Если не используем @test_time
res = get_nod(2, 1000000)
print(res)
"""
Время работы: 0.025832653045654297 сек
НОД: 2
"""


get_nod = test_time(get_nod)  # Вариант декорирования функции (для примера) Если не используем @test_time
get_fast_nod = test_time(get_fast_nod)  # Вариант декорирования функции (для примера) Если не используем @test_time

res1 = get_nod(2, 1000000)
res2 = get_fast_nod(2, 1000000)

print(res1, res2)
"""
Время работы: 0.025289058685302734 сек
Время работы: 0.0 сек
НОД: 2 НОД: 2
"""


#  универсальный шаблон для декораторов...

def decorator(func):  # Сюда передаём функцию которую нужно декорировать
    def wrapper(*args, **kwargs):  # Сюда передаём аргументы декорированной функции
        # print(f'{func.__name__} started')  # декорирующие действия 1 (необязательно)
        result = func(*args, **kwargs)  # *args -чтобы работать с разным кол-вом аргументов
        # print(f'{func.__name__} finished')  # декорирующие действия 2 (необязательно)
        return f'Сумма: {result}'  # возвращаем результат

    return wrapper  # передаём ссылку на вложенную функцию


@decorator  # сахар для вызова декоратора (навешиваем декоратор)
def summ(a, b):  # функция которую нужно декорировать в этот момент: summ = wrapper
    return a + b

print(summ(2, 3))


#  *   *   *   *   *   TASK    *   *   *   *   *

#  *   *   *   *   *   TASK    *   *   *   *   *


"""
Объявите функцию с именем get_sq, которая вычисляет площадь прямоугольника по двум параметрам: 
width и height - ширина и высота прямоугольника. 
И возвращает результат (сама ничего на экран не выводит). 
То есть, функция имеет сигнатуру:  def get_sq(width, height): ...
Определите декоратор func_show для этой функции, 
который отображает результат на экране в виде строки (без кавычек):
"Площадь прямоугольника: <значение>"
Вызывать функцию и декоратор не нужно, только объявить. 
Применять декоратор к функции также не нужно.
Input:  8 11
Output: Площадь прямоугольника: 88
"""
# Решение для ответа (в приемную консоль)
def func_show(square):
    def wrapper(*args):
        res_inner = square(*args)
        print(f'Площадь прямоугольника: {res_inner}')
    return wrapper


def get_sq(width, height):
    res = width * height
    return res


# Решение для PyCharm
width, height = map(int, input().split())

def func_show(square):
    """Декоратор"""
    def wrapper(*args):
        res_inner = square(*args)
        return f'Площадь прямоугольника: {res_inner}'
    return wrapper


def get_sq(width, height):
    res = width * height
    return res


f_show = func_show(get_sq)
res = f_show(width, height)
print(res)




"""
На вход программы поступает строка с названиями пунктов меню, записанные в одну строчку через пробел. 
Необходимо задать функцию с именем get_menu, 
которая преобразует эту строку в список из слов и возвращает этот список. Сигнатура функции, следующая:
def get_menu(s): ...
Определите декоратор для этой функции с именем show_menu, который отображает список на экран в формате:
1. Пункт_1
2. Пункт_1
...
N. Пункт_N

Примените декоратор show_menu к функции get_menu, используя оператор @. 
P.S. В программе необходимо только объявить декоратор и применить его к функции.
     Более ничего в программе делать не нужно. Сами функции не вызывать.
Input:  Главная Добавить Удалить Выйти
Output: 1. Главная
        2. Добавить
        3. Удалить
        4. Выйти
"""
# Решение для ответа (в приемную консоль)

def show_menu(funk):
    """декоратор"""
    def wrapper(*args):
        res = funk(*args)
        for num, st in enumerate(res):
            print(f'{num + 1}. {st}')
    return wrapper


@show_menu
def get_menu(s):
    ls = list(s.split())
    return ls

# st = 'Главная Добавить Удалить Выйти'
# get_menu(st)


"""
На вход программы поступает строка из целых чисел, записанных через пробел. 
Напишите функцию get_list, которая преобразовывает эту строку в список из целых чисел и возвращает его. 
Определите декоратор для этой функции, который сортирует список чисел по возрастанию. 
Результат сортировки должен возвращаться при вызове декоратора.
Вызовите декорированную функцию get_list и отобразите полученный отсортированный список lst командой:
print(*lst)
Input:  8 11 -5 4 3 10
Output: -5 3 4 8 10 11
"""

def get_sort(funk):
    """Сортировка списка (декоратор)"""
    def wrapper(ls: str):
        res = funk(ls)
        res.sort()
        return res
    return wrapper

#  Вариант
# def get_sort(funk):
#     def wrapper(*args):
#         res = sorted(funk(*args))
#         return res
#     return wrapper

@get_sort
def get_list(s: str):
    res = list(map(int, s.split()))
    return res


s_in = input()
print(*get_list(s_in))



"""
Вводятся две строки из слов (слова записаны через пробел). 
Объявите функцию, которая преобразовывает эти две строки в два списка слов и возвращает эти списки.
Определите декоратор для этой функции, который из двух списков формирует словарь, 
в котором ключами являются слова из первого списка, а значениями - соответствующие элементы из второго списка. 
Полученный словарь должен возвращаться при вызове декоратора.
Примените декоратор к первой функции и вызовите ее для введенных строк. 
Результат (словарь d) отобразите на экране командой: print(*sorted(d.items()))

Input:  house river tree car
        дом река дерево машина
Output: ('car', 'машина') ('house', 'дом') ('river', 'река') ('tree', 'дерево')
"""

s1, s2 = input(), input()
# s1 = 'house river tree car'
# s2 = 'дом река дерево машина'


def get_dict(funk):
    def wrapper(key, val):
        items = funk(key, val)
        res_dict = {items[0][el]: items[1][el] for el in range(len(items[0]))}
        # res_dict = dict(zip(items[0], items[1]))  # короче
        return res_dict
    return wrapper

# Вариант
# def get_dict(funk):
#     def wrapper(*args):
#         items = funk(*args)
#         res_dict = dict(zip(items[0], items[1]))
#         return res_dict
#     return wrapper


@get_dict
# def get_double_list(st1: str, st2: str) -> tuple:
def get_double_list(st1, st2):
    ls1 = list(map(str, st1.split()))
    ls2 = list(map(str, st2.split()))
    return ls1, ls2


d = get_double_list(s1, s2)
# print(d)
# (['house', 'river', 'tree', 'car'], ['дом', 'река', 'дерево', 'машина'])
print(*sorted(d.items()))
# ('car', 'машина') ('house', 'дом') ('river', 'река') ('tree', 'дерево')


"""
Объявите функцию, которая принимает строку на кириллице и преобразовывает ее в латиницу, 
используя словарь 't'  для замены русских букв на соответствующее латинское написание.
Функция должна возвращать преобразованную строку. 
Замены делать без учета регистра (исходную строку перевести в нижний регистр - малые буквы). 
Все небуквенные символы ": ;.,_" превращать в символ '-' (дефиса).
Определите декоратор для этой функции, который несколько подряд идущих дефисов, превращает в один дефис. 
Полученная строка должна возвращаться при вызове декоратора. (Сам декоратор на экран ничего выводить не должен).
Примените декоратор к первой функции и вызовите ее для введенной строки s на кириллице: s = input()

Input:  Python - это круто!
Output: python-eto-kruto!
"""
t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}


def remove_hyphen(func):
    def wrapper(*arg):
        res = func(*arg)
        while '--' in res:
            res = res.replace('--', '-')
        return res
    return wrapper

@remove_hyphen
def get_translate(st: str):
    s = st.lower()
    s_out = ''
    for el in s:
        if el in t.keys():
            s_out += t[el]
        elif el in ': ;.,_':
            s_out += '-'
        else:
            s_out += el
    return s_out

# Вариант
# @remove_hyphen
# def get_translate(st: str):
#     s = list(st.lower())
#     for idx, el in enumerate(s):
#         if 'а' <= el <= 'я' or el == 'ё':
#             s[idx] = t[el]
#         elif el in ": ;.,_":
#             s[idx] = '-'
#     return ''.join(s)

s = input()
print(get_translate(s))

