# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
# utilizando as seguintes fórmulas:
# a) Para homens: (72.7*h) - 58
# b) Para mulheres: (62.1*h) - 44.7

alt = float(input('Digite a altura em metros: '))
peso_ideal_h = (72.7 * alt) - 58
peso_ideal_m = (62.1 * alt) - 44.7

print(f'Com a altura de {alt}mts, o pesoal ideal para homens é: {peso_ideal_h:.2f}Kg e para mulher é: {peso_ideal_m:.2f}kg')