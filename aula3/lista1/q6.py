numero = int(input("Digite o número: "))
contador = numero
fatorial = numero

while contador > 1:
    fatorial = fatorial * (contador - 1)
    contador = contador - 1

print("O fatorial de "+str(numero)+" é: "+str(fatorial))