def buscaReversa(dicionario, chave):
    if chave in dicionario:
        return dicionario[chave]
    else:
        return None
    
def main():
    dicionario = eval(input())
    chave = input()
    result = buscaReversa(dicionario, chave)
    print(result)

main()

