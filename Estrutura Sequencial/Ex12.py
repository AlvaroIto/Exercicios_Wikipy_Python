# Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a
# seguinte fórmula: (72.7*altura) - 58

alt = float(input('Digite a altura em metros: '))
peso_ideal = (72.2 * alt) - 58

print(f'Para uma pessoa com altura de {alt}mts, o pesoal ideal é de: {peso_ideal:.2f}kgs')