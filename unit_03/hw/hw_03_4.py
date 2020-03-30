"""
4. Определить, какое число в массиве встречается чаще всего.
"""

from random import randint

source = [randint(0, randint(0, 30)) for _ in range(randint(10, 50))]
print(f'source list:\t\t{source}')

if len(source) == len(set(source)):
    print('All nums in source list are different')

else:
    counter = {}
    for n in source:
        counter[n] = counter.get(n, 0) + 1

    max_count, max_item = tuple(counter.items())[0]

    for item, count in counter.items():
        if count > max_count:
            max_count = count
            max_item = item

    print(f'most common num:\t{max_item}')
