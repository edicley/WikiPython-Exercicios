"""
Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os
valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:

Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os
demais valores, sendo encerrado;

Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
"""

print('Vamos calcular as raízes de uma equação do 2º grau.')

a = int(input('Informe o valor de a: '))

if a == 0:
    print('Não é uma equação do 2º grau.')
else:
    b = int(input('Informe o valor de b: '))
    c = int(input('Informe o valor de c: '))
    delta = (b ** 2 - 4 * a * c)

    if delta < 0:
        print('Delta negativo. Não possui raiz real.')
    elif delta == 0:
        raiz = -b / (2 * a)
        print(f'Delta = 0. A equação possui apenas uma raiz: {raiz}')
    else:
        x1 = (-b + delta**(1/2)) / (2*a)
        x2 = (-b - delta**(1/2)) / (2*a)
        print(f'Raiz x: {x1:.1f}')
        print(f'Raiz y: {x2}')
