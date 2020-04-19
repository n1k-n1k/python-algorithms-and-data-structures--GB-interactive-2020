"""
Сортировка Шелла
"""

import random

size = 10
array = [i for i in range(size)]
random.shuffle(array)
print(array)


def shell_sort(array):
    assert len(array) < 4000, 'Массив слишком большой. Используйте другую сортировку'

    def new_increment(array):

        inc = [1, 4, 10, 23, 57, 132, 301, 701, 1750]

        while len(array) <= inc[-1]:
            inc.pop()

        while len(inc) > 0:
            yield inc.pop()

    count = 0  # счётчик перестановок

    for increment in new_increment(array):
        for i in range(increment, len(array)):
            for j in range(i, increment - 1, -increment):
                if array[j - increment] <= array[j]:
                    break
                array[j], array[j - increment] = array[j - increment], array[j]
                count += 1

    print(count)

shell_sort(array)
print(array)
