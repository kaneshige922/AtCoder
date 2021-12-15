import math

t,n = map(int,input().split())

print(math.ceil(100*n/t)+(n-1))

