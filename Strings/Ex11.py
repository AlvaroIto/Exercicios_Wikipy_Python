# Jogo de Forca. Desenvolva um jogo da forca. O programa terá uma lista de palavras lidas de um arquivo texto e
# escolherá uma aleatoriamente. O jogador poderá errar 6 vezes antes de ser enforcado.

# Digite uma letra: A
# -> Você errou pela 1ª vez. Tente de novo!

# Digite uma letra: O
# A palavra é: _ _ _ _ O

# Digite uma letra: E
# A palavra é: _ E _ _ O

# Digite uma letra: S
# -> Você errou pela 2ª vez. Tente de novo!

from random import randint

texto = ('Em linguistica a nocao de texto e ampla e ainda aberta a uma definicao mais precisa Grosso modo pode ser '
         'entendido como manifestacao linguistica das ideias de um autor que serso interpretadas pelo leitor de acordo '
         'com seus conhecimentos linguisticos e culturais Seu tamanho e variavel').lower()
palavras = texto.split()
lista =[]
erro = 0
ganhou = False

# colocar na lista somente palavras acima de 2 letras
for p in palavras:
    if len(p) > 2:
        lista.append(p)

#sortear palavra
palavra = lista[randint(1, len(lista))]


jogo = ['_' for i in range(len(palavra))]



print(palavra)

print('Jogo da Forca')
print(' '.join(jogo).upper())
print('')

while erro < 6 and not ganhou:
    letra = str(input(f'Digite uma letra: ')).lower()

    for i, v in enumerate(palavra):
        if v == letra:
            jogo[i] = letra
            print(jogo)

    if letra not in palavra:
        erro += 1
        print(f'{erro}º erro')
        if erro >= 6:
            print('Fim de jogo')
            break

    if '_' not in jogo:
        ganhou = True

if ganhou:
    print('Ganhou')
else:
    print('Perdeu')

