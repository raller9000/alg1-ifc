import math

l1 = float(input("Digite o valor de um lado em cm. \n"))
l2 = float(input("Digite o valor do outro lado em cm. \n"))
l3 = float(input("Digite o valor do outro lado em cm. \n"))

# so pensei q seria interessante tentar fazer as condicoes, imagino que seja um exercicio futuro
if l1 <= 0 or l2 <= 0 or l3 <= 0:
    print("todos os lados devem ser positivos.")

# achava q em python era else if, interessante ser elif
elif l1 + l2 <= l3 or l1 + l3 <= l2 or l2 + l3 <= l1:
    print("os valores fornecidos nao formam um triangulo.")

else:
    x = (l1 + l2 + l3) / 2
    area = math.sqrt(x * (x - l1) * (x - l2) * (x - l3))


print("area do triangulo ", f"{area:.2f}", "cm^2 \n")