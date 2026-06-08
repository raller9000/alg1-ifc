def countRange(lista, maior, menor):
    count = 0
    for number in lista:
        if number > maior and number < menor:
            count += 1
    return count

def main():
    lista1 = []
    
    while True:
        numero = input()
        if numero == '':
            break
        lista1.append(int(numero))
    
    maior = int(input())
    menor = int(input())
    
    print(countRange(lista1, maior, menor))

main()
