from collections import deque

h,w = map(int,input().split())

c = [list(input()) for i in range(h)]

q = deque()
v = set()

for i in range(h):
    for j in range(w):
        if c[i][j] == "s":
            q.append(tuple([i,j]))
            v.add(tuple([i,j]))
            break
    if q:
        break

to = [(0,1),(-1,0),(0,-1),(1,0)]

while q:
    n = q.popleft()
    for i in to:
        x = n[0]+i[0] 
        y = n[1]+i[1]
        if (0 <= x and x < h) and (0 <= y and y < w):
            if tuple([x,y]) not in v:
                t = tuple([x,y])
                if c[x][y] == "#":
                    v.add(t)
                elif c[x][y] == ".":
                    v.add(t)
                    q.append(t)
                else:
                    print("Yes")         
                    exit()

print("No")





