"""
Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50).
Выведите на экран исходный и отсортированный массивы.
"""

import random

arr_min = 0
arr_max = 49
array = [random.uniform(arr_min, arr_max) for i in range(arr_min, arr_max + 1)]
print(array)


def merge_sort(array):
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left_list = merge_sort(array[:mid])
    right_list = merge_sort(array[mid:])

    def merge(left_list, right_list):
        result = []
        left_list_i = 0
        right_list_i = 0
        left_list_len = len(left_list)
        right_list_len = len(right_list)

        for _ in range(left_list_len + right_list_len):
            if left_list_i < left_list_len and right_list_i < right_list_len:
                if left_list[left_list_i] <= right_list[right_list_i]:
                    result.append(left_list[left_list_i])
                    left_list_i += 1
                else:
                    result.append(right_list[right_list_i])
                    right_list_i += 1

            elif left_list_i == left_list_len:
                result.append(right_list[right_list_i])
                right_list_i += 1

            elif right_list_i == right_list_len:
                result.append(left_list[left_list_i])
                left_list_i += 1

        return result

    return merge(left_list, right_list)


print(merge_sort(array))
