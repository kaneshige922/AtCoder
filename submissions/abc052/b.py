n,a,b = map(int,input().split())
x = list(map(int,input().split()))

ans = 0
for i in range(1,n):
    dif = x[i] - x[i-1]
    if dif*a >= b:
        ans += b
    else:
        ans += dif*a

print(ans)
