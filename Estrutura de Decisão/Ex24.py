# Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da
# operação deve ser acompanhado de uma frase que diga se o número é:
# par ou ímpar;
# positivo ou negativo;
# inteiro ou decimal.

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

print('Digite a operação desejada: \n'
      '+ Soma \n'
      '- Subtração \n'
      '* Multiplicação \n'
      '/ Divisão')

operacao = input()

if operacao == '+':
    resultado = n1 + n2
    print(f'{n1} + {n2} = {resultado}')
elif operacao == '-':
    resultado = n1 - n2
    print(f'{n1} - {n2} = {resultado}')
elif operacao == '*':
    resultado = n1 * n2
    print(f'{n1} * {n2} = {resultado}')
elif operacao == '/':
    resultado = n1 / n2
    print(f'{n1} / {n2} = {resultado}')

res_int = round(resultado)

if res_int % 2 == 0:
    print(f'O resultado {res_int} é par')
else:
    print(f'O resultado {res_int} é ímpar')



if resultado == res_int:
    print(f'O resultado {resultado} é inteiro')
else:
    print(f'O resultado {resultado} é decimal')

if resultado > 0:
    print(f'O resultado {resultado} é positivo')
else:
    print(f'O resultado {resultado} é negativo')
