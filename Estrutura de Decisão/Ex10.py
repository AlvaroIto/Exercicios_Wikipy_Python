# Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

turno = str(input('Digite o turno que você estuda (M - Matutino / V - Vespertino / N - Noturno: ')).upper()

if turno in 'M':
    print(f'Turno {turno}. Bom dia!')
elif turno in 'V':
    print(f'Turno {turno}. Boa tarde!')
elif turno in 'N':
    print(f'Turno {turno}. Boa noite!')
else:
    print(f'Turno {turno} desonhecido. Valor inválido!')