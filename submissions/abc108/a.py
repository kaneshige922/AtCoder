import math

n,k = map(int,input().split())

if k % 2 == 0:
    a = math.floor((n + k//2)/k)
    b = math.floor(n/k)
    print(a**3 + b ** 3)
else:
    b = math.floor(n/k)
    print(b ** 3)
