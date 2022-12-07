# Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, Faça um programa que calcule o valor de H com N termos.

num = int(input('Digite um número: '))
soma = 1

print('1', end=' + ')

for n in range(2, num+1):
    print(f'1/{n}', end='')
    print(f' + ' if n < num else ' = ', end='')
    calc = 1 / n
    soma += calc

print(f'{soma:.2f}')
