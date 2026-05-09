#digits on n

def count(n):
    i = 0
    if n == 0:
        return "Error"
    else:
        while n > 0:
            n = n//10
            i = i + 1    
    print(i," digitos")

n = int(input())
count(n)