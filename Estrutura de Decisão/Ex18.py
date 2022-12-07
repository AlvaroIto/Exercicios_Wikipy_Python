# Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

dia = int(input('Digite o dia (xx): '))
mes = int(input('Digite o mês (xx): '))
ano = int(input('Digite o ano (xxxx): '))



if mes in [1, 3, 5, 7, 8, 10, 12]:
    if dia < 0 or dia > 31:
        print(f'Dia {dia} inválido!')
    else:
        print(f'{dia}/{mes}/{ano}')

elif mes in [2, 4, 6, 9, 11]:
    if dia < 0 or dia > 30:
        print(f'Dia {dia} inválido!')
    else:
        print(f'{dia}/{mes}/{ano}')


if mes < 0 or mes > 12:
    print(f'Mês {mes} inválido!')
else:
    print(f'{dia}/{mes}/{ano}')

if ano < 0:
    print(f'Ano {ano} inválido!')
else:
    print(f'{dia}/{mes}/{ano}')

