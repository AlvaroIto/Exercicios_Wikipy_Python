# Altere o programa anterior para mostrar no final a soma dos números.

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

numeros = range(n1, n2)
for n in numeros:
    print(n, end=' ')
    print(' + ' if n < n2-1 else ' = ', end='')

soma = sum(range(n1, n2))
print(f'{soma}')

