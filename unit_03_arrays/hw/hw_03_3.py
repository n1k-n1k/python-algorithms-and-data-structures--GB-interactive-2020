"""
3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""

from random import randint, shuffle

source = [i for i in range(0, randint(2, 10))]
shuffle(source)
print(f'source list:\t{source}')

max_i = min_i = 0
max_n = min_n = source[0]

for i, n in enumerate(source):
    if n > max_n:
        max_n = n
        max_i = i
    if n < min_n:
        min_n = n
        min_i = i

source[max_i], source[min_i] = source[min_i], source[max_i]
print(f'result list:\t{source}')
