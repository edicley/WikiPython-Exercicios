"""
Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar
quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais.
O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas
existentes na máquina.

Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50,
uma nota de 5 e uma nota de 1;

Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50,
quatro notas de 10, uma nota de 5 e quatro notas de 1.
"""
print('Caixa Eletrônico')
print('Valor mínimo R$ 10 - Valor máximo R$ 600')
valor = int(input('Informe o valor para saque: '))

if 10 <= valor <= 600:
    nota_100 = valor // 100
    nota_50 = (valor - (nota_100 * 100)) // 50
    nota_10 = (valor - (nota_100 * 100) - (nota_50 * 50)) // 10
    nota_5 = (valor - (nota_100 * 100) - (nota_50 * 50) - (nota_10 * 10)) // 5
    nota_1 = valor - (nota_100 * 100) - (nota_50 * 50) - (nota_10 * 10) - (nota_5 * 5)

    print('Notas do saque:')
    if nota_100 == 1:
        print(f'{nota_100} nota de R$ 100.')
    elif nota_100 > 1:
        print(f'{nota_100} notas de R$ 100. ')
    if nota_50 == 1:
        print(f'{nota_50} nota de R$ 50.')
    elif nota_50 > 1:
        print(f'{nota_50} notas de R$ 50.')
    if nota_10 == 1:
        print(f'{nota_10} nota de R$ 10.')
    elif nota_10 > 1:
        print(f'{nota_10} notas de R$ 10.')
    if nota_5 == 1:
        print(f'{nota_5} nota de R$ 5.')
    elif nota_5 > 1:
        print(f'{nota_5} notas de R$ 5.')
    if nota_1 == 1:
        print(f'{nota_1} nota de R$ 1.')
    elif nota_1 > 1:
        print(f'{nota_1} notas de R$ 1.')
else:
    print('Valor inválido para saque.')
