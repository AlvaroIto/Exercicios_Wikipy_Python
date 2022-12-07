# Faça um programa que mostre os n termos da Série a seguir:
#   S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.
# Imprima no final a soma da série.

lista_impar = []
lista_num = []
num = int(input('Digite um número: '))
soma_num = 0
soma_impar = 0
c = 1

#lista com os números 1 até N
for n in range(1, num+1):
    lista_num.append(n)

#Lista com os números ímpares de 1 até 100
for m in range(1, 100):
    if m % 2 != 0:
        lista_impar.append(m)
print('S = ', end='')

#mostrar a lista números / lista impares
for v in range(len(lista_num)):
    print(f'{lista_num[v]}/{lista_impar[v]}', end=' ')
    print(' + ' if lista_num[v] < len(lista_num) else ' = ', end='')
    soma_num += lista_num[v]
    soma_impar += lista_impar[v]

print(f'{soma_num} / {soma_impar}')