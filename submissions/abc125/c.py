import math

n =int(input())
a =list(map(int,input().split()))

if n == 2:
    print(max(a))
    exit()

g = a[0]
g0 = a[0]
for i in a[1:]:
    g0 = max(g,math.gcd(g0,i))
    g = math.gcd(g,i)
g2 = a[1]
for i in a[2:]:
    g2 = math.gcd(g2,i)

print(max(g0,g2))
