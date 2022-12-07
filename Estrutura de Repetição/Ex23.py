# Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. O programa
# deverá mostrar também o número de divisões que ele executou para encontrar os números primos. Serão avaliados o
# funcionamento, o estilo e o número de testes (divisões) executados.

num = int(input('Digite um número: '))
cont = 1
cont_primo = 0
primo = [1]
while cont < num:
    div = num / cont
    cont += 1

    if num % cont == 0:
        cont_primo += 1
        primo.append(cont)

if cont_primo > 1:
    print(f'Foram feitas {cont} divisões e o número {num} não é primo, número divisível {cont_primo+1} vezes pelos números: {primo}')
else:
    print(f'Foram feitas {cont} divisões e o número {num} é primo')