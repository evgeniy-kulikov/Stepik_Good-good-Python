# 2.3 Математические функции и модуль math

# Встроенные математические функции
# round специфически работает с пятерками, если последнее целое число 0
# round округляет 5 в меньшую сторону, если последнее целое число 0, иначе в большую сторону
print(round(130.5), round(131.5), round(130.05, 1), round(130.15, 1))
print(round(130.53854321), round(130.50000001), round(130.5000001, 0), round(130.598463))
a = max(round(130.50001), 2, abs(min(10, 5, -3)), pow(-10, 2) + 30)
print(a)

# модуль числа
print(abs(-500))

# Модуль math
import math

# округление до наибольшего целого
print(math.ceil(5.2))
print(math.ceil(-5.2))

# округление до наименьшего целого
print(math.floor(5.99))
print(math.floor(-3.3))

# факториал
print(math.factorial(6))

# отброс дробной части
print(math.trunc(5.3))
print(int(5.8))
print(int("5"))

# логарифмы
print(math.log2(4))
print(math.log10(1000))
print(math.log(2.7))
print(math.log(27, 3))

# квадратные корни
print(math.sqrt(49))

# Тригонометрия
print(math.sin(3.14 / 2))
print(math.cos(0))
print(math.pi)
print(math.e)


#  *   *   *   *   *   TASK    *   *   *   *   *


# # task 1
d = int(input())
print(abs(d))

# # task 2
# ввод целого числа
d1, d2, d3, d4, d5 = map(int, input().split())
# здесь продолжите программу
print(min(d1, d2, d3, d4, d5))

# task 3
# ввод целого числа
d1, d2, d3, d4, d5 = map(int, input().split())
# здесь продолжите программу
print(max(d1, d2, d3, d4, d5))

# task 4
# ввод данных
n, k = map(int, input().split())
# здесь продолжите программу
# import math
Cnk = math.factorial(n) / (math.factorial(k) * math.factorial(n - k))
print(math.trunc(Cnk))
