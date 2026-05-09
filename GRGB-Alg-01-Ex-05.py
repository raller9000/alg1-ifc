#potencia(x, y)

def potencia(x, y):
    resultado = 1

    while y > 0:
        resultado *= x
        y -= 1

    return resultado

x = float(input())
y = int(input())

print(potencia(x, y))