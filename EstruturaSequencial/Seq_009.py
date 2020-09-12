# Faça um Programa que peça a temperatura em graus Fahrenheit,
# transforme e mostre a temperatura em graus Celsius.

fahrenheit = float(input('Informe a temperatura atual em graus Fahrenheit: '))
celsios = 5 * ((fahrenheit-32) / 9)

print(f'{fahrenheit}º são equivalentes a {celsios:.1f}º celsios.')