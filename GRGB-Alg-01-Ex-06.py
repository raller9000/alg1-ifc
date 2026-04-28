#parity bits

while True:
    x = input()
    if x == "":
        break
    elif len(x) != 8 or any(c not in "01" for c in x):
        print("Invalido")
        continue

    um = x.count("1")
    if um % 2 == 0:
        print("Paridade par")
    else:
        print("Paridade impar")
        