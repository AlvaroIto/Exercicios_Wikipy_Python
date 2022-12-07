# Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em formato de escada.
# F
# FU
# FUL
# FULA
# FULAN
# FULANO

nome = str(input('Digite o nome: '))
c = 0

while c <= len(nome):
    print(nome[:c])
    c += 1
