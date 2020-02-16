print("Informe suas duas notas, calcularemos a média e exibiremos o conceito obtido.")
n1 = float(input("Informe a primeira nota: "))
n2 = float(input("Informe a segunda nota: "))

media = (n1 + n2) / 2
conceito = ''
if media >= 9.0 and media <= 10.0:
    conceito = 'A'
elif media >= 7.5 and media < 9.0:
    conceito = 'B'
elif media >= 6 and media < 7.0:
    conceito = 'C'
elif media >= 4 and media < 6.0:
    conceito = 'D'
elif media < 4 and media >= 0:
    conceito = 'E'

if conceito == 'A' or conceito == 'B' or conceito == 'C':
    resultado = 'Aprovado'
else:
    resultado = 'Reprovado'
    
print(f"Primeira nota: {n1}")
print(f"Segunda nota: {n2}")
print(f"Média: {media} | Conceito: {conceito} | Resultado: {resultado}.")