#input with some operations until empty input

x = input()

i = 0

if x == '':
    exit()
else:
    x = int(x)

xm = x
xmin = x
xman = x


while i > -1:
    x = input()
    if x == '':
        break
    else:
        x = int(x)

        xm += x

        if x < xmin:
            xmin = x

        if x > xman:
            xman = x

    i += 1

xm = xm / i

print("media:", xm)
print("menor:", xmin)
print("maior:", xman)