'''
Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.
'''

a = 5
b = 6

print(f'a\t\t=  {a} ({bin(a)})')
print(f'b\t\t=  {b} ({bin(b)})')
print()
print(f'a OR b\t=  {a | b} ({bin(a | b)})')
print(f'a AND b\t=  {a & b} ({bin(a & b)})')
print(f'a XOR b\t=  {a ^ b} ({bin(a ^ b)})')
print(f'a >> 2\t=  {a >> 2} ({bin(a >> 2)})')
print(f'a << 2\t=  {a << 2} ({bin(a << 2)})')
