#  3.3 Основные методы строк
""""""


s = "python"
print(type(s))

# Преобразование всех букв в заглавные, не действует на цифры
print("upper/lower")
print(s.upper())
res = s.upper()
print(s, res)

# Преобразование всех букв в строчные
print(res.lower())

# Поиск количества повторений подстроки в строке. Опции - стартовый и конечный индексы
print('\n', "count", sep='')
msg = 'abrakadabra'
print(msg.count("ra"))
print(msg.count("ra", 4))
print(msg.count("ra", 4, 10))
print(msg.count("ra", 4, 11))

# Поиск индекса первого повторения подстроки в строке. Если элемент не найден, возвращается -1
print("\n", 'find', sep='')
print(msg.find("br"))
print(msg.find("br", 2))
print(msg.find("brr", 2))
print(msg.find("br", 2, 10))
print("rfind")
print(msg.rfind("ra"))
# индекс работает так же, как find, но если подстрока не найдена, возвращает ошибку
print("index")
print(msg.index("ra"))

# Замена, можно указать макс. число замен
print("\n", "replace", sep='')
print(msg.replace("a", "o"))
print(msg.replace("ab", "AB"))
print(msg.replace("ab", ""))
print(msg.replace("a", "o", 2))

# проверка на буквы, цифры. пробел не буква, точка не цифра
print("\n", "isalpha",  sep='')
print(msg.isalpha())
print("Hello world".isalpha())
print("56".isdigit())
print("56.38".isdigit())
print("-56".isdigit())

# rjust (добавляет символы заполнители слева до указанной длины строки) и ljust (аналогично справа)
# по умолчанию заполняет пробелами
print("\n" + "rjust/ljust")
print("9".rjust(5, "0"))
print("b".ljust(4, "*"))

# Разделение строк
# string.split(sep=None, maxsplit=-1)
# возвращает коллекцию строк, на которую разбивается исходная строка
# разделитель по умолчанию - пробел
print("\n" + "split")
print("Иванов Иван Иванович".split())
digs = '1,   2,3,     4,    5,6'
d = digs.replace(" ", "").split(",")
print(d)

# Объединение списка строк в строку
print("\n" + "join")
sj = ", ".join(d)
print(sj)
fio = "Иванов Иван Иванович"
fio2 = ", ".join(fio.split())
print(fio2)

# strip - убирает лишние пробелы и служебные символы
print("\n" + "strip")
ss3 = "            hello world      \n"
print(ss3.strip())
print(ss3.rstrip())
print(ss3.lstrip())


#  *   *   *   *   *   TASK    *   *   *   *   *


# # Task 8
a, b, c = input().split()
print(a.rjust(3, "0"))
print(b.rjust(3, "0"))
print(c.rjust(3, "0"))


# Task 9
# Variant 1
s = input()
print(s.count(" ")+1)

# Variant 2
a = input()
print(len(a.split()))


# Task 10
s = input()
print(";".join(s.split()))