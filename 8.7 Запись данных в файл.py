# 8.7 Запись данных в файл
""""""

import pickle

# Открытие файла в текстовом режиме доступа на запись (по умолчанию стоит "r" - на чтение)
# Если файла нет, то он будет создан. Если файл был, то его содержимое перезапишется
file = open("out.txt", "w")
#  Запись строки в файл
file.write("Hello World!")
file.close()

# try/except и менеджер контекста with обязательны при работе с файлами
# открытие файла на запись
try:
    with open("out1.txt", "w") as file:
        file.write("Hello1")
        file.write("Hello2")
        file.write("Hello3")
except:
    print("Ошибка при работе с файлом")


# Открытие файла на дозапись (append). Исходные данные не стираются. Идет добавление к последней позиции.
try:
    with open("out2.txt", "a") as file:
        file.write("Hello1\n")
        file.write("Hello2\n")
        file.write("Hello3\n")
        # чтение файла в этом режиме невозможно
        # s = file.readlines()
except:
    print("Ошибка при работе с файлом")

# режим одновременного добавления и чтения данных
try:
    with open("out2.txt", "a+") as file:  # "a+" режим одновременного добавления и чтения данных
        # файловая позиция в режиме "а+" указывает на конец файла
        # поэтому файловую позицию на чтение надо переместить в начало
        file.seek(0)
        # файловые позиции на запись и чтение отличаются
        file.write("Hello4\n")  # Запись одной строки
        file.writelines(["Hello5\n", "Hello6\n"])  # Запись нескольких строк
        s = file.readlines()
        # считываются только те данные, которые были записаны в файл ранее
        print(s)

except:
    print("Ошибка при работе с файлом")

try:
    with open("out2.txt", "a+") as file:
        file.seek(0)  # Ставим указатель на начало
        # файловые позиции на запись и чтение отличаются
        file.write("Hello4\n")  # Запишется в конец. Метод записи сместит указатель в конец
        file.writelines(["Hello5\n", "Hello6\n"])  # Запишется после предыдущего ("Hello4\n")
        s = file.readlines()
        print(s)
except:
    print("Ошибка при работе с файлом")


# Бинарный режим доступа к файлу

books = [
    ("Евгений Онегин", "Пушкин А.С.", 200),
    ("Муму", "Тургенев И.С.", 250),
    ("Мастер и Маргарита", "Булгаков М.А.", 500),
    ("Мертвые души", "Гоголь Н.В.", 190)
]

try:
    # "wb" режим бинарной записи данных в файл
    with open("out3.bin", "wb") as file:
        pickle.dump(books, file)  # pickle.dump() загрузка данных в файл
except Exception:
    print("Ошибка при работе с файлом")

try:
    with open("out3.bin", "rb") as file:
        bs = pickle.load(file)  # pickle.load() чтение (выгрузка) данных из файла
        print(bs)
except Exception:
    print("Ошибка при работе с файлом")


# сохранение значений нескольких переменных в бинарный файл
book1 = ["Евгений Онегин", "Пушкин А.С.", 200]
book2 = ["Муму", "Тургенев И.С.", 250]
book3 = ["Мастер и Маргарита", "Булгаков М.А.", 500]
book4 = ["Мертвые души", "Гоголь Н.В.", 190]

try:
    with open("new_folder/out4.bin", "wb") as file:  # Запись данных
        pickle.dump(book1, file)  # Построчная загрузка
        pickle.dump(book2, file)
        pickle.dump(book3, file)
        pickle.dump(book4, file)
except Exception:
    print("Ошибка при работе с файлом")

try:
    with open("new_folder/out4.bin", "rb") as file:  # Чтение данных
        b1 = pickle.load(file)
        b2 = pickle.load(file)
        b3 = pickle.load(file)
        b4 = pickle.load(file)
except Exception:
    print("Ошибка при работе с файлом")

print(b1, b2, b3, b4, sep="\n")


#  *   *   *   *   *   TASK    *   *   *   *   *

# Запись списка
t = ["– Скажи-ка, дядя, ведь не даром",
    "Я Python выучил с каналом",
    "Балакирев что раздавал?"]

try:
    with open("out1.txt", "w") as file:
        file.writelines(t)
except:
    print("Ошибка при работе с файлом")


# Запись словаря
d = {'car': 'машина', 'tree': 'дерево', 'road': 'дорога'}
try:
    # "wb" режим бинарной записи данных в файл
    with open("out3.bin", "wb") as file:
        pickle.dump(d, file)  # pickle.dump() загрузка данных в файл
except Exception:
    print("Ошибка при работе с файлом")

try:
    with open("out3.bin", "rb") as file:
        bs = pickle.load(file)  # pickle.load() чтение (выгрузка) данных из файла
        print(bs)
except Exception:
    print("Ошибка при работе с файлом")
