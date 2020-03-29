"""
3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""

from random import randint, shuffle

source = [i for i in range(0, randint(2, 10))]
shuffle(source)
print(f'source list:\t{source}')

min_i = source.index(min(source))
max_i = source.index(max(source))
source[max_i], source[min_i] = source[min_i], source[max_i]
print(f'result list:\t{source}')
