# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão
# é sempre pelo mais barato.

barato = []

p1 = float(input('Digite o preço do primeiro produto: R$'))
p2 = float(input('Digite o preço do segundo produto: R$'))
p3 = float(input('Digite o preço do terceiro produto: R$'))

if p1 < p2 and p1 < p3:
    print(f'O valor do produto 1 é mais barato: R${p1:.2f}')
elif p2 < p1 and p2 < p3:
    print(f'O valor do produto 2 é mais barato: R${p2:.2f}')
else:
    print(f'O valor do produto 3 é mais barato: R${p3:.2f}')
