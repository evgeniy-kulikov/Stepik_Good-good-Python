# 2.4 Функции print и input

print(3, 5, 7)

a = -6.84
print(abs(a * 2 + 3))

print("hello")

# разделитель
b = 7
c = 25.6
print(a, b, c, sep=" | ")
# по умолчанию sep=" "

# конец строки
print("Hello", end=" ")
print("World!")
# по умолчанию end="\n"

x = 5.76
y = -8
print("Координаты точки: x = ", x, "; y = ", y, sep="")

# Начиная с Python 3.6 F-строки
print(f"Координаты точки: x = {x}; y = {y}")

# Ввод данных, преобразование типов
a = input()
print(a, type(a))
a = int(a)
b = abs(a)
print(b)

c = float(input())
print(a, type(a))
d = abs(a)
print(d)

#  *   *   *   *   *   TASK    *   *   *   *   *

# Вычисление периметра прямоугольника
# Вариант 1
a = float(input("Введите длину прямоугольника: "))
b = float(input("Введите ширину прямоугольника: "))
print("Периметр: ", 2 * (a + b))

# Вариант 2
a, b = map(float, input("Введите две стороны прямоугольника: ").split())
print("Периметр: ", 2 * (a + b))

# Вариант 2
print("")
a, b, c = map(int, input("Введите стороны треугольника: ").split())
print("Периметр: ", a + b + c)
