# Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do
# mesmo.
# Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
# 326 = 3 centenas, 2 dezenas e 6 unidades
# 12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

num = int(input('Digite um número até 999: '))

c = num // 100 % 10
d = num // 10 % 10
u = num // 1 % 10

if c > 1:
    c_nome = 'centenas'
else:
    c_nome = 'centena'
if d > 1:
    d_nome = 'dezenas'
else:
    d_nome = 'dezena'
if u > 1:
    u_nome = 'unidades'
else:
    u_nome = 'unidade'

print(f'{num} = {c} {c_nome}, {d} {d_nome} e {u} {u_nome}')
