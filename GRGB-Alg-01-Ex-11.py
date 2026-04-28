#phrasereverse

while True:
    x = input()
    if x == "":
        break

    x = x.replace(" ","")
    y = x[::-1]

    if y.casefold() == x.casefold():
        print("\npalindromo")
        print(x,"=",y)
    else:
        print("\nnao palindromo")
        print(x,"!=",y)
    