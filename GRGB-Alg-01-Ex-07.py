#sorteia_dado() but one million times

import random

def sorteia_dado():
    one = two = three = four = five = six = med = 0
    for y in range(1000000):
        x = random.randint(1,6)
        print(x, end=" ")
    
        if x == 1:
            one = one + 1
        elif x == 2:
            two = two + 1
        elif x == 3:
            three = three + 1
        elif x == 4:
            four = four + 1
        elif x == 5:
            five = five + 1
        else:
            six = six + 1

    p1 = one/10000
    p2 = two/10000
    p3 = three/10000
    p4 = four/10000
    p5 = five/10000
    p6 = six/10000

    print(f"\n1: {p1:.2f}%")
    print(f"\n2: {p2:.2f}%")
    print(f"\n3: {p3:.2f}%")
    print(f"\n4: {p4:.2f}%")
    print(f"\n5: {p5:.2f}%")
    print(f"\n6: {p6:.2f}%")

    print("sim :3")

sorteia_dado()