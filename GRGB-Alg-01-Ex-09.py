#newton sqrt method

x = int(input())
y = x/2
thegoodenough = 0.001 #could be anything (0.n+1, n= quantity of zeros) :)

while abs(y**2 - x) > thegoodenough:
    y = (y + x/y)/2
print(y)
