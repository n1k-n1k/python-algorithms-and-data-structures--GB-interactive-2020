"""
5. В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию в массиве.

Примечание к задаче: пожалуйста не путайте «минимальный»
и «максимальный отрицательный». Это два абсолютно разных значения.
"""

from random import randint

source = [randint(randint(-10, 0), randint(0, 10)) for _ in range(randint(5, 15))]
print(f'source list: {source}')

negatives = [s for s in source if s < 0]
if not negatives:
    print('There are no negative numbers in source list')

else:
    max_n = negatives[0]
    max_i = source.index(max_n)

    for i, n in enumerate(source):
        if max_n < n < 0:
            max_n = n
            max_i = i

    print(f'max negative = {max_n} with index = {max_i}')
