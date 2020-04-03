"""
Рекурсивный поиск чисел Фибоначчи
"""

import cProfile


def test_fib(func):
    lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    for i, item in enumerate(lst):
        assert item == func(i)
        print(f'Test {i} OK')


def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


# timeit
# в терминале:
# python -m timeit -n 1000 -s "import lesson_04_2" "lesson_04_2.fib(10)"

# "lesson_04_2.fib(10)"
# 1000 loops, best of 5: 20.1 usec per loop

# "lesson_04_2.fib(15)"
# 1000 loops, best of 5: 216 usec per loop

# "lesson_04_2.fib(20)"
# 1000 loops, best of 5: 2.51 msec per loop


cProfile.run('fib(20)')

# cProfile
# fib(10)
# 180 function calls (4 primitive calls) in 0.000 seconds
# 177/1    0.000    0.000    0.000    0.000 lesson_04_2.py:16(fib)

# fib(15)
# 1976 function calls (4 primitive calls) in 0.001 seconds
# 1973/1    0.001    0.000    0.001    0.001 lesson_04_2.py:16(fib)

# fib(20)
# 21894 function calls (4 primitive calls) in 0.006 seconds
# 21891/1    0.005    0.000    0.005    0.005 lesson_04_2.py:16(fib)
