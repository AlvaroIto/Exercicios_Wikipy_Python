# Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:
# quantos espaços em branco existem na frase.
# quantas vezes aparecem as vogais a, e, i, o, u.


frase = str(input('Digite uma frase: ')).lower()
frase_tup = tuple(frase)
espaco = frase.count(' ')
vogal_cont = 0

print(frase_tup)

for n in frase_tup:
    if n in 'aeiou':
        vogal_cont += 1

print(f'A frase "{frase}" tem {espaco} espaços em branco')
print(f'A frase "{frase}" possui {vogal_cont} vogais')