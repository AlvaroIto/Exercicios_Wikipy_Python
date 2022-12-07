# Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes
# intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar quando for lido um número negativo.

ate_25 = []
ate_50 = []
ate_75 = []
ate_100 = []

while True:
    num = int(input('Digite um número: '))
    if num > 0:
        if num <= 25:
            ate_25.append(num)
        elif 25 < num <= 50:
            ate_50.append(num)
        elif 50 < num <= 75:
            ate_75.append(num)
        else:
            ate_100.append(num)
    else:
        break

print(f'Dos números digitados:\n'
      f'{len(ate_25)} números entre 0 e 25: {ate_25}\n'
      f'{len(ate_50)} números entre 26 e 50: {ate_50}\n'
      f'{len(ate_75)} números entre 51 e 75: {ate_75}\n'
      f'{len(ate_100)} números entre 76 e 100: {ate_100}')

