"""
Сортировка выбором
"""

import random

size = 10
array = [i for i in range(size)]
random.shuffle(array)
print(array)


def selection_sort(array):
    count = 0  # счётчик перестановок

    for i in range(len(array)):
        idx_min = i

        for j in range(i + 1, len(array)):
            if array[j] < array[idx_min]:
                idx_min = j
                count += 1

        array[idx_min], array[i] = array[i], array[idx_min]

    print(count)


selection_sort(array)
print(array)
