# Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir
# os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
# Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os
# demais valores, sendo encerrado;
# Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
# Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
# Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

from math import sqrt

a = int(input('Digite o valor de a: '))
b = int(input('Digite o valor de b: '))
c = int(input('Digite o valor de c: '))

if a == 0:
    print('Equação não é de segundo grau!')
else:
    delta = ((b**2) - 4 * (a * c))
    if delta < 0:
        print(f'Delta {delta} negativo, não possui raizes reais')
    elif delta == 0:
        x = -b / (2 * a)
        print(f'Delta {delta}, apenas 1 raiz real = {x}')
    else:
        x_pos = (-b + sqrt(delta)) / 2
        x_neg = (-b - sqrt(delta)) / 2
        print(f'Delta {delta}, com 2 raizes = {x_pos} e {x_neg}')



