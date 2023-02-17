nome = input("Escreva seu nome: ")
nascimento = input("Escreva o ano que você nasceu: ")
nascimento = int(nascimento)
idade = 2023 - nascimento

frase = nome + " " + idade

print(frase)