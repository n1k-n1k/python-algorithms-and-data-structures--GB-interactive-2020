"""
9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
Вывести на экран это число и сумму его цифр.
"""

n = int(input('Введите количество натуральных чисел: '))
nums = [input(f'Введите {i + 1}-е число: ') for i in range(n)]

res_max = 0
res_sum = 0

for i in nums:
    tmp_sum = sum(map(int, list(i)))
    if tmp_sum >  res_sum:
        res_sum = tmp_sum
        res_max = i

print(f'Масимальное по сумме цифр - число {res_max}: сумма цифр = {res_sum}')
