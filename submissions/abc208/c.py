n,k = map(int,input().split())
a = list(map(int,input().split()))
A = {}
b = sorted(a)
for i in range(n):
    if i <= k%n-1:
        A[str(b[i])] = k//n +1
    else:
        A[str(b[i])] = k//n
for i in range(n):
    print(A[str(a[i])])
