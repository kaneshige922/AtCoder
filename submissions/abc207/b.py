import math

a,b,c,d = map(int,input().split())
if a == 0:
    print(0)
elif  c*d - b <= 0:
    print(-1)
else:
    print(math.ceil(a/(c*d-b)))
