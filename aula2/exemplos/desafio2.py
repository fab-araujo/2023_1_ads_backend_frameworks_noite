print("Bem-vindo à calculadora!")
print("Escolha uma das opções abaixo:")
print("1 - Soma")
print("2 - Substração")
print("3 - Multiplicação")
print("4 - Divisão")
print("5 - Sair")

opcao = input("Qual a opção desejada? ")

opcao = int(opcao)

while(opcao != 5):
    n1 = input("Digite o primeiro número: ")
    n2 = input("Digite o segundo número: ")
    n1 = float(n1)
    n2 = float(n2)

    if opcao == 1:
        soma = n1 + n2
        print("O resultado da soma é: "+str(soma))
    elif opcao == 2:
        subtracao = n1 - n2
        print("O resultado da subtração é: "+str(subtracao))
    elif opcao == 3:
        multiplicacao = n1 * n2
        print("O resultado da multiplicação é: "+str(multiplicacao))
    elif opcao == 4:
        divisao = n1 / n2
        print("O resultado da divisão é: "+str(divisao))

    print("--------")
    print("Operação finalizada! Recomeçando...")
    opcao = input("Qual a opção desejada? ")
    opcao = int(opcao)
print("Bye!")