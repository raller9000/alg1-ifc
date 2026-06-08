def func(string):
    conta = set()

    for letra in string:
        if letra in conta:
            return False
        conta.add(letra)
    return True

# baseado no codigo dado pelo slide e de uso para resto da lista, nao ha motivo para usar uma versao pior ou igual em semantica e mais verbosa
def main():
    string = input()
    
    if func(string):
        print("unico.")
    else:
        print("repetidos.")

main()