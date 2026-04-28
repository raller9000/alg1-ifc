#distance from a point to another, very hard

perimeter = 0

x = input()
if x == "":
    exit()
y = input()

x0 = float(x)
y0 = float(y)

lastx = x0
lasty = y0

while True:
    try:
        xi = input()        
        if x == "":
            break
        yi = input()

        x = float(xi)
        y = float(yi)

    except ValueError:
        break

    distance = ((lastx - x)**2 + (lasty - y)**2)**0.5
    perimeter += distance

    lastx = x
    lasty = y

distance = ((lastx - x0)**2 + (lasty - y0)**2)**0.5
perimeter += distance

print("perimetro: ", perimeter) 