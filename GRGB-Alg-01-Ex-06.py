x = float(input("Digite o valor do prato principal. \n"))
y = float(input("Digite o valor da bebida, se houver. \n"))
z = float(input("Digite o valor da sobremesa, se houver. \n"))

total = (x + y + z)
tax = total * 0.10
final = total + tax

print("Valor total a pagar: R$", f"{final:.2f}", "\n")