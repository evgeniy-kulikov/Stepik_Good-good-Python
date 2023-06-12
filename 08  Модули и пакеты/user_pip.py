# 8.3 Установка сторонних модулей. Пакетная установка

import sys
from pprint import pprint

# Работа в терминале
# перечень установленных пакетов
# pip list

# Обновления
# pip freeze | %{$_.split('==')[0]} | %{pip install --upgrade $_}

# pip help

# pip install ...
# pip install <имя пакета>
# pip install flask

# pip install <имя пакета>==<номер версии>
# pip install flask==1.1.2

# pip uninstall ...

pprint(sys.path)

# создание файла для пакетной установки
# pip freeze > requirements.txt

# установка пакета модулей из файла:
# pip install -r requirements.txt
