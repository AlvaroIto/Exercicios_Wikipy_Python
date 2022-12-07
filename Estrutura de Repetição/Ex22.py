# Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é
# divisível.

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
    print(f'Número {num} não  é primo, número divisível {cont_primo+1} vezes pelos números: {primo} ')
else:
    print(f'Número {num} é primo')
