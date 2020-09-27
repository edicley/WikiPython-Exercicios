"""
Uma fruteira está vendendo frutas com a seguinte tabela de preços:

                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda
um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a
quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.
"""
valor_morango = 0
valor_maca = 0

kg_maca = float(input('Informe em quilos quanto você está levando de maçã: '))
kg_morango = float(input('Informe em quilos quanto você está levando de morango: '))

if kg_morango <= 5:
    valor_morango = 2.50
elif kg_morango > 5:
    valor_morango = 2.20

if kg_maca <= 5:
    valor_maca = 1.80
elif kg_maca > 5:
    valor_maca = 1.50

valor_total_morango = kg_morango * valor_morango
valor_total_maca = kg_maca * valor_maca
total_kg = kg_morango + kg_maca
valor_total_compra = valor_total_morango + valor_total_maca

if total_kg > 8 or valor_total_compra > 25:
    desconto = valor_total_compra * 0.1
    valor_total_compra = valor_total_compra - desconto

print(valor_total_compra)
