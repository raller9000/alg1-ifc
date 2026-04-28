#while loop, binary to decimal

x = input()
y = 0
z = len(x)
ac = 0

while ac < z:
    if x[ac] == "1":
        y = y * 2
        y = y + 1
    ac = ac + 1
print(y)

