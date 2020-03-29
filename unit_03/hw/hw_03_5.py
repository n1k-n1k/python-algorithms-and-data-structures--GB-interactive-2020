"""
5. В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию в массиве.

Примечание к задаче: пожалуйста не путайте «минимальный»
и «максимальный отрицательный». Это два абсолютно разных значения.
"""

from random import randint

source = [randint(randint(-10, 0), randint(0, 10)) for _ in range(randint(5, 15))]
print(f'source list: {source}')

result = sorted([(s, i) for i, s in enumerate(source) if s < 0])[-1]
print(f'max negative = {result[0]} with index = {result[1]}')
