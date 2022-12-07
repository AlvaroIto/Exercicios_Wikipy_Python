# Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números primos existentes entre
# 1 e um número inteiro informado pelo usuário.

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