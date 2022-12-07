# Jogo da palavra embaralhada. Desenvolva um jogo em que o usuário tenha que adivinhar uma palavra que será mostrada com
# as letras embaralhadas. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente.
# O jogador terá seis tentativas para adivinhar a palavra. Ao final a palavra deve ser mostrada na tela, informando se o
# usuário ganhou ou perdeu o jogo.

from random import randint

texto = ('Em linguistica a nocao de texto e ampla e ainda aberta a uma definicao mais precisa Grosso modo pode ser '
         'entendido como manifestacao linguistica das ideias de um autor que serso interpretadas pelo leitor de acordo '
         'com seus conhecimentos linguisticos e culturais Seu tamanho e variavel').lower()
palavras = texto.split()
lista =[]
erro = 0


# colocar na lista somente palavras acima de 2 letras
for p in palavras:
    if len(p) > 3:
        lista.append(p)

#sortear palavra
palavra = lista[randint(1, len(lista))]
palavra_mist = sorted(palavra)
print(''.join(palavra_mist))

while erro < 6:
    chute = input('Tente acertar a palavra embaralhada: ')

    if chute == palavra:
        print(f'acertou! palavra: {palavra}')
        break
    else:
        erro += 1
        print(f'Errou, tentativa {erro} de 6')
        print(f'Palavra: {palavra}')

    if erro == 6:
        print('Fim de jogo')
