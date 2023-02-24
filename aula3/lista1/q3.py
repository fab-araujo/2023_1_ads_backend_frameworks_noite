soma = 0
for i in range(5):
    num = float(input("Digite o número "+str(i)+": "))
    soma = soma + num

media = soma / 5

print("A soma dos números é: "+str(soma))
print("A média dos números é: "+str(media))

