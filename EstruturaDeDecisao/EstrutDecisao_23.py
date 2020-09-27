"""
Faça um Programa que peça um número e informe se o número é inteiro ou decimal.
Dica: utilize uma função de arredondamento.
"""
print('Informe um número e direi se ele é inteiro ou decimal.')
numero = float(input('Informe um numero: '))

if numero == round(numero):
    print('É um número inteiro.')
else:
    print('É um número decimal.')
