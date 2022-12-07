# Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a quantidade
# de alunos para cada turma. As turmas não podem ter mais de 40 alunos.
turmas = int(input('Digite a quantidade de turmas: '))
alunos_tot = []
alunos = 0



for t in range(turmas):
    alunos = int(input(f'Digite a quantidade de alunos da {t + 1}ª turma: '))
    while alunos > 40:
        print('Quantidade de alunos não pode passar de 40')
        alunos = int(input(f'Digite a quantidade de alunos da {t + 1}ª turma: '))

    alunos_tot.append(alunos)

media = sum(alunos_tot) / turmas
print(f'A média de alunos por sala das {turmas} turmas é: {media:.2f}')
