# encaixa 2

def encaixa(a, b):

    while a != b and a > 0:
        a = a//10

    # mudei pra encaixar a funcao

    return a == b

def segmento(a, b):

    if a > b:
        maior = a
        menor = b
        
    else:
        maior = b
        menor = a

    while maior > 0:

        if encaixa(maior, menor):
            return "segmento"
        
        maior = maior // 10

    return "nao segmento"

a = int(input())
b = int(input())

print(segmento(a, b))