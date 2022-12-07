# Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que
# é divisível somente por ele mesmo e por 1.

num = int(input('Digite um número: '))
cont = 1
cont_primo = 0

while cont < num:
    div = num / cont
    cont += 1

    if num % cont == 0:
        cont_primo += 1

if cont_primo > 1:
    print(f'Número {num} não  é primo, número divisível {cont_primo+1} vezes')
else:
    print(f'Número {num} é primo')
