# Faça um Programa que leia três números e mostre-os em ordem decrescente.

lista = []

n1 = int(input('Digite o primeiro número: '))
lista.append(n1)
n2 = int(input('Digite o segundo número: '))
lista.append(n2)
n3 = int(input('Digite o terceiro número: '))
lista.append(n3)

print(sorted(lista))
