base = float(input("Digite o valor da base: "))
expoente = int(input("Digite o valor do expoente: "))
resultado = 1

for n in range(expoente):
    resultado = resultado * base

print("O valor de "+str(base)+" elevador a "+str(expoente)+" é: "+str(resultado))
