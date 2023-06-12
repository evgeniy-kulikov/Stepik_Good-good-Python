#  3.1 Введение в строки. Операции над строками
""""""


s1 = 'Панда'
s2 = "Panda"

print(s1)
print(s2)

text = '''Я Python бы выучил только за то,
что есть популярные курсы.
Много хороших курсов.
'''
print(text)

a = ""
b = " "

# конкатенация
s1 = "Я люблю"
s2 = "язык Python"
print(s1 + s2)
print(s1 + " " + s2)

# перевод других типов данных в строку
print(s1 + " " + str(5))
print(str(True))
print(str(65.8))

# умножение строк
print("xa " * 5)

# вычисление длины строки
print(len("hello"))
a = "hello"
print(len(a))

# проверка наличия фрагмента в строке
print()
print('ab' in 'abracadabra')
print('abc' in 'abracadabra', "\n")

# операторы сравнения строк
print("проверка на равенство")
print(a == "hello")
print(a == "Hello")
print(a != "Hello")
print(a != "hello")
print(a != " hello")
print("сравнение происходит по кодам таблиц ASCII. Например, коды малых букв больше кодов заглавных")
print('кот' > 'кит')
print('кот' > 'кот')
print('кот' >= 'кот')
print('Кот' < 'кот', "\n")

# определение кода символа
print(ord('К'))
print(ord('к'))


#  *   *   *   *   *   TASK    *   *   *   *   *

# Task 5
s1 = str(input())
s2 = str(input())
print(s1 + " " + s2)

# Task 7
# Var 1
s1, s2 = map(str, input().split())
print((s1 + ' ') * 2 + (s2 + ' ') * 3)
# Var 2
s1, s2 = input().split()
print((s1 + ' ') * 2 + (s2 + ' ') * 3)

# Task 8
a, b = map(int, input().split())
print("Переменная a = " + str(a) + ", переменная b = " + str(b))

# Task 9
# Var 1
a = str(input())
print("Строка: " + a + ". Длина:", len(a))

# Var 2
# Конкатенацию можно проводить для любого типа данных
# Работает, если дать на вход строку, целое, вещественное или булево значение
# Функция input() по умолчанию считывает строку
new_var = input()
print(type(new_var))
print('Строка: ' + new_var + '. Длина:', len(new_var))

# Task 10
s1, s2 = input().split()
print(s1 in s2, s1 == s2, s1 > s2, s1 < s2)

# Task 11
# Коды ASCII
c1, c2 = input().split()
print(f'Коды: {c1} = {ord(c1)}, {c2} = {ord(c2)}')

print(chr(1050))  # К
print(chr(1082))  # к
