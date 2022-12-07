# Faça um programa que leia 5 números e informe a soma e a média dos números.

numeros = []

for n in range(5):
    num = int(input(f'Digite o {n+1}º número: '))
    numeros.append(num)

media = sum(numeros) / 5

print(f'Números digitados: {numeros}')
print(f'Média dos números digitados: {media}')