# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet
# (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

tamanho = int(input('Digite o tamanho do arquivo em Mb: '))
velocidade = int(input('Digite a velocidade de internet em Mbps: '))

tempo = tamanho / velocidade

tempo_min = tempo // 60

print(f'Para uma internet de {velocidade}Mbps e um arquivo de {tamanho}Mb, será necessário {tempo_min} minuto(s) para '
      f'fazer o download')