# 6.1 Введение в словари
""""""

"""
Словари в Python - неупорядоченные коллекции произвольных объектов с доступом по ключу.

Чтобы работать со словарём, его нужно создать:
d = {}
d = {'dict': 1, 'dictionary': 2}
d = dict([[1, 'one'], [2, 'two'], ['3', 'three']])
d = dict(short='dict', long='dictionary')
# {'short': 'dict', 'long': 'dictionary'}

1. Пустой словарь: {} или dict()
2. Ключ - значение: в {} это : , а в dict() это =
3. Ключ в {} не может быть строкой без кавычек!
4. Ключ в dict() не может быть строкой в кавычках. Тут же правило называния ключа такое же как у переменной (не начинать с цифры)


d = dict.fromkeys(['a', 'b'])
# {'a': None, 'b': None}

d = dict.fromkeys(['a', 'b'], 100)
# {'a': 100, 'b': 100}

d = dict.fromkeys(['a', 'b'], [100, 200])
# {'a': [100, 200], 'b': [100, 200]}

d = {a: a ** 2 for a in range(7)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}
"""

"""
Добавление записей в словарь и извлечение значения ключей:
d = {1: 2, 2: 4, 3: 9}
d[1]
# 2
d[4] = "four"
# {1: 2, 2: 4, 3: 9, 4: "four"}
"""

"""
Методы словарей
dict.clear() - очищает словарь.

dict.copy() - возвращает копию словаря.

classmethod dict.fromkeys(seq[, value]) - создает словарь с ключами из seq и значением value (по умолчанию None).

dict.get(key[, default]) - возвращает значение ключа, но если его нет, не бросает исключение, а возвращает default (по умолчанию None).

dict.items() - возвращает пары (ключ, значение).

dict.keys() - возвращает ключи в словаре.

dict.pop(key[, default]) - удаляет ключ и возвращает значение. Если ключа нет, возвращает default (по умолчанию бросает исключение).

dict.popitem() - удаляет и возвращает пару (ключ, значение). Если словарь пуст, бросает исключение KeyError. Помните, что словари неупорядочены.

dict.setdefault(key[, default]) - возвращает значение ключа, но если его нет, не бросает исключение, а создает ключ со значением default (по умолчанию None).

dict.update([other]) - обновляет словарь, добавляя пары (ключ, значение) из other. Существующие ключи перезаписываются. Возвращает None (не новый словарь!).

dict.values() - возвращает значения в словаре.
"""

"""
Методы словарей
d = {1: True, "2": 2, 3: "три", 4: "four"}

d.clear() - очищает словарь.
# {}

d.copy() - возвращает копию словаря.
# {1: True, "2": 2, 3: "три", 4: "four"}

d.get(key[, default]) - возвращает значение ключа, но если его нет, не бросает исключение, а возвращает default (по умолчанию None).
d.get(4)
# 'four'
d.get(5, "five")
# 'five'

d.items() - возвращает пары (ключ, значение).
# dict_items([(1, True), ('2', 2), (3, 'три'), (4, 'four')])

d.keys() - возвращает ключи в словаре.
# dict_keys([1, '2', 3, 4])

d.values() - возвращает значения в словаре.
# dict_values([True, 2, 'три', 'four'])

d.pop(1)
# True
d >>>
# {'2': 2, 3: 'три', 4: 'four'}

d.pop(key[, default]) - удаляет ключ и возвращает значение. Если ключа нет, возвращает default (по умолчанию бросает исключение).

d.popitem() - удаляет (последнюю) и возвращает пару (ключ, значение). Если словарь пуст, бросает исключение KeyError. Словари с 3.7 упорядочены.
# (4, 'four')
d >>>
# {'2': 2, 3: 'три'}

d.update([other]) - обновляет словарь, добавляя пары (ключ, значение) из other. Существующие ключи перезаписываются. Возвращает None (не новый словарь!).
# новое в Python 3.9
dict |= other
other = {1: "one"}
d.update(other)
d >>>
{'2': 2, 3: 'три', 1: 'one'}
"""


# Task
"""
Вводятся данные в формате ключ=значение в одну строчку через пробел. 
Значениями здесь являются целые числа (см. пример ниже). 
Необходимо на их основе создать словарь d с помощью функции dict() 
и вывести его на экран командой: print(*sorted(d.items()))
Input:  one=1 two=2 three=34
Output: ('one', 1) ('three', 34) ('two', 2)
"""
# s = "one=1 two=2 three=34"
s = input()
s = [row.split("=") for row in s.split()]
# [['one', '1'], ['two', '2'], ['three', '34']]
s = dict((row[0], int(row[1])) for row in s)
# {'one': 1, 'two': 2, 'three': 34}
print(*sorted(s.items()))



