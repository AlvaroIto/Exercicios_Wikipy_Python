# Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a
# entrada e permita repetir a operação.

pop_a = int(input('Digite a quantidade da população A: '))
pop_b = int(input('Digite a quantidade da população B: '))
taxa_a = float(input('Digite a taxa de crescimento da população A: '))
taxa_b = float(input('Digite a taxa de crescimento da população B: '))
cont = 0

porc_pop_a = pop_a * (taxa_a / 100)
porc_pop_b = pop_b * (taxa_b / 100)

while pop_a <= pop_b:
    pop_a += porc_pop_a
    pop_b += porc_pop_b
    cont += 1
print(f'Serão necessários {cont} anos para a população A ({pop_a}) ultrapassar a populaçao B ({pop_b})')
