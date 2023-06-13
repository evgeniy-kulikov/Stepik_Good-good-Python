# 9.4 Функция filter
""""""

# filter(function, iterable) - Возвращает итератор из тех элементов, для которых function возвращает истину.

#
#  *   *   *   *   *   TASK    *   *   *   *   *
#


# 01
"""
Вводятся названия городов в одну строчку через пробел. 
Необходимо определить функцию filter, которая бы возвращала только названия длиной более 5 символов. 
Извлеките первые три полученных значения с помощью функции next
Input:  Тула Ульяновск Хабаровск Владивосток Омск Уфа
Output: Ульяновск Хабаровск Владивосток
"""
# st = ['Тула', 'Ульяновск', 'Хабаровск', 'Владивосток', 'Омск', 'Уфа']
st = input().split()

def get_len(el: str):
    if len(el) > 5:
        return True
    return False

res = filter(get_len, st)
for _ in range(3):
    print(next(res), end=' ')

# Короче
res = filter(lambda el: len(el) > 5, input().split())
print(*(next(res) for _ in range(3)))


# 02
"""
Вводится список предметов в виде списка:
название_1: вес_1
...
название_N: вес_N
С помощью функции map, необходимо сначала преобразовать этот список строк в кортеж, 
элементами которого также являются кортежи:
(('название_1', 'вес_1'), ..., ('название_N', 'вес_N'))
А, затем, отфильтровать (исключить) все предметы с весом менее 500, используя функцию filter. 
Вывести на экран список оставшихся предметов (только их названия) в одну строчку через пробел.
Input:  зонт=1000
        палатка=10000
        спички=22
        котелок=543
Output: зонт палатка котелок
"""
import sys
# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))
# lst_in = ['зонт=1000', 'палатка=10000', 'спички=22', 'котелок=543']

ls = tuple(map(tuple, [el.split('=') for el in lst_in]))
# ls = (('зонт', '1000'), ('палатка', '10000'), ('спички', '22'), ('котелок', '543'))
res = filter(lambda el: int(el[1]) >= 500, ls)
print(*(el[0] for el in res))

# Вариант
import sys
lst_in = list(map(str.strip, sys.stdin.readlines()))
ls = map(lambda el: tuple(el.split('=')), lst_in)
res = filter(lambda el: int(el[1]) >= 500, ls)
print(*(el[0] for el in res))


# 03
"""
Вводится список целых чисел в одну строчку через пробел. 
Необходимо оставить в нем только двузначные числа. 
Реализовать программу с использованием функции filter. 
Результат отобразить на экране в виде последовательности оставшихся чисел в одну строчку через пробел.
Input:  8 11 0 -23 140 1
Output: 11 -23
"""
ls = map(int, input().split())
res = list(filter(lambda el: 9 < abs(el) < 100, ls))
# res = list(filter(lambda el: 0 < abs(el // 10) < 10, ls))
print(*res)


# 04
"""
https://stepik.org/lesson/567074/step/5?unit=561348
выделить значения, присутствующие в обоих списках и оставить среди них только четные.
Результат вывести на экран в виде строки полученных чисел в порядке их возрастания через пробел
Input:  1 5 2 7 10 25 50 100
        5 2 3 7 10 25 55
Output: 2 10
"""
d1 = set(map(int, input().split()))
d2 = set(map(int, input().split()))
res = list(filter(lambda el: el % 2 == 0, d1 & d2))
print(*(sorted(res)))

# Вариант
d1, d2 = map(str.split, (input(), input()))
res = list(filter(lambda el: int(el) % 2 == 0, set(d1) & set(d2)))
print(*(sorted(res)))


# 05
"""
https://stepik.org/lesson/567074/step/6?unit=561348
водится список email-адресов в одну строчку через пробел. 
Среди них нужно оставить только корректно записанные адреса.
(используют латинские буквы, цифры и символ подчеркивания,
также в адресе должен быть символ "@", а после него символ точки)
Input:  abc@it.ru dfd3.ru@mail biba123@list.ru sc_lib@list.ru $fg9@fd.com
Output: abc@it.ru biba123@list.ru sc_lib@list.ru
"""
from string import ascii_letters, digits
symb = ascii_letters + digits + '_'
st = input().lower().split()

def get_email(el: str):
    post = ''
    if el.count('@') == 1:
        ls = el.split('@')
        post += ls[0]
        if ls[1].count('.') == 1:
            post += ls[1].replace('.', '')
            for el in post:
                if el not in symb:
                    return False
            return True
        return False
    return False

res = list(filter(get_email, st))
print(*res)
