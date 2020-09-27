"""
Faça um Programa que peça as 4 notas bimestrais e mostre a média.
"""

print('Informe as suas quatro notas do bimestre e calcularemos a média.')
nota_01 = float(input('Informe a primeira nota: '))
nota_02 = float(input('Informe a segunda nota: '))
nota_03 = float(input('Informe a terceira nota: '))
nota_04 = float(input('Informe a quarta nota: '))

media = (nota_01 + nota_02 + nota_03 + nota_04) / 4

print(f'Sua média foi: {media}')
