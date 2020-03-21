'''
Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.
'''


def print_expression_result(expr):
    result = eval(expr)
    print(f'{expr}\t=  {result} ({bin_str(result)})')


def bin_str(n):
    return bin(n)[2:]


a = 5
b = 6
expressions = ['a | b', 'a & b', 'a ^ b', 'a >> 2', 'a << 2']

print(f'a\t\t=  {a} ({bin_str(a)})')
print(f'b\t\t=  {b} ({bin_str(b)})')
print()

for e in expressions:
    print_expression_result(e)
