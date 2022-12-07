# Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o
# fatorial a números inteiros positivos e menores que 16.


while True:
    num = int(input('Digite um número entre 1 e 16: '))
    fat = 1
    if 0 < num <= 16:
        while num > 0:
            print(f'{num}', end='')
            print(' x ' if num > 1 else ' = ', end='')
            fat *= num
            num -= 1
    else:
        print('Fim do programa')
        break
    print(f'{fat}')
