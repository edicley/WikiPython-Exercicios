'''
Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe
se este ano é ou não bissexto.
'''

print('Informe um ano e lhe direi se ele é bissexto ou não.')
ano = int(input('Informe um ano: '))

if ano % 4 == 0 and ano % 400 == 0:
    print(f'{ano} é um ano bissexto.')
else:
    print(f'{ano} não é um ano bissexto.')
