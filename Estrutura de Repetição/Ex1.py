# Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue
# pedindo até que o usuário informe um valor válido.

nota = int(input('Digite uma nota válida (0 - 10): '))
while nota not in range(11):
    print(f'Nota {nota} inválida!')
    nota = int(input('Digite uma nota válida (0 - 10): '))
else:
    print(f'Nota {nota} válida!')