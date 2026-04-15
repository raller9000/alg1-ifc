#complex thing

A = 1.0

N = int(input())
i = 1

while i > 0:

    if i + 2 > 2*N - 1:
        break

    A += 1/(i+2)
    i += 2
print(A)