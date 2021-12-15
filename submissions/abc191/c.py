from collections import deque


h,w = map(int,input().split())
s = [list(input()) for i in range(h)]
g = [[0]*(w+1) for i in range(h+1)]

sx = -1
sy = -1

flag = True
for i in range(h):
    for j in range(w):
        if s[i][j] == "#":
            g[i][j] += 1
            g[i][j+1] += 1
            g[i+1][j] += 1
            g[i+1][j+1] += 1
            if flag:
                sx = i;sy = j
                flag = False

"""""
qu = deque([tuple([sx,sy])])
v = set([tuple([sx,sy])])

to = [(-1,0),(1,0),(0,-1),(0,1)]
dir = -1
ans = 0
while(qu):
    now = qu.popleft()
    for i in range(4):
        x = now[0] + to[i][0]
        y = now[1] + to[i][1]
        xy = tuple([x,y])
        if xy == tuple([sx,sy]) and ans >= 3:
            if dir != i:
                ans += 1
            break
        if (0<=x<=h and 0<=y<=w) and xy not in v:
            if 1 <= g[x][y] <= 3:
                qu.append(xy)
                v.add(xy)
                if dir != i:
                    ans += 1
                    dir = i
                break
"""

ans = 0

for i in range(h+1):
    for j in range(w+1):
        if g[i][j] == 1 or g[i][j] == 3:
            ans += 1



print(ans)
