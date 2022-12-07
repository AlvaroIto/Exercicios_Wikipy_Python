# Em uma competição de salto em distância cada atleta tem direito a cinco saltos. No final da série de saltos de cada
# atleta, o melhor e o pior resultados são eliminados. O seu resultado fica sendo a média dos três valores restantes.
# Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois
# informe a média dos saltos conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a
# média). Faça uso de uma lista para armazenar os saltos. Os saltos são informados na ordem da execução, portanto não
# são ordenados. O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser
# conforme o exemplo abaixo:
# Atleta: Rodrigo Curvêllo
#
# Primeiro Salto: 6.5 m
# Segundo Salto: 6.1 m
# Terceiro Salto: 6.2 m
# Quarto Salto: 5.4 m
# Quinto Salto: 5.3 m
#
# Melhor salto:  6.5 m
# Pior salto: 5.3 m
# Média dos demais saltos: 5.9 m
#
# Resultado final:
# Rodrigo Curvêllo: 5.9 m

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
        for n in range(1, 6):
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
        media = sum(salto_media) / 3

        print(f'Melhor salto: {maior_salto}m')
        print(f'Pior salto: {menor_salto}m')
        print(f'Média dos demais saltos: {media:.2f}m')
        print('Resultado final:')
        print(f'{atleta}: {media:.2f}')

    else:
        print('FIM')
        break


