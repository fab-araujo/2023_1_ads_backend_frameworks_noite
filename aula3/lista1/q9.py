numero = int(input("Digite um número: "))
contador = 1

while contador <= numero:
    contador_aux = 1
    while contador_aux <= contador:
        print(contador_aux, end=" ")
        contador_aux = contador_aux + 1
    print("")
    contador = contador + 1