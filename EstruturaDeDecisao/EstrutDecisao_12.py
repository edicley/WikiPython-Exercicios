
hora = float(input("Qual o valor da sua hora de trabalho? "))
total_horas = int(input("Qual sua carga horária mensal?"))
salario_bruto = hora * total_horas

if salario_bruto <= 900:
    ir = 0
elif salario_bruto > 900 and salario_bruto <= 1500:
    ir = 5
elif salario_bruto > 1500 and salario_bruto <= 2500:
    ir = 10
else:
    ir = 20
    
valor_ir = salario_bruto * ir /100
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