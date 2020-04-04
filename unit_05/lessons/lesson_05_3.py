"""
Коллекции. Модуль Collections
defaultdict
"""

from collections import defaultdict

s = 'sdkfjghsdkfghsdlkfvjsdhlkfjvhsld'
b = defaultdict(int)
for i in s:
    b[i] += 1
print(b)

list_1 = [('cat', 1), ('dog', 5), ('cat', 2), ('mouse', 1), ('dog', 1)]
c = defaultdict(list)
for k, v in list_1:
    c[k].append(v)
print(c)

list_2 = [('cat', 1), ('dog', 5), ('cat', 2), ('mouse', 1), ('dog', 1), ('dog', 5)]
d = defaultdict(set)
for k, v in list_2:
    d[k].add(v)
print(d)

f = defaultdict(lambda: 'unknown')
f.update(rex='dog', thomas='cat')
print(f)
print(f['rex'])
print(f['jerry'])
