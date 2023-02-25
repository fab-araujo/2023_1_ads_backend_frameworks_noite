def mes_extenso(mes):
    meses = {
        '01': 'janeiro',
        '02': 'fevereiro',
        '03': 'março',
        '04': 'abril',
        '05': 'maio',
        '06': 'junho',
        '07': 'julho',
        '08': 'agosto',
        '09': 'setembro',
        '10': 'outubro',
        '11': 'novembro',
        '12': 'dezembro'        
    }
    return meses[mes]

dia = input("Digite o dia: ")
mes = input("Digite o mês: ")
ano = input("Digite o ano: ")

mes_por_extendo = mes_extenso(mes)
print(dia+" de "+mes_por_extendo+" de " +ano)