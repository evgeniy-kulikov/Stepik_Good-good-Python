# 7.7 Рекурсивные функции
""""""

def recursive(val):
    print(val)
    if val < 3:
        recursive(val + 1)
"""
recursive(1)
1
2
3
"""

print(recursive(1))
def recursive(val):
    print(val)
    if val < 3:
        recursive(val + 1)
    print(val)
"""
recursive(1)
1
2
3
3
2
1
"""
def recursive(val):
    # print(val)
    if val < 3:
        recursive(val + 1)
    print(val)
"""
recursive(1)
3
2
1
"""


"""
Факториал натурального числа
n! = 1 * 2 * 3 * 4 * ... * n
n! = (n - 1)! * n
(n - 1)! = (n - 2)! * (n - 1)
2! = 1 * 2
1! = 1

Определяем функцию для определения факториала числа "n"
factorial(n) = n!
factorial(n) = factorial(n - 1) * n
"""

def fact(n):
    if n == 0:
        return 1
    else:
        return fact(n - 1) * n

print(fact(5))  # 6 * 5 * 4 * 3 * 2 * 1 = 120


"""
Вводится целое положительное число N. 
Необходимо написать рекурсивную функцию с именем get_rec_N, 
которая отображает на экране последовательность целых чисел от 1 до N (включительно). 
Каждое число выводится с новой строки. 
В качестве параметра функция get_rec_N должна принимать одно числовое значение. 
То есть, иметь только один параметр. Начальный вызов функции будет выглядеть так
get_rec_N(N)
Input:  5
Output: 1
        2
        3
        4
        5
"""
n = int(input())

def get_rec_N(num):
    if num > 1:
        get_rec_N(num - 1)
    print(num)

# get_rec_N(n)



"""
Вводится список целых чисел в одну строчку через пробел. 
Необходимо вычислить сумму этих введенных значений, 
используя рекурсивную функцию (для перебора элементов списка) с именем get_rec_sum. 
Функция должна возвращать значение суммы.
Вызовите эту функцию и выведите вычисленное значение суммы на экран.
Input:  8 11 -5 4 3
Output: 21
"""

lst = list(map(int, input().split()))


def get_rec_sum(a):
    if not a:  # если список пуст
        return 0
    else:
        return a[0] + get_rec_sum(a[1:])

print(get_rec_sum(lst))


# Короче
def get_rec_sum(a):
    return a[0] + get_rec_sum(a[1:]) if a else 0

print(get_rec_sum(lst))


"""
Вводится натуральное число N. 
Необходимо с помощью рекурсивной функции fib_rec(N, f=[]) 
(здесь N - общее количество чисел Фибоначчи; f - начальный список этих чисел) 
сформировать последовательность чисел Фибоначчи по правилу: 
первые два числа равны 1 и 1, а каждое следующе значение равно сумме двух предыдущих. 
Пример такой последовательности для первых 7 чисел: 1, 1, 2, 3, 5, 8, 13, ...
Функция должна возвращать список сформированной последовательности длиной N.
Input:  7
Output: 1 1 2 3 5 8 13
"""


N = int(input())
def fib_rec(N, f=[]):
    if N == 2:
        f.extend((1, 1))
    else:
        fib_rec(N - 1, f)
        f.append(f[-1] + f[-2])
    return f

print(fib_rec(N))


# Не рекурсия. Это цикл (((
N = int(input())
def fib_rec(N, f=[1, 1]):
    if len(f) < N:
        f += [f[-1] + f[-2]]
        fib_rec(N, f)
    return f

print(fib_rec(N))



"""
Вводится целое неотрицательное число n. 
Необходимо с помощью рекурсивной функции fact_rec вычислить факториал числа n. 
Напомню, что факториал числа, равен: n! = 1 * 2 * 3 *...* n. Функция должна возвращать вычисленное значение.
Input:  6
Output: 720
"""
n = int(input())
def fact_rec(n):
    if n == 0:
        return 1
    else:
        return fact_rec(n - 1) * n


print(fact_rec(n))


"""
Имеется следующий многомерный список:
d = [1, 2, [True, False], ["Москва", "Уфа", [100, 101], ['True', [-2, -1]]], 7.89]
С помощью рекурсивной функции get_line_list
 создать на его основе одномерный список из значений элементов списка d. 
Функция должна возвращать новый созданный одномерный список. 
Input:  -
Output: -
"""
d = [1, 2, [True, False], ["Москва", "Уфа", [100, 101], ['True', [-2, -1]]], 7.89]

def get_line_list(d, a=None):
    if a is None:
        a = []
    for el in d:
        if isinstance(el, list):
        # if type(el) == list:
            get_line_list(el, a)
        else:
            a.append(el)
    return a

print(get_line_list(d))

# Вариант
def get_line_list(d, a=[]):
    for el in d:
        # if isinstance(el, list):
        if type(el) == list:
            get_line_list(el, a)
        else:
            a.append(el)
    return a

print(get_line_list(d))


"""
https://stepik.org/lesson/567058/step/8?unit=561332
Лягушка прыгает вперед и может скакнуть либо на одно деление, либо сразу на два. 
Определить количество вариантов маршрутов, которыми лягушка может достичь риски под номером N
Input:  7
Output: 21
"""
n = int(input())

def get_path(n):
    if n < 2:
        return 1
    elif n == 2:
        return 2
    else:
        return get_path(n-1) + get_path(n-2)

print(get_path(n))



"""
Метод слияния списков
Сортировка массива методом слияния
Вычислительная сложность N*log(2)N = 7 * log(2)7 < 21
Простейшие алгоритмы имеют сложность O(N^2) = 7^2 = 49

Вспомогательная функция для разделения списка на две половины, если его длина больше 1
# def div_lst(lst):
#     if len(lst) > 1:
#         dl = round(len(lst)/2)
#         return lst[:dl], lst[dl:]
"""



"""
Вводится список из целых чисел в одну строчку через пробел. 
Необходимо выполнить его сортировку по возрастанию с помощью алгоритма сортировки слиянием. 
Функция должна возвращать новый отсортированный список.
Вызовите результирующую функцию сортировки для введенного списка и 
отобразите результат на экран в виде последовательности чисел, записанных через пробел.
Input:  8 11 -6 3 0 1 1
Output: -6 0 1 1 3 8 11
"""
lst_in = list(map(int, input().split()))

def merge_lst(lst_1, lst_2):
    """Сортировка 2-х списков методом слияния"""
    lst = []
    i = k = 0
    while i < len(lst_1):
        while k < len(lst_2) and lst_2[k] < lst_1[i]:
            lst.append(lst_2[k])
            k += 1
        lst.append(lst_1[i])
        i += 1
    if k < len(lst_2):
        lst += lst_2[k:]
    return lst


def sort_mrg(lst):
    """Делим списки пополам"""
    if len(lst) > 1:
        # half = int(len(lst)/2)
        half = round(len(lst)/2)
        return merge_lst(sort_mrg(lst[:half]), sort_mrg(lst[half:]))
    else:
        return lst


print(*sort_mrg(lst_in))

