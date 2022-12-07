# Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos
# utilizados são:
# 1 , 2, 3, 4  - Votos para os respectivos candidatos
# (você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
# 5 - Voto Nulo
# 6 - Voto em Branco
# Faça um programa que calcule e mostre:
# O total de votos para cada candidato;
# O total de votos nulos;
# O total de votos em branco;
# A percentagem de votos nulos sobre o total de votos;
# A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero.

votos = []
nulo = 0
branco = 0
voto = 0

print('======Eleição======\n'
      '1 - José\n'
      '2 - João\n'
      '3 - Maria\n'
      '4 - Carla\n'
      '5 - Nulo\n'
      '6 - Branco\n'
      '===================')
while True:
    cod = int(input('Escolha seu candidato pelo número: '))
    if cod != 0:
        votos.append(cod)
        voto += 1
        if cod == 5:
            nulo += 1
        if cod == 6:
            branco += 1
    else:
        break

percentual_nulo = (nulo * 100) / voto
percentual_branco = (branco * 100) / voto

print(f'Total de votos: {voto}')

for n in range(1, 5):
    print(f'Candidato {n} obteve {votos.count(n)} votos')
print(f'Votos nulos = {nulo}, a porcentagem de votos nulos é de {percentual_nulo:.2f}%')
print(f'Votos brancos = {branco}, a porcentagem de votos brancos é de {percentual_branco:.2f}%')