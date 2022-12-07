# Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor
# votar e ao final mostrar o número de votos de cada candidato.

eleitores = int(input('Digite a quantidade de eleitores: '))
voto_tot = []

print('=========== ELEIÇÃO ============\n'
      'Escolha o candidato pelo número:\n'
      '1- Primeiro candidato\n'
      '2- Segundo candidato\n'
      '3- Terceiro candidadto\n'
      '================================')

for e in range(eleitores):
    voto = int(input(f'Digite a escolha do {e+1}º eleitor: '))
    if 1 < voto > 3:
        voto = 0
    voto_tot.append(voto)

print(f'Primeiro candiato com {voto_tot.count(1)} votos\n'
      f'Segundo candidato com {voto_tot.count(2)} votos\n'
      f'Terceiro candaide com {voto_tot.count(3)} votos\n'
      f'Votos nulos ou brancos com {voto_tot.count(0)} votos')