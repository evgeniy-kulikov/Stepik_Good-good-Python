# 9.2 Функция-генератор. Оператор yield
""""""

# обычная функция
def get_list():
    for x in [1, 2, 3, 4]:
        return x


a = get_list()
print(a)


# оператор yield
# yield превращает любую функцию в генератор
def get_list1():
    for x in [1, 2, 3, 4]:
        yield x


a1 = get_list1()
print(a1)  # <generator object get_list1 at 0x0000025AB0945890>

# вывод через next
# print(next(a1))
# print(next(a1))
# print(next(a1))
# print(next(a1))

# вывод через цикл
for el in a1:
    print(el)


# вычисление среднего арифметического для убывающего списка
def get_list2():
    for i in range(1, 10):
        a = range(i, 11)
        yield sum(a) / len(a)


a2 = get_list2()
print(list(a2))


# получение данных из файла через генератор
def find_word(file_txt, word):
    g_indx = 0
    for line in file_txt:
        indx = 0
        while indx != -1:
            indx = line.find(word, indx)
            if indx > -1:
                yield g_indx + indx
                indx += 1
        g_indx += len(line)


try:
    with open("lesson_54.txt", encoding="utf-8") as file:
        a = find_word(file, "генератор")
        print(list(a))
except FileNotFoundError:
    print("Файл не найден")
except:
    print("Ошибка при работе с файлом")


#
#  *   *   *   *   *   TASK    *   *   *   *   *
#


"""
Вводится натуральное число N. Необходимо определить функцию-генератор с именем get_sum, 
которая бы возвращала текущую сумму чисел последовательности длины N в диапазоне целых чисел [1; N]:
- для первого числа 1 сумма равна 1;
- для второго числа 2 сумма равна 1 + 2 = 3
....
- для N-го числа сумма равна 1 + 2 +...+ (N - 1) + N
Input:  5
Output: 1 3 6 10 15
"""
N = int(input())

def get_sum(num):
    sum = 0
    for el in range(1, num + 1):
        sum += el
        yield sum


# Красиво - умно )
def get_sum(num):
    for el in range(1, num + 1):
        yield el * (el + 1) // 2

# res = get_sum(N)
# for el in res:
#     print(el, end=' ')



"""
Последовательность чисел Фибоначчи, строится по правилу: каждое последующее число равно сумме двух предыдущих. 
По аналогии будем генерировать каждое последующее как сумму трех предыдущих чисел. 
При этом первые три числа равны 1 и имеем такую последовательность:
1, 1, 1, 3, 5, 9, 17, 31, 57, ...
На вход программы поступает натуральное число N (N > 5) и необходимо определить функцию-генератор, 
которая бы возвращала N первых чисел такой последовательности (включая первые три единицы).
Реализуйте эту функцию без использования коллекций (списков, кортежей, словарей и т.п.)
Input:  7
Output: 1 1 1 3 5 9 17
"""
def get_sum_new(num):
    a, b, c = 1, 1, 1
    for el in range(num):
        if el < 3:
            yield c
        else:
            summ = a + b + c
            a, b, c = b, c, summ
            yield c

n = int(input())
res = get_sum_new(n)
for el in res:
    print(el, end=' ')

# Вариант вывода на печать
print(*get_sum_new(n))


# Красиво - умно
def get_sum(N):
    a, b, c = 1, 1, 1
    for _ in range(N):
        a, b, c = b, c, a + b + c
        yield a

n = int(input())
print(*get_sum(n))


"""
https://stepik.org/lesson/567072/step/4?unit=561346
Вводится натуральное число N (N > 8). Необходимо определить функцию-генератор, 
которая бы выдавала пароль длиной N символов из случайных букв, цифр и некоторых других знаков. 
Функция-генератор должна при каждом вызове возвращать новый пароль 
из случайно выбранных символов chars длиной N
Сгенерируйте с помощью этой функции первые пять паролей и выведите их
Input:  10
Output: riGp?58WAm
        !dX3a5IDnO
        dcdbWB2d*C
        4?DSDC6Lc1
        mxLpQ@2@yM
"""
import random
from string import ascii_lowercase, ascii_uppercase

random.seed(1)  # генерация одинакового "случайного числа"

def get_pass(n):
    chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"
    while True:
        res = ''
        for el in range(n):
            indx = random.randint(0, len(chars) - 1)
            res += chars[indx]
        yield res


n = int(input())
psw = get_pass(n)
for _ in range(5):
    print(next(psw))


# Вариант
def get_pass(n):
    chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"
    while True:
        indx = random.randint(0, len(chars) - 1)
        yield ''.join([chars[indx] for _ in range(n)])

pwd = get_pass(n)
[print(next(pwd)) for _ in range(5)]


"""
https://stepik.org/lesson/567072/step/5?unit=561346
задайте функцию-генератор, 
которая бы возвращала случайно сформированные email-адреса с доменом mail.ru и длиной в N символов. 
Input:  8
Output: iKZWeqhF@mail.ru
        WCEPyYng@mail.ru
        FbyBMWXa@mail.ru
        SCrUZoLg@mail.ru
        ubbbPIay@mail.ru
"""

import random
from string import ascii_lowercase, ascii_uppercase

random.seed(1)  # генерация одинакового "случайного числа"

def get_pass(n):
    chars = ascii_lowercase + ascii_uppercase
    while True:
        res = ''
        for el in range(n):
            indx = random.randint(0, len(chars) - 1)
            res += chars[indx]
        yield res + '@mail.ru'


n = int(input())
psw = get_pass(n)
for _ in range(5):
    print(next(psw))


"""
Определите функцию-генератор, которая бы возвращала простые числа. 
(Простое число - это натуральное число, которое делится только на себя и на 1). 
Выведите с помощью этой функции первые 20 простых чисел (начиная с 2) в одну строчку через пробел.
Output: 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 
"""
def get_simple_num():
    num = 1
    while True:
        num += 1
        for el in range(2, num // 2 + 1):
            if num % el == 0:
                break
        else:
            yield num


# Вариант
def get_simple_num():
    num = 1
    while True:
        num += 1
        for el in range(2, int(num ** 0.5) + 1):
            if num % el == 0:
                break
        else:
            yield num


res = get_simple_num()

for _ in range(20):
    print(next(res), end=' ')

