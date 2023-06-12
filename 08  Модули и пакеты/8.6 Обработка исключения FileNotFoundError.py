#  8.6 Обработка исключения FileNotFoundError и менеджер контекста
""""""

"""
try:
    Блок операторов критического кода (код, который может вызвать ошибку)
except:
    Блок операторов обработки исключения (ошибки)
finally:
    Блок операторов всегда исполняемых, вне зависимости от возникновения исключения (ошибки)
"""




try:
    file = open("usr_file.txt", encoding="utf-8")
    s = file.readlines()  # критический код
    print(s)
    file.close()
except FileNotFoundError:
    print("Невозможно открыть файл")


#  Обрабатываем несколько участков критического кода
try:
    file = open("usr_file.txt", encoding="utf-8")  # критический код 1
    try:
        s = file.readlines()
        # int(s)  # вызывает ошибку при работе с файлом (критический код 2)
        print(s)
    finally:
        file.close()  # Блок отработает всегда (в данной секции блока "try")
# обработка исключения
except FileNotFoundError:
    print("Невозможно открыть файл")
except:
    print("Ошибка при работе с файлом")

# выполняется в любом случае, произошли ошибки или нет
# finally


# менеджер контекста
# замена try/finally
# автоматически закрывает файл
try:
    with open("usr_file.txt", encoding="utf-8") as file:
        s = file.readlines()
        # int(s)
        print(s)
except FileNotFoundError:
    print("Невозможно открыть файл")
except Exception:
    print("Ошибка при работе с файлом")
finally:
    print(file.closed)


#  *   *   *   *   *   TASK    *   *   *   *   *


"""
Имеется фрагмент программы (см. листинг ниже). 
f = open("abc.txt")
r = f.read(1)
f.close()

При его выполнении возникает ошибка FileNotFoundError. Запишите конструкцию try / except, 
чтобы отображалось сообщение "File Not Found", если файл не удается открыть.
"""
try:
    f = open("abc.txt")
    r = f.read(1)
    f.close()
except FileNotFoundError:
    print("File Not Found")


# Вариант
try:
    with open("abc.txt", encoding="utf-8") as f:
        r = f.read(1)
        f.close()
except FileNotFoundError:
    print('File Not Found')
