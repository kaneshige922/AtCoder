import math

a,b,h,m = map(int,input().split())

theta = abs(30*h - 5.5*m)

ans = math.sqrt(a**2 + b**2 - 2*a*b*math.cos(math.radians(theta)))

print(ans)
