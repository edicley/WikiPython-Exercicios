"""
Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo.
Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:

Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;
"""
print("Informe três valores e lhe direi se é possível criar um triângulo. Se for possível, lhe direi a categoria dele.")
l1 = float(input("Informe o primeiro valor: "))
l2 = float(input("Informe o segundo valor: "))
l3 = float(input("Informe o terceiro valor: "))

if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    print("É um triângulo.")
    if l1 == l2 and l1 == l3:
        print("Temos um triângulo Equilátero.")
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print("Temos um triângulo Isósceles.")
    else:
        print("Temos um triângulo Escaleno.")
else:
    print("Não podemos formar um triângulo com esses valores.")
