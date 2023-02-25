import random

numero = (random.randint(0,9))

escolha = int(input("Digite um número: "))

while numero != escolha:
    print("Não foi dessa vez!")
    if escolha > numero:
        print("Você digitou um número maior que o escolhido pelo sistema")
    else:
        print("Você digitou um número menor que o escolhido pelo sistema")
    print("Tente novamente: ")
    escolha = int(input("Digite um número: "))

print("Você acertou!")