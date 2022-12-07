# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o
# total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5%
# para o sindicato, faça um programa que nos dê:
# a) salário bruto.
# b) quanto pagou ao INSS.
# c) quanto pagou ao sindicato.
# d) o salário líquido.
# e) calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$
# Obs.: Salário Bruto - Descontos = Salário Líquido.

valor_hora = float(input('Digite o valor hora: R$'))
hora_trabalhada = int(input('Digite as horas trbalhadas no mês: '))

salario_bruto = valor_hora * hora_trabalhada
inss = salario_bruto * 0.08
ir = salario_bruto * 0.11
sindicato = salario_bruto * 0.05
descontos = inss + ir + sindicato
salario_liquido = salario_bruto - descontos

print(f'Salário Bruto: R${salario_bruto:.2f}\n'
      f'IR (11%): R${ir:.2f}\n'
      f'INSS (8%): R${inss:.2f}\n'
      f'Sindicato (5%): R${sindicato:.2f}\n'
      f'Salário Líquido: R${salario_liquido:.2f}')