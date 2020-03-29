"""
4. Определить, какое число в массиве встречается чаще всего.
"""

from random import randint


source = [randint(0, randint(0, 10)) for _ in range(randint(10, 50))]
print(f'source list:\t\t{source}')

count = {}
for n in source:
    count[n] = count.get(n, 0) + 1

s = sorted(count.items(), key=lambda x: x[1], reverse=True)
print(f'most common num:\t{s[0][0]}')
