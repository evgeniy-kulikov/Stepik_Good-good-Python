#  3.4 Спецсимволы и экранирование символов
""""""


"""
\n - перевод строки
\\ - символ обратного слэша
\' - символ апострофа
\" - символ двойной кавычки
\a - звуковой сигнал
\b - эмуляция клавиши backspace
\f - перевод формата
\r - возврат каретки
\t - горизонтальная табуляция (4 пробела)
\v - вертикальная табуляция
\0 - символ Null (не признак конца строки)
\xhh - символ с шестнадцатеричным кодом hh
\ooo - символ в восьмеричным кодом ооо
\N{id} - идентификатор их кодовой таблицы Unicode
\uhhhh - 16-битный символ Unicode в шестнадцатеричной форме
\Uhhhhhhhh - 32-битный символ Unicode в шестнадцатеричной форме
\другое - не является экранированной последовательностью
"""

# import unicodedata
# \xa0 - NO-BREAK SPACE
# \x20 - SPACE

# спецсимволы имеют длину 1 символ
# например, перевод строки "\n" это 1 символ
text = """hello
python"""
print(text)
print(len(text))

t = "panda needs\npython"
print(t)

# обратный слэш \ - маркер спецсимвола
# \t - табуляция
t = "\t" + t
print(t)

# экранирование
t = "panda \needs\ python"
print(t)
t = "panda \\needs\\ python"
print(t)
path = "D:\Python\Projects\stepik\tex1.py"
print(path)
path = "D:\\Python\\Projects\\stepik\\tex1.py"
print(path)
s = "Марка вина \"Rioja\""
print(s)
s = 'Марка вина \"Rioja\"'
print(s)

# сырые "raw" строки
# добавить r перед строкой, тогда все спецсимволы будут проигнорированы
print("\v")
path = r"D:\Python\Projects\stepik\tex1.py"
print(path)
print("\r")
print("\a")


#  *   *   *   *   *   TASK    *   *   *   *   *


# Task 1
s1, s2 = input().split()
print(s1 + "\\" + s2)

# Task 4
# Variant 1
s = input().split()
print(s[0] + '\'' + s[1] + '\"' + s[2] + '\"' + s[3] + '\"' + s[4])

# Variant 2
s = input()
print(s.replace(' ', '\'', 1).replace(' ', '\"'))
