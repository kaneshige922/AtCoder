import math

r,x,y = map(float,input().split())

le = math.sqrt(x**2+y**2)
if le == r:
    print(1)
elif le <= 2*r:
    print(2)
else:
    print(math.ceil((le-2*r)/r)+2)
