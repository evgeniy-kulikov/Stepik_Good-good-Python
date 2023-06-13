# 9.3 Функция map
""""""


#
#  *   *   *   *   *   TASK    *   *   *   *   *
#

# 01
s = map(float, input().split())
for _ in range(3):
    print(next(s), end=' ')

# Короче
print(*(next(s) for _ in range(3)))


# 02
"""
На вход поступает строка из целых чисел, записанных через пробел. 
С помощью функции map преобразовать эту строку в список целых чисел, взятых по модулю.
"""

st = list(map(lambda el: abs(int(el)), input().split()))
print(*st)

# Вариант
st = list(map(abs, map(int, input().split())))
print(*st)


# 03
"""
Вводится таблица целых чисел. Используя функцию map и генератор списков, 
преобразуйте список строк lst_in (см. листинг) в двумерный список с именем lst2D, содержащий целые числа. 
Input:  8 11 -5
        3 4 10
        -1 -2 3
        4 5 6
Output: True
"""
# lst_in = ['8 11 -5', '3 4 10', '-1 -2 3', '4 5 6']
import sys
# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

lst2D = [list(map(int, el.split())) for el in lst_in]

# Варианты
lst2D = [[*map(int, el.split())] for el in lst_in]

lst2D = [*map(lambda el: [*map(int, el.split())], lst_in)]

lst2D = [*map(lambda x: [int(el) for el in x.split()], lst_in)]


# 04
"""
На вход программы поступает строка в формате:
ключ_1=значение_1 ключ_2=значение_2 ... ключ_N=значение_N
Необходимо с помощью функции map преобразовать ее в кортеж tp вида:
tp = (('ключ_1', 'значение_1'), ('ключ_2', 'значение_2'), ..., ('ключ_N', 'значение_N'))
Input:  house=дом car=машина men=человек tree=дерево
Output: True
"""
# s_lst = ['house=дом', 'car=машина', 'men=человек', 'tree=дерево']
s = input()
s_lst = s.split()

tp = tuple(map(lambda el: tuple(el.split('=')), s_lst))

# Вариант
tp = tuple(map(tuple, [el.split('=') for el in s_lst]))

# без map()
tp = tuple(tuple(el.split("=")) for el in s_lst)


# 05
"""
определен словарь "t".
Вводится строка. Необходимо в ней заменить кириллические символы 
на соответствующие латинские обозначения (без учета регистра букв), 
а все остальные символы - на символ дефиса (-).
Input:  Привет Питон
Output: privet-piton
Привет Питон58КРуТоЙ
"""
t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}

st = input().lower()
res = map(str, [t.get(el, '-') for el in st])
print(''.join(res))

# Вариант
st = input().lower()
res = map(lambda el: t.get(el, '-'), st)
print(''.join(res))


# 06
"""
Вводятся названия городов в одну строчку через пробел. 
Необходимо определить функцию map, которая бы возвращала названия городов только длиной более 5 символов. 
Вместо остальных названий - строку с дефисом ("-").
Input:  Москва Уфа Вологда Тула Владивосток Хабаровск
Output: Москва - Вологда - Владивосток Хабаровск
"""
st = input().split()
res = map(lambda x: x if len(x) > 5 else '-', st)
print(*res)

# без map()
st = input().split()
res = [el if len(el) > 5 else '-' for el in st]
print(*res)
