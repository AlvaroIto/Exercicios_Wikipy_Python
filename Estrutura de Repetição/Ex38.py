# Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
# a- Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
# b- Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
# c- A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior.
# Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o programa permitindo que
# o usuário digite o salário inicial do funcionário.
'''
ano_inicial = 1997
ano_atual = 2022
anos = ano_atual - ano_inicial
salario_inicial = float(input('Digite o salário inicial: R$'))
percentual = 0.015
aumento = salario_inicial + (percentual * salario_inicial)
print(f'Primeiro salário: R${salario_inicial:.2f}')
print(f'Primeiro aumento: R${aumento:.2f}')

while ano_inicial < ano_atual:
    percentual = (2 * (aumento * 0.015))
    aumento += percentual
    print(f'Salário de {ano_inicial} = R${aumento:.2f}')
    ano_inicial += 1

'''

salario = int(input('Digite o salário do funcionário: '))
ano = 1996
porcentagem = 1.5/100
salario_1 = salario
while ano <= 2020:
    salario = salario + (porcentagem * salario_1)
    ano += 1
    porcentagem += porcentagem
print(salario)