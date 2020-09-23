'''
Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador
módulo (resto da divisão).
'''

print('Informe um número e direi se ele é ímpar ou par.')
numero = int(input('Informe o número: '))

if numero % 2 == 0:
    print(f'{numero} é um número par.')
else:
    print(f'{numero} é um número ímpar.')