"""
2. Во втором массиве сохранить индексы четных элементов первого массива.
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, второй массив
надо заполнить значениями 0, 3, 4, 5 (помните, что индексация начинается
с нуля), т. к. именно в этих позициях первого массива стоят четные числа.
"""

from random import randint

source = [randint(0, randint(0, 10)) for _ in range(randint(2, 10))]
even_indexes = [i for i, n in enumerate(source) if not n % 2]

print(f'source list:\t\t\t\t{source}')
print(f'indexes of even elements:\t{even_indexes}')
