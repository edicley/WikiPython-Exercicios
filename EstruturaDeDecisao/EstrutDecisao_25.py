"""
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?"

O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
"""

print('Estamos investigando um assassinato, tenho 5 perguntas para você. Responda [ 1 ] para SIM e [ 0 ] para NÃO.')
pergunta_01 = int(input('Telefonou para a vítima? '))
pergunta_02 = int(input('Esteve no local do crime? '))
pergunta_03 = int(input('Mora perto da vítima? '))
pergunta_04 = int(input('Devia para a vítima? '))
pergunta_05 = int(input('Já trabalhou com a vítima? '))

resultado = pergunta_01 + pergunta_02 + pergunta_03 + pergunta_04 + pergunta_05

if resultado <= 1:
    print('Você é inocente.')
elif resultado == 2:
    print('É um suspeito.')
elif resultado == 3 or resultado == 4:
    print('É um cúmplice.')
else:
    print('É o assassino.')
