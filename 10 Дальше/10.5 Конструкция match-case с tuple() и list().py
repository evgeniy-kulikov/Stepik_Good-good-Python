# 10.5 Конструкция match/case с кортежами и списками
""""""

data = ("Автор Ф.И.О.", "Python FAQ", 2023)
# data = ["Автор Ф.И.О.", "Python FAQ", 2023]  # список работает аналогично кортежу

match data:
    case tuple() as book:
        print(f"Это кортеж {book}")
    case _:  # wildcard  (подстановочный знак)
        print("Неверный формат")
# Это кортеж ('Автор Ф.И.О.', 'Python FAQ', 2023)


match data:
    case autor, title, year:  # распаковка
        print(f"Книга: {title}, {autor}, {year}")
    case _:  # wildcard  (подстановочный знак)
        print("Неверный формат")
# Книга: Python FAQ, Автор Ф.И.О., 2023


data = ("Автор Ф.И.О.", "Python FAQ", 2023, 7.40, True, "string")

match data:
    case autor, title, year, *_:  # распаковка  (*_  принимает все остальное)
        print(f"Книга: {title}, {autor}, {year}")
    case _:  # wildcard  (подстановочный знак)
        print("Неверный формат")
# Книга: Python FAQ,Автор Ф.И.О.,2023


data = ("Автор Ф.И.О.", "Python FAQ", 2023, 7.40, True, "string")

match data:
    case (str() as autor, str(title), int() as year, *_data) if len(data) < 10:  # с проверкой типа данных и длиной
        print(f"Книга: {title}, {autor}, {year}")
    case _:  # wildcard  (подстановочный знак)
        print("Неверный формат")
# Книга: Python FAQ, Автор Ф.И.О., 2023


match data:
    case autor, title, year, *arg:  # распаковка
        print(f"Книга: {title}, {autor}, {year} - {arg}")
    case _:  # wildcard  (подстановочный знак)
        print("Неверный формат")
# Книга: Python FAQ, Автор Ф.И.О., 2023 - [7.4, True, 'string']


# Комбинированный шаблон
data = ("Автор Ф.И.О.", "Python FAQ", 2023)
data = [1, "Автор Ф.И.О.", "Python FAQ", 2023, 7.40]

match data:
    # имена переменных должны совпадать. Допускается только применение "_"
    case [autor, title, year] | (_, autor, title, year, _):  # () [] это просто группирующие скобки
        print(f"Книга: {title}, {autor}, {year}")
    case _:  # wildcard  (подстановочный знак)
        print("Неверный формат")
# Книга: Python FAQ, Автор Ф.И.О., 2023


data = ("Автор Ф.И.О.", "Python FAQ", 2023)
data = [1, "Автор Ф.И.О.", "Python FAQ", 2023, 7.40]

match data:
    # При различном кол-ве имен переменных нужно делать отдельный кейс.
    case [autor, title, year]:
        print(f"Книга: {title}, {autor}, {year}")
    case (_, autor, title, year, price):
        print(f"Книга: {title}, {autor}, {year}, {price}")
    case _:  # wildcard  (подстановочный знак)
        print("Неверный формат")
# Книга: Python FAQ, Автор Ф.И.О., 2023
# Книга: Python FAQ, Автор Ф.И.О., 2023, 7.4


# Проверка типа данных data
data = ("Автор Ф.И.О.", "Python FAQ", 2023)
data = [1, "Автор Ф.И.О.", "Python FAQ", 2023, 7.40]

match data:
    case tuple():
        print("Неверный формат данных: кортеж")
    case [autor, title, year]:
        print(f"Книга: {title}, {autor}, {year}")
    case (_, autor, title, year, price):
        print(f"Книга: {title}, {autor}, {year}, {price}")
    case _:  # wildcard  (подстановочный знак)
        print("Неверный формат")
# Неверный формат данных: кортеж
# Книга: Python FAQ, Автор Ф.И.О., 2023, 7.4


#
#  *   *   *   *   *   TASK    *   *   *   *   *
#


# 01
fio = ('Сидоров', 'Петр', 'Иванович')

match fio:
    case f1, f2, f3:
        res = ", ".join([f2, f3, f1])
    case _:
        res = "Некорректный формат данных"

