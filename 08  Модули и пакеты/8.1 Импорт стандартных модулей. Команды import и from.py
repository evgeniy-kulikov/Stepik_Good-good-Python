# 8.1 Импорт стандартных модулей. Команды import и from
""""""

import math
import time
import pprint
# по стандарту PEP-8 каждый модуль импортируется на отдельной строчке в начале программы

# Вывод одной строкой
print(locals())
"""
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x0000021F1AC26D00>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'D:\\__PythonProject\\Good, good Python [S. Balakirev]\\test_02.py', '__cached__': None, 'pprint': <module 'pprint' from 'C:\\Python39\\lib\\pprint.py'>}

"""

# Построчный вывод
pprint.pprint(locals())
"""
{'__annotations__': {},
 '__builtins__': <module 'builtins' (built-in)>,
 '__cached__': None,
 '__doc__': None,
 '__file__': 'D:\\__PythonProject\\Good, good Python [S. '
             'Balakirev]\\test_02.py',
 '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x0000020E49C36D00>,
 '__name__': '__main__',
 '__package__': None,
 '__spec__': None,
 'pprint': <module 'pprint' from 'C:\\Python39\\lib\\pprint.py'>}

"""

a = math.ceil(1.8)
print(a)  # 2
print(math.pi)  # 3.141592653589793


# Замена модуля на локальную переменную
pprint.pprint(locals())
"""
...
 'math': <module 'math' (built-in)>,
...
"""

# Переопределяем модуль math
math = "математика"
pprint.pprint(locals())
"""
...
 'math': 'математика',
...
"""
# Дальше будет ошибка !!!
# a = math.ceil(1.8)
# print(a)  # AttributeError: 'str' object has no attribute 'ceil'
# print(math.pi)  # AttributeError: 'str' object has no attribute 'pi'


# Импорт модуля под псевдонимом

import math as mt

pprint.pprint(locals())
a = mt.ceil(1.8)
print(a)
print(mt.pi)


# Импорт отдельных функций

from math import ceil, pi

pprint.pprint(locals())
a = ceil(1.8)
print(a)
print(pi)


def ceil(x):
    print("\n", "# наша функция ceil", "\n")
    return x


a = ceil(1.8)
pprint.pprint(locals())
print(a)
print(pi)


# Импорт отдельных функций под псевдонимом

from math import ceil as cl, pi

pprint.pprint(locals())
a = cl(1.8)
print(a)
print(pi)

# импорт всего содержимого библиотеке (крайне не рекомендуется)
# from math import *


#  *   *   *   *   *   TASK    *   *   *   *   *

# Task 01
from math import ceil
num = float(input())
print(ceil(num))


# Task 02
from math import floor
num = float(input())
print(floor(num))


# Task 03
from math import factorial as fact

def factorial(n):
    p = 1
    for i in range(2, n+1):
        p *= i

    print("my factorial")
    return p


# Task 04
from random import seed, randint
#  функция seed используется для генерации одних и тех же случайных чисел
seed(1)
print(randint(10, 50))


# Task 05
from random import seed, random as rnd
#  функция seed используется для генерации одних и тех же случайных чисел
seed(10)
print(round(rnd(), 2))
