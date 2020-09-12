'''
Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
'''

tamanho_arquivo = float(input('Informe o tamanho do arquivo em MB: '))
velocidade_internet = float(input('Informe a velocidade da sua internet em Mbps: '))

tempo = velocidade_internet / tamanho_arquivo

print(f'Em aproximadamente {tempo} minutos o seu download será concluído.')