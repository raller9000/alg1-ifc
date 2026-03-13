import math

a = int(input("Digite um número inteiro. \n"))
b = int(input("Digite outro número inteiro. \n"))

sum = a + b
diff = b - a
multi = a * b
div = a / b
rest = a % b
log10 = math.log10(a)
elevated = a ** b

print(f"Soma {sum} \nDiferença {diff} \nMultiplicacao {multi} \nDiviso {div:.2f} \nResto da diviso {rest} \nLogaritmo 10 {log10:.2f} \nElevado a {elevated:.2f} \n")