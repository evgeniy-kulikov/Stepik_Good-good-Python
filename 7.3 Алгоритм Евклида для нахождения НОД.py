# 7.3 Алгоритм Евклида для нахождения НОД
""""""


import time


def get_nod(a, b):
    """
    Медленный алгоритм Евклида для нахождения НОД для 2-х натуральных чисел
    :param a: int
    :param b: int
    :return: int  (НОД)
    """
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a

    return a  # можно и  return b   т.к. a  == b


# res = get_nod(8, 36)  # 4
# print(res)

# Вывод описания функции в терминале
# help(get_nod)


# Тестирующая функция
def test_nod(func):
    # test 01
    a = 28
    b = 35
    res = func(a, b)
    if res == 7:
        print("test 01 - OK")
    else:
        print("test 01 - fail")

    # test 02
    a = 100
    b = 1
    res = func(a, b)
    if res == 1:
        print("test 02 - OK")
    else:
        print("test 02 - fail")

    # test 03
    a = 2
    b = 50000000
    nod_start = time.time()
    res = func(a, b)
    nod_end = time.time()
    delta = nod_end - nod_start
    if res == 2 and delta < 1:
        print("test 03 - OK")
    else:
        print("test 03 - fail")

# Вызов тестирующей функции
test_nod(get_nod)


def get_nod_fast(a, b):
    """
    Быстрый алгоритм Евклида для нахождения НОД для 2-х натуральных чисел
    :param a: int
    :param b: int
    :return: int  (НОД)
    """
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b

    return a

# Вызов тестирующей функции
test_nod(get_nod_fast)


"""
Повторите быстрый алгоритм Евклида для нахождения наибольшего общего делителя двух натуральных чисел a и b. 
В программе необходимо объявить функцию get_nod, которая принимает два аргумента a и b (натуральные числа) и 
возвращает вычисленное значение НОД(a, b).
"""
def get_nod_var(a: int, b: int) -> int:
    """
    Быстрый алгоритм Евклида для нахождения наибольшего общего делителя двух натуральных чисел a и b
    :param a: int
    :param b: int
    :return: int (НОД)
    """
    while b:
        a, b = b, a % b
    return a

# Вызов тестирующей функции
test_nod(get_nod_var)
