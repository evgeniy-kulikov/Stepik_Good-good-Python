# 9.8 Функция isinstance для проверки типов данных
""""""

# Проверка на принадлежность объекта определенному типу данных

a = 5
isinstance(a, int)  # True
isinstance(a, float)  # False


b = True
# тип bool наследуется от типа int
isinstance(b, bool)  # True
isinstance(b, int)  # True

# строгая проверка - type
print(type(b) == bool)  # True
print(type(b) == int)  # False

# оператор 'is' соответствует оператору '=='
print(type(b) is bool)  # True
print(type(b) is int)  # False


""" Проверка соответствия нескольким типам данных """
b = True
print(type(b) in (bool, float, str))  # True

# отличия isinstance от type:
# isinstance осуществляет проверку с учетом иерархии наследования объектов
# isinstance была разработана для проверки принадлежности объекта тому или иному классу

# посчитать сумму только вещественных чисел в кортеже
data = (4.5, 8.7, True, "книга", 8, 10, -11, [True, False])

# вариант 1
s = 0
for x in data:
    if isinstance(x, float):
        s += x
print(s)  # 13.2

# вариант 2
# встроенные функции языка Python работают быстрее
s = sum(filter(lambda x: isinstance(x, float), data))
print(s)  # 13.2

# проверка на int
s = sum(filter(lambda x: type(x) is int, data))
print(s)  # 7

# множественные проверки
print(isinstance(a, (int, float)))  # True
# это аналог
print(isinstance(a, int) or isinstance(a, float))  # True


#
#  *   *   *   *   *   TASK    *   *   *   *   *
#


# 01
"""
Определите функцию с именем get_add, 
которая складывает или два числа или две строки (но не число со строкой) 
и возвращает полученный результат. Если сложение не может быть выполнено, 
то функция возвращает значение None. 
"""
def get_add(a, b):
    if type(a) in (int, float) and type(b) in (int, float):
        return a + b
    if isinstance(a, str) and isinstance(b, str):
        return a + b

# Вариант
def get_add(a, b):
    if {type(a), type(b)} in ({str}, {int}, {float}, {int, float}):
        return a + b


# 02
"""
Определите функцию с именем get_sum, 
которая принимает на входе итерируемый объект (список, строку, кортеж, словарь, множество) 
и вычисляет сумму только целых чисел, взятых из элементов итерируемого объекта. 
Вычисленная сумма возвращается функцией. Если целых чисел нет, то возвращается 0.
Input => Output:
get_sum([1,2,3, "a", True, [4, 5], "c", (4, 5)])  => 6
get_sum({5, 6, 7, '8', 5, '4'})  => 18
get_sum((10, "f", '33', True, 12))  => 22
get_sum(['1', True, False, (1, 23)])  => 0
"""
def get_sum(data):
    return sum(filter(lambda el: type(el) is int, data))


# 03
"""
Определите функцию с именем get_even_sum, 
которая принимает на входе итерируемый объект (список, строку, кортеж, словарь, множество) 
и вычисляет сумму только целых четных чисел, взятых из элементов итерируемого объекта. 
Результат возвращается функцией. 
Если целых чисел нет, то возвращается 0.
"""
def get_even_sum(data):
    return sum(filter(lambda el: type(el) is int and el % 2 == 0, data))


# 04
"""
Определите функцию с именем get_list_dig, 
которая возвращает список только из числовых значений переданной ей коллекции (список или кортеж).
"""
def get_list_dig(lst):
    return [el for el in lst if type(el) in (int, float)]

# Вариант
def get_list_dig(lst):
    return list(filter(lambda el: type(el) in (int, float), lst))

# Вариант
def get_list_dig(lst):
    return [*filter(lambda el: type(el) in (int, float), lst)]

# lst = ([5], 6, 7.2, '8', 5, '4', True)
# print(get_list_dig(lst))  # [6, 7.2, 5]
