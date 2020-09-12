# Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo
# que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

print('Informe sua altura e lhe direi qual é o seu peso ideal.')

altura = float(input('Informe a sua altura: '))
altura = altura / 100
peso_ideal = 72.7 * altura - 58

print(f'Seu peso ideal é {peso_ideal:.2f} kg.')