"""
Решето Эратосфена.

Задача. Найти простые числа до заданного числа N.
"""


# по коду урока -- до N НЕ ВКЛЮЧИТЕЛЬНО
def simples_excl_n(n):
    sieve = [i for i in range(n)]
    sieve[1] = 0

    for i in range(2, n):
        if sieve[i] != 0:
            j = i * 2

            while j < n:
                sieve[j] = 0
                j += i

    result = [i for i in sieve if i != 0]
    return result


# правки для "до N включительно"
# "range(n)" --> "range(n + 1)" и "while j < n" --> "while j <= n"
def simples_incl_n(n):
    sieve = [i for i in range(n + 1)]
    sieve[1] = 0

    for i in range(2, n + 1):
        if sieve[i] != 0:
            j = i * 2

            while j <= n:
                sieve[j] = 0
                j += i

    result = [i for i in sieve if i != 0]
    return result


# 41 - простое число
print(simples_excl_n(41))  # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
print(simples_incl_n(41))  # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
