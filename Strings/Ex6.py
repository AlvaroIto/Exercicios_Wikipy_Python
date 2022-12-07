# Data por extenso. Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome do mês por extenso.
# Data de Nascimento: 29/10/1973
# Você nasceu em  29 de Outubro de 1973.

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

dia = int(input('Digite o dia do nascimento: '))
mes = int(input('Digite o mês de nascimento: '))
ano = int(input('Digite o ano de nascimento: '))

print(f'Você nasceu em {dia} de {meses[mes-1]} de {ano}')


