# Palíndromo. Um palíndromo é uma seqüência de caracteres cuja leitura é idêntica se feita da direita para esquerda ou
# vice−versa. Por exemplo: OSSO e OVO são palíndromos. Em textos mais complexos os espaços e pontuação são ignorados.
# A frase SUBI NO ONIBUS é o exemplo de uma frase palíndroma onde os espaços foram ignorados. Faça um programa que leia
# uma seqüência de caracteres, mostre−a e diga se é um palíndromo ou não.

normal = str(input('Digite a palavra ou frase: ')).lower().replace(' ', '')
inverso = normal[::-1]

print(f'Normal: {normal}')
print(f'Inverso: {inverso}')

if normal == inverso:
    print(f'A palavra {normal} é palindromo {inverso}')
else:
    print(f'A palvra {normal} não é palindromo {inverso}')