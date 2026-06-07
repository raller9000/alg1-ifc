lista = []

while True:
    numero = int(input())
    
    if numero == 0:
        break
    
    lista.append(numero)
    
lista.sort()
print(lista)
