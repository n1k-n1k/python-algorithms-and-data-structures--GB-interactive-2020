"""
6. В одномерном массиве найти сумму элементов,
находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""

from random import randint

source = [randint(randint(-10, 0), randint(0, 10)) for _ in range(randint(5, 15))]

max_i = min_i = 0
max_n = min_n = source[0]
sum_n = 0

for i, n in enumerate(source):
    if n > max_n:
        max_n = n
        max_i = i
    if n < min_n:
        min_n = n
        min_i = i

if max_i < min_i:
    max_i, min_i = min_i, max_i

for i in range(min_i + 1, max_i):
    sum_n += source[i]

print(f'source list: {source}')
print(f'min = {min_n}, min_index = {min_i}')
print(f'max = {max_n}, max_index = {max_i}')
print(f'sum([min---max]): {sum_n}')
