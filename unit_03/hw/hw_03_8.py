"""
8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и записывать
ее в последнюю ячейку строки. В конце следует вывести полученную матрицу.
"""

ROWS = 5
COLS = 4

m = [[0 for _ in range(COLS + 1)] for _ in range(ROWS)]
m_rows_sum = [0 for _ in range(ROWS)]
for i in range(ROWS):
    sum_row = 0
    for j in range(COLS):
        m[i][j] = int(input(f'Строка {i + 1}, введите элемент столбца {j + 1}: '))
        sum_row += m[i][j]
    m[i][COLS] = sum_row

for i in range(ROWS):
    print(*m[i], sep='\t')
