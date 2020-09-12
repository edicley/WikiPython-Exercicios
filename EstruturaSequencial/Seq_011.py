# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# - O produto do dobro do primeiro com metade do segundo .
# - A soma do triplo do primeiro com o terceiro.
# - O terceiro elevado ao cubo.

print('Informe três números.')

n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo número: '))
n3 = float(input('Informe o terceiro número: '))

print(f'O produto do dobro do primeiro com metade do segundo é: {(n1 * 2) + (n2 / 2)}')
print(f'A soma do triplo do primeiro com o terceiro é: {(n1 * 3) + n3}')
print(f'O terceiro elevado ao cubo é: {n3 ** 3}')

