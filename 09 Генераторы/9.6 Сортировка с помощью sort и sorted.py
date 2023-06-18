#  9.6 Сортировка с помощью sort и sorted
""""""

""""""
# Функция sort()

# Только для списка. Исходный список при этом изменяется.

a = [4, 3, -10, 1, 7, 12.5]
a.sort()  #[-10, 1, 3, 4, 7, 12.5]


# метод sort ничего не возвращает
ls = a.sort()
print(ls)  # None


# метод sort только для объектов одного типа
b = [4, 3, -10, 1, 7, 12.5, "abc"]
# a.sort()  # метод sort вернет ошибку

a = [True, False, True]
a.sort()  # [False, True, True]


# Сортировка по убыванию
a = [4, 3, -10, 1, 7, 12.5]
a.sort(reverse=True)  # [12.5, 7, 4, 3, 1, -10]


""""""
# Функция sorted

a = [4, 3, -10, 1, 7, 12.5]
c = sorted(a)  # [-10, 1, 3, 4, 7, 12.5]
d = sorted(a, reverse=True)  # [12.5, 7, 4, 3, 1, -10]
print(a)  # [4, 3, -10, 1, 7, 12.5]


# Сортировка кортежей
r = ("Волга", "Лена", "Дон", "Енисей")
s = sorted(r)  # ['Волга', 'Дон', 'Енисей', 'Лена']

# сортировка строки
s = sorted("python")  # ['h', 'n', 'o', 'p', 't', 'y']


# сортировка словарей
d = {"river": "река", "house": "дом", "tree": "дерево", "road": "дорога"}

# по умолчанию - сортировка ключей
k = sorted(d)  # ['house', 'river', 'road', 'tree']
k = sorted(d, reverse=True)  # ['tree', 'road', 'river', 'house']

# сортировка значений
v = sorted(d.values())  # ['дерево', 'дом', 'дорога', 'река']

# сортировка пар ключ-значение (по умолчанию - сортируются ключи)
item = sorted(d.items())
# [('house', 'дом'), ('river', 'река'), ('road', 'дорога'), ('tree', 'дерево')]


item = sorted(d.items(), reverse=True)
# [('tree', 'дерево'), ('road', 'дорога'), ('river', 'река'), ('house', 'дом')]


#
#  *   *   *   *   *   TASK    *   *   *   *   *
#


# 01
"""
На вход поступает список целых чисел, записанных в одну строчку через пробел. 
Преобразуйте сначала эту строку в список из целых чисел, а затем список в кортеж из целых чисел. 
То есть, в программе будет две разные коллекции: список и кортеж. 
Отсортируйте по возрастанию значений эти коллекции методом sort, если это возможно, 
а иначе - примените функцию sorted.
Input:  -2 -1 8 11 4 5 
Output: True
"""
s = input()  # '-2 -1 8 11 4 5'

lst = list(map(int, s.split()))  # [-2, -1, 8, 11, 4, 5]
lst.sort()  # [-2, -1, 4, 5, 8, 11]

tp_lst = tuple(map(int, s.split()))  # (-2, -1, 8, 11, 4, 5)
tp_lst = tuple(sorted(tp_lst))  # (-2, -1, 4, 5, 8, 11)


# 02
"""
На вход функции с именем get_sort поступает словарь, например, такой:
d = {'cat': 'кот', 'horse': 'лошадь', 'tree': 'дерево', 'dog': 'собака', 'book': 'книга'}
Необходимо отсортировать словарь d по убыванию ключей (лексикографическая сортировка строк) 
и возвратить список из соответствующих значений ключей словаря. 
Например, для указанного словаря d, результатом должен быть список:
['дерево', 'лошадь', 'собака', 'кот', 'книга']
"""
def get_sort(d):
    dic = sorted(d.items(), reverse=True)
    res = [el[1] for el in dic]
    return res

# d = {'cat': 'кот', 'horse': 'лошадь', 'tree': 'дерево', 'dog': 'собака', 'book': 'книга'}
# print(get_sort(d))

# Вариант
def get_sort(d):
    return [d[key] for key in sorted(d, reverse=True)]


# 03
"""
На вход программы поступает список целых чисел, записанных в одну строчку через пробел. 
Необходимо выбрать из них четыре наибольших уникальных значения. 
Input:  10 5 4 -3 2 0 5 10 3
Output: 10 5 4 3
"""
st = set(map(int, input().split()))
ls = sorted(list(st), reverse=True)[:4]
print(*ls)


# 04
"""
На вход программы поступают два списка целых чисел (каждый в отдельной строке), 
записанных в одну строчку через пробел. Длины списков могут быть разными. 
Необходимо первый список отсортировать по возрастанию, а второй - по убыванию. 
Полученные пары из обоих списков сложить друг с другом и получить новый список чисел.
Input:  7 6 4 2 6 7 9 10 4
        -4 5 10 4 5 65
Output: 67 14 9 11 10 3
"""
ls_1 = sorted(list(map(int, input().split())))
ls_2 = sorted(list(map(int, input().split())), reverse=True)
res = [a + b for a, b in zip(ls_1, ls_2)]
print(*res)

# Короче
print(*map(sum, zip(ls_1, ls_2)))


# 05
"""
На вход программы поступает список товаров в формате:
название_1:цена_1
...
название_N:цена_N
Необходимо преобразовать этот список в словарь, 
ключами которого выступают цены (целые числа), 
а значениями - соответствующие названия товаров. 
Необходимо написать функцию, которая бы принимала на входе словарь
и возвращала список из наименований трех наиболее дешевых товаров.
Вызовите эту функцию и отобразите на экране полученный список 
в порядке возрастания цены в одну строчку через пробел.
Input:  смартфон:120000
        яблоко:2
        сумка:560
        брюки:2500
        линейка:10
        бумага:500
Output: яблоко линейка бумага
"""
# lst_in = ['смартфон:120000', 'яблоко:2', 'сумка:560', 'брюки:2500', 'линейка:10', 'бумага:500']
import sys
# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

ls_2d = [el.split(':') for el in lst_in]
d_in = {int(el[1]): el[0] for el in ls_2d}

def get_goods(d: dict) -> list:
    ls_key = sorted(d)
    ls_val = [d.get(el) for el in ls_key][:3]
    return ls_val

res = get_goods(d_in)
print(*res)


# Короче
def get_goods(d):
    ls_val = dict(sorted(d.items())).values()
    return list(ls_val)[:3]


d_in = {int(key): val for val, key in [x.split(':') for x in lst_in]}
print(*get_goods(d_in))
