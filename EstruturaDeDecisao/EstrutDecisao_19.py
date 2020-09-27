"""
Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas,
dezenas e unidades do mesmo.
Observando os termos no plural, a colocação do "e", da vírgula entre outros. Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades

Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
"""

print('Informe um número inteiro menor que 1000')
numero = int(input('Informe o número: '))

if numero < 1000:
    numero = str(numero)
    mensagem = ''

    if len(numero) == 3:
        centena = numero[0]
        dezena = numero[1]
        unidade = numero[2]
        centena = int(centena)
        dezena = int(dezena)
        unidade = int(unidade)

        if centena == 1:
            mensagem = f'{centena} centena, '
        elif centena > 1:
            mensagem = f'{centena} centenas, '
        if dezena <= 1:
            mensagem += f'{dezena} dezena e '
        elif dezena > 1:
            mensagem += f'{dezena} dezenas e '
        if unidade <= 1:
            mensagem += f'{unidade} unidade.'
        elif unidade > 1:
            mensagem += f'{unidade} unidades.'
    elif len(numero) == 2:
        dezena = numero[0]
        unidade = numero[1]
        dezena = int(dezena)
        unidade = int(unidade)

        if dezena <= 1:
            mensagem += f'{dezena} dezena e '
        elif dezena > 1:
            mensagem += f'{dezena} dezenas e '
        if unidade <= 1:
            mensagem += f'{unidade} unidade.'
        elif unidade > 1:
            mensagem += f'{unidade} unidades.'
    elif len(numero) == 1:
        unidade = numero[0]
        unidade = int(unidade)

        if unidade <= 1:
            mensagem += f'{unidade} unidade.'
        elif unidade > 1:
            mensagem += f'{unidade} unidades.'
    print(mensagem)
else:
    print('Número inválido.')
