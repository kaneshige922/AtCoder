import math

n,q =map(int,input().split())
a = list(map(int,input().split()))
k = [int(input()) for i in range(q)]
A = [0]
for i in range(n):
    A.append(a[i]-(i+1))
for i in k:
    if i > A[n]:
        print(a[n-1]+i-A[n])
    else:
        left = 0
        right = n
        mid = math.ceil((left+right)/2)
        while  not(A[mid-1]<i and A[mid]>=i):
            if A[mid] >= i:
                right = mid
            else:
                left = mid
            mid = math.ceil((left+right)/2)
        print(a[mid-1]-1-(A[mid]-i))
