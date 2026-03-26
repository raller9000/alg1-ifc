inputos = input("Digite uma squencia qualquer de ints de ate 4 digitos")

a, b, c, d = map(int, inputos.split())
total = a + b + c + d

print(f"Total: {total}\n")