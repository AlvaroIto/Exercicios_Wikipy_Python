# Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino,
# M - Masculino, Sexo Inválido.

sexo = str(input('Digite o sexo M (masculino) ou F (feminino): ')).upper()

if sexo in 'Mm':
    print('Masculino')
elif sexo in 'Ff':
    print('Feminino')
else:
    print(f'Sexo {sexo} inválido!')