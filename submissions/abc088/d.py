from collections import deque

h,w = map(int,input().split())
s = [input() for i in range(h)]
#print(s)
q = deque()
q.append((0,0))
v = [[True for j in range(w)] for i in range(h)]
v[0][0] = False
ans = [[float("inf") for j in range(w)] for i in range(h)]
ans[0][0] = 0
block = 0
while q:
    t = q.popleft()   
    x = t[0]
    y = t[1]
    if t == (h-1,w-1):
        break
    if x-1 >= 0:
        if v[x-1][y]:
            if s[x-1][y] == ".":
                q.append((x-1,y))
                ans[x-1][y] = ans[x][y]+1
            v[x-1][y] = False
    if x +1 <= h-1:
        if v[x+1][y]:
            if s[x+1][y] == ".":
                q.append((x+1,y))
                ans[x+1][y] = ans[x][y]+1
            v[x+1][y] = False
    if y-1 >= 0:
        if v[x][y-1]:
            if s[x][y-1] == ".":
                q.append((x,y-1))
                ans[x][y-1] = ans[x][y]+1
            v[x][y-1] = False
    if y+1 <= w-1:
        if v[x][y+1]:
            if s[x][y+1] == ".":
                q.append((x,y+1))
                ans[x][y+1] = ans[x][y]+1
            v[x][y+1] = False
for i in range(h):
    for j in range(w):
        if s[i][j] == "#":
            block += 1


if ans[h-1][w-1] == float("inf"):
    print(-1)
else:
    print(h*w-(ans[h-1][w-1]+1)-block)



