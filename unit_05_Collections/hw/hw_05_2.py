"""
Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого — цифры числа.

Например, пользователь ввёл A2 и C4F.
Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Примечание: Если воспользоваться функциями hex() и/или int()
для преобразования систем счисления, задача решается в несколько строк.
Для прокачки алгоритмического мышления такой вариант не подходит.
Поэтому использование встроенных функций для перевода из одной
системы счисления в другую в данной задаче под запретом.
"""


# использование встроенных функций hex() и int() - под запретом,
# но это не мешает "изобрести велосипед"
# и упаковать его в кастомный класс,
# экземпляры которого являются списком символов,
# и переопределить методы сложения и умножения
#
# по-прежнему считаем пользователя идеальным

class HexList:

    def __init__(self, st):
        """внутреннее представление экземпляра - список символов"""
        self.lst = list(str(st).upper())

    def __repr__(self):
        """
        печатаем экземпляр класса по шаблону визуализации списка;
        если нужен вывод в визуализации шестнадцатиричного значения, то:
        return ''.join(self.lst)
        """
        tmp = [f"'{s}'" for s in self.lst]
        return f'[{", ".join(tmp)}]'

    def __add__(self, other):
        return HexList(self._to_hex(self._to_dec(self.lst) + self._to_dec(other.lst)))

    def __mul__(self, other):
        return HexList(self._to_hex(self._to_dec(self.lst) * self._to_dec(other.lst)))

    @staticmethod
    def _to_dec(lst: list) -> int:
        hxs = {s: i for i, s in enumerate(list('0123456789ABCDEF'))}
        return sum([int(hxs[s]) * 16 ** i for i, s in enumerate(lst[::-1])])

    @staticmethod
    def _to_hex(num: int) -> str:
        dcs = {i: s for i, s in enumerate(list('0123456789ABCDEF'))}
        st = ''
        while num % 16 > 0:
            st += dcs[num % 16]
            num //= 16
        return st[::-1]


h1 = HexList(input('Введите первое шестнадцатеричное число: '))
h2 = HexList(input('Введите второе шестнадцатеричное число: '))

print()
print(f'h1 =\t\t{h1}')
print(f'h2 =\t\t{h2}')
print(f'h1 + h2 =\t{h1 + h2}')
print(f'h1 * h2 =\t{h1 * h2}')
