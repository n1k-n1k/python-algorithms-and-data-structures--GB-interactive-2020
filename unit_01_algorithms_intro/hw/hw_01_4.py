"""
Пользователь вводит две буквы.
Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
"""

print('Введите две латинские буквы, по одной в строке.')
letter1 = input('Первая: ')
letter2 = input('Вторая: ')

a_pos, letter1_pos, letter2_pos = map(ord, ('a', letter1, letter2))

print(f'Позиция буквы {letter1} в алфавите: {letter1_pos - a_pos + 1}')
print(f'Позиция буквы {letter2} в алфавите: {letter2_pos - a_pos + 1}')
delta_pos = 0 if letter1 == letter2 else abs(letter2_pos - letter1_pos) - 1
print(f'Между ними находится букв: {delta_pos}')
