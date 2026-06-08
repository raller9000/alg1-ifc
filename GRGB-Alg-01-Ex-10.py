def func():
    lista = []
    
    while True:
        palavra = input()
        
        if palavra == '':
            break
        
        lista.append(palavra)
    
    if len(lista) == 0:
        exit()
    elif len(lista) == 1:
        print(lista[0])
    elif len(lista) == 2:
        print(lista[0] + " e " + lista[1])
    else:
        print(", ".join(lista[:-1]) + " e " + lista[-1])

func()

def main():
    print("")
    print("\ndeclarar lista e loop de palavras")
    print("""while True:
        palavra = input()
        
        if palavra == '':
            break
        
        lista.append(palavra)""")
    print("")
    print("\ncondiçoes para imprimir a lista")
    print("""f len(lista) == 0:
        exit()
          
        se ela e vazia, apenas termina
          
    elif len(lista) == 1:
        print(lista[0])
          
        apenas uma o programa so printa posicao zero
        ('banana')

    elif len(lista) == 2:
        print(lista[0] + " e " + lista[1])
          
        2 palavras = a e b
        ('banana e laranja')
          
    else:
        print(", ".join(lista[:-1]) + " e " + lista[-1])
          
          
        mais de duas palavras faz toda a logica de printar com virgula ate a penultima palavra, precisa de exemplo?""")
    
main()