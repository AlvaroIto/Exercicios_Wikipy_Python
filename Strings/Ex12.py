# Valida e corrige número de telefone. Faça um programa que leia um número de telefone, e corrija o número no caso deste
# conter somente 7 dígitos, acrescentando o '3' na frente. O usuário pode informar o número com ou sem o traço separador.

# Valida e corrige número de telefone
# Telefone: 461-0133
# Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.
# Telefone corrigido sem formatação: 34610133
# Telefone corrigido com formatação: 3461-0133

from collections import deque

num = deque(input('Digite o número de telefone: '))

if '-' in num:
    if len(num) <= 7:
        print(f"Telefone {''.join(num)} incompleto")
    else:

        if '-' in num[3]:
            if len(num) <= 8:
                print('Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.')
                num.appendleft('3')
                print(''.join(num))
            else:
                print(''.join(num))
        else:
            num.appendleft('3')
            num[5] = num[4]
            num[4] = '-'
            print('Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.')
            print(''.join(num))

else:
    if len(num) == 7:
        print('Telefone sem formatação.')
        num.appendleft('0')
        num[0] = num[1]
        num[1] = num[2]
        num[2] = num[3]
        num[3] = '-'
        num.appendleft('3')
        print(''.join(num))
    else:
        print('Telefone sem formatação.')
        num.append('0')
        num[8] = num[7]
        num[7] = num[6]
        num[6] = num[5]
        num[5] = num[4]
        num[4] = '-'
        print(''.join(num))
