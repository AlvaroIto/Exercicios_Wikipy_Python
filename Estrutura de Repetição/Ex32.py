# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120. A saída
# deve ser conforme o exemplo abaixo:
# Fatorial de: 5
# 5! =  5 . 4 . 3 . 2 . 1 = 120

num = int(input('Digite um número: '))
fat = 1

print(f'{num}! = ', end='')

while num > 0:
    print(f'{num}', end='')
    print(' * ' if num > 1 else ' = ', end='')
    fat *= num
    num -= 1
print(f'{fat}')
