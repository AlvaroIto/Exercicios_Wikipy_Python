# Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.
numeros = []
quant = int(input('Digite a quantidade de números a serem digitados: '))

for n in range(quant):
    num = int(input(f'Digite o {n+1}º número: '))
    numeros.append(num)
print(f'Números digitados: {numeros}\n'
      f'Maior número digitado: {max(numeros)}\n'
      f'Menor número digitado: {min(numeros)}')

