N,A,X,Y = map(int,input().split())
if N <= A :
    sums = X*N
else:
    sums = X*A + Y*(N-A)
print(sums)
