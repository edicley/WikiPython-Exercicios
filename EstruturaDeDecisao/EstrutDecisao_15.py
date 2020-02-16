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
    