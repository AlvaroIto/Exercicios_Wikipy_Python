# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver
# o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário
# atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.

salario = float(input('Digite o salário: R$'))

if salario <= 280:
    porcentagem = 20
    aumento = salario * 0.20
    salario_novo = salario + aumento

elif 280 < salario < 700:
    porcentagem = 15
    aumento = salario * 0.15
    salario_novo = salario + aumento

elif 700 < salario < 1500:
    porcentagem = 10
    aumento = salario * 0.10
    salario_novo = salario + aumento

else:
    porcentagem = 5
    aumento = salario * 0.05
    salario_novo = salario + aumento

print(f'Salário antigo: R${salario:.2f}\n'
      f'Percentual de aumento: {porcentagem}%\n'
      f'Valor do aumento: R${aumento:.2f}\n'
      f'Salário novo: R${salario_novo:.2f}\n')
