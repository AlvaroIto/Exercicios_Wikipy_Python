# Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.
numeros = []
quant = int(input('Digite a quantidade de números a serem digitados: '))

for n in range(quant):
    num = int(input(f'Digite o {n+1}º número entre (0 e 1000): '))
    cont = 0
    while cont < quant:
        if num < 0 or num > 1000:
            print(f'O número precisa ser entre 0 e 1000')
            num = int(input(f'Digite o {n + 1}º número entre (0 e 1000): '))
        else:
            cont += 1
    numeros.append(num)


print(f'Números digitados: {numeros}\n'
      f'Maior número digitado: {max(numeros)}\n'
      f'Menor número digitado: {min(numeros)}')


