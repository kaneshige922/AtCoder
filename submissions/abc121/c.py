n,m = map(int,input().split())
ab = [list(map(int,input().split())) for i in range(n)]

ab.sort()

ans = 0

for i in range(n):
    ans += ab[i][0]*min(ab[i][1],m)
    m -= min(ab[i][1],m)
    if m == 0:
        break

print(ans)
