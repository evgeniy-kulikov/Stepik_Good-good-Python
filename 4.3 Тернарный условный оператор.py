# 4.3 Тернарный условный оператор

"""
Имеется список базовых нот:
m = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']
Вводятся три целых числа в диапазоне от 1 до 7 - номера нот, в одну строчку через пробел.
Необходимо отобразить указанные ноты в виде строки через пробел,
но перед нотами до и фа дополнительно ставить символ диеза '#'
"""
a, b, c = map(int, input().split())
m = ['#', 'до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']
d1 = (m[a], '#' + m[a])[a in (1, 4)]
d2 = (m[b], '#' + m[b])[b in (1, 4)]
d3 = (m[c], '#' + m[c])[c in (1, 4)]
print(d1, d2, d3)

# Мой другой вариант
s = list(map(int, input().split()))
m = ['#', 'до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']
lst = []
for el in s:
    lst.append((m[el], '#' + m[el])[el in (1, 4)])
print(*lst)  # '*' распаковывает список в строку [1, a, 3, b]  --> 1 a 3 b
