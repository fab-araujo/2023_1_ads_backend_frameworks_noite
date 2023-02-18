n = int(input("Digite o número para a tabuada: "))

print("A tabuada de "+str(n)+" é: ")

for i in range(11):
    print(str(n)+" x "+str(i)+" = "+str(i*n))