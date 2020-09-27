# Faça um Programa que peça dois números e imprima o maior deles.

n1 = int(input("Informe o 1º número: "))
n2 = int(input("Informe o 2º número: "))

if n1 > n2:
    print(n1)
elif n2 > n1:
    print(n2)
else:
    print("Os números são iguais.")
