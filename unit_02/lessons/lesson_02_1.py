"""
Даны два целых числа: A и В.

Необходимо вывести все числа от A до B включительно, в порядке возрастания,
если A < B, или в порядке убывания, если A > B.

Рекурсивный алгоритм.
"""


def func(a, b):
    if a == b:
        return f'{a}'

    if a > b:
        result = f'{a}, {func(a - 1, b)}'
        return result

    if a < b:
        result = f'{a}, {func(a + 1, b)}'
        return result


print(func(1, 10))
print(func(10, 1))
