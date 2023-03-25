# ввод данных. Данные вводятся через пробел, одной строкой
# n, k = map(int, input().split())
""""""
"""
тернарный оператор:

[when_true] if [condition] else [when_false]
is_fast = True
car = "Ferrari" if is_fast else "Sedan"

тернарный оператор с кортежем:
(when_false, when_true)[condition]
is_fast = True
car = ("Sedan", "Ferrari")[is_fast]
"""

lst = ["a", "b", "c"]
''.join(map(str, lst))  # способ преобразовать список в строку
"abc"


# реализация функции enumerate()
def get_even(list_of_nums):
    for el in list_of_nums:
        if el % 2 == 0:
            yield el


list_of_nums = [1, 2, 3, 8, 15, 42]
# вывод только четных значений из списка
for item in get_even(list_of_nums):
    print(item, end=" ")  # 2 8 42
