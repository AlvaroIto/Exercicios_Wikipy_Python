# Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, mas a tabuada
# não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados também pelo
# usuário, conforme exemplo abaixo:
# Montar a tabuada de: 5
# Começar por: 4
# Terminar em: 7
#
# Vou montar a tabuada de 5 começando em 4 e terminando em 7:
# 5 X 4 = 20
# 5 X 5 = 25
# 5 X 6 = 30
# 5 X 7 = 35
# Obs: Você deve verificar se o usuário não digitou o final menor que o inicial.
'''
num = int(input('Digite um número entre 1 a 10: '))
cont = 0
while cont <= 10:
    print(f'{cont} * {num} = {cont * num}')
    cont += 1
'''

num = int(input('Digite um número entre 1 a 10: '))
inicio = int(input('Digite o valor inicial: '))
fim = int(input('Digite o valor final: '))

while inicio > fim:
    print(f'Valor de inicio {inicio} não pode ser maior que valor final {fim}')
    inicio = int(input('Digite o valor inicial: '))
    fim = int(input('Digite o valor final: '))

while inicio <= fim:
    print(f'{num} * {inicio} = {inicio * num}')
    inicio += 1
