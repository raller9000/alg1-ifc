#eh_bissexto(ano)

def eh_bissexto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    else:
        return False

ano = int(input())
if eh_bissexto(ano):
    print(ano, "é um ano bissexto.") 
else:
    print(ano, "não é um ano bissexto.")
