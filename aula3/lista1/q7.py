cardapio = {
    100: 1.2,
    101: 1.3,
    102: 1.5,
    103: 1.2
}
total = 0

opcao = int(input("Digite uma opção ou 0 para sair: "))
if opcao != 0:
    qtd = int(input("Digite a quantidade: "))
while opcao != 0:
    total = total + (cardapio[opcao] * qtd)
    opcao = int(input("Digite uma opção ou 0 para sair: "))
    if opcao != 0:
        qtd = int(input("Digite a quantidade: "))

print("O total da conta é R$ "+str(total))