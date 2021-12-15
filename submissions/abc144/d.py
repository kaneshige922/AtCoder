import math

a,b,x = map(int,input().split())

l = a**2*b-x
ans = 0
if 2*(b-x/a**2) < b:
    ans = math.degrees(math.atan(2*(b-x/a**2)/a))
else:
    ans = 90 - math.degrees(math.atan(2*x/(a*b**2)))
print(ans)
