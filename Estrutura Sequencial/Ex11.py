# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# a) o produto do dobro do primeiro com metade do segundo .
# b) a soma do triplo do primeiro com o terceiro.
# c) o terceiro elevado ao cubo.

n1 = int(input('Digite o primeiro número inteiro: '))
n2 = int(input('Digite o segundo número inteiro: '))
n3 = float(input('Digite um número real: '))

a = (n1 * 2) * (n2 / 2)
b = ((n1 * 3) + n3)
c = (n3 ** 3)

print(f'Produto do dobro do primeiro com metade do segundo: {a}\n'
      f'Soma do triplo do primeiro com terceiro: {b:.2f}\n'
      f'Terceiro elevado ao cubo: {c:.2f}')