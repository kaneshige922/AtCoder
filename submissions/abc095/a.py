a,b,c,x,y = map(int,input().split())

if a+b > 2*c:
    if x >= y:
        ans = 2*y*c + min((x-y)*a,2*(x-y)*c)
    else:
        ans = 2*x*c + min((y-x)*b,2*(y-x)*c)
else:
    ans = x*a + y*b

print(ans)
