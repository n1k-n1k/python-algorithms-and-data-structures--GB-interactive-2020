"""
Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
Найдите в массиве медиану.

Медианой называется элемент ряда, делящий его на две равные части:
в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.

Примечание: задачу можно решить без сортировки исходного массива.
Но если это слишком сложно, используйте метод сортировки,
который не рассматривался на уроках (сортировка слиянием также недопустима).
"""

import random


# Сортировка кучей
def heap_sort(array):
    n = len(array)

    for i in range(n, -1, -1):
        heapify(array, n, i)

    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)


def heapify(array, heap_size, root_ind):
    max_ind = root_ind
    left_child_ind = (2 * root_ind) + 1
    right_child_ind = (2 * root_ind) + 2

    if left_child_ind < heap_size and array[left_child_ind] > array[max_ind]:
        max_ind = left_child_ind

    if right_child_ind < heap_size and array[right_child_ind] > array[max_ind]:
        max_ind = right_child_ind

    if max_ind != root_ind:
        array[root_ind], array[max_ind] = array[max_ind], array[root_ind]
        heapify(array, heap_size, max_ind)


arr_min = 0
arr_max = 100
m = int(input('Введите m: '))

array = [random.randint(arr_min, arr_max) for i in range(2 * m + 1)]
print(f'Исходный несортированный массив:\n{array}')
heap_sort(array)
print(f'Отсортированный массив:\n{array}')
print(f'Медиана = {array[m]}')
