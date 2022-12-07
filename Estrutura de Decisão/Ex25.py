# Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?"
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como
# "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

cont = 0
resposta = []

print('Digite S - sim ou N - não')
p1 = input('Telefonou para a vítima? ').upper()
p2 = input('Esteve no local do crime? ').upper()
p3 = input('Mora perto da vítima? ').upper()
p4 = input('Devia para a vítimia? ').upper()
p5 = input('Já trabalhou com a vítima? ').upper()

resposta.append(p1)
resposta.append(p2)
resposta.append(p3)
resposta.append(p4)
resposta.append(p5)


for r in resposta:
    if r == 'S':
        cont += 1

if cont == 2:
    print(f'{cont} Respostas positivas. SUSPEITO')
elif cont == 5:
    print(f'{cont} Respostas positivas. ASSASSINO')
elif cont <= 1:
    print(f'{cont} Resposta positiva. INOCENTE')
else:
    print(f'{cont} Respostas positivas. CÚMPLICE')

