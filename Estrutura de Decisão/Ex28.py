# O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#                       Até 5 Kg           Acima de 5 Kg
# File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
# Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
# Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
# Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há
# limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um
# desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo
# usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de
# pagamento, valor do desconto e valor a pagar.


print('Digite o código do tipo de carne desejado: \n'
             'COD - Tipo de Carne\n'
             ' F  - Filé Duplo\n'
             ' A  - Alcatra\n'
             ' P  - Picanha')

tipo = input().upper()

kg = int(input('Digite a quantidade de kg deseja comprar: '))

cartao = input('Cartão Tabajara? (S/N): ').upper()

if tipo == 'F':
    if kg <= 5:
        val_tot = 4.90 * kg
    else:
        val_tot = 5.80 * kg
elif tipo == 'A':
    if kg <= 5:
        val_tot = 5.90 * kg
    else:
        val_tot = 6.80 * kg
elif tipo == 'P':
    if kg <= 5:
        val_tot = 6.90 * kg
    else:
        val_tot = 7.80 * kg

if cartao == 'S':
    val_tot_desc = val_tot - (val_tot * 0.10)
    print(f'Tipo de carne:{tipo}\n'
          f'Kilos: {kg}Kgs\n'
          f'Valor: R${val_tot}\n'
          f'Valor com cartão: R${val_tot_desc:.2f}')
else:
    print(f'Tipo de carne:{tipo}\n'
          f'Kilos: {kg}Kgs\n'
          f'Valor: R${val_tot}')

