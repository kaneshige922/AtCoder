import math

a,b = map(int,input().split())

if 10*b > math.ceil(12.5*(a+1))-1:
    print(-1)
elif 10*(b+1)-1 < math.ceil(12.5*a):
    print(-1)
else:
    print(max(10*b,math.ceil(12.5*a)))
