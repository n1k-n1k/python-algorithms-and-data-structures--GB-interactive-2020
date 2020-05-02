"""
Определение количества различных подстрок с использованием хеш-функции.
Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.

Примечания:
* в сумму не включаем пустую строку и строку целиком;
* задача считается решённой, если в коде использована функция вычисления хеша
(hash(), sha1() или любая другая из модуля hashlib)
"""

import hashlib


def rabin_karp_mod(s: str, subs: str, start: int) -> int:
    assert len(s) > 0 and len(subs) > 0, 'Строки не могут быть пустые'
    assert len(s) > len(subs), 'Подстрока должна быть короче строки'

    len_subs = len(subs)
    h_subs = hashlib.sha1(subs.encode('utf-8')).hexdigest()

    for i in range(start, len(s) - len_subs + 1):
        if h_subs == hashlib.sha1(s[i:i + len_subs].encode('utf-8')).hexdigest():

            if s[i:i + len_subs] == subs:
                return i

    return -1


def subs_count(s: str, subs: str) -> int:
    start = 0
    count = 0
    len_s = len(s)
    len_subs = len(subs)

    while start < len_s:
        pos = rabin_karp_mod(s, subs, start)
        if pos != -1:
            count += 1
            start = pos + len_subs
        else:
            break

    return count


s_1 = input('Введите строку: ')
s_2 = input('Введите подстроку для поиска: ')

n = subs_count(s_1, s_2)
print(f'Подстрока найдена в строке, раз: {n}' if n != 0 else 'Подстрока не найдена')
