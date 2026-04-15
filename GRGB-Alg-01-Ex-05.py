#fractions of N where A = N + (N-1) + (N-2) + ... + 1/N

N = int(input())
A = N

for i in range(1, N):
    A += (N-i)/(i+1)

print(A)