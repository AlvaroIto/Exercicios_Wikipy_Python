# Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por
# eles.

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

numeros = range(n1, n2)
for n in numeros:
    print(n)