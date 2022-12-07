# Faça um Programa que leia três números e mostre o maior e o menor deles.
maior = 0
menor = 0

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

if n1 > n2 and n1 > n3:
    print(f'O {n1} é maior que o {n2} e {n3}')
elif n2 > n1 and n2 > n3:
    print(f'O {n2} é maior que o {n1} e {n3}')
elif n3 > n1 and n3 > n2:
    print(f'O {n3} é maior que o {n1} e {n2}')
else:
    print(f'Os número {n1, n2, n3} são iguais')

if n1 < n2 and n1 < n3:
    print(f'O {n1} é menor que o {n2} e o {n3}')
elif n2 < n1 and n2 < n3:
    print(f'O {n2} é menor que o {n1} e {n3}')
elif n3 < n1 and n3 < n2:
    print(f'O {n3} é menor que o {n1} e {n2}')
else:
    print(f'Os número {n1, n2, n3} são iguais')