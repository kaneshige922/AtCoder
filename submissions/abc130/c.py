w,h,p,q = map(int,input().split())
""""
a = (2*h-2*q)/(w-p)
b = (q*w-2*h*p+p*q)/(w-p)
c = (2*w-2*p)/(h-q)
d = (p*h-2*w*q+p*q)/(h-q)

count = -1
if (a*w+b >=0 and a*w+b<=h) and (b>=0 and b<=h):
    count += 1
if (c*h+d>=0 and c*h+d <=w) and (d>=0 and d<=w):
    count += 1
"""
if 2*p == w and 2*q == h:
    print(w*h/2,1)
else:
    print(w*h/2,0)
