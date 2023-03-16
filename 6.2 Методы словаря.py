# 6.2 Методы словаря
""""""

"""
Вводится строка из русских букв и символов пробела. Необходимо ее закодировать азбукой Морзе,
где каждой букве ставится в соответствие код из точки и тире.
После каждой закодированной буквы должен стоять пробел.
После последнего кода пробела быть не должно (в конце строки).
Input: Сергей Балакирев
Output: ... . .-. --. . .--- -...- -... .- .-.. .- -.- .. .-. . .--
"""
morze = {'а': '.-', 'б': '-...', 'в': '.--', 'г': '--.', 'д': '-..', 'е': '.', 'ё': '.', 'ж': '...-', 'з': '--..',
         'и': '..', 'й': '.---', 'к': '-.-', 'л': '.-..', 'м': '--', 'н': '-.', 'о': '---', 'п': '.--.', 'р': '.-.',
         'с': '...', 'т': '-', 'у': '..-', 'ф': '..-.', 'х': '....', 'ц': '-.-.', 'ч': '---.', 'ш': '----',
         'щ': '--.-', 'ъ': '--.--', 'ы': '-.--', 'ь': '-..-', 'э': '..-..', 'ю': '..--', 'я': '.-.-', ' ': '-...-'}

s_in, s_out = input().lower(), ""

for el in s_in:
    s_out += morze.get(el) + " "
print(s_out[:-1])

# Вариант
s_in = input().lower()
s_out = [morze.get(el) for el in s_in if el in morze]
print(*s_out)



"""
Имеется закодированная строка с помощью азбуки Морзе. Коды разделены между собой пробелом. 
Необходимо ее раскодировать.
Input:  .-- ... . -...- .-- . .-. -. ---
Output: все верно
"""
morze = {'а': '.-', 'б': '-...', 'в': '.--', 'г': '--.', 'д': '-..', 'е': '.', 'ё': '.', 'ж': '...-', 'з': '--..',
         'и': '..', 'й': '.---', 'к': '-.-', 'л': '.-..', 'м': '--', 'н': '-.', 'о': '---', 'п': '.--.', 'р': '.-.',
         'с': '...', 'т': '-', 'у': '..-', 'ф': '..-.', 'х': '....', 'ц': '-.-.', 'ч': '---.', 'ш': '----',
         'щ': '--.-', 'ъ': '--.--', 'ы': '-.--', 'ь': '-..-', 'э': '..-..', 'ю': '..--', 'я': '.-.-', ' ': '-...-'}

s_in, s_out = input().split(), ""
# В словаре "morze" меняем местами ключ - значение
reversed_morze = {val: key for key, val in morze.items()}
# вынужденный отказ от буквы "ё"
reversed_morze['.'] = 'е'
for el in s_in:
        s_out += reversed_morze.get(el)
print(s_out)

# Вариант без переворота словаря
s_in, s_out = input().split(), []
for el in s_in:
    s_out += [key for key, value in morze.items() if el == value and key != 'ё']
print(''.join(map(str, s_out)))  # способ преобразовать список в строку


"""
Вводится список целых чисел в одну строчку через пробел. 
С помощью словаря выделите только уникальные (не повторяющиеся) введенные значения и, 
затем, сформируйте список из уникальных чисел. 
Выведите его на экран в виде набора чисел, записанных через пробел.
Input:  8 11 -4 5 2 11 4 8
Output: 8 11 -4 5 2 4
"""
s_in = input().split()
d = dict.fromkeys(s_in)
print(*d.keys())


"""
Вводятся данные в формате:
<день рождения 1> имя_1
<день рождения 2> имя_2
...
<день рождения N> имя_N

Дни рождений и имена могут повторяться. На их основе сформировать словарь и вывести его в формате (см. пример ниже):
день рождения 1: имя1, ..., имяN1
день рождения 2: имя1, ..., имяN2
...
день рождения M: имя1, ..., имяNM
Input:  
3 Сергей
5 Николай
4 Елена
7 Владимир
5 Юлия
4 Светлана
Output: 
3: Сергей
5: Николай, Юлия
4: Елена, Светлана
7: Владимир
"""
import sys
lst_in = list(map(str.strip, sys.stdin.readlines()))
d = {}
lst_out = [el.split() for el in lst_in]
# [['3', 'Сергей'], ['5', 'Николай'], ['4', 'Елена'], ['7', 'Владимир'], ['5', 'Юлия'], ['4', 'Светлана']]

for el in lst_out:
    d.setdefault(el[0], []).append(el[1])
    # {'3': ['Сергей'], '5': ['Николай', 'Юлия'], '4': ['Елена', 'Светлана'], '7': ['Владимир']}

for el in d.items():
    print(f"{el[0]}: {', '.join(map(str, el[1]))}")

# for key, value in d.items():
#     print(f"{key}: {', '.join(map(str, value))}")


# Улучшенный вариант
import sys
lst_in = list(map(str.strip, sys.stdin.readlines()))
d = {}

for el in lst_in:
    el = el.split()
    d.setdefault(el[0], []).append(el[1])

for key, value in d.items():
    print(f"{key}: {', '.join(map(str, value))}")

"""
 Имеется словарь "things" с наименованиями предметов и их весом (в граммах):

things = {'карандаш': 20, 'зеркальце': 100, 'зонт': 500, 'рубашка': 300, 
          'брюки': 1000, 'бумага': 200, 'молоток': 600, 'пила': 400, 'удочка': 1200,
          'расческа': 40, 'котелок': 820, 'палатка': 5240, 'брезент': 2130, 'спички': 10}

Сергей собирается в поход и готов взвалить на свои хрупкие плечи максимальный вес в N кг (вводится с клавиатуры). 
Он решил класть в рюкзак предметы в порядке убывания их веса (сначала самые тяжелые, затем, все более легкие) так, 
чтобы их суммарный вес не превысил значения N кг. 
Все предметы даны в единственном экземпляре. 
Выведите список предметов (в строчку через пробел), которые берет с собой Сергей в порядке убывания их веса.

Input:  10
Output: палатка брезент удочка брюки пила карандаш спички
"""
things = {'карандаш': 20, 'зеркальце': 100, 'зонт': 500, 'рубашка': 300,
          'брюки': 1000, 'бумага': 200, 'молоток': 600, 'пила': 400, 'удочка': 1200,
          'расческа': 40, 'котелок': 820, 'палатка': 5240, 'брезент': 2130, 'спички': 10}
d = {}
num = int(input()) * 1000
max_num = 0
# Сортируем словарь по значению
sorted_things = dict(sorted(things.items(), key=lambda item: item[1], reverse=True))
# sorted_things = sorted([[value, key] for key, value in things.items()], reverse=True)

for key, value in sorted_things.items():
    max_num += value
    if max_num > num:
        max_num -= value
    else:
        d[key] = value
print(*d.keys())

# Вариант
n = int(input()) * 1000
result = []
for el in sorted(things.values(), reverse=True):
    if el <= n:
        result.append(el)  # [5240, 2130, 1200, 1000, 400, 20, 10]
        n -= el
for el in result:
    for k, v in things.items():
        if el == v:
            print(k, end=' ')
