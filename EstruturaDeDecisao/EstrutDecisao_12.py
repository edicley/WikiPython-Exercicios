"""
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda,
que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário
Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os
descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20%

Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de
hora é 220.

        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00
"""

hora = float(input("Qual o valor da sua hora de trabalho? "))
total_horas = int(input("Qual sua carga horária mensal?"))
salario_bruto = hora * total_horas

if salario_bruto <= 900:
    ir = 0
elif 900 < salario_bruto <= 1500:
    ir = 5
elif 1500 < salario_bruto <= 2500:
    ir = 10
else:
    ir = 20
    
valor_ir = salario_bruto * ir / 100
inss = 10
fgts = 11
sindicado = 3
valor_inss = salario_bruto * inss / 100
valor_fgts = salario_bruto * fgts / 100
valor_sindicato = salario_bruto * sindicado / 100
total_desconto = valor_ir + valor_inss + valor_sindicato
salario_liquido = salario_bruto - total_desconto

print(f"Salário Bruto: ({hora} * {total_horas})         R${salario_bruto}")
print(f"(-) IR{ir}%                                 R${valor_ir}")
print(f"(-) INSS{inss}%               R${valor_inss}")
print(f"(-) Imposto Sindical{sindicado}%       R${valor_sindicato}")
print(f"(-) FGTS{fgts}%         R${valor_fgts}")
print(f"Total de desconto:    R${total_desconto}")
print(f"Salário Líquido:      R${salario_liquido}")
