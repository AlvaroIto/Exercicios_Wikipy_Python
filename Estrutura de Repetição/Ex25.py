# Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da
# turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a
# média calculada.

quant = int(input('Digite a quantiade de pessoas para pesquisar: '))
soma = 0
for n in range(quant):
    idade = int(input(f'Digite a idade da {n+1}ª pessoa: '))
    soma += idade

media = soma // quant
if 0 < media <= 25:
    print(f'Média de iddade: {media}. Turma Jovem')
elif 26 < media <= 60:
    print(f'Média de iddade: {media}. Turma Adulta')
else:
    print(f'Média de iddade: {media}. Turma Idosa')