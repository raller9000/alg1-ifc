#price calculation

ac = 0.0
inputs = 0

while True:

    x = input()
    if x == "":
        break

    x = float(x)

    if x <= 2:
        ac += 0.0
        inputs += 1

    elif x >=3 and x <= 12:
        ac += 15.00
        inputs += 1

    elif x >= 65:
        ac += 18.00
        inputs += 1

    else:
        ac += 23.00
        inputs += 1

print(f"total: {ac:.2f}")