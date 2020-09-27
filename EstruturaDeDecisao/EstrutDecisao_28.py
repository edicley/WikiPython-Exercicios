"""
O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:

                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há
limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um
desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo
usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total,
tipo de pagamento, valor do desconto e valor a pagar.
"""

preco = 0.0
desconto = 0.0
valor_liquido = 0.0
descricao_pagamento = ''

print('Estamos em promoçao,mas você só pode levar um dos tipos de carne.')
print('[1] - Filé Duplo')
print('[2] - Alcatra')
print('[3] - Picanha')

carne = ''
tipo_carne = int(input('Escolha o tipo de carne.'))
kg = float(input('Quantos quilos você levará? '))

if tipo_carne == 1:
    if kg <= 5:
        preco = 4.90
    else:
        preco = 5.80
elif tipo_carne == 2:
    if kg <= 5:
        preco = 5.90
    else:
        preco = 6.80
elif tipo_carne == 3:
    if kg < 5:
        preco = 6.90
    else:
        preco = 7.80

valor_total = kg * preco

forma_pagamento = int(input('Qual a forma de pagamento? [1]Dinnheiro [2]Cartão Tabajara [3]Outros'))

if forma_pagamento == 1:
    descricao_pagamento = 'Dinheiro'
    valor_liquido = valor_total - desconto
elif forma_pagamento == 2:
    descricao_pagamento = 'Cartão Tabajara'
    desconto = valor_total * 0.1
    valor_liquido = valor_total - desconto
elif forma_pagamento == 3:
    descricao_pagamento = 'Outros'
    valor_liquido = valor_total - desconto

if tipo_carne == 1:
    carne = 'Filé Duplo'
elif tipo_carne == 2:
    carne = 'Alcatra'
elif tipo_carne == 3:
    carne = 'Picanha'

print(f'Tipo de carne: {carne}')
print(f'Peso total Kg: {kg}')
print(f'Valor da compra: {valor_total}')
print(f'Tipo de pagamento: {descricao_pagamento}')
print(f'Valor do desconto: {desconto}')
print(f'Total a pagar: {valor_liquido}')
