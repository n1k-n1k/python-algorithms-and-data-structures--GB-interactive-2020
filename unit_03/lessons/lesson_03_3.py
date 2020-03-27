"""
Вставка элемента в произвольное место массива
"""

import random

array = [random.randint(-100, 100) for _ in range(100)]
print(array)

num = int(input('Введите целое число для вставки: '))
pos = int(input('На какую позицию вставить число: '))

array.append(None)  # добавляем в конец массива пустой элемент
i = len(array) - 1

while i > pos:
    array[i], array[i - 1] = array[i - 1], array[i]  # сдвигаем элементы в конец
    i -= 1

array[pos] = num
print()
print(array)

'''
# встроенная функция вставки, работу которой мы реализовали
array.insert(pos, num)

# можно реализовать вставку организацией нового массива, но это требует в 2 раза больше памяти
new_array = array[:pos] + [num] + array[pos:]
'''
