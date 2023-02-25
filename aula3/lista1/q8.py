numero = int(input("Digite um número: "))
contador = 1

while contador <= numero:
    contador_aux = contador
    while contador_aux > 0:
        print(contador, end=" ")
        contador_aux = contador_aux - 1
    print("")
    contador = contador + 1