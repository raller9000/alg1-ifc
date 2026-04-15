#fractions of A until N

N = int(input())+1 #seria +1 para compensar pelo loop for e n dar pra dividir pro i=0
A = 1.0

for i in range(1, N):
    A = A + 1/i
    print(A)
