# Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida, valor
# dos juros, quantidade de parcelas e valor da parcela.

# Os juros e a quantidade de parcelas seguem a tabela abaixo:
# Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
# 1       0
# 3       10
# 6       15
# 9       20
# 12      25

# Exemplo de saída do programa:
# Valor da Dívida       Valor dos Juros         Quantidade de Parcelas          Valor da Parcela
# R$ 1.000,00                  0                          1                       R$  1.000,00
# R$ 1.100,00                 100                         3                       R$    366,00
# R$ 1.150,00                 150                         6                       R$    191,67

divida = float(input('Digite o valor da dívida: R$'))

valor_1 = 0
valor_3 = divida * 0.10
valor_3_tot = divida + valor_3
parcela_3 = valor_3_tot / 3
valor_6 = divida * 0.15
valor_6_tot = divida + valor_6
parcela_6 = valor_6_tot / 6
valor_9 = divida * 0.20
valor_9_tot = divida + valor_9
parcela_9 = valor_9_tot / 9
valor_12 = divida * 0.25
valor_12_tot = divida + valor_12
parcela_12 = valor_12_tot / 12

print(f'Segue tabela com valores da dívida de R${divida:.2f}')
print('VALOR DA DÍVIDA          VALOR DOS JUROS         QUANTIDADE DE PARCELAS          VALOR DA PARCELA')
print(f'R${divida:.2f}                      {valor_1:.2f}                         1                        R${divida:.2f}')
print(f'R${valor_3_tot:.2f}                     {valor_3:.2f}                        3                        R${parcela_3:.2f}')
print(f'R${valor_6_tot:.2f}                     {valor_6:.2f}                        6                        R${parcela_6:.2f}')
print(f'R${valor_9_tot:.2f}                     {valor_9:.2f}                        9                        R${parcela_9:.2f}')
print(f'R${valor_12_tot:.2f}                     {valor_12:.2f}                        12                       R${parcela_12:.2f}')