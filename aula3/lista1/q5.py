pares = 0
impares = 0

for i in range(10):
    num = int(input("Digite um número: "))
    if num % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1

print("Foram digitados "+str(pares)+" números pares.")
print("Foram digitados "+str(impares)+" números ímpares.")