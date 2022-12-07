# O cardápio de uma lanchonete é o seguinte:
# Especificação   Código  Preço
# Cachorro Quente 100     R$ 1,20
# Bauru Simples   101     R$ 1,30
# Bauru com ovo   102     R$ 1,50
# Hambúrguer      103     R$ 1,20
# Cheeseburguer   104     R$ 1,30
# Refrigerante    105     R$ 1,00
# Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule e mostre o valor a ser pago
# por item (preço * quantidade) e o total geral do pedido. Considere que o cliente deve informar quando o pedido deve
# ser encerrado.

soma = 0
produto = []
quantidade = []
valor =[]
while True:
    cod = int(input('===============LANCHONETE================\n'
                    'Pedido             Código      Preço\n'
                    'Hot Dog            100         R$1.20\n'
                    'Bauru Simples      101         R$1.30\n'
                    'Bauru com Ovo      102         R$1.50\n'
                    'Hamburguer         103         R$1.20\n'
                    'Cheeseburguer      104         R$1.30\n'
                    'Refrigerante       105         R$1.00\n'
                    'Digite o código do pedido ou 000 para encerrar o pedido: '))
    produto.append(cod)

    if cod != 0:
        quant = int(input(f'Digite a quantidade do produto {cod}: '))
        quantidade.append(quant)
        if cod == 100:
            val = 1.2 * quant
            valor.append(val)

        elif cod == 101:
            val = 1.30 * quant
            valor.append(val)

        elif cod == 102:
            val = 1.50 * quant
            valor.append(val)

        elif cod == 103:
            val = 1.20 * quant
            valor.append(val)

        elif cod == 104:
            val = 1.30 * quant
            valor.append(val)

        elif cod == 105:
            val = 1.00 * quant
            valor.append(val)

        else:
            cod = 000

    else:
        break

print(              'PEDIDO ENCERRADO!')
print(f'Pedido          Quantidade          Preço')
for n in range(len(quantidade)):
    print(f'{produto[n]}                  {quantidade[n]}              R${valor[n]:.2f}')

print(f'VALOR TOTAL                         R${sum(valor):.2f}')