print(res)
# Петр, Иванович, Сидоров


# 02
size = [100, 200, 50]

match size:
    case s1, s2:  # 1-й блок case
        res = ", ".join(map(str, [s2, s1]))
    case s1, s2, s3:  # 2-й блок case
        res = ", ".join(map(str, [s2, s3, s1]))
    case _:  # 3-й блок case
        res = "Некорректный формат данных"

# res = '200, 50, 100'  # 2-й блок case


#03
student = ['Троечников С.М.', 2, 3, 3, 2, 3, 4, 3, 5, 5, 1]

match student:
    case fio, m1, m2, m3:               # 1-й case
        print(f"{fio}: {m1} {m2} {m3}")
    case tuple() as fio, m1, m2, m3, *_: # 2-й case
        print(f"{fio}: {m1} {m2} {m3}")
    case list() as fio, m1, m2, m3, *_: # 3-й case
        print(f"{fio}: {m1} {m2} {m3}")
    case tuple() as fio, m1, m2, m3:    # 4-й case
        print(f"{fio}: {m1} {m2} {m3}")
    case _:                             # 5-й case
        print("Некорректный формат данных")

# Некорректный формат данных


# 04
"""
https://stepik.org/lesson/988837/step/5?unit=996322
Вводятся данные по книге в виде строки через запятую в формате (некоторые значения могут отсутствовать):
id, автор, название, цена, год издания
с помощью команд:
t = (int, str, str, float, int)
book = [t[i](x) if t[i] != str else x.strip() for i, x in enumerate(input().split(","))]

Сокращаем код автора
book = [t[i](x) for i, x in enumerate(input().split(", "))]

Например, при вводе:
"1, Балакирев С.М., Python, 2100, 2023"
получим список:
book = [1, 'Балакирев С.М.', 'Python', 2100.0, 2023]

С помощью оператора match/case необходимо определить шаблоны для выделения следующей информации:
автор, название
автор, название, цена
автор, название, год издания
автор, название, цена, год издания

Input:  1, Балакирев С.М., Python, 2100.0, 2023
Output: Yes
"""
t = (int, str, str, float, int)
book = [t[idx](el) for idx, el in enumerate(input().split(", "))]
# [1, 'Балакирев С.М.', 'Python', 2100.0, 2023]


match book:
    case _, author, title:
        print('Yes')
    case _, author, title, price:
        print('Yes')
    case _, author, title, year:
        print('Yes')
    case _, author, title, price, year:
        print('Yes')
    case _:
        print('No')

# Короче
match book:
    case _, author, title, *_:
        print('Yes')
    case _:
        print('No')


# 05
"""
https://stepik.org/lesson/988837/step/6?unit=996322
Вводятся данные по книге в виде строки через запятую в формате (некоторые значения могут отсутствовать):
id, автор, название, цена, год издания
С помощью оператора match/case необходимо определить шаблоны для выделения следующей информации 
с дополнительными проверками:

автор, название (автор - не менее 6 символов, название - не менее 10 символов)
автор, название, цена (автор не менее 6 символов, цена - положительное число)
автор, название, год издания (год издания от 2020 и выше)
автор, название, цена, год издания (цена - положительное число и год издания от 2020 и выше)

Первый шаблон срабатывает, если есть только автор и название; 
второй, если появляется еще и цена; 
третий, если есть автор, название, год издания, но нет цены; 
последний, если имеются все данные.

При срабатывании шаблона вывести на экран строку "Yes". 
Если ни один из шаблонов не сработал, то вывести строку "No".

Input:  1, Балакирев С.М., Python, 2100.0, 2023
Output: Yes

Input:  1, Балакирев С.М., Python, 0
Output: No
"""
t = (int, str, str, float, int)
book = [t[idx](el) for idx, el in enumerate(input().split(", "))]


match book:
    case (_, author, title) if len(author) >= 6 and len(title) >= 10:
        print('Yes')
    case (_, author, title, price) if len(author) >= 6 and price > 0:
        print('Yes')
    case _, author, title, year if year >= 2020:
        print('Yes')
    case(_, author, title, price, year) if price > 0 and year >= 2020:
        print('Yes')
    case _:
        print('No')
