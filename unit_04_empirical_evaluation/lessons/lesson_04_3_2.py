"""
Поиск чисел Фибоначч с сохранением в list и в dict
Мемоизация
"""

import cProfile


def test_fib(func):
    lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    for i, item in enumerate(lst):
        assert item == func(i)
        print(f'Test {i} OK')


def fib_list(n):
    fib_l = [None] * 1000
    fib_l[:2] = [0, 1]

    def _fib_list(n):
        if fib_l[n] is None:
            fib_l[n] = _fib_list(n - 1) + _fib_list(n - 2)
        return fib_l[n]

    return _fib_list(n)


test_fib(fib_list)
