# Faça um Programa que leia três números e mostre o maior e o menor deles.

n1 = int(input("Insira o 1º número: "))
n2 = int(input("Insira o 2º número: "))
n3 = int(input("Insira o 3º número: "))

if n1 > n2 and n1 > n3:
    print(n1, "é o maior dos três números.")
elif n2 > n1 and n2 > n3:
    print(n2, "é o maior dos três números.")
else:
    print(n3, "é o maior dos três números.")

if n1 < n2 and n1 < n3:
    print(n1, "é o menor dos três números.")
elif n2 < n1 and n2 < n3:
    print(n2, "é o menor dos três números.")
else:
    print(n3, "é o menor dos três números.")
