# Em uma competição de ginástica, cada atleta recebe votos de sete jurados. A melhor e a pior nota são eliminadas. A sua
# nota fica sendo a média dos votos restantes. Você deve fazer um programa que receba o nome do ginasta e as notas dos
# sete jurados alcançadas pelo atleta em sua apresentação e depois informe a sua média, conforme a descrição acima
# informada (retirar o melhor e o pior salto e depois calcular a média com as notas restantes). As notas não são
# informados ordenadas. Um exemplo de saída do programa deve ser conforme o exemplo abaixo:
# Atleta: Aparecido Parente
# Nota: 9.9
# Nota: 7.5
# Nota: 9.5
# Nota: 8.5
# Nota: 9.0
# Nota: 8.5
# Nota: 9.7
#
# Resultado final:
# Atleta: Aparecido Parente
# Melhor nota: 9.9
# Pior nota: 7.5
# Média: 9,04

nome_atleta = []
saltos = []
maior_salto = 0
menor_salto = 0
salto_media = []
media = 0

while True:
    atleta = str(input('Digite o nome do atleta: '))
    nome_atleta.append(atleta)
    if atleta != '':
        for n in range(1, 8):
            salto = float(input(f'{n}º Salto: '))
            saltos.append(salto)
            if n == 1:
                maior_salto = salto
                menor_salto = salto
            else:
                if salto > maior_salto:
                    maior_salto = salto
                if salto < menor_salto:
                    menor_salto = salto

        salto_media = saltos
        salto_media.remove(max(salto_media))
        salto_media.remove(min(salto_media))
        media = sum(salto_media) / 5

        print(f'Melhor salto: {maior_salto}m')
        print(f'Pior salto: {menor_salto}m')
        print(f'Média dos demais saltos: {media:.2f}m')
        print('Resultado final:')
        print(f'{atleta}: {media:.2f}')

    else:
        print('FIM')
        break


