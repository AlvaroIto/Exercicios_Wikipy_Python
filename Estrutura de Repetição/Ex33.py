# O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto
# indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das
# temperaturas.
'''
soma_temp = 0
maior = 0
menor = 0

quant = int(input('Digite a quantidade de temperaturas a serem inseridas: '))

for n in range(quant):
    temp = float(input(f'Digite a {n+1}ª temperatura: '))
    soma_temp += temp
    if n == 0:
        maior = temp
        menor = temp
    else:
        if temp > maior:
            maior = temp
        if temp < menor:
            menor = temp
media = soma_temp / quant
print(f'A maior temperatura registrada foi: {maior}ºC')
print(f'A menor tempertura registrada foi: {menor}ºC')
print(f'A média das temperaturas registrada é: {media:.2f}ºC')

'''
temperaturas = []
quant = int(input('Digite a quantidade de temperaturas a serem inseridas: '))

for n in range(quant):
    temp = float(input(f'Digite a {n+1}ª temperatura: '))
    temperaturas.append(temp)
media = sum(temperaturas) / quant

print(f'A maior temperatura registrada foi: {max(temperaturas)}ºC')
print(f'A menor tempertura registrada foi: {min(temperaturas)}ºC')
print(f'A média das temperaturas registrada é: {media:.2f}ºC')