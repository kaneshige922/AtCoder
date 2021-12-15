n =int(input())
a = list(map(int,input().split()))

ans = 0

for r in range(n):
    s = [i for i in range(r+1)]
    s.reverse()
    ma = a[r]
    for l in s:
        ma = min(ma,a[l])
        ans = max(ans,ma*(r-l+1))

print(ans)



