# Faça um programa que calcule o mostre a média aritmética de N notas.

quant = int(input('Digite a quantidade de notas a serem inseridas: '))
numeros = []

for n in range(quant):
    num = int(input(f'Digite a {n+1}ª nota: '))
    numeros.append(num)

media = sum(numeros) / quant
print(f'Números digitados: {numeros}\n'
      f'Média: {media}')

