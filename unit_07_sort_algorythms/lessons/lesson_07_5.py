"""
Быстрая сортировка Хоара
"""

import random

size = 10
array = [i for i in range(size)]
random.shuffle(array)
print(array)


def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = random.choice(array)
    s_ar = []
    m_ar = []
    l_ar = []

    for item in array:

        if item < pivot:
            s_ar.append(item)
        elif item > pivot:
            l_ar.append(item)
        elif item == pivot:
            m_ar.append(item)
        else:
            raise Exception('Случилось непредвиденное')

    return quick_sort(s_ar) + m_ar + quick_sort(l_ar)


def quick_sort_no_memory(array, fst, lst):
    if fst > lst:
        return

    pivot = array[random.randint(fst, lst)]
    i, j = fst, lst

    while i <= j:

        while array[i] < pivot:
            i += 1

        while array[j] > pivot:
            j -= 1

        if i <= j:
            array[i], array[j] = array[j], array[i]
            i, j = i + 1, j - 1

    quick_sort_no_memory(array, fst, j)
    quick_sort_no_memory(array, i, lst)


array_new = quick_sort(array)
print(array_new)

print('*' * 50)
print(array)
quick_sort_no_memory(array, 0, len(array) - 1)
print(array)
