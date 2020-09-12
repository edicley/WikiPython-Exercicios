login = input("Informe o nome do usuário: ")
senha = input("Crie sua senha: ")

while login == senha:
    print("A senha não pode ser igual a nome de usuário. Tente novamente!")
    senha = input("Crie sua senha: ")
print("Cadastro realizado com sucesso!")