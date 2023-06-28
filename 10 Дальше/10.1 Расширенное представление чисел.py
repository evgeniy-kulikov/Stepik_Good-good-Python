# 10.1 Расширенное представление чисел
""""""

"""
10-я система: всем понятно

EXP (Экспоненциальный формат):  1e2 = 100,  1e-2 = 0.01

2-ная система: префикс - 0b, суффикс - только нули и единицы

8-ная система: префикс - 0o, суффикс - цифры от 0 до 7

16-наяя система: префикс - 0x, суффикс - цифры от 0 до 9 и буквы  A(10), B(11), C(12), D(13), E(14), F(15)
"""


# 10-я система:
"""
Используется десять цифр 0 - 9  т.е. основание 10
 2 1 0 - разряды степени для десяти: 10 в степени
 1 2 3 - число
 123 = 1 * 10^2 + 2 * 10^1 + 3 * 10^0 = 1*100 + 2*10 + 3*1 = 100 + 20 + 3
"""

# 2-ная система
"""
Используется две цифры 0, 1  (биты)  т.е. основание 2
Перевод из двоичной в десятичную
 2 1 0
 0 0 1 = 0 * 2^2 + 0 * 2^1 + 1 * 2^0 = 1
 
 3210
 1101 = 1*2^3 + 1*2^2 + 0*2^1 + 1*2^0 = 1*8 + 1*4 + 0*2 + 1*1 = 13 
 
 76543210
 10001101 = 1*2^7 + 1*2^3 + 1*2^2 + 1*2^0 = 128 + 8 + 4 + 1 = 141
"""

# перевод из двоичной в десятичную:
# 1*2**5 + 1*2**4 + 0*2**3 + 0*2**2 + 1*2**1 + 1*2**0 = 51
b = 0b110011  # 51

b = -0b1111  # -15


# перевод из 10-ной в двоичную
# 14 % 2 = "0"; 14//2 = 7; 7 % 2 = "1"; 7//2 = 3; 3 % 2 = "1"; 3//2 = 1; 1 % 2 = "1"; 1//2 = 0
a = bin(14)  # 0b1110


# Шестнадцатеричная система
"""
цифры от 0 до 9 и буквы  A(10), B(11), C(12), D(13), E(14), F(15)
0 - 9, A, B, C, D, E, F  т.е. основание 16

1A = 1*16^1 + A*16^0 = 1*16 + 10*1 = 26 

FB = F*16^1 + B*16^0 = 15*16 + 11*1 = 240 + 11 = 251

3210
C2DE = C*16^3 + 2*16^2 + D*16^1 + E*16^0 = 12*4096 + 2*256 + 13*16 + 14*1 = 49152 + 512 + 208 + 14 = 49886
"""
# перевод из 16-ной в 10-ную
# 3*16**4 + 2*16**3 + 1*16**2 + 12*16**1 + 0*16**0 = 205248
f = 0x321c0  # 205248

b = -0x34a  # -842


# восьмеричная система, положительные числа
"""
Используется  цифры 0, 7  т.е. основание 8

27 = 2*8^1 + 7*8^0 =23
"""
e = 0o123  # 83

# отрицательные
e = -0o17  # -15



# запись в обратном порядке: 1110
b = oct(779)  # '0o1413'
c = hex(779)  # '0x30b'


# дробные числа:
# 1234.567 = 1000 + 200 + 30 + 4 + 0.5 + 0.06 + 0.007 = 1·103+2·102+3·101+4·100+5·10-1+6·10-2+7·10-3

g = 5.4e8  # 540000000.0

h = 2.71e-7  # 2.71e-07


# перевод из любой системы счисления, от 2 до 36
x = int('11011', 5)  # 756

