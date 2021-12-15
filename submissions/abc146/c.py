a,b,x = map(int,input().split())

def f (n):
    s = str(n)
    return a*n+b*len(s)

if f(10**9) <= x:
    print(int(10**9))
    exit()
elif f(1) > x:
    print(0)
    exit()

ans = 0
for i in range(1,11):
    x1 = x - b*i
    k = x1//a
    if k >= 10**i:
        k = 10**i -1 
    ans = max(k,ans)
print(ans)