"""
На вход программы поступают данные в виде набора строк в формате: 
ключ1=значение1
ключ2=значение2
...
ключN=значениеN

Ключами здесь выступают целые числа (см. пример ниже). 
Необходимо их преобразовать в словарь d (без использования функции dict())
Input:  5=отлично
        4=хорошо
        3=удовлетворительно
Output: (3, 'удовлетворительно') (4, 'хорошо') (5, 'отлично')
"""
import sys
lst_in = list(map(str.strip, sys.stdin.readlines()))
# lst_in = ['5=отлично', '4=хорошо', '3=удовлетворительно']
s = [el.split("=") for el in lst_in]  # [['5', 'отлично'], ['4', 'хорошо'], ['3', 'удовлетворительно']]
# s = dict((int(row[0]), (row[1])) for row in s)
d = {int(row[0]): row[1] for row in s}
print(*sorted(d.items()))


"""
Вводятся данные в формате ключ=значение в одну строчку через пробел. 
Необходимо на их основе создать словарь, затем проверить, 
существуют ли в нем ключи со значениями: 'house', 'True' и '5' (все ключи - строки). 
Если все они существуют, то вывести на экран ДА, иначе - НЕТ.
Input:  house=дом True=1 5=отлично 9=божественно
Output: ДА
"""
s = list(map(str, input().split()))  # ['house=дом', 'True=1', '5=отлично', '9=божественно']
d = [el.split("=") for el in s]  # [['house', 'дом'], ['True', '1'], ['5', 'отлично'], ['9', 'божественно']]
# d = dict((el[0], el[1]) for el in d)  # {'house': 'дом', 'True': '1', '5': 'отлично', '9': 'божественно'}
d = dict(d)  # {'house': 'дом', 'True': '1', '5': 'отлично', '9': 'божественно'}
d = d.keys()  # ['house', 'True', '5', '9']
if 'house' in d and 'True' in d and '5' in d:
    print("ДА")
else:
    print("НЕТ")

# Вариант 1
s = list(map(str, input().split()))
d = [el.split("=") for el in s]
d = dict((el[0], el[1]) for el in d)
d = d.keys()
check_values = ['house', 'True', '5']
for el in check_values:
    if el not in d:
        print('НЕТ')
        break
else:
    print('ДА')


# Вариант 2
d = {}
for el in input().split():
    k, v = el.split('=')
    d[k] = v
print(['НЕТ', 'ДА'][all([i in d.keys() for i in ['house', 'True', '5']])])



"""
Вводятся данные в формате ключ=значение в одну строчку через пробел. 
Необходимо на их основе создать словарь d, 
затем удалить из этого словаря ключи 'False' и '3', если они существуют. 
Ключами и значениями словаря являются строки
Input:  лена=имя дон=река москва=город False=ложь 3=удовлетворительно True=истина
Output: ('True', 'истина') ('дон', 'река') ('лена', 'имя') ('москва', 'город')
"""
s = list(map(str, input().split()))
d = [el.split("=") for el in s]
dct = dict(d)
if 'False' in dct:
    del dct['False']
if '3' in dct:
    del dct['3']
print(*sorted(dct.items()))

# Метод с проверкой get()
s = list(map(str, input().split()))
d = [el.split("=") for el in s]
dct = dict(d)
if dct.get("False", False):
    dct.pop("False")
# Проверка наличия ключа
# если ключа нет, возвращается "False", а значит "if" не выполниться
if dct.get("3", False):
    dct.pop("3")
print(*sorted(dct.items()))

# Генератор списков
d = dict([el.split('=') for el in input().split()])
if 'False' in d:
    del d['False']
if '3' in d:
    del d['3']
print(*sorted(d.items()))


"""
Вводятся номера телефонов в одну строчку через пробел с разными кодами стран: +7, +6, +2, +4 и т.д. 
Необходимо составить словарь d, где ключи - это коды +7, +6, +2 и т.п., 
а значения - список номеров (следующих в том же порядке, что и во входной строке) с соответствующими кодами. 
Input:  +71234567890 +71234567854 +61234576890 +52134567890 +21235777890 +21234567110
Output: ('+2', ['+21235777890', '+21234567110']) ('+5', ['+52134567890']) ('+6', ['+61234576890']) 
        ('+7', ['+71234567890', '+71234567854'])
"""
tel = list(input().split())
# tel = ['+71234567890', '+71234567854', '+61234576890', '+52134567890', '+21235777890', '+21234567110', '+71232267890']
dict_tel = dict((el[:2], [k for k in tel if el[:2] == k[:2]]) for el in tel)
print(*sorted(dict_tel.items()))

# вариант
tel = list(input().split())
d = {}
for el in tel:
    d.setdefault(el[:2], []).append(el)
print(*sorted(d.items()))

