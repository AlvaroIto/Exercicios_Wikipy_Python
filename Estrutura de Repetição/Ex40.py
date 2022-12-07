# Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos
# os seguintes dados:
# Código da cidade;
# Número de veículos de passeio (em 1999);
# Número de acidentes de trânsito com vítimas (em 1999).
# Deseja-se saber:
# a- Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
# b- Qual a média de veículos nas cinco cidades juntas;
# c- Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.

maior = 0
menor = 0
maior_cod = 0
menor_cod = 0
soma_tot = 0
soma = 0
cont = 0


for n in range(1, 6):
    cod_cid = int(input(f'Digite o código da {n}ª cidade: '))
    num_vei = int(input(f'Digite o número de veículos da cidade de cógigo {cod_cid}: '))
    num_vit = int(input(f'Digite o número de acidentes da cidade de código {cod_cid}: '))

    if n == 1:
        maior = num_vit
        menor = num_vit
    else:
        if num_vit > maior:
            maior = num_vit
            maior_cod = cod_cid
        if num_vit < menor:
            menor = num_vit
            menor_cod = cod_cid

    if num_vei < 2000:
        cont += 1
        soma += num_vit
        print(soma)
        media_menos_2k = soma / cont
        print(media_menos_2k)

    soma_tot += num_vei
    media_tot = soma / 5


print(f'A cidade com maior índice de acidentes é a cidade {maior_cod} com {maior} vítimas')
print(f'A cidade com menor índice de acidentes é a cidade {menor_cod} com {menor} vítimas')
print(f'A média de veículos nas cinco cidades é {media_tot}')
print(f'A média de acidentes de trânsito nas cidades com menos de 2000 veículos é de: {media_menos_2k:.2f}')





