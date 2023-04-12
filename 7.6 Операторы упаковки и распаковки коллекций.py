# 7.6 Операторы упаковки и распаковки коллекций
""""""

"""
Вводится список из семи целых чисел в одну строчку через пробел. 
Необходимо первые четыре числа занести в переменную lst, а остальные три в отдельные переменные x, y, z. 
Сделать с использованием оператора упаковки. Вывести список lst на экран с помощью команды:
print(*lst)
Input:  56 4 -23 2 0 3 5
Output: 56 4 -23 2
"""
ls = tuple(map(int, input().split()))
*lst, x, y, z = ls
print(*lst)

# Вариант
*lst, x, y, z = input().split()
print(*lst)


"""
Вводятся названия городов в одну строчку через пробел. 
На основе этой строки необходимо сформировать список из названий. 
А, затем, используя оператор распаковки *, преобразовать этот список в кортеж lst_c. 
Результат вывести на экран командой:
print(lst_c)
Input:  Москва Уфа Тверь Самара
Output: ('Москва', 'Уфа', 'Тверь', 'Самара')
"""
lst_c = tuple(map(str, input().split()))
print(lst_c)

# Вариант
lst_c = *input().split(),
print(lst_c)


"""
Вводятся два целых значения a и b (a < b) в одну строчку через пробел. 
Необходимо сформировать список из целых чисел от a до b (включительно) с шагом изменения 1, 
используя функцию range, оператор [] и оператор распаковки *. 
Вывести полученный список на экран командой: print(*lst)
Input:  3 11
Output: 3 4 5 6 7 8 9 10 11
"""

a, b = map(int, input().split())
lst = [el for el in range(a, b + 1)]
print(*lst)

# Вариант
a, b = map(int, input().split())
lst = [*range(a, b + 1)]
print(*lst)


"""
Вводится список вещественных чисел и список названий городов, 
каждый в отдельной строке. 
Необходимо сформировать единый список lst, в котором сначала идут числа, 
а затем, названия городов. 
Реализовать программу с помощью оператор распаковки *
Вывести полученный список на экран командой: print(*lst)
Input:  5.8 11.0 4.3
        Уфа Омск Тверь Самара
Output: 5.8 11.0 4.3 Уфа Омск Тверь Самара
"""
num = map(float, input().split())
city = map(str, input().split())
lst = [*num, *city]
# lst = [*num] + [*city]
print(*lst)


"""
Имеется словарь, содержащий пункты меню:
menu = {'Главная': 'home', 'Архив': 'archive', 'Новости': 'news'}
Дополнительно вводятся еще пункты меню в виде строк в формате:
название_1=url_1
...
название_N=url_N

Необходимо эту введенную информацию преобразовать в словарь и добавить к словарю menu, 
используя оператор распаковки для словарей. На результирующий словарь должна вести переменная menu. 
Выводить словарь не нужно, только сформировать.
P. S. Для считывания списка целиком в программе уже записаны начальные строчки.
Input:  Города=about-cities
        Машины=read-of-cars
        Самолеты=airplanes
Output: Архив Главная Города Машины Новости Самолеты
        about-cities airplanes archive home news read-of-cars
"""
import sys
lst_in = list(map(str.strip, sys.stdin.readlines()))
menu = {'Главная': 'home', 'Архив': 'archive', 'Новости': 'news'}
# здесь продолжайте программу (используйте список lst_in и menu)
# lst_in = ['Города=about-cities', 'Машины=read-of-cars', 'Самолеты=airplanes']
lst_out = [el.split('=') for el in lst_in]
d = dict(lst_out)
menu.update(d)


# Вариант
menu = dict(**menu, **d)
d = dict([el.split('=') for el in lst_in])
menu = dict(**menu, **d)

