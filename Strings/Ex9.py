# Verificação de CPF. Desenvolva um programa que solicite a digitação de um número de CPF no formato xxx.xxx.xxx-xx e
# indique se é um número válido ou inválido através da validação dos dígitos verificadores edos caracteres de formatação.

cpf = input('Digite o cpf no formato xxx.xxx.xxx-xx: ')

if cpf[3] in '.':
    if cpf[7] in '.':
        if cpf[11] in '-':
            print(f'CPF: {cpf} válido!')
        else:
            print(f'CPF: {cpf} inválido!')
    else:
        print(f'CPF: {cpf} inválido!')
else:
    print(f'CPF: {cpf} inválido!')