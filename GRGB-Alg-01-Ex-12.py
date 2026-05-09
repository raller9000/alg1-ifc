# encaixa(a, b)

def encaixa(a, b):

    while a != b and a > 0:
        a = a//10
    if a == b:
        return "encaixa"
    else:
        return "nao encaixa"

a = int(input())
b = int(input())
print(encaixa(a, b))