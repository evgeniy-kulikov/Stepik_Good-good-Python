# 10.6 Конструкция match/case со словарями и множествами
""""""

# Для словарей достаточно наличие указанных ключей. Соответствие количества ключей не обязательно.
dic_1 = {'key1': 'val_1', 'key2': 'val_2', 'key3': 3, 'key4': True}

match dic_1:
    case {'key1': a, 'key3': b}:
        print(f'key1 = {a}  key3 = {b}')
    case _:
        print("нет данных")

# Проверка типа данных
dic_2 = {'key1': 'val_1', 'key2': 'val_2', 'key3': 3, 'key4': True}

match dic_2:
    # case {'key1': str() as a, 'key3': int(b), 'key4': True | False}:  # True | False  - допустимые значения ключа 'key4'
    case {'key1': str() as a, 'key3': int(b),} | {'key1': str(a),'key3': int(b), 'key4': True | False}:

        print(f'key1 = {a}  key3 = {b}')
    case _:
        print("нет данных")

dic_3 = {'key1': 'val_1', 'key2': 5, 'key3': 100}


match dic_3:
    # case {'key1': str() as a, 'key2': int(b), 'key3': 100 | 200}:  # key1= val_1,  key2= 5
    case {'key1': str() as a, 'key2': int(b), 'key3': 50 | 200}:  # нет данных
        print(f'key1= {a},  key2= {b}')
    case _:
        print("нет данных")

# Проверка параметров входного словаря
dic_4 = {'key1': 'val_1', 'key2': 5, 'key3': 100}

match dic_4:
    case {'key1': str() as a, 'key2': int(b)} if len(dic_4) <= 3:  # key1= val_1,  key2= 5
        print(f'key1= {a},  key2= {b}')
    case _:
        print("нет данных")

# Проверка параметров кейса
dic_5 = {'key1': 'val_1', 'key2': 5, 'key3': 100, 'key4': 200}

match dic_5:
    case {'key1': str(a), 'key2': int(b), **kwargs} if len(kwargs) <= 1:
        print(f'key1= {a},  key2= {b}')
    case _:
        print("нет данных")  # нет данных

dic_5 = {'key1': 'val_1', 'key2': 5}
match dic_5:
    case {'key1': str(a), 'key2': int(b), **kwargs} if not kwargs:
        print(f'key1= {a},  key2= {b}')  # key1= val_1,  key2= 5
    case _:
        print("нет данных")  # key1= val_1,  key2= 5

# Срабатывания кейса в зависимости от значения ключа 'type': 'list'
dic_6 = {'key1': 'val_1', 'type': 'list', 'data_ls': [1, 2, 3]}
match dic_6:
    case {'type': 'list', 'data_ls': list() as ls}:
        print(f'Данные: type_list= {ls}')  # Данные: type_list= [1, 2, 3]
    case _:
        print("нет данных")

# Срабатывания кейса в зависимости от значения ключа 'type': 'list'
dic_6 = {'key1': 'val_1', 'type': 'list', 'data_ls': [1, 2, 3]}
match dic_6:
    case {'type': 'list', 'data_ls': list() as ls}:
        print(f'Данные: type_list= {ls}')  # Данные: type_list= [1, 2, 3]
    case _:
        print("нет данных")


# Срабатывания кейса в зависимости от значения ключа 'flag': True
json_data = {'flag': True, 'info': ['2023-07-05', {'log': '123', 'email': 'user@post.ru'}, True, 5]}
match json_data:
    case {'flag': True, 'info': [_, {'email': email}, _, _]}:
        print(f'Данные_dict: {email}')  # Данные_dict: user@post.ru
    case _:
        print("нет данных")


# Множество
set_keys = {1, 2, 3}
match set_keys:
    case set() as keys if len(keys) == 3:
        print(f'Данные ключей: {keys}')  # Данные ключей: {1, 2, 3}
    case _:
        print("нет данных")


#
#  *   *   *   *   *   TASK    *   *   *   *   *
#


# 02
"""
Отметьте все шаблоны, которые срабатывают только при возрасте age равным 22. 
"""

json_data = {'fio': 'sm_b', 'marks': [2, 2, 3, 2, 3, 4], 'age': 22}

match json_data:
    # case {'marks': ms, 'age': age, 'fio': fio} if age == 22:  # только при возрасте age равным 22
    # case {'marks': ms, 'age': age} if age == 22:  # только при возрасте age равным 22
    # case {'marks': m, 'age': 22}:  # только при возрасте age равным 22
    case {'fio': fio, 'marks': ms, 'age': age}:  # при любом значении ключа 'age'
        print('age == 22')
    case _:
        print("нет")


# 03
"""
Отметьте все шаблоны, которые срабатывают 
только если в оценках marks имеются хотя бы две двойки (от двух и более).
"""

json_data = {'fio': 'sm_b', 'marks': [2, 2, 3, 2, 3, 4], 'age': 22}

match json_data:
    # case {'marks': ms, 'age': age, 'fio': fio} if ms.count(2) > 1:  # да
    # case {'marks': ms, 'fio': str(fio)} if ms.count(2) > 1:  # да
    # case {'marks': ms, 'age': age} if ms.count(2) > 1:  # да
    case {'marks': ms, 'age': int() | float() as age, 'fio': fio} if ms.count(2) > 1:  # да
        print('да')
    case _:
        print("нет")


# 04
"""
С помощью оператора match/case в функцию parse_json добавьте в самое начало шаблон 
для выделения значения ключа access с проверкой на тип bool 
и для выделения даты (первое значение списка) из поля data с проверкой, что data является списком. 
Возвратите выделенные два значения в виде кортежа в формате (access, date).
"""
def parse_json(data):
    match data:
        # здесь прописывайте шаблон
        case {'access': bool(a), 'data': list() as ls}:
            return a, ls[0]

        # Вариант
        case {'access': bool(a), 'data': list([dt, {}, _])}:
            return a, dt

        case {'id': ids, 'data': [_, {'login': login}, _, _]}:
            return ids, login
    return None

json_data = {'id': 2, 'access': False, 'data': ['26.05.2023', {'login': '1234', 'email': 'xxx@mail.com'}, 2000, 56.4]}


# 05
"""
С помощью оператора match/case в функцию parse_json добавьте в самое начало шаблон 
для выделения значений ключей login и email с проверкой, что они являются строками 
и при условии, что поле access принимает значение True. 
Возвратите выделенные два значения в виде кортежа в формате (login, email).

!!! В условии не указывается, что список может иметь произвольную длину. По этому пишем в конце 'data' распаковку *_
"""
def parse_json(data):
    match data:
        # здесь прописывайте шаблон
        case {'access': True, 'data': [_, {'login': str(login), 'email': str(email)}, *_]}:
            return login, email

        case {'id': ids, 'data': [_, {'login': login}, _, _]}:
            return ids, login

    return None

json_data = {'id': 2, 'access': True, 'data': ['26.05.2023', {'login': '1234', 'email': 'xxx@mail.com'}, 2000, 56.4]}

