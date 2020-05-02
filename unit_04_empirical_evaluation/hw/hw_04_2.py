"""
Написать два алгоритма нахождения i-го по счёту простого числа.
Функция нахождения простого числа должна принимать на вход натуральное
и возвращать соответствующее простое число.
Проанализировать скорость и сложность алгоритмов.
Первый — с помощью алгоритма «Решето Эратосфена».
Второй — без использования «Решета Эратосфена».

Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков.
Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.

"""


def simple_sieve(n):
    sieve = [i for i in range(n + 1)]
    sieve[1] = 0

    for i in range(2, n + 1):
        if sieve[i] != 0:
            j = i * 2

            while j <= n:
                sieve[j] = 0
                j += i

    simples = [i for i in sieve if i != 0]
    return simples[-1]


def simple_classic(n):
    simples = []

    for i in range(2, n + 1):
        for j in simples:
            if i % j == 0:
                break
        else:
            simples.append(i)

    return simples[-1]

# Решето Эратосфена
# simple_sieve(1000)
# 1000 loops, best of 5: 23.7 usec per loop

# simple_sieve(1000)
# 1000 loops, best of 5: 287 usec per loop

# simple_sieve(10000)
# 1000 loops, best of 5: 3.23 msec per loop


# классический алгоритм, оптимизированный в части поиска
# делителей только среди уже определённных ранее простых чисел
# simple_classic(100)
# 1000 loops, best of 5: 23.8 usec per loop

# simple_classic(1000)
# 1000 loops, best of 5: 766 usec per loop

# simple_classic(10000)
# 1000 loops, best of 5: 41.4 msec per loop

# вывод: для 100-го простого числе оба алгоритма работают за сопоставимое время,
# для 1 000-го разница составляет 2-3 раза,
# для 10 000-го - 50 раз
# вычислений для 100 000-го классическим алгоритмом не дождался...
