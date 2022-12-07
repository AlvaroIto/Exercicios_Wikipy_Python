# Faça um programa que leia 5 números e informe o maior número.
numeros = []
for n in range(5):
    num = int(input(f'Digite o {n+1}º número: '))
    numeros.append(num)

print(max(numeros))