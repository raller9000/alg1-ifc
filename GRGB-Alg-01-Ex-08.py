#10 input with some operations

x = int(input())
xm = x
xmin = x
xman = x
i=0

while i < 10:
    x = int(input())
    xm += x
    if x < xmin:
        xmin = x
    if x > xman:
        xman = x
    i += 1

xm = xm / 10

print("media:", xm)
print("menor:", xmin)
print("maior:", xman)