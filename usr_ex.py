file = open('usr_file.txt', encoding='utf-8')

# Читаем все содержимое файла
# print(file.read())

# Читаем только первые 4 символа из содержимого файла (с учетом первого невидимого символа кодировки utf-8  - #FEFF )
print(file.read(4))  # — Да
# При повторном вызове читаем дальше
print(file.read(4))  # , бы

# Сдвигаем файловый указатель в начало
file.seek(0)
print(file.read(8))  # — Да, бы

# Получаем номер байта для текущего файлового указателя
pos = file.tell()
print(pos)
file.seek(0)  # Сдвигаем файловый указатель в начало

# Получаем первую строку (метод ищет символ  \n  или конец файла, при его отсутствии)
# print(file.readline())

# Для избежания печати полученного символа  \n
print(file.readline(), end='')
print(file.readline(), end='')

# file.seek(0)  # Сдвигаем файловый указатель в начало

for el in file:
    print(el, end='')

file.seek(0)  # Сдвигаем файловый указатель в начало

# Получаем список всех строк. ВНИМАНИЕ !!! в память помещается весь файл (метод использовать для небольших файлов)
ls = file.readlines()
print(ls)
# ['— Да, были люди в наше время,\n', 'Не то, что нынешнее племя:\n', 'Богатыри — не вы!\n', ... 'Не отдали б Москвы!']

# По завершении работы файл ВСЕГДА нужно закрыть.
file.close()
