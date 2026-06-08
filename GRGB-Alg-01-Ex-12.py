def ordered(lista):
    if len(lista) == 0:
        return True
    
    if lista == sorted(lista):
        return True
    elif lista == sorted(lista, reverse=True):
        return True
    else:
        return False

def main():
    lista1 = []
    
    while True:
        numero = input()
        if numero == '':
            break
        lista1.append(int(numero))
    if ordered(lista1):
        print('classificada')
    else:
        print('desclassificada')

main()