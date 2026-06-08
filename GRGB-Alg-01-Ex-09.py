lista = []
listaUnder = []
listaPlus = []
listameds = []

while True:
    number = input()
    
    if number == '':
        break
    
    lista.append(int(number))

med = sum(lista) // len(lista)

for number in lista:
    if number < med:
        listaUnder.append(number)
    elif number > med:
        listaPlus.append(number)
    elif number == med:
        listameds.append(number)

print("Média: " + str(med))
print("Elementos abaixo da média: " + str(listaUnder))
print("Elementos iguais à média: " + str(listameds))
print("Elementos acima da média: " + str(listaPlus))

