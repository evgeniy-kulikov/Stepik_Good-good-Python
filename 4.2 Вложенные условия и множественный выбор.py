# 4.2 Вложенные условия и множественный выбор

"""
Вводятся три целых числа в одну строку через пробел. Необходимо определить наименьшее среди них и вывести его на экран.
Реализовать программу, используя условный оператор, без использования функции min.
"""
a, b, c = map(int, input().split())
if b < a:
    a, b = b, a
if c < a:
    a, c = c, a
print(a)

# Другой вариант 1
a, b, c = map(int, input().split())
a += (b - a) * (a > b)  # False = 0, True = 1
a += (c - a) * (a > c)
print(a)


"""
Дата некоторого дня характеризуется двумя натуральными числами: m (порядковый номер месяца) и n (число).
По введенным m и n (в одну строку через пробел) определить:

а) дату предыдущего дня (принять, что m и n не характеризуют 1 января);
б) дату следующего дня (принять, что m и n не характеризуют 31 декабря).

В задаче принять, что год не является високосным. Вывести предыдущую дату и следующую дату
(в формате: mm.dd, где m - число месяца; d - номер дня) в одну строчку через пробел.
"""

month, day = 2, 28
# month, day = map(int, input().split())
num_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if day == 1:  # первое число
    print(f'{(month - 1):02}.{(num_day[month - 2]):02} {month:02}.{(day + 1):02}')
elif day == num_day[month - 1]:  # конец месяца
    print(f'{month:02}.{(num_day[month - 1] - 1):02} {(month + 1):02}.{1:02}')
else:  # остальные дни
    print(f'{month:02}.{(day - 1):02} {month:02}.{(day + 1):02}')


"""
Вводится целое число k (1 <= k <= 365). Определить, каким днем недели 
(понедельник, вторник, среда, четверг, пятница, суббота или воскресенье) 
является k-й день не високосного года, в котором 1 января является понедельником.
"""

day = int(input())
days_of_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days_of_week = ['понедельник','вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']

index_of_week = day % 7 - 1
print(days_of_week[index_of_week])
