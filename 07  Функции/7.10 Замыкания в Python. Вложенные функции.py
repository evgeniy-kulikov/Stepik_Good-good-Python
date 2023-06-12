#  7.10 Замыкания в Python. Вложенные функции
""""""

def say_name(name):
    def say_goodbye():
        print(f'goodbye {name}')
    return say_goodbye

a = say_name('1')
a()  # goodbye 1

b = say_name('2')
b()  # goodbye 2



def counter(start=0):
    def step():
        nonlocal start
        start += 1
        return start

    return step

cnt1 = counter(10)
cnt2 = counter()

print(cnt1(), cnt2())  # 11 1
print(cnt1(), cnt2())  # 12 2
print(cnt1(), cnt2())  # 13 3


def strip_string(strip_chars=' '):
    def do_strip(string):
        return string.strip(strip_chars)

    return do_strip


str_1 = strip_string()
str_2 = strip_string(' .,:;!?&*-')
print(str_1('  *;?&строка.,! '))  # *;?&строка.,!
print(str_2('  *;?&строка.,! '))  # строка


#  *   *   *   *   *   TASK    *   *   *   *   *


"""
Используя замыкания функций, определите вложенную функцию, 
которая бы увеличивала значение переданного параметра на 5 и возвращала бы вычисленный результат. 
При этом внешняя функция должна иметь следующую сигнатуру:
def counter_add(): ...

Вызовите функцию counter_add и результат ее работы присвойте переменной с именем cnt. 
Вызовите внутреннюю функцию через переменную cnt со значением k, введенным с клавиатуры:
k = int(input())
Input:  7
Output: 12
"""

# Ожидаемое решение
k = int(input())

def counter_add():
    def counter_in(num):
        num += 5
        return num
    return counter_in

cnt = counter_add()
print(cnt(k))


"""
Используя замыкания функций, объявите внутреннюю функцию, 
которая увеличивает значение своего аргумента на некоторую величину n - параметр внешней функции с сигнатурой:
def counter_add(n):
Вызовите внешнюю функцию counter_add со значением аргумента 2 и результат присвойте переменной cnt. 
Вызовите внутреннюю функцию через переменную cnt со значением k, введенным с клавиатуры:
k = int(input())

Input:  5
Output: 7
"""
k = int(input())

def counter_add(n):
    def inner_add(num):
        return num + n
    return inner_add


cnt = counter_add(2)
print(cnt(k))


"""
Используя замыкания функций, объявите внутреннюю функцию, которая заключает в тег h1 строку s 
(s - строка, параметр внутренней функции). 
Далее, на вход программы поступает строка и ее нужно поместить в тег h1 с помощью реализованного замыкания. 
Результат выведите на экран.
P. S. Пример добавления тега h1 к строке "Python": <h1>Python</h1>
Input:  Balakirev
Output: <h1>Balakirev</h1>
"""

def get_str():
    def make_tag(s):
        return f'<h1>{s}</h1>'
    return make_tag

st = input()
res = get_str()
print(res(st))


"""
Используя замыкания функций, объявите внутреннюю функцию, которая заключает строку s 
(s - строка, параметр внутренней функции) в произвольный тег, 
содержащийся в переменной tag - параметре внешней функции. 
Далее, на вход программы поступают две строки: первая с тегом, вторая с некоторым содержимым. 
Вторую строку нужно поместить в тег из первой строки с помощью реализованного замыкания.
P. S. Пример добавления тега h1 к строке "Python": <h1>Python</h1>
Input:  div
        Сергей Балакирев
Output: <div>Сергей Балакирев</div>
"""

def get_str(t):
    def make_tag(s):
        return f'<{t}>{s}</{t}>'
    return make_tag


tg = input()
st = input()

res = get_str(tg)
print(res(st))


"""
Используя замыкания функций, объявите внутреннюю функцию, 
которая преобразует строку из списка целых чисел, записанных через пробел, либо в список, либо в кортеж. 
Тип коллекции определяется параметром tp внешней функции. Если tp = 'list', то используется список, 
иначе (при другом значении) - кортеж.
Далее, на вход программы поступают две строки: 
первая - это значение для параметра tp; 
вторая - список целых чисел, записанных через пробел. 
С помощью реализованного замыкания преобразовать эти данные в соответствующую коллекцию. 

Input:  list
        -5 6 8 11 0 111 -456 3
Output: [-5, 6, 8, 11, 0, 111, -456, 3]
"""

def get_iter(tp):
    def make_iter(ls):
        if tp == 'list':
            return list(ls)
        elif tp == 'tuple':
            return tuple(ls)
    return make_iter


name_iter = input()
mum_list = map(int, input().split())

res = get_iter(name_iter)
print(res(mum_list))

