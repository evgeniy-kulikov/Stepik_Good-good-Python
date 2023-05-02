# 2.5 Логический тип Bool. Операторы сравнения

# логические переменные и операторы
# <class 'bool'>
# True / False
# <
# >
# <=
# >=
# ==
# !=
# and, or, not

# элементарные операции с логическими переменными
print()
print("элементарные операции с логическими переменными")
a = 5
b = 7.8
res = a <= b
print(res, type(res))
res = False
print(res, "\n")

# приоритет арифметических операций перед логическими
print("приоритет арифметических операций перед логическими")
print(5 == 7 - 2, "\n")

# проверка на четность
print("проверка на четность")
x = 6
print(x % 2 == 0, "\n")
# проверка на нечетность
print("проверка на нечетность")
y = 7
print(y % 2 != 0, "\n")

# проверка на кратность
print("проверка на кратность")
print(a % 3 == 0)
a = 9
print(a % 3 == 0, "\n")

# операции над множествами, составные условия
print("операции над множествами")
y = 1.85
res = y >= -2 and y <= 5
print(res)
res = -2 <= y <= 5
print(res)
res = y < -2 or y > 5
print(res)
y = -10
res = y < -2 or y > 5
print(res)
res = -2 > y > 5
print(res)
x = 7
print(x, x % 2 == 0 or x % 3 == 0)
print(x, x % 2 != 0 and x % 3 != 0)
print(x, not(x % 2 == 0 or x % 3 == 0), "\n")

# функция bool() True False
print("функция bool()")
print(bool(1))
print(bool(2))
print(bool(0))
print(bool(""))
print(bool(" "))
print(bool("0"))


#  *   *   *   *   *   TASK    *   *   *   *   *



# # Task 5
a = float(input("Введите вещественное число: "))
b = int(a) % 3 == 0
print(b)

# # Task 6
# variant 1
a = float(input())
b = a - int(a) > 0.5
print(b)
# variant 2
digit = float(input())
print(digit % 1 > .5)

# Task 7
# variant 1
a, b = map(int, input().split())
print((a / b) % 1 == 0)
# variant 2
a, b = map(int, input().split())
print(a % b == 0)
# variant 3
a, b = map(int, input().split())
print(not (a % b))

# # Task 10
a, b, c = map(int, input().split())
d = max(a, b, c)
print(a + b + c - d > d)

# Task 11
# Variant 1
a = float(input())
print((0 <= a <= 2) or (10 <= a <= 20))
# Variant 2
a = float(input())
print((0 <= a <= 2) != (10 <= a <= 20))
