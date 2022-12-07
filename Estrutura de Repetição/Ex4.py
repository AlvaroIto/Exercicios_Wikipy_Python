# Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a
# população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o
# número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as
# taxas de crescimento.

pop_a = 80000
pop_b = 200000
cont = 0

porc_pop_a = 80000 * 0.03
porc_pop_b = 200000 * 0.015

while pop_a <= pop_b:
    pop_a += porc_pop_a
    pop_b += porc_pop_b
    cont += 1
print(f'Serão necessários {cont} anos para a população A ({pop_a}) ultrapassar a populaçao B ({pop_b})')