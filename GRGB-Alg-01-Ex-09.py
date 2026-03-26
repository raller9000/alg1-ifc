data = input("Digite uma data em 6 digitos (dia, mes, ano sem separador) \n")

if len(data) == 6 and data.isdigit():
    dia = str(data[0:2])
    mes = int(data[2:4])
    ano = int(data[4:6])
    print(f"data: {ano}{mes}{dia} \n")