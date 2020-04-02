"""
9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""

from random import randint

ROWS = 5
COLS = 5
RAND_RANGE = (0, 50)

m = [[randint(*RAND_RANGE) for _ in range(COLS)] for _ in range(ROWS)]
m_cols_min = [RAND_RANGE[1] + 1 for _ in range(COLS)]
max_elem = RAND_RANGE[0] - 1

for j in range(COLS):
    for i in range(ROWS):
        if m[i][j] < m_cols_min[j]:
            m_cols_min[j] = m[i][j]
    if m_cols_min[j] > max_elem:
        max_elem = m_cols_min[j]

for i in range(ROWS):
    print(*m[i], sep='\t')

print()
print(max_elem)
