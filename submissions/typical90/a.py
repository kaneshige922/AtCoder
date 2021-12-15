h,w = map(int,input().split())

g = [list(map(int,input().split())) for i in range(h)]
g2 = [list(map(int,input().split())) for i in range(h)]

for i in range(h):
    for j in range(w):
        g[i][j] -= g2[i][j]

ans = 0

for i in range(h-1):
    for j in range(w-1):
        a = abs(g[i][j])
        ans += a
        if g[i][j] >= 0:
            g[i][j] -= a
            g[i+1][j] -= a
            g[i][j+1] -= a
            g[i+1][j+1] -= a
        else:
            g[i][j] += a
            g[i+1][j] += a
            g[i][j+1] += a
            g[i+1][j+1] += a

t = True
for i in range(h):
    for j in range(w):
        if g[i][j] != 0:
            t = False

if(t):
    print("Yes")
    print(ans)
else:
    print("No")
