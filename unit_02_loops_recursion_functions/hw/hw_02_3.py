"""
3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, надо вывести 6843.
"""


def reverse(x):
    tmp = ''
    while x != 0:
        tmp += str(x % 10)
        x //= 10
    return int(tmp)


n = int(input('Введите натуральное число: '))
print(f'Обратное по порядку цифр число: {reverse(n)}')
