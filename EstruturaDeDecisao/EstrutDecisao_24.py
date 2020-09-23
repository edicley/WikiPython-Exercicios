'''
Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
par ou ímpar;
positivo ou negativo;
inteiro ou decimal.
'''

primero_numero = int(input('Informe o primeiro número: '))
segundo_numero = int(input('Informe o segundo número: '))

print('Informe que operação você deseja realizar')

print('Informe [ + ] para somar.')
print('Informe [ - ] para subtrair. ')
print('Informe [ * ] para multipicar. ')
print('Informe [ / ] para dividir.')

operacao = input('Deseja realizar que operação? ')

if operacao == '+':
    print('Você escolheu somar.')
    resultado = primero_numero + segundo_numero
elif operacao == '-':
    print('Você escolheu subtrair.')
    resultado = primero_numero - segundo_numero
elif operacao == '*':
    print('Você escolheu multiplicar.')
    resultado = primero_numero * segundo_numero
elif operacao == '/':
    print('Você escolheu dividir.')
    resultado = primero_numero / segundo_numero

if resultado % 2 == 0:
    mensagem = 'é número par'
else:
    mensagem = 'é número ímpar'
if resultado > 0:
    mensagem += ', positivo'
else:
    mensagem += ', negativo'
if type(resultado) == int:
    mensagem += ' e inteiro.'
else:
    mensagem += ' e decimal.'

print(f'{resultado} {mensagem}')

