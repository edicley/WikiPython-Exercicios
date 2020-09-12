# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando
# as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

print('Informe sua altura e lhe direi qual é o seu peso ideal.')

altura = float(input('Informe a sua altura: '))
altura = altura / 100

peso_ideal_homem = 72.7 * altura - 58
peso_ideal_mulher = 62.1 * altura - 44.7

print(f'Para um homem com {altura}m de altura, o peso ideal é: {peso_ideal_homem} kg.')
print(f'Para uma mulher com {altura}m de altura, o peso ideal é: {peso_ideal_mulher} kg.')
