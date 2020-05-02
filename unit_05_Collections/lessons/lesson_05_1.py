"""
Коллекции. Модуль Collections
Counter
"""

from collections import Counter

a = Counter()
b = Counter('abracadabra')
c = Counter({'red': 2, 'blue': 4})
d = Counter(cats=4, dogs=5)

print(a, b, c, d, sep='\n')

print(list(b.elements()))  # итерируемый объект
print(b.most_common())  # список кортежей, по аналогии с dict.items()

# унарные операции
print('*' * 50)
z = Counter(a=2, b=-4)
print(+z)  # оставляет только положительные
print(-z)  # оставляет толь ко отрицательные и меняет знак
