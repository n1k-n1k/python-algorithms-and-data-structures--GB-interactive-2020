"""
Поиск подстроки в строке
(с использованием алгоритма Рабина-Карпа, 1987)
"""

import hashlib


def Rabin_Karp(s: str, subs: str) -> int:
    assert len(s) > 0 and len(subs) > 0, 'Строки не могут быть пустые'
    assert len(s) >= len(subs), 'Подстрока длиннее строки'

    len_subs = len(subs)
    h_subs = hashlib.sha1(subs.encode('utf-8')).hexdigest()

    for i in range(len(s) - len_subs + 1):
        if h_subs == hashlib.sha1(s[i:i + len_subs].encode('utf-8')).hexdigest():

            if s[i:i + len_subs] == subs:
                return i

    return -1


s_1 = input('Введите строку: ')
s_2 = input('Введите подстроку для поиска: ')

pos = Rabin_Karp(s_1, s_2)

print(f'Подстрока найдена в позиции {pos}' if pos != -1 else 'Подстрока не найдена')
