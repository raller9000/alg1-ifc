#prime fatorization of a number

fator = 2
n = int(input())

while n > 1:
    if n % fator == 0:
        print(fator)
        n = n/fator
    else:
        fator = fator + 1