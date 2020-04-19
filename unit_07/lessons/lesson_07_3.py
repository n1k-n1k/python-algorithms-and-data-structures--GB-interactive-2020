"""
Сортировка вставками
"""

import random

size = 10
array = [i for i in range(size)]
random.shuffle(array)
print(array)


def insertion_sort(array):
    count = 0  # счётчик перестановок

    for i in range(1, len(array)):
        spam = array[i]
        j = i

        while array[j - 1] > spam and j > 0:
            array[j] = array[j - 1]
            j -= 1

        array[j] = spam
        count += 1

    print(count)


insertion_sort(array)
print(array)
