# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o
# total do seu salário no referido mês.

valor_hora = float(input('Digite o valor recebido por hora: R$'))
horas_trabalhada = int(input('Digite as horas trabalhadas no mês: '))
salario = horas_trabalhada * valor_hora
print(f'Valor da hora: R${valor_hora:.2f}\n'
      f'Horas trabalhadas no mês: {horas_trabalhada}hrs\n'
      f'Salário: R${salario:.2f}')
