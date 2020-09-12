# Faça um Programa que pergunte quanto você ganha por hora e o número de horas
# trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

valor_hora = float(input("Qual o valor da sua hora de trabalho? "))
quantidade_horas = float(input("Quantas horas você trabalha no mês? "))

salario = valor_hora * quantidade_horas

print(f'Seu salário é R$ {salario} por mês.')