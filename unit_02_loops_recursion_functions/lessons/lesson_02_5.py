"""
Функция перевода десятичного числа в двоичный формат
"""


def binary(num):
    s = ''
    while num > 0:
        s = f'{num % 2}{s}'
        num //= 2
    return s


# print(binary(255))  # 11111111

# выводить binary-значение, пока пользователь на введёт 0
while True:
    n = int(input('Введите целое [положительное] число [(0 - завершение)]: '))
    if n != 0:
        print(binary(n))
    else:
        break
