"""
7. В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба минимальны), так и различаться.
"""

from random import randint

source = [randint(randint(-10, 0), randint(0, 10)) for _ in range(randint(5, 15))]

if source[0] < source[1]:
    min1 = source[0]
    min2 = source[1]
else:
    min1 = source[1]
    min2 = source[0]

for s in source:
    if s <= min1 <= min2:
        min2 = min1
        min1 = s
    elif min1 <= s <= min2:
        min2 = s

print(f'source list:\t{source}')
print(f'min1:\t{min1}')
print(f'min2:\t{min2}')
