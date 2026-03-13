x = float(input("Digite quantos vasilhames de menos de um litro. \n"))
y = float(input("Digite quantos vasilhames de um litro ou mais. \n"))

total = (x * 0.10) + (y * 0.25)

print("Valor total em credito: R$", f"{total:.2f}", "\n")