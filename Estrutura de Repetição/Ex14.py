# Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de
# números impares.

numeros = []
par = []
impar = []
for n in range(10):
    num = int(input(f'Digite o {n+1}º número: '))
    numeros.append(num)
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)

print(f'Números digitados: {numeros}\n'
      f'Números pares digitados: {par}\n'
      f'Números ímpares digitados: {impar}')
