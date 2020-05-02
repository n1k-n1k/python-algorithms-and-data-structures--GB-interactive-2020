"""
Коллекции. Модуль Collections
namedtuple
"""

from collections import namedtuple

hero_1 = ('Aaz', 'Izverg', 100, 0.0, 250)
print(hero_1[4])


# ал-я конструктор класса
# в качестве первого параметра --> имя класса, второй --> перечень полей через пробел
NewPerson = namedtuple('NewPerson', 'name race health mana strenght')
hero_3 = NewPerson('Aaz', 'Izverg', 100, 0.0, 250)
print(hero_3.race)

# перечень полей можно передавать листом
props = ['name', 'race', 'health', 'mana', 'strenght']
NewPerson2 = namedtuple('NewPerson2', props)
hero_4 = NewPerson2('Aaz', 'Izverg', 100, 0.0, 250)
print(hero_4.race)


print('*' * 50)
Point = namedtuple('Point', 'x , y, z')
p1 = Point(2, z=3, y=4)
print(p1)

t = [5, 10, 15]
p2 = Point._make(t)
print(p2)

d2 = p2._asdict()
print(d2)

p3 = p2._replace(x=6)
print(p3)

print(p3._fields)  # список полей: кортеж ('x', 'y', 'z')

# можно распаковать значения аргументов из словаря, через **
print('*' * 50)
dct = {'x': 10, 'y': 20, 'z': 30}
p5 = Point(**dct)
print(p5)
