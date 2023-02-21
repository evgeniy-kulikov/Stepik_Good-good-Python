# 5.9 Вложенные циклы и вложенные генераторы списков
""""""


"""
Простой вариант:
[<способ формирования значения> for <переменная> in <итерируемый объект> if <условие (опционально)>]


Вариант с дополнительными вложениями:
[<способ формирования значения> for <переменная_1> in <итерируемый объект> if <условие (опционально)>  # 1 внешний цикл
                                for <переменная_2> in <итерируемый объект> if <условие (опционально)>  # 2 внутренний цикл для 1
                                for <переменная_3> in <итерируемый объект> if <условие (опционально)>]  # 3 внутренний цикл для 2


[<оператор> for <счетчик> in <итерируемый объект> if <условие (опционально)>]
[<оператор> for <счетчик> in <итерируемый объект>]

"""

a = [(i, k) for i in range(3) for k in range(4)]
print(a)
# [(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (2, 3)]

# аналогичная запись
a = [(i, k)
     for i in range(3)
     for k in range(4)]
print(a)
# [(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (2, 3)]

a = [f"{i} * {k} = {i * k}"
     for i in range(1, 3)
     for k in range(1, 4)]
print(a)
# ['1 * 1 = 1', '1 * 2 = 2', '1 * 3 = 3', '2 * 1 = 2', '2 * 2 = 4', '2 * 3 = 6']

# преобразование 2-х мерного списка в одномерный
matrix = [[0, 1, 2, 3],
          [10, 11, 12, 13],
          [20, 21, 22, 23]]

a = [x for row in matrix for x in row]
# аналогичная запись
b = [x
     for row in matrix
     for x in row
     ]
print(a)
# [0, 1, 2, 3, 10, 11, 12, 13, 20, 21, 22, 23]


""" *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  """
#              Вложенные генераторы списков
""" *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  """

# [<оператор> for <счетчик> in <итерируемый объект> <условие (опционально)>]

# [[генератор списка] for <счетчик> in <итерируемый объект> <условие (опционально)>]

# [[генератор списка] for <счетчик> in <итерируемый объект>]
s = [[(i + 1) * 2] for i in range(4)]
# [[2], [4], [6], [8]]

# [<переменная> for <счетчик> in [генератор списка]]
s = [k * 2 for k in [i + 1 for i in range(4)]]
# [2, 4, 6, 8]



m, l = 3, 4
matrix = [[i for i in range(m)] for k in range(l)]
#     ВЛОЖЕННЫЙ генератор списка___ВНЕШНИЙ цикл
#
print(matrix)
# [[0, 1, 2], [0, 1, 2], [0, 1, 2], [0, 1, 2]]

c = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
s = [[i ** 2 for i in row] for row in c]
# Вложенный генератор списка__внешний генератор
print(s)
# [[1, 4, 9], [16, 25, 36], [49, 64, 81]]

d = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
d = [[row[i] for row in d] for i in range(len(d[0]))]
print(d)
# [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

# [<оператор> for <счетчик> in <итерируемый объект>]
# [<оператор> for <переменная> in [генератор списка]
e = [i ** 2 for i in [k + 1 for k in range(5)]]
print(e)
# [1, 4, 9, 16, 25]

"""  Транспонирование матрицы  """
s = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
d = [[row[i] for row in s] for i in range(len(s[0]))]
# >>> [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]


""" Task """

"""
Вводится двумерный список в виде таблицы целых чисел (см. пример ниже). 
С помощью list comprehension преобразовать двумерный список в одномерный так, 
чтобы значения элементов шли в обратном порядке. 
Результат отобразить в виде строки из чисел, записанных через пробел.
P. S. Для считывания списка целиком в программе уже записаны начальные строчки.

Input:  1 2 3 4
        5 6 7 8
        9 8 7 6
        5 4 3 2
Output: 2 3 4 5 6 7 8 9 8 7 6 5 4 3 2 1
"""
import sys
# считывание списка из входного потока
s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]
# lst_in = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6], [5, 4, 3, 2]]
lst_out = [x[::-1] for row in lst_in for x in row[::-1]]
print(lst_in)
# 2 3 4 5 6 7 8 9 8 7 6 5 4 3 2 1

