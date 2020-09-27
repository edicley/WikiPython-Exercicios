"""
Um posto está vendendo combustíveis com a seguinte tabela de descontos:

Álcool:
até 20 litros, desconto de 3% por litro
acima de 20 litros, desconto de 5% por litro

Gasolina:
até 20 litros, desconto de 4% por litro
acima de 20 litros, desconto de 6% por litro

Escreva um algoritmo que leia o número de litros vendidos,
o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser
pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
"""

print('Posto de combustível.')
litros = float(input('Você quer abastecer com quantos litros? '))
combustivel = str(input('Qual o combustível? Informe [A] para álcool e [G] para gasolina.'))
total_pagar = 0

if combustivel.upper() == 'A':
    if litros <= 20:
        valor = 1.90
        total_bruto = (litros * valor)
        valor_desconto = total_bruto * 0.03
        total_pagar = total_bruto - valor_desconto
        print(total_pagar)
    elif litros > 20:
        valor = 1.90
        total_bruto = (litros * valor)
        valor_desconto = total_bruto * 0.05
        total_pagar = total_bruto - valor_desconto
        print(total_pagar)
elif combustivel.upper() == 'G':
    if litros <= 20:
        valor = 2.50
        total_bruto = (litros * valor)
        valor_desconto = total_bruto * 0.03
        total_pagar = total_bruto - valor_desconto
        print(total_pagar)
    elif litros > 20:
        valor = 2.50
        total_bruto = (litros * valor)
        valor_desconto = total_bruto * 0.05
        total_pagar = total_bruto - valor_desconto
        print(total_pagar)

print(f'Valor total de à pagar: R$ {total_pagar}')
