# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

num = int(input('Digite um número: '))
fat = 1

while num > 0:
    print(f'{num}', end='')
    print(' x ' if num > 1 else ' = ', end='')
    fat *= num
    num -= 1
print(f'{fat}')
