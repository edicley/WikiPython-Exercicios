# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, 
# sabendo que a decisão é sempre pelo mais barato.

prod1 = int(input("Qual o preço do quiejo coalho? "))
prod2 = int(input("Qual o preço do quiejo mussarela? "))
prod3 = int(input("Qual o preço do quiejo prato? "))

if prod1 < prod2 and prod1 < prod3:
    print("Leve o queijo coalho.")
elif prod2 < prod1 and prod2 < prod3:
    print("Leve o queijo mussarela.")
else:
    print("Leve o queijo prato.")