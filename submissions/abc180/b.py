import math

n = int(input())
x = list(map(int,input().split()))
x = [abs(i) for i in x]
x2 = [i**2 for i in x]
m = sum(x)
c = max(x)
u = math.sqrt(sum(x2))

print(m)
print(u)
print(c)
