# Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais
# magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, sua altura e
# seu peso. O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. Ao encerrar o
# programa também deve ser informados os códigos e valores do clente mais alto, do mais baixo, do mais gordo e do mais
# magro, além da média das alturas e dos pesos dos clientes

cliente = {}
lista_cliente = []
alto = 0
alto_cod = 0
baixo = 999
baixo_cod = 0
gordo = 0
gordo_cod = 0
magro = 999
magro_cod = 0


while True:
    cod = int(input('Digite o código do cliente: '))
    if cod != 0:
        alt = float(input(f'Digite a altura do cliente {cod}: '))
        peso = float(input(f'Digite o peso do cliente {cod}: '))
        cliente = {'COD': cod, 'ALT': alt, 'PES': peso}
        lista_cliente.append(cliente)

        if len(lista_cliente) == 0:
            alto = alt
            baixo = alt
        else:
            if alt > alto:
                alto = alt
                alto_cod = cod
            if alt < baixo:
                baixo = alt
                baixo_cod = cod

        if len(lista_cliente) == 0:
            gordo = peso
            magro = peso
        else:
            if peso > gordo:
                gordo = peso
                gordo_cod = cod
            if peso < magro:
                magro = peso
                magro_cod = cod

    else:
        break

print(lista_cliente)
print(f'Código do mais alto: {alto_cod} medindo: {alto}cm')
print(f'Código do mais baixo: {baixo_cod} medindo: {baixo}cm')
print(f'Código do mais gordo: {gordo_cod} pesando: {gordo}kgs')
print(f'Código do mais magro: {magro_cod} pesando: {magro}kgs')

