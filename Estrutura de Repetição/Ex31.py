# O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências.
# Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá receber um número desconhecido de
# valores referentes aos preços das mercadorias. Um valor zero deve ser informado pelo operador para indicar o final da
# compra. O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para
# então calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial, para
# registrar a próxima compra. A saída deve ser conforme o exemplo abaixo:
# Lojas Tabajara
# Produto 1: R$ 2.20
# Produto 2: R$ 5.80
# Produto 3: R$ 0
# Total: R$ 9.00
# Dinheiro: R$ 20.00
# Troco: R$ 11.00
# ...

lista = []

while True:
    print('================== LOJAS TABAJARA ======================')
    while True:
        soma = 0
        valor = float(input(f'Digite o valor do produto: R$'))
        if valor != 0:
            lista.append(valor)

        else:
            break

    for n in range(len(lista)):
        print(f'Produto {n+1}: R$ {lista[n]:.2f}')

    print(f'Total: R${sum(lista):.2f}')
    pagamento = float(input('Digite o valor dado em dinheiro: R$'))
    troco = pagamento - sum(lista)
    print(f'Dinheiro: R${pagamento:.2f}')
    print(f'Troco: R${troco:.2f}')
    print(f'========================================================')
