# 2.1 Переменные, операции присваивания, функции type и id

# тип int, длинные комменты
print("""
тип int
code:   a = 7
code:   print(a)
>>> """)
a = 7
print(a)

# тип str
print("""
тип str
code:   var_a = 'hello'
code:   print(var_a)
>>> """)
var_a = 'hello'
print(var_a)

# тип float
print("""
тип float
a = 6.8
print(a)
>>> """)
a = 6.8
print(a)

# сохранение значения второй переменной при изменении первой, изменение адреса хранения значения
print("""
сохранение значения второй переменной при изменении первой, изменение адреса хранения значения
b = a
print('a = ', a, "/ id = ", id(a))
print('b = ', b, "/ id = ", id(b))
a = 8
print('a = ', a, "/ id = ", id(a))
print('b = ', b, "/ id = ", id(b))
>>> """)
b = a
print('a = ', a, "/ id = ", id(a))
print('b = ', b, "/ id = ", id(b))
a = 8
print('a = ', a, "/ id = ", id(a))
print('b = ', b, "/ id = ", id(b))

# динамическое изменение типа переменной, строгая типизация
a = 7
b = "Hello"
b = 0
b = 8.4
print(a, b)

# функция, возвращающая адрес переменной
# групповое присваивание
a = b = c = 0
print(a, b, c)
print(id(a), id(b), id(c))

a, b = 1, 2
print(a, b)
print(id(a), id(b))

a, b = b, a
print(a, b)
print(id(a), id(b))

# функция, возвращающая тип переменной
print(type(a))
x = 5.8
s = "Hello"
print(type(x), type(s))

# Регистр имеет значение
msg = "Сообщение"
count = 0
arg = 0
Arg = 1
print(msg, count, arg, Arg)

# Не присваивать переменным имена ключевых слов (keywords) или функций
e = f = "hi!"
print(e, f)
