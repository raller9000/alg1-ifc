#heads or tails!!!

import random

i = 0
ac = ""
ac2 = ""
fullac = ""
total = 0
fulltotal = 0

while i < 10:

    if ac == "AAA" or ac2 == "OOO":
        print(fullac)
        ac2 = ""
        ac = ""
        i += 1
        total = fullac.count("A") + fullac.count("O")
        print(f"total de sorteios: {total}")
        fulltotal = fulltotal + total
        fullac = ""

    else:
        x = random.randint(0,1)

        if x == 0:
            ac = ac + "A"
            ac2 = ""
            fullac = fullac + "A"

        else:
            ac2 = ac2 + "O"
            ac = ""
            fullac = fullac + "O"

med = fulltotal/10
print(f"media de sorteios: {med:.2f}")