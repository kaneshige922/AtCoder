import math

n = int(input())
a = list(map(int,input().split()))

g = a[0]
for i in a[1:]:
    g = math.gcd(g,i)

print(g)
