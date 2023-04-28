#  3.2 Индексы и срезы строк
""""""


# Строка - упорядоченный набор символов
# индекс задается номером символа в квадратных скобках
print("Индексы")
s = "hello python"
print(s[0])
print(s[1])
print(s[2])
print(s[11])
print(len(s) - 1)

# отрицательные индексы идут с конца, последний символ имеет номер -1
print(s[len(s) - 1], s[-1], s[-2])

# можно вызвать произвольный символ от строки, а не от переменной
print("panda"[3], "\n")

# срез - строка[start:stop], конечный индекс не включается в срез
print("Срезы")
print(s[1:3])
print(s[1:])
print(s[:5])
print(s[:])

# выделение всей строки дает ссылку на ту же строку, а не копирует объект
a = s[:]
print(id(s), id(a))

# срез можно делать от отрицательного индекса
print(s[2:-2])
print(s[0])

# срез в обратную сторону дает пустую строку
print(s[-2:2])
print(s[4:2], "\n")

# в срезах можно указывать шаг перебора символов
# строка[start:stop:step]
print("Шаг среза")
print(s[2:10:2])
print(s[2::3])
print(s[:5:3])
print(s[::2])
print(s[::-1])
print(s[::-2], "\n")

# строки относятся к неизменяемым типам данных
# один символ в строке изменить нельзя
# только так
print("Модификация строки через индексы и срезы")
s2 = 'H' + s[1:]
print(s2, id(s), id(s2))


#  *   *   *   *   *   TASK    *   *   *   *   *


# Task 1
s = input()
print(s[-3:])

# Task 8
# При отрицательном шаге начальный и конечный индексы надо указывать в обратном порядке
# variant 1
s8 = 'abrakadabra'
print(s8[4::-1])
# variant 2
print(input()[:5][::-1])


# Task 9
s1, s2 = input().split()
print(s2[:len(s1)])


# Task 10
s1, s2 = input().split()
print(s1[1:len(s2):2] == s2[1::2])
