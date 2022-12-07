# Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# Álcool:
# até 20 litros, desconto de 3% por litro
# acima de 20 litros, desconto de 5% por litro
# Gasolina:
# até 20 litros, desconto de 4% por litro
# acima de 20 litros, desconto de 6% por litro
# Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma:
# A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina
# é R$ 2,50 o preço do litro do álcool é R$ 1,90.

litros = int(input('Digite a quantidade de litros desejado: '))
tipo = input('Digite o tipo desejado A - álcool ou G - gasolina: ').upper()

if tipo == 'A':
    if litros <= 20:
        desconto = 3
        valor = litros * (1.90 - (1.90 * 0.03))
        print(f'Litros: {litros}\n'
              f'Tipo: {tipo} \n'
              f'Desconto: {desconto}%\n'
              f'Valor: R${valor:.2f}')
    else:
        desconto = 5
        valor = litros * (1.90 - (1.90 * 0.05))
        print(f'Litros: {litros}\n'
              f'Tipo: {tipo} \n'
              f'Desconto: {desconto}%\n'
              f'Valor: R${valor:.2f}')
elif tipo == 'G':
    if litros <= 20:
        desconto = 4
        valor = litros * (2.50 - (2.50 * 0.04))
        print(f'Litros: {litros}\n'
              f'Tipo: {tipo} \n'
              f'Desconto: {desconto}%\n'
              f'Valor: R${valor:.2f}')
    else:
        desconto = 6
        valor = litros * (2.50 - (2.50 * 0.06))
        print(f'Litros: {litros}\n'
              f'Tipo: {tipo} \n'
              f'Desconto: {desconto}%\n'
              f'Valor: R${valor:.2f}')
