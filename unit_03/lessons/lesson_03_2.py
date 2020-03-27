"""
Разделить массив на два массива: с положительными и отрицательными значениями
"""

import random

array = [random.randint(-100, 100) for _ in range(100)]
print(array)

arr_neg = []
arr_pos = []

# при испольщовании генераторов списков в данном случае будет двойной проход по массиву,
# поэтому следует использовать цикл с условиями
for item in array:
    if item > 0:
        arr_pos.append(item)
    elif item < 0:
        arr_neg.append(item)

print()
print(arr_neg)
print(arr_pos)
