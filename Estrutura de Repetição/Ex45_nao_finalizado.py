# Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve perguntar ao
# aluno a resposta de cada questão e ao final comparar com o gabarito da prova e assim calcular o total de acertos e a
# nota (atribuir 1 ponto por resposta certa). Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro
# aluno vai utilizar o sistema. Após todos os alunos terem respondido informar:
# a- Maior e Menor Acerto;
# b- Total de Alunos que utilizaram o sistema;
# c- A Média das Notas da Turma.

# Gabarito da Prova:
#
# 01 - A
# 02 - B
# 03 - C
# 04 - D
# 05 - E
# 06 - E
# 07 - D
# 08 - C
# 09 - B
# 10 - A
# Após concluir isto você poderia incrementar o programa permitindo que o professor digite o gabarito da prova antes dos
# alunos usarem o programa.

aluno_cont = 0
aluno_esp = []
aluno_bur = []
resp_c = 0
resp_e = 0
maior_c = 0
maior_e = 10
soma_notas = 0
resposta = []
gabarito = ['A', 'B', 'C', 'D', 'E', 'E', 'D', 'C', 'B', 'A']

while True:
    #verificar se um aluno novo irá digitar no sistema
    aluno = input('Há um aluno para inserir nota? (S/N): ').upper()
    if aluno == 'S':
        aluno_cont += 1

        #loop das respostas
        for n in range(1, 11):
            resp = str(input(f'Digite a resposta da pergunta {n}: ')).upper()
            resposta.append(resp)

        #dicionário parar comparar as respostas
        junto = zip(gabarito, resposta)

        #comparando respostas
        for c, v in junto:
            if c == v:
                resp_c += 1
                soma_notas += 1
                maior_c += 1
            else:
                resp_e += 1
                maior_e += 1

        #verificar o alunno que mais acertou e o que mais errou
        if aluno_cont == 1:
            maior = maior_c
            menor = maior_e
            aluno_esp.append(n)
            aluno_bur.append(n)
        else:
            if maior > maior_c:
                maior = maior_c
                aluno_esp.append(n)

            if menor < maior_e:
                menor = maior_e
                aluno_bur.append(n)

    else:
        break


print(f'O aluno que mais acertou foi o aluno {aluno_esp} com {maior} acertos')
print(f'O aluno que mais errou foi o aluno {aluno_bur} com {menor} erros')
print(f'{aluno_cont} alunos usaram o sistema')
print(resposta)
#print(f'A média total das notas dos alunos é: {resp_c/aluno_cont:.2f}')

