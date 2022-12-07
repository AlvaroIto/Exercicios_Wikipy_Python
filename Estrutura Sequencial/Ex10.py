# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

c = float(input('Digite a temperatura em graus Celsius: '))
f = ((c * (9 / 5)) + 32)

print(f'A temperatura {c}ºC convertida para Fahrenheit é: {f:.2f}ºF')