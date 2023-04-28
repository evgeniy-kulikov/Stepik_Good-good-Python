#  3.5 Форматирование строк и F-строки
""""""

age = 35
name = "Дмитрий"

s = "Меня зовут " + name + ", мне " + str(age) + " и я люблю язык Python"
print(s)

# метод strings.format
# можно обращаться по номерам переменных или по именам ключей
s1 = 'Меня зовут {0}, мне {1} и я люблю язык Python'.format(name, age)
print(s1)
s1 = 'Меня зовут {0}, мне {1} и я люблю язык {0} Python'.format(name, age)
print(s1)
s1 = 'Меня зовут {fio}, мне {old} и я люблю язык Python'.format(fio=name, old=age)
print(s1)

# f-строки начиная с Python 3.6
# PEP498
# наиболее популярный сейчас формат
s2 = f'Меня зовут {name}, мне {age} и я люблю язык Python'
print(s2)
s2 = f'Меня зовут {name.upper()}, мне {age * 2} и я люблю язык Python'
print(s2)
s2 = f'Меня зовут {len(name)}, мне {age * 2} и я люблю язык Python'
print(s2)


#  *   *   *   *   *   TASK    *   *   *   *   *


# Task 1
# variant 1
name = input()
surname = input()
age = input()
print("Уважаемый {0} {1}! Поздравляем Вас с {2}-летием!".format(name, surname, age))
# variant 2
s1, s2, s3 = input(), input(), input()
print('Уважаемый {} {}! Поздравляем Вас с {}-летием!'.format(s1, s2, s3))

# Task 3
# Вводятся: два целых числа в одну строку через пробел.
# С помощью F-строки отобразить их по возрастанию в одну строку через пробел. Результат вывести на экран.
# P.S. Реализовать программу без использования условных операторов. Подумайте, как это можно сделать.

# variant 1
a, b = map(int, input().split())
print(f'{min(a, b)} {max(a, b)}')

# variant 2
a, b = map(int, input().split())
print(f'{(a < b) * a + b * (b < a)} {(a > b) * a + b * (b > a)}')

# variant 3
a, b = sorted(list(map(int, input().split())))
print(f'{a} {b}')

# variant 4
a, b = map(int, input().split())
print(*[a, b][::1 - 2 * (a > b)])

# variant 5
print(*sorted(input().split()))

# Task 4
city, street, house, flat = input(), input(), input(), input()
print(f'г. {city}, ул. {street}, д. {house}, кв. {flat}')

