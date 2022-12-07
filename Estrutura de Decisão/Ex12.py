# Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que
# depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário
# Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os
# descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
# Desconto do IR:
# Salário Bruto até 900 (inclusive) - isento
# Salário Bruto até 1500 (inclusive) - desconto de 5%
# Salário Bruto até 2500 (inclusive) - desconto de 10%
# Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo.
# No exemplo o valor da hora é 5 e a quantidade de hora é 220.
#         Salário Bruto: (5 * 220)        : R$ 1100,00
#         (-) IR (5%)                     : R$   55,00
#         (-) INSS ( 10%)                 : R$  110,00
#         FGTS (11%)                      : R$  121,00
#         Total de descontos              : R$  165,00
#         Salário Liquido                 : R$  935,00

valor_hora = float(input('Digite o valor por hora: R$'))
horas_trabalhadas = int(input('Digite as horas trabalhadas:'))

bruto = valor_hora * horas_trabalhadas
fgts = bruto * 0.11
inss = bruto * 0.10


if bruto <= 900:
    ir = 0
    desconto = inss + ir
    salario_liquido = bruto - desconto
    print(f'Salário Bruto:          R${bruto:>7.2f}\n'
          f'(-) IR:                 Isento\n'
          f'(-) INSS (10%):         R${inss:>7.2f}\n'
          f'FGTS (11%):             R${fgts:>7.2f}\n'
          f'Total de descontos:     R${desconto:>7.2f}\n'
          f'Salário Liquido:        R${salario_liquido:>7.2f}')

elif 900 < bruto <= 1500:
    ir = bruto * 0.05
    desconto = inss + ir
    salario_liquido = bruto - desconto
    print(f'Salário Bruto:          R${bruto:>7.2f}\n'
          f'(-) IR:                 R${ir:>7.2f}\n'
          f'(-) INSS (10%):         R${inss:>7.2f}\n'
          f'FGTS (11%):             R${fgts:>7.2f}\n'
          f'Total de descontos:     R${desconto:>7.2f}\n'
          f'Salário Liquido:        R${salario_liquido:>7.2f}')
elif 1500 < bruto <= 2500:
    ir = bruto * 0.10
    desconto = inss + ir
    salario_liquido = bruto - desconto
    print(f'Salário Bruto:          R${bruto:>7.2f}\n'
          f'(-) IR:                 R${ir:>7.2f}\n'
          f'(-) INSS (10%):         R${inss:>7.2f}\n'
          f'FGTS (11%):             R${fgts:>7.2f}\n'
          f'Total de descontos:     R${desconto:>7.2f}\n'
          f'Salário Liquido:        R${salario_liquido:>7.2f}')
else:
    ir = bruto * 0.20
    desconto = inss + ir
    salario_liquido = bruto - desconto
    print(f'Salário Bruto:          R${bruto:>7.2f}\n'
          f'(-) IR:                 R${ir:>7.2f}\n'
          f'(-) INSS (10%):         R${inss:>7.2f}\n'
          f'FGTS (11%):             R${fgts:>7.2f}\n'
          f'Total de descontos:     R${desconto:>7.2f}\n'
          f'Salário Liquido:        R${salario_liquido:>7.2f}')