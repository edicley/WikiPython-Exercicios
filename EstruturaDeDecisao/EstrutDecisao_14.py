"""
Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule
a sua média. A atribuição de conceitos obedece à tabela abaixo:

  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0            A
  Entre 7.5 e 9.0             B
  Entre 6.0 e 7.5             C
  Entre 4.0 e 6.0             D
  Entre 4.0 e zero            E

O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito
for A, B ou C ou “REPROVADO” se o conceito for D ou E.
"""

print("Informe suas duas notas, calcularemos a média e exibiremos o conceito obtido.")
n1 = float(input("Informe a primeira nota: "))
n2 = float(input("Informe a segunda nota: "))

media = (n1 + n2) / 2
conceito = ''
if 9.0 <= media <= 10.0:
    conceito = 'A'
elif 7.5 <= media < 9.0:
    conceito = 'B'
elif 6 <= media < 7.0:
    conceito = 'C'
elif 4 <= media < 6.0:
    conceito = 'D'
elif 4 > media >= 0:
    conceito = 'E'

if conceito == 'A' or conceito == 'B' or conceito == 'C':
    resultado = 'Aprovado'
else:
    resultado = 'Reprovado'
    
print(f"Primeira nota: {n1}")
print(f"Segunda nota: {n2}")
print(f"Média: {media} | Conceito: {conceito} | Resultado: {resultado}.")