# Вариант
s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]
lst_out = [x for row in lst_in for x in row]
print(*lst_out[::-1])
# 2 3 4 5 6 7 8 9 8 7 6 5 4 3 2 1


"""
Вводится список целых чисел в строку через пробел. 
С помощью list comprehension сформировать из них двумерный список lst размером N x N (квадратную таблицу чисел). 
Гарантируется, что из набора введенных чисел можно сформировать квадратную матрицу (таблицу). 

Input:  1 2 3 4 5 6 7 8 9
Output: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
"""
from math import sqrt
s = list(map(int, input().split()))
# s = [1, 2, 3, 4, 5, 6, 7, 8, 9]
row_len = int(sqrt(len(s)))
c = iter(s)
s_out = [[next(c) for k in range(row_len)] for i in range(row_len)]
print(s_out)

# Переделанное мной решение
s = list(map(int, input().split()))
row_len = int((len(s)) ** 0.5)
s_out = [s[k * row_len:k * row_len + row_len] for k in range(row_len)]
print(s_out)

# Вариант
s = list(map(int, input().split()))
# s = [1, 2, 3, 4, 5, 6, 7, 8, 9]
row_len = int(len(s) ** 0.5)
res = [[int(s[k + i * row_len]) for k in range(row_len)] for i in range(row_len)]
print(res)

"""
Необходимо преобразовать писок "t" в двумерный (вложенный) список "lst", 
где каждая строка представляется списком из слов (слова разделяются пробелом), 
но сохранять слова только длиной более трех символов. 
Input:  
t = ["– Скажи-ка, дядя, ведь не даром",
    "Я Python выучил с каналом",
    "Балакирев что раздавал?",
    "Ведь были ж заданья боевые,",
    "Да, говорят, еще какие!",
    "Недаром помнит вся Россия",
    "Как мы рубили их тогда!"]
Output: 
lst = [['Скажи-ка,', 'дядя,', 'ведь', 'даром'], 
      ['Python', 'выучил', 'каналом'], 
      ['Балакирев', 'раздавал?'], 
      ['Ведь', 'были', 'заданья', 'боевые,'], 
      ['говорят,', 'какие!'], 
      ['Недаром', 'помнит', 'Россия'], 
      ['рубили', 'тогда!']]
"""
t = ["– Скажи-ка, дядя, ведь не даром",
    "Я Python выучил с каналом",
    "Балакирев что раздавал?",
    "Ведь были ж заданья боевые,",
    "Да, говорят, еще какие!",
    "Недаром помнит вся Россия",
    "Как мы рубили их тогда!"]
lst = [[i for i in row.split() if len(i) > 3] for row in t]
print(lst)

#  Для большего понимания
t = [[i for i in row.split()] for row in t]
# [['–', 'Скажи-ка,', 'дядя,', 'ведь', 'не', 'даром'], ['Я', 'Python', 'выучил', 'с', 'каналом'], .....]
lst = [[i for i in row if len(i) > 3] for row in t]
# [['Скажи-ка,', 'дядя,', 'ведь', 'даром'], ['Python', 'выучил', 'каналом'],  .....]



"""
Транспонированием прямоугольной матрицы с помощью list comprehension. 
На вход поступает таблица целых чисел, на выходе нужно отобразить эту же таблицу 
в транспонированном виде (строки заменяются на столбцы), 
используя команду:
for row in A:
    print(*row)
где A - транспонированный двумерный список.
P. S. Для считывания списка целиком в программе уже записаны начальные строчки.
Input:  1 2 3
        4 5 6
        7 8 9
        5 4 3
Output: 1 4 7 5
        2 5 8 4
        3 6 9 3
"""
import sys
# считывание списка из входного потока
s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]
# [[1, 2, 3], [4, 5, 6], [7, 8, 9], [5, 4, 3]]
lst_out = [[row[i] for row in lst_in] for i in range(len(lst_in[0]))]
# [[1, 4, 7, 5], [2, 5, 8, 4], [3, 6, 9, 3]]
for row in lst_out:  # построчный вывод каждого вложенного списка
    print(*row)
# 1 4 7 5
# 2 5 8 4
# 3 6 9 3
