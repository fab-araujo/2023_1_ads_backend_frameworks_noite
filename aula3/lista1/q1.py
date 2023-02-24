usuario = input("Digite o seu usuário: ")
senha = input("Digite a sua senha: ")

while usuario == senha:
    print("Usuário e senha não podem ser iguais! Tente novamente!")
    usuario = input("Digite o seu usuário: ")
    senha = input("Digite a sua senha: ")

print("Usuário e senha são válidos. Obrigado!")