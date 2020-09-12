'''
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18
litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
'''
from math import ceil

tamanho = float(input('Informe a área a ser pintada: '))
litros_necessarios = tamanho / 3
latas_necessarias = (litros_necessarios / 18)
preco_total = latas_necessarias * 80

print(f'Você vai precisar de {latas_necessarias} latas de tinta.')
print(f'O valor total da compra é R${preco_total:.2f}')
