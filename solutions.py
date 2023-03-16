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
