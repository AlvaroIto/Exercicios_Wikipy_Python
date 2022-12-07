# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = str(input('Digite uma letra: '))

if letra in 'AaEeIiOoUu':
    print(f'Letra {letra} é vogal')
else:
    print(f'Letra {letra} é consoante')