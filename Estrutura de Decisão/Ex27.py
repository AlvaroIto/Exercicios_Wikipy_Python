# Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#                       Até 5 Kg           Acima de 5 Kg
# Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
# Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um
# desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade
# (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

kg_mo = int(input('Digite quantos kg de morango deseja comprar: '))
kg_ma = int(input('Digite quantos kg de maçã deseja comprar: '))

kg_tot = kg_ma + kg_mo


if kg_mo <= 5:
    val_mo = kg_mo * 2.50
else:
    val_mo = kg_mo * 2.20

if kg_ma <= 5:
    val_ma = kg_ma * 1.80
else:
    val_ma = kg_ma * 1.50

val_tot = val_ma + val_mo

if kg_tot > 8 or val_tot > 25:
    val_tot_desc = val_tot - (val_tot * 0.10)
    print(f'KG de morango: {kg_mo}kg\n'
          f'KG de maçã: {kg_ma}kg\n'
          f'Valor total: R${val_tot:.2f}\n'
          f'Valor total com desconto: R${val_tot_desc:.2f}')
else:
    print(f'KG de morango: {kg_mo}kg\n'
          f'KG de maçã: {kg_ma}kg\n'
          f'Valor total: R${val_tot:.2f}\n')
