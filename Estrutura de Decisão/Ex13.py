# Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar
# outro valor deve aparecer valor inválido.

print(('Digite um dia da semana\n'
                '1 - Segunda\n'
                '2 - Terça\n'
                '3 - Quarta\n'
                '4 - Quinta\n'
                '5 - Sexta\n'
                '6 - Sabado\n'
                '7 - Domingo'))
dia = int(input())

dia_semana = ['Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sabado', 'Domingo']
print(dia_semana[dia-1])
