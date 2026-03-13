import math

n = int(input("digite um numero de lados \n"))
l = float(input("digite o comprimento dos lados \n"))

if n < 0 or l < 0:
    print("o numero de lados e o comprimento dos lados devem ser positivos. \n")

else:
    area = (n * (l ** 2)) / (4 * math.tan(math.pi / n))

print("area do poligono ", f"{area:.2f}", "cm^2 \n")