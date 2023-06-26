# 9.9 Функции all и any
""""""

# если ВСЕ элементы списка принимаются значение True, функция all возвращает значение True
a = [True, True, True, True]
b = all(a)
print(b)  # True

a[2] = False  # a = [True, True, False, True]
print(all(a))  # False

c = [0, 1, 2.5, "", "python", [], [1, 2], {}]  # [0, '', [], {}] - дают False
print(all(c))  # False

c = [1, 2.5, "python", [1, 2]]
print(all(c))  # True

# все элементы перед оценкой функцией all превращаются в тип bool
# все пустое является ложью
print(bool(0))  # False
print(bool(''))  # False
print(bool([]))  # False
print(bool({}))  # False

# не пустое - True
print(bool(1))  # True
print(bool([1, 2]))  # True
print(bool([False]))  # True

d = [1, 2.5, "python", [1], [1, 2]]
print(all(d))  # True

# имитация работы функции all
# Если хоть один элемент bool(el) будет False, то all_res станет False
all_res = True
for el in d:
    all_res = all_res and bool(el)
print(all_res)


""" Функция any """
# функция any - возвращает True, если хотя бы одно из значений True
# возвращает False только, когда все - False
a = [True, 1, False, '']
print(any(a))  # True

a = [False, 0, '', []]
print(any(a))  # False


# имитация работы функции any
d = [True, 0, False, '']
# d = [[], 0, False, '']

any_res = False
for el in d:
    any_res = any_res or bool(el)
print(any_res)  # True
# print(any_res)  # False


""" Пример применения функции all - крестики-нолики:"""

P = ['x', 'x', 'o', 'o', 'x', 'o', 'x', 'x', 'x']
# P = ['x', 'x', 'o',
#      'o', 'x', 'o',
#      'x', 'x', 'x']

print(P)
row_1 = all(map(lambda x: x == 'x', P[:3]))
row_2 = all(map(lambda x: x == 'x', P[3:6]))
row_3 = all(map(lambda x: x == 'x', P[6:]))
print(row_1, row_2, row_3)  # False False True


# или
def true_x(a):
    return a == 'x'


row_1 = all(map(true_x, P[:3]))
row_2 = all(map(true_x, P[3:6]))
row_3 = all(map(true_x, P[6:]))
print(row_1, row_2, row_3)

# Проверка по столбцам
col_1 = all(map(true_x, P[::3]))
col_2 = all(map(true_x, P[1::3]))
col_3 = all(map(true_x, P[2::3]))
print(col_1, col_2, col_3)  # False True False

diag_1 = all(map(true_x, P[::4]))
diag_2 = all(map(true_x, P[2::2]))
print(diag_1, diag_2)


""" Пример применения функции any - Сапер:"""
N = 10
P = [0] * (N * N)  # поле

print(P)

P[4] = '*'  # мина

loss = any(map(lambda x: x == '*', P))
print(loss)  # True


#
#  *   *   *   *   *   TASK    *   *   *   *   *
#


# 01
"""
Вводится строка целых чисел через пробел. 
Необходимо определить, являются ли все эти числа четными. 
Вывести True, если это так и False - в противном случае.
Input:  2 4 6 8 22 56
Output: True
"""
# ls = ['2', '4', '6', '8', '22', '56']
ls = input().split()
print(all(map(lambda el: int(el) % 2 == 0, ls)))

# Вариант
ls = input().split()
print(not any(int(el) % 2 for el in ls))  # not any([0, 0, 0, 0, 0, 0])  -> not False  -> True


# 02
"""
Вводится строка вещественных чисел через пробел. 
Необходимо определить, есть ли среди них хотя бы одно отрицательное. 
Вывести True, если это так и False - в противном случае.
Input:  8.2 -11.0 20 3.4 -1.2
Output: True
"""
ls = input().split()
print(any(map(lambda el: float(el) < 0, ls)))

# Вариант
ls = input().split()
print(any(float(el) < 0 for el in ls))  # [False, True, False, False, True]


# 03
"""
Объявить функцию с именем is_string, 
на вход которой поступает коллекция (список, кортеж, множество). 
Она должна возвращать True, если все элементы коллекции строки 
и False - в противном случае.
"""
def is_string(data) -> bool:
    all_res = True
    for el in data:
        all_res = type(el) == str and all_res
    return all_res


"""
Объявить функцию с именем is_string, 
на вход которой поступает коллекция (список, кортеж, множество). 
Она должна возвращать True, если все элементы коллекции строки 
и False - в противном случае.
"""
def is_string(data) -> bool:
    if data:  # Проверка на пустую коллекцию
        all_res = True
        for el in data:
            all_res = type(el) == str and all_res
        return all_res
    return False

# Вариант
def is_string(data) -> bool:
    if data:  # Проверка на пустую коллекцию
        return all(map(lambda el: type(el) == str, data))
    return False

# Вариант
def is_string(data) -> bool:
    if data:
        return all(isinstance(el, str) for el in data)
    return False


# 04
"""
Вводятся оценки студента в одну строчку через пробел. 
Необходимо определить, имеется ли в этом списке хотя бы одна оценка ниже тройки. 
Если это так, то вывести на экран строку "отчислен", иначе - "учится".
Input:  3 3 3 2 3 3
Output: отчислен
"""
# ls = ['3', '3', '3', '2', '3', '3']
def get_grade(data) -> str:
    if all(map(lambda el: int(el) > 2, data)):
        return 'учится'
    return 'отчислен'

ls = input().split()
print(get_grade(ls))


# Вариант
lst = map(int, input().split())
if any(map(lambda el: el < 3, lst)):
    print('отчислен')
else:
    print('учится')

# Короче
lst = map(int, input().split())
print('отчислен' if any(el < 3 for el in lst) else 'учится')


# 05
"""
https://stepik.org/lesson/567079/step/6?unit=561353
Вводится текущее игровое поле для игры "Крестики-нолики" в виде следующей таблицы:
# x o
x # x
o o #
Здесь # - свободная клетка. 
Нужно объявить функцию с именем is_free, 
на вход которой поступает игровое поле в виде двумерного (вложенного) списка. 
Данная функция должна возвращать True, 
если есть хотя бы одна свободная клетка и False - в противном случае.
Input:  # x o
        x # x
        o o #
Output: True
loss = any(map(lambda x: x == '*', P))
"""
lst = ['# x o', 'x # x', 'o o #']

def is_free(lst):
    for row in lst:
        if any(map(lambda el: el == '#', row)):
            return True
    return False

print(is_free(lst))

# Короче
def is_free(lst):
    return any(map(lambda el: '#' in el, lst))


# Еще короче
def is_free(lst):
    return any('#' in el for el in lst)


