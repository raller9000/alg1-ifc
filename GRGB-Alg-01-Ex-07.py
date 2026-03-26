N = input("Digite uma squencia qualquer de ints de ate 3 digitos \n")

C, D, U= map(int, N)
C = C * 100
D = D * 10

print(f"centena: {C} \n")
print(f"dezena: {D} \n")
print(f"unidade: {U} \n")