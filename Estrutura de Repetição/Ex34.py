# Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia. Um número primo é
# aquele que é divisível apenas por um e por ele mesmo. Faça um programa que peça um número inteiro e determine se ele
# é ou não um número primo.

cont = 0
num = int(input('Digite um número: '))

for n in range(2, num+1):
    if num % n == 0:
        cont += 1

if cont == 1:
    print(f'O número {num} é primo')
else:
    print(f'O número {num} não é primo')