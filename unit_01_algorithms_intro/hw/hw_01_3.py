"""
Написать программу, которая генерирует в указанных пользователем границах:
a. случайное целое число,
b. случайное вещественное число,
c. случайный символ.

Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
"""

import random

print('Введите диапазон чисел или латинских букв.')
print('По одному значению в строке.')
a = input('Начало диапазона: ')
b = input('Конец диапазона: ')

if a.isalpha() and b.isalpha():
    a, b = map(ord, (a, b))
    if a > b:
        a, b = b, a
    print(f'Случайная латинская буква: {chr(random.randint(a, b))}')

elif a.isnumeric() and b.isnumeric():
    a, b = map(int, (a, b))
    if a > b:
        a, b = b, a
    print(f'Случайное целое число: {random.randint(a, b)}')

else:
    a, b = map(float, (a, b))
    if a > b:
        a, b = b, a
    print(f'Случайное вещественное число: {random.triangular(a, b)}')
