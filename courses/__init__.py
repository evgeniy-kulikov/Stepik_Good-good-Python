#  8.4 Пакеты (package) в Python
""""""

"""
__init__.py  это инициализатор пакета, указывающий что нужно импортировать
"""


# абсолютный импорт (указывается полный путь)
# Функция "get_python" добавляется в пространство имен всего пакета "courses"
# from courses.python import get_python

# варианты импорта в файл __init__.py
# нужно указывать абсолютный или относительный путь

# Относительный путь
# import courses.java
# import java
# from courses.java import *



# # относительный импорт (РЕКОМЕНДУЕТСЯ (вдруг имя пакета в дальнейшем поменяется))
# # только через from
# from .python import get_python
from . import html, java, python


# # внутри пакетов допустимо делать импорт всего содержимого модуля
# from .php import *

#  Импортируем подпакет "doc"
# from .doc import *

NAME = "package courses"


