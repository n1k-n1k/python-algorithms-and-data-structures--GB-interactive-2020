"""
Пользователь вводит данные о количестве предприятий, их наименования
и прибыль за четыре квартала для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
"""

# Продолжаем считать пользователя идеальным

from collections import namedtuple

comp_cnt = int(input('Введите количество предприятий: '))
comps = []
comps_above = []
comps_below = []
comps_eq = []
profit_all = 0

Company = namedtuple('Company', ['name', 'profit'])

for i in range(comp_cnt):
    name = input(f'Название {i + 1}-й компании: ')
    profit = sum([float(input(f'Прибыль компании за {j}-й квартал: ')) for j in '1234'])
    profit_all += profit
    c = Company(name, profit)
    comps.append(c)

profit_all_avg = profit_all / comp_cnt

for c in comps:
    if c.profit < profit_all_avg:
        comps_below.append(c)
    elif c.profit > profit_all_avg:
        comps_above.append(c)
    else:
        comps_eq.append(c)

print()
print(f'Средняя прибыль за год по всем компаниям: {profit_all_avg:.2f}')

if comps_above:
    print(f'Компании с прибылью выше средней:')
    for c in comps_above:
        print(f'{c.name}: {c.profit:.2f}')
    print()

if comps_eq:
    print(f'Компании с прибылью равной средней:')
    for c in comps_eq:
        print(f'{c.name}: {c.profit:.2f}')
    print()

if comps_below:
    print(f'Компании с прибылью ниже средней:')
    for c in comps_below:
        print(f'{c.name}: {c.profit:.2f}')
