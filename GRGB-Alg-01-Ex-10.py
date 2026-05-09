#conta_digitos(n, d)

def conta_digitos(n, d):
    if 0 < d <= 9:
        i = 0
        while n > 0:
            if n % 10 == d:
                i = i + 1
            n = n//10
        return i
        #print(i," vezes o digito ",d) tirado para compatibilidade com outra questao
    else:
        return "Error"

n = int(input())
d = int(input())

conta_digitos(n, d)