#more and more precise

i = 0
pi = 3
sinal = 1

part1, part2, part3 = 2, 3, 4
while i < 15:
    pip = pi + sinal * 4 / (part1 * part2 * part3)
    i += 1
    sinal *= -1
    part1 += 2
    part2 += 2
    part3 += 2
    pi = pip
    print(pi)
