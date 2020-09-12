# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo
# (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a
# variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite
# e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

peso_peixes = float(input('Informe quantos kg de peixe você pescou: '))

limite_peixe = 50
excesso = peso_peixes - limite_peixe
multa = 4 * excesso

print(f'Você pescou {peso_peixes} kg.')
print(f'Excedeu o limite em {excesso:.3f} kg.')
print(f'O valor da multa será: R${multa:.2f}')
