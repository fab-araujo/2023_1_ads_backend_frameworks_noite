n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o primeiro número: "))
n3 = int(input("Digite o primeiro número: "))
n4 = int(input("Digite o primeiro número: "))
n5 = int(input("Digite o primeiro número: "))

numeros = [n1, n2, n3, n4, n5]

maior = numeros[0]
menor = numeros [0]

for i in numeros:
    if i > maior:
        maior = i

    if i < menor:
        menor = i

print("O maior número é: "+str(menor))
print("O maior número é: "+str(maior))