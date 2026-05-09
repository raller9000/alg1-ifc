#duas func

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
        return -1
    
def permutacao(a, b):

    for d in range(10):
         if conta_digitos(a, d) != conta_digitos(b, d):
             return False
         
    return True

a = int(input())
b = int(input())

print(permutacao(a, b))