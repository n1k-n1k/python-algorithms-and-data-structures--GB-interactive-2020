"""
7. Написать программу, доказывающую или проверяющую, что для множества натуральных чисел
выполняется равенство: 1+2+...+n = n(n+1)/2, где n — любое натуральное число.
"""

n = int(input('Введите натуральное число: '))

left = sum([i for i in range(n + 1)])
right = n * (n + 1) / 2

if left == right:
    print(f'Выражение 1+2+...+n = n(n+1)/2 верно для n = {n}')
else:
    print(f'Выражение 1+2+...+n = n(n+1)/2 НЕ верно для n = {n}')
