from collections import deque

h,w = map(int,input().split())
s = [list(input()) for i in range(h)]
to = [[-1,0],[1,0],[0,-1],[0,1]]

ans = -1

for i in range(h):
    for j in range(w):
        if s[i][j] == ".":
            q = deque([[i,j]])
            v = set()
            v.add(tuple([i,j]))
            k = [[0]*w for i in range(h)]
            while q:
                n = q.popleft()
                for l in to:
                    x = n[0]+l[0] 
                    y = n[1]+l[1]
                    if (0 <= x and x <h) and (0 <= y and y<w):
                        if tuple([x,y]) not in v and s[x][y] == ".":
                            v.add(tuple([x,y]))
                            q.append([x,y])
                            k[x][y] = k[n[0]][n[1]] + 1
                            ans = max(ans,k[x][y])

print(ans)


