# Повторная загрузка модуля "usermodule"
# import importlib
# import usermodule
# from usermodule import *

import usermodule

# importlib.reload(usermodule)

# Добавление директории модуля к системным путям проекта
# Такое решение используется крайне редко
# Обычно пусть указывается при импорте модуля
# from userdir import usermodule
# sys.path.append(r'D:\__PythonProject\Good, good Python [S. Balakirev]\userdir')

# a = usermodule.floor(5.4)
# print(a)

# a = floor(5.4)
# print(a)

# pprint.pprint(dir(usermodule))

# длинную иерархию пространства имен обычно не используют
# a = usermodule.math.floor(5.6)
# a = usermodule.floor(5.6)
# b = usermodule.ceil(5.6)
# print(a)
# print(a)
# print(b)

# # Список путей по которым происходит поиск модулей
# pprint.pprint(sys.path)

print('user_ex')

c = usermodule.math.pi

# if __name__ == '__main__':
#     print('user_ex')

