hora = int(input("Digite a hora: "))
minuto = int(input("Digite os minutos: "))
am_pm = "am"

if hora > 12:
    hora = hora - 12
    am_pm = "pm"

print("A hora é: "+str(hora)+":"+str(minuto)+" "+am_pm)