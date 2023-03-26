# 7.1 Что такое функции. Их объявление и вызов
""""""

#  *   *   *   *   *   TASK    *   *   *   *   *


"""
Задайте функцию, которая не принимает никаких аргументов и просто выводит на экран строку:
It's my first function
Вызовите эту функцию.
"""
def print_text():
    text = "It's my first function"
    print(text)

print_text()


"""
Запишите функцию без аргументов, которая считывает с клавиатуры имя и фамилию, 
записанные в одну строку через пробел, и выводит на экран сообщение (без кавычек):
"Уважаемый, <имя> <фамилия>! Вы верно выполнили это задание!"
Вызовите эту функцию.
Input:  Сергей Балакирев
Output: Уважаемый, Сергей Балакирев! Вы верно выполнили это задание!
"""
def print_text():
    text = input()
    print(f"Уважаемый, {text}! Вы верно выполнили это задание!")

print_text()


"""
Объявите функцию, которая имеет один параметр - вес предмета и выводит на экран сообщение (без кавычек):
"Предмет имеет вес: x кг."
где x - переданное значение функции. 
После объявления функции прочитайте (с помощью функции input) вещественное число и вызовите функцию с этим значением.
Input:  12.67
Output: Предмет имеет вес: 12.67 кг.
"""
def print_text(weight: float):
    print(f"Предмет имеет вес: {weight} кг.")

num = float(input())
print_text(num)



"""
Объявите функцию, которая принимает список, 
находит максимальное, минимальное и сумму значений этого списка и 
выводит результат в виде строки (без кавычек):
"Min = v_min, max = v_max, sum = v_sum"
где v_min, v_max, v_sum - вычисленные значения минимального, максимального и суммы значений списка.
После объявления функции прочитайте (с помощью функции input) список целых чисел, 
записанных в одну строку через пробел, и вызовите функцию с этим списком.
Input:  8 11 5 -10 12 0
Output: Min = -10, max = 12, sum = 26
"""
def get_value(lst):
    num_min = min(lst)
    num_max = max(lst)
    num_sum = sum(lst)
    print(f"Min = {num_min}, max = {num_max}, sum = {num_sum}")


list_num = list(map(int, input().split()))
get_value(list_num)


"""
Объявите функцию с двумя параметрами width и height (ширина и высота прямоугольника), 
которая выводит сообщение (без кавычек):
"Периметр прямоугольника, равен x"
где x - вычисленный периметр прямоугольника. 
После объявления функции прочитайте (с помощью функции input) два целых числа, 
записанных в одну строку через пробел, и вызовите функцию с этими значениями.
Input:  8 11
Output: Периметр прямоугольника, равен 38
"""
def get_value(width, height):
    perimeter = 2 * (width + height)
    print(f"Периметр прямоугольника, равен {perimeter}")

# width, height = list(map(int, input().split()))
width, height = map(int, input().split())
get_value(width, height)



"""
Напишите функцию, которая проверяет корректность переданного ей email-адреса в виде строки. 
Будем полагать, что адрес верен, если он обязательно содержит символы '@' и '.', 
а все остальные символы могут принимать значения: 'a-z', 'A-Z', '0-9' и '_'. 
Если email верен, то функция выводит ДА, иначе - НЕТ.
После объявления функции прочитайте (с помощью функции input) строку с email-адресом и 
вызовите функцию с этим аргументом.
Input:  sc_lib@list.ru
Output: ДА
"""
def check_email(email):
    cnt = 0
    if "@" in email and email.count("@") == 1 and len(email) > 4:
        ls_email = email.split("@")
        if "." in ls_email[1] and email.count(".") == 1:
            email_part = ls_email.pop().split(".")
            ls_email.append(email_part[0])
            ls_email.append(email_part[1])
            if cnt == 0:
                for item in ls_email:
                    for el in item:
                        if 96 < ord(el) < 123 or ord(el) == 95 or el.isdigit():
                            continue
                        else:
                            cnt += 1
                            break
        else:
            cnt += 1
    else:
        cnt += 1

    if cnt == 0:
        print("ДА")
    else:
        print("НЕТ")


email = input().lower()
check_email(email)

# Вариант
# пропускает .@.@.@
def check_mail(mail):
    allow = set("abcdefghijklmnopqrstuvwxyz0123456789_@.")
    nesessary = {"@", "."}
    print("ДА") if nesessary <= mail <= allow else print("НЕТ")


msg = set(input().lower())
check_mail(msg)
