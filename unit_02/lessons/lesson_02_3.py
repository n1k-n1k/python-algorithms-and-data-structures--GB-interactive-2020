"""
Алгоритм Евклида.

Задача. Найти наибольший общий делитель (НОД, greatest common divisor, gcd) пары чисел.

Вариант 1. Простейший циклический алгоритм основанный на вычитании.
Вариант 2. Рекурсивный алгоритм основанный на нахождении остатка от деления.
Вариант 3. Циклический алгоритм основанный на нахождении остатка от деления.
"""


# Вариант 1
def gcd_sub(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


# Вариант 2
def gcd_recursive(a, b):
    if b == 0:
        return a
    return gcd_recursive(b, a % b)


# Вариант 3
def gcd_iterative(a, b):
    while b != 0:
        a, b = b, a % b
    return a


print(gcd_sub(54, 24))  # 6
print(gcd_recursive(540, 24458732646))  # 6
print(gcd_iterative(540, 24458732646))  # 6
