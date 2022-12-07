# Faça um programa que leia e valide as seguintes informações:
# a- Nome: maior que 3 caracteres;
# b- Idade: entre 0 e 150;
# c- Salário: maior que zero;
# d- Sexo: 'f' ou 'm';
# e- Estado Civil: 's', 'c', 'v', 'd';

nome = input('Digite o nome: ')
while len(nome) < 3:
    print(f'Nome {nome} precisa ter mais que 3 letras')
    nome = input('Digite o nome: ')

idade = int(input('Digite a idade: '))
while idade <= 0 or idade > 150:
    print(f'Idade {idade} precisa ser entre 0 e 150')
    idade = int(input('Digite a idade: '))

salario = float(input('Digite o salário: R$'))
while salario < 0:
    print(f'Salário R${salario:.2f} precisa ser maior que R$0.00')
    salario = float(input('Digite o salário: R$'))


sexo = input('Digite o sexo (M/F): ').upper()
while sexo not in 'FM':
    print(f'Sexo {sexo} precisa ser F ou M')
    sexo = input('Digite o sexo (M/F): ').upper()

estado = input('Digite o estado civil (S - solteiro, C - casado, V - Viuvo, D - Divorciado): ').upper()
while estado not in 'SCVD':
    print(f'Estado precisa ser S, C, V ou D')
    estado = input('Digite o estado civil (S - solteiro, C - casado, V - Viuvo, D - Divorciado): ').upper()

print(f'Nome: {nome}\n'
      f'Idade: {idade}\n'
      f'salario: R${salario:.2f}\n'
      f'Sexo: {sexo}\n'
      f'Estado Civil: {estado}')