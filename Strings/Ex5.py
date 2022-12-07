# Nome na vertical em escada invertida. Altere o programa anterior de modo que a escada seja invertida.
# FULANO
# FULAN
# FULA
# FUL
# FU
# F

nome = str(input('Digite o nome: '))
c = len(nome)

while c >= 0:
    print(nome[:c:])
    c -= 1