# вариант
tel = list(input().split())
d = {}
for el in tel:
    d[el[:2]] = d.get(el[:2], []) + [el]
print(*sorted(d.items()))



"""
Вводятся номера телефонов в формате:
номер_1 имя_1
номер_2 имя_2
...
номер_N имя_N

Необходимо создать словарь d, где ключами будут имена, 
а значениями - список номеров телефонов для этого имени. 
Одному имени может принадлежать несколько разных номеров.
P. S. Для считывания списка целиком в программе уже записаны начальные строчки.
Input:  +71234567890 Сергей
        +71234567810 Сергей
        +51234567890 Михаил
        +72134567890 Николай 
Output: ('Михаил', ['+51234567890']) ('Николай', ['+72134567890']) ('Сергей', ['+71234567890', '+71234567810'])
"""
import sys
lst_in = list(map(str.strip, sys.stdin.readlines()))
lst = []
d = {}
for el in lst_in:
    lst.append(el.split())
for el in lst:
    d.setdefault(el[1], []).append(el[0])
print(*sorted(d.items()))


# вариант
import sys
lst_in = list(map(str.strip, sys.stdin.readlines()))
d = {}
for el in lst_in:
    el = el.split()
    if el[1] in d:
        d[el[1]].append(el[0])
    else:
        d[el[1]] = [el[0]]

print(*sorted(d.items()))

# вариант
lst_in = list(map(str.strip, sys.stdin.readlines()))
d = {}
for el in lst_in:
    value, key = el.split()
    if key in d:
        d[key] += [value]
    else:
        d[key] = [value]

print(*sorted(d.items()))


"""
Пользователь вводит в цикле целые положительные числа, пока не введет число 0. 
Для каждого числа вычисляется квадратный корень (с точностью до сотых) и 
значение выводится на экран (в столбик). 
С помощью словаря выполните кэширование данных так, 
чтобы при повторном вводе того же самого числа результат не вычислялся, 
а бралось ранее вычисленное значение из словаря. 
При этом на экране должно выводиться:
значение из кэша: <число>
Input:  1
        2
        3
        3
        2
        4
        0
Output: 1.0
        1.41
        1.73
        значение из кэша: 1.73
        значение из кэша: 1.41
        2.0
"""

d = {}
while True:
    key = int(input())
    if key == 0:
        break
    if key in d:
        print("значение из кэша:", d[key])
    else:
        d[key] = round(key ** 0.5, 2)
        print(d[key])

# моржовый оператор
d = {}
while key := int(input()):
    if key in d:
        print("значение из кэша:", d[key])
    else:
        d[key] = round(key ** 0.5, 2)
        print(d[key])



"""
Тестовый веб-сервер возвращает HTML-страницы по URL-адресам (строкам). 
На вход программы поступают различные URL-адреса. Если адрес пришел впервые, 
то на экране отобразить строку (без кавычек):
"HTML-страница для адреса <URL-адрес>"

Если адрес приходит повторно, то следует взять строку 
"HTML-страница для адреса <URL-адрес>" из словаря и вывести на экран сообщение (без кавычек):
"Взято из кэша: HTML-страница для адреса <URL-адрес>"

Сообщения выводить каждое с новой строки.
P. S. Для считывания списка целиком в программе уже записаны начальные строчки.

Input:  ustanovka-i-zapusk-yazyka
        ustanovka-i-poryadok-raboty-pycharm
        arifmeticheskiye-operatsii
        ustanovka-i-poryadok-raboty-pycharm
Output:     HTML-страница для адреса ustanovka-i-zapusk-yazyka
            HTML-страница для адреса ustanovka-i-poryadok-raboty-pycharm
            HTML-страница для адреса arifmeticheskiye-operatsii
            Взято из кэша: HTML-страница для адреса ustanovka-i-poryadok-raboty-pycharm
"""
# lst_in = ['ustanovka-i-zapusk-yazyka', 'ustanovka-i-poryadok-raboty-pycharm',
# 'peremennyye-operator-prisvaivaniya-tipy-dannykh', 'arifmeticheskiye-operatsii', 'ustanovka-i-poryadok-raboty-pycharm']

import sys
lst_in = list(map(str.strip, sys.stdin.readlines()))
d = {}
for el in lst_in:
    if el in d:
        print(f"Взято из кэша: HTML-страница для адреса {d[el]}")
    else:
        print(f"HTML-страница для адреса {el}")
        d.setdefault(el, el)


# вариант
import sys
lst_in = list(map(str.strip, sys.stdin.readlines()))
d = {}
for key, val in enumerate(lst_in):
    if val in d.values():
        print(f'Взято из кэша: HTML-страница для адреса {val}')
    else:
        d[key] = val
        print(f'HTML-страница для адреса {d[key]}')
