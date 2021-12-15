import math

n = int(input())

l = 2

for i in range(3,n+1):
    l = (l*i)//math.gcd(l,i)

print(l+1)
