# Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto
# em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.
quant = int(input('Digite a quantidade de CDs que o colecionador possui: '))
valor_tot = 0
for n in range(quant):
    valor = float(input(f'Digite o valor do {n+1}º CD: R$'))
    valor_tot += valor

media = valor_tot / quant
print(f'Quantidade de CDs na coleção = {quant}\n'
      f'Valor  médio gasto em cada CD = R${media:.2f}')