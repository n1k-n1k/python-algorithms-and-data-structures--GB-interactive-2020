"""
Задача.
Пользователь вводит количество предприятий, названия, плановую и фактическую прибыль каждого предприятия.
Вычислить процент выполнения плана и вывести данные с предварительной фильтрацией.
"""

k = int(input('Введите количество предприятий: '))
enterpises = {}

for i in range(1, k + 1):
    name = input('Введите название предприятия: ')
    enterpises[name] = [float(input('План: ')), float(input('Факт: '))]
    enterpises[name].append(enterpises[name][1] / enterpises[name][0])

print('Фактическая прибыть больше 10, но план не выполнен (меньше 100%)')

for key, value in enterpises.items():
    if value[1] > 10 and value[2] < 1:
        print(f'Предприятие {key} заработало {value[1]}, что составило {value[2] * 100:.2f}%')
