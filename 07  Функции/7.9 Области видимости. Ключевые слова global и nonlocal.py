# 7.9 Области видимости. Ключевые слова global и nonlocal
""""""

"""
Инструкция nonlocal применяется во вложенных функциях если нужно изменять переменные, 
которые были объявлены в объемлющих функциях.

Отличие между инструкциями nonlocal и global следующее:

инструкция global позволяет изменять значения переменных в глобальной области видимости модуля;
инструкция nonlocal изменяет значение переменных в объемлющей функции. 
Для глобальной области видимости инструкция nonlocal не имеет действия
"""
x = 0
def outer():
    x = 1
    def inner():
        x = 2
        print("inner: ", x)  # inner: 2

    inner()
    print("outer: ", x)  # outer: 1

outer()
print("global: ", x)  # global: 0



x = 0
def outer():
    x = 1
    def inner():
        nonlocal x
        x = 2
        print("inner: ", x)  # inner: 2

    inner()
    print("outer: ", x)  # outer: 2

outer()
print("global: ", x)  # global: 0



x = 0
def outer():
    global x
    x = 1
    def inner():
        # nonlocal x # Иначе будет ошибка
        x = 2
        print("inner: ", x)  # inner: 2

    inner()
    print("outer: ", x)  # outer: 1

outer()
print("global: ", x)  # global: 1


# Инструкция nonlocal
# Несколько объемлющих функций

def Fn1():
    # эта переменная не изменяется из функции Fn3(),
    # потому что ее перекрывает переменная из функции Fn2()
    x1 = 25

    def Fn2():
        x1 = 33  # эта переменная будет изменяться в функции Fn3()

        def Fn3():
            nonlocal x1
            x1 = 55  # Fn2.x1 = 55

        Fn3()
        print('Fn2.x1 = ', x1)  # Fn2.x1 = 55

    Fn2()
    print('Fn1.x1 = ', x1)  # Fn1.x1 = 25

Fn1()


#  *   *   *   *   *   TASK    *   *   *   *   *


"""
Имеется программа (см. листинг ниже), 
где читается глобальная переменная WIDTH (из входного потока) и функция с именем func1. 
Допишите в теле функции команду, которая бы позволяла изменять глобальную переменную WIDTH.
"""

WIDTH = int(input())


def func1():
    global WIDTH # Теперь можем менять глобальную переменную
    WIDTH += 1
    return WIDTH


print(func1())



"""
Имеется программа (см. листинг ниже). 
Необходимо в теле функции func2 дописать команду, 
которая бы меняла значение уже существующей переменной msg, объявленной в функции func1.
Input:  Сергей
        Балакирев
Output: Балакирев
        Балакирев
"""

def func1():
    msg = input()

    def func2():
        nonlocal msg
        msg = input()
        print(msg)

    func2()
    print(msg)

func1()


"""
Объявите функцию с именем create_global, которая имеет, следующую сигнатуру:
def create_global(x): ...
Эта функция должна создавать глобальную переменную с именем TOTAL и присваивать ей значение x. 
(Ничего выводить на экран она не должна, только создавать переменную).
"""

def create_global(x):
    global TOTAL
    TOTAL = x
