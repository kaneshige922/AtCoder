from collections import deque

h,w = map(int,input().split())
c = list(map(int,input().split()))
d = list(map(int,input().split()))
c = [i-1 for i in c]
d = [i-1 for i in d]


s = [list(input()) for i in range(h)]

g = [[-1]*w for i in range(h)]

cnt = 1
v = set()
def bfs(p):
    global cnt
    v.add(tuple(p))
    q = deque()
    if s[p[0]][p[1]] == ".":
        q = deque([p])
        g[p[0]][p[1]] = cnt
        while q:
            n = q.popleft()
            if n[0]-1 >= 0 and tuple([n[0]-1,n[1]]) not in v:
                v.add(tuple([n[0]-1,n[1]]))
                if s[n[0]-1][n[1]] == ".":
                    g[n[0]-1][n[1]] = cnt
                    q.append([n[0]-1,n[1]])
            if n[1]-1 >= 0 and tuple([n[0],n[1]-1]) not in v:
                v.add(tuple([n[0],n[1]-1]))
                if s[n[0]][n[1]-1] == ".":
                    g[n[0]][n[1]-1] = cnt
                    q.append([n[0],n[1]-1])
            if n[0]+1 < h and tuple([n[0]+1,n[1]]) not in v:
                v.add(tuple([n[0]+1,n[1]]))
                if s[n[0]+1][n[1]] == ".":
                    g[n[0]+1][n[1]] = cnt
                    q.append([n[0]+1,n[1]])
            if n[1]+1 < w and tuple([n[0],n[1]+1]) not in v:
                v.add(tuple([n[0],n[1]+1]))
                if s[n[0]][n[1]+1] == ".":
                    g[n[0]][n[1]+1] = cnt
                    q.append([n[0],n[1]+1])
        cnt += 1

bfs(c)
if g[c[0]][c[1]] == g[d[0]][d[1]]:
    print(0)
    exit()
bfs(d)
for i in range(h):
    for j in range(w):
        if tuple([i,j]) not in v:
            bfs([i,j])

path = [set() for i in range(cnt-1)]

for i in range(h):
    for j in range(w):
        if g[i][j] >= 1:
            """""
            if i+2 < h and j + 2 < w:
                if g[i][j] != g[i+2][j+2] and g[i+2][j+2] != -1:
                    path[g[i][j]-1].add(g[i+2][j+2]-1)
                    path[g[i+2][j+2]-1].add(g[i][j]-1)
            if i+2 < h and j + 1 < w:  
                if g[i][j] != g[i][j+2] and g[i][j+2] != -1:
                    path[g[i][j]-1].add(g[i][j+2]-1)
                    path[g[i][j+2]-1].add(g[i][j]-1)
                if g[i][j] != g[i+1][j+2] and g[i+1][j+2] != -1:
                    path[g[i][j]-1].add(g[i+1][j+2]-1)
                    path[g[i+1][j+2]-1].add(g[i][j]-1)
                if g[i][j] != g[i+1][j+1] and g[i+1][j+1] != -1:
                    path[g[i][j]].add(g[i+1][j+1]-1)
                    path[g[i+1][j+1]-1].add(g[i][j]-1)
                if g[i][j] != g[i+2][j] and g[i+2][j] != -1:
                    path[g[i][j]-1].add(g[i+2][j]-1)
                    path[g[i+2][j]-1].add(g[i][j]-1)
                if g[i][j] != g[i+2][j+1] and g[i+2][j+1] != -1:
                    path[g[i][j]-1].add(g[i+2][j+1]-1)
                    path[g[i+2][j+1]-1].add(g[i][j]-1)
                """
            for k in range(5):
                for l in range(5):
                    x = i-2+k
                    y = j-2+l
                    if (0 <= x and x < h) and (0 <= y and y < w):
                        if g[i][j] != g[x][y] and g[x][y] != -1:
                            path[g[i][j]-1].add(g[x][y]-1)
                            path[g[x][y]-1].add(g[i][j]-1)
            
ans = [0 for i in range(cnt-1)]
q2 = deque([0])
v2 = set([0])
while q2:
    n = q2.popleft()
    for i in path[n]:
        if i not in v2:
            ans[i] = ans[n] + 1
            v2.add(i)
            q2.append(i)
            if i == 1:
                break

if ans[1] == 0:
    print(-1)
else:
    print(ans[1])


