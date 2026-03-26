rawcents = int(input("digite os centavos (0, 99): \n"))

fifty, remainder = divmod(rawcents, 50)
twentyfive, remainder = divmod(remainder, 25)
ten, remainder = divmod(remainder, 10)
five, remainder = divmod(remainder, 5)
rest = remainder

print(f"Moedas de 50 centavos: {fifty}")
print(f"Moedas de 25 centavos: {twentyfive}")
print(f"Moedas de 10 centavos: {ten}")
print(f"Moedas de 5 centavos: {five}")
print(f"Resto: {rest} centavos \n")