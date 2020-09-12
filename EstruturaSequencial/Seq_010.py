# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

celsios = float(input('Informe a temperatura atual em graus celsios: '))

fahrenheit = (( 1.8 * celsios) + 32)

print(f'{celsios}º celsios são equivalentes a {fahrenheit:.1f}º fahrenheit.')