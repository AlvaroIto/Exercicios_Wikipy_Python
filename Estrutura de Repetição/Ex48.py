# Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero invertido.
# Exemplo:
#   12376489
#   => 98467321


num = input('Digite um número: ')

num_rev = num[::-1]
print(f'Número digitado: {num}. Reverso do número é: {num_rev}')