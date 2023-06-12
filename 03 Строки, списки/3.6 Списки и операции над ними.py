#  3.6 Списки и операции над ними
""""""

# Список - упорядоченная коллекция данных

l1 = ["Москва", "Тверь", "Вологда"]
print(l1)

marks = [2, 3, 4, 3, 5, 2]
print(marks)
print(marks[0])
print(marks[1])
res = (marks[0] + marks[1] + marks[2] + marks[3] + marks[4] + marks[5]) / 6
print(res)
# последний элемент списка, отрицательное число - перебор с конца
print(marks[-1])

# список - изменяемый тип данных
marks[0] = 3
print(marks)
marks[1] = "удовлетворительно"
print(marks)

# элементами списка могут быть любые типы данных
lst = ["Москва", 1320, 5.8, True, "Тверь", False]
print(lst)
lst2 = [1, 2.5, [-1, -2, -3], 4]
print(lst2)

# пустые списки
a = []
b = list()
print(a, b)

# функция list, создает копии списков
b = list([True, False])
print(b)
c = list("python")
print(c)
# list - создает список на базе любых перебираемых (итерируемых) объектов

# функции списков
# len() - длина списка
# max() - нахождение макс. значения
# min() - нахождение мин. значения
# sum() - вычисление суммы списка
# sorted() - для сортировки коллекции

# len()
print(len(marks))
print(len([]))

# max/min
t = [23.5, 25.6, 27.3, 26.0, 30.4, 29.5]
print(min(t))
print(max(t))

# sum
print(sum(t), sum(t)/len(t))

# sorted
print(sorted(t))
print(t)
t_sort = sorted(t)
print(t_sort)
t_sort = sorted(t, reverse=True)
print(t_sort)

# работа max/min и сортировки с другими типами данных
s = list("python")
print(max(s))
print(min(s))
print(sorted(s))

# сортировка списка с ключом, преобразующим все буквы в строчные перед сравнением
print('Крутой пример из хелпа питона')
print(r'https://docs.python.org/3.10/howto/sorting.html#sortinghowto')
s1 = sorted("This is a test string from Andrew".split(), key=str.lower)
print(s1, '\n')

# операторы списков
# + соединение двух списков в один
# * дублирование
# in проверка вхождения элемента в список
# del удаление элемента из списка

# +
print([1, 2, 3] + [4, 5])
print([1, 2, 3] + [4])

# * умножать только на целое значение
lst1 = ["Я", "люблю", "Python"]
print(lst1 * 3)
lst2 = ["Я"] + ["люблю"] * 3 + ["Python"]
print(lst2)

# in
lst = ["Москва", 1320, 5.8, True, "Тверь", False]
print(lst)
print(1320 in lst)
print(132 in lst)
print([1, 2] in lst)
lst = lst + [[1, 2]]
print(lst)
print([1, 2] in lst)
print("Москва" in lst)
del lst[2]
print(lst)


s = '1 2   3'
l1 = list(map(str, s.split()))  # удаляет все пробелы между элементами
l2 = list(map(str, s.split(' ')))  # удаляет по одному пробелу между элементами
print(l1)  # ['1', '2', '3']
print(l2)  # ['1', '2', '', '', '3']

print(*lst)  # напечатать все элементы списка без отображения скобок и запятых


#  *   *   *   *   *   TASK    *   *   *   *   *


# Task 3
lst = list(map(int, input().split()))
print(lst)

# Task 4
cities = input().split()
print("Москва" in cities)
# print((False, True)['Москва' in cities])

# Task 6
cities = input().split()
print(cities[-1])

# Task 7
marks = list(map(int, input().split()))
print(round(sum(marks) / len(marks), 1))

# Task 8
# Variant 1
book = [input(), input(), int(input()), float(input())]
print(book)
del book[2]
book[1] = 'Пушкин'
book[2] *= 2
print(book)
# Variant 2
title, author, page, coin = input(), input(), int(input()), float(input())
book = [title, author, page, coin]
book[1] = 'Пушкин'
book[-1] = book[-1] * 2
del book[2]
print(book)

# Task 9
lst = list(map(int, input().split()))
print(max(lst), min(lst), sum(lst))

# Task 10
# Variant 1
lst = list(map(int, input().split()))
lst = sorted(lst, reverse=True)
print(*lst)
# Variant 2
lst = list(map(int, input().split()))
lst.sort(reverse=True)
print(*lst)
# Variant 3
# Итогом sorted уже будет список, можно сразу map скармливать
print(*sorted(map(int, input().split()), reverse=True))

# как отсортировать строку?
# использовать срез с отрицательным шагом
# отсортировать, затем объединить получившийся список
a = 'привет'
print(a[::-1])  # тевирп
a1 = sorted(a, reverse=True)
print(a1)  # ['т', 'р', 'п', 'и', 'е', 'в']
print(''.join(a1))  # трпиев

# Task 12
# Variant 1
cities = ["Москва", "Тверь", "Вологда"]
lst = input().split()
cities += lst
print(*cities)
# Variant 2
cities = ["Москва", "Тверь", "Вологда"]
lst = cities + (input().split())
print(*lst )
# Variant 3
lst = input().split()
cities = ["Москва", "Тверь", "Вологда"]
lst = cities + lst
print(*lst)
# Variant 4
cities = ["Москва", "Тверь", "Вологда"] + input().split()
print(*cities)

# Task 13
cities = ["Москва", "Тверь", "Вологда"]
lst = input().split()
lst += cities
print(*lst)

# Task self- Сортировка списка фамилий
lst = input("Введите список фамилий: ").split()
print(sorted(lst, key=str.lower))
