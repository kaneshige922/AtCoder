import math

x,y,a,b = map(int,input().split())

if x*a >= y and a+b >= y:
    ans = 0
elif (a-1)*x >= b:
    ans = (y-1-x)//b
else:
    t = math.ceil(math.log(b/((a-1)*x),a))
    ans = (y-1-x*(a**t))//b + t

print(ans)
