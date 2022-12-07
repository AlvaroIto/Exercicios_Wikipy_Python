# Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo
# representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais
# alto e o número do aluno mais baixo, junto com suas alturas.

alunos = []
alturas = []
junto = {}
alto_cod = 0
alto = 0
baixo_cod = 0
baixo = 999

for n in range(3):
    aluno = int(input('Digite o número do aluno: '))
    altura = int(input(f'Digite a altura do aluno {aluno} em centímetros: '))
    alunos.append(aluno)
    alturas.append(altura)
    if n == 0:
        alto = altura
        baixo = altura
    else:
        if altura > alto:
            alto = altura
            alto_cod = aluno
        if altura < baixo:
            baixo = altura
            baixo_cod = aluno

maior = max(alturas)
menor = min(alturas)

print(f'O número do aluno mais alto é: {alto_cod} e tem atlura de {alto}cm.')
print(f'O número do aluno mais baixo é: {baixo_cod} e tem atlura de {baixo}cm.')
