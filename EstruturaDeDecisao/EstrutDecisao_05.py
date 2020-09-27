# Calcular média e informar sobre aprovação.

n1 = float(input("Informe sua primeira nota: "))
n2 = float(input("Informe sua segunda nota: "))

media = (n1 + n2) / 2

if media == 10:
    print("Aprovado com louvor!")
elif 7 <= media < 10:
    print("Aprovado")
else:
    print("Reprovado")
