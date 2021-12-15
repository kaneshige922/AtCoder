from collections import deque
from typing import List

r,c = map(int,input().split())
s = list(map(int,input().split()))
g = list(map(int,input().split()))
s = tuple([i-1 for i in s])
g = tuple([i-1 for i in g])
mp = [list(input()) for i in range(r)]

ans = [[float("Inf") for j in range(c)] for i in range(r)]

q = deque()
v = set()

q.append(s)
v.add(s)
ans[s[0]][s[1]] = 0

to = [(-1,0),(1,0),(0,-1),(0,1)]

while q:
    h = q.popleft()
    for i in to:
        x = h[0] + i[0]
        y = h[1] + i[1]
        xy = tuple([x,y])
        if (0<=x<r and 0<=y<c) and xy not in v:
            if mp[x][y] == ".":
                q.append(xy)
                v.add(xy)
                ans[x][y] = ans[h[0]][h[1]] + 1
            else:
                v.add(xy)


print(ans[g[0]][g[1]])
