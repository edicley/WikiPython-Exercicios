"""
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores
e lhe contrataram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério,
baseado no salário atual:

salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.
"""

print("Você receberá um aumento!")
salario = float(input("Informe o seu salário: "))

if salario <= 280:
    percentual = 20
elif 280 < salario < 700:
    percentual = 15
elif 700 <= salario <= 1500:
    percentual = 10
else:
    percentual = 5
    
valor_aumento = (salario*percentual) / 100
novo_salario = salario + valor_aumento

print("####EXTRATO #####")
print(f"Antigo Salário: R${salario}")
print(f"Percentual de aumento aplicado:, {percentual}%")
print(f"Valor do aumento recebido: R${valor_aumento}")
print(f"Salário atualizado: R$ {novo_salario}")
