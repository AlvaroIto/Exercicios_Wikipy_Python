# Número por extenso. Escreva um programa que solicite ao usuário a digitação de um número até 99 e imprima-o na tela
# por extenso.

num = int(input('Digite um número de 0 a 99: '))
dicionario_numerico = {
        0: 'zero', 1: 'um', 2: 'dois', 3: 'três', 4: 'quatro', 5: 'cinco',
        6: 'seis', 7: 'sete', 8: 'oito', 9: 'nove', 10: 'dez',
        11: 'onze', 12: 'doze', 13: 'treze', 14: 'quatorze', 15: 'quinze',
        16: 'dezesseis', 17: 'dezessete', 18: 'dezoito', 19: 'dezenove', 20: 'vinte',
        30: 'trinta', 40: 'quarenta', 50: 'cinquenta', 60: 'sessenta', 70: 'setenta',
        80: 'oitenta', 90: 'noventa',
    }

if num > 99 or num < 0:
    print('O número deve ser de 0 a 99')
else:

    if num < 20:
        print(f'{num}: {dicionario_numerico[num]}')

    else:
        dezena = (num // 10 % 10) * 10
        unidade = num // 1 % 10
        print(f'{num}: {dicionario_numerico[dezena]} e {dicionario_numerico[unidade]}')
