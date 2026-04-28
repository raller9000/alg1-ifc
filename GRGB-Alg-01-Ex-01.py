#0 to drop
import sys

x = int(input())
y = 1
z = 0

if x == 0:
    sys.exit("Valor deve ser maior que 0")

else:
    while x > 0:
        x = int(input())
        y = y + 1
        z = z + x

med = z/y

print("media: ", med)