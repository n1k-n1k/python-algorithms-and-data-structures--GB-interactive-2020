"""
Коллекции. Модуль Collections
ChainMap
"""

from collections import ChainMap

d1 = {'a': 2, 'b': 4, 'c': 6}
d2 = {'a': 10, 'b': 20, 'c': 40}

d_map = ChainMap(d1, d2)
print(d_map)
d2['a'] = 100
print(d_map)

print('*' * 50)
x = d_map.new_child()
print(x)
print(x.parents)

print('*' * 50)
y = d_map.new_child()
print(y)
print(y['a'])
