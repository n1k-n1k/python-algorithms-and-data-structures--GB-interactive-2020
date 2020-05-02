"""
Виды алгоритмов, оценка сложности
cProfile
"""

import cProfile


def get_len(array):
    return len(array)


def get_sum(array):
    s = 0
    for i in array:
        s += i
    return s


def main():
    lst = [i for i in range(10000000)]
    a = get_len(lst)
    b = get_sum(lst)


cProfile.run('main()')
