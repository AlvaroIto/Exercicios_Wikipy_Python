# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18
# litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
from math import ceil

area = float(input('Digte o tamanho em m² da área a ser pintada: '))
litros = area / 3

if area <= 54:
    print(f'Para uma área de {area}m² será necessário 1 lata de tinta R$80.00')
else:
    lata_tot = ceil((area / 54))
    valor = lata_tot * 80
    print(f'Para uma área de {area}m² sérão necessários {lata_tot} de tintas no valor de R${valor:.2f}')

