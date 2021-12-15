
n,w = map(int,input().split())
ab = [list(map(int,input().split())) for i in range(n)]

ab.sort(reverse=True)

ans = 0

for a,b in ab:
    ans += a*min(b,w)
    w -= min(b,w)
    if w == 0:
        break

print(ans)
