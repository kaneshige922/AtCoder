from collections import deque

h,w = map(int,input().split())
s = tuple(list(map(int,input().split())))
t = tuple(list(map(int,input().split())))
S = [list(input()) for i in range(h)]

que1 = deque()
que2 = deque()

to = [(0,1),(0,-1),(1,0),(-1,0)]

ans = [[float("inf") for i in range(w)] for j in range(h)]

que1.append((s[0]-1,s[1]-1,0,-1))
ans[s[0]-1][s[1]-1] = 0

now = que1.popleft()
for i in range(4):
    x = now[0] + to[i][0]
    y = now[1] + to[i][1]
    if(0<=x<h) and (0<=y<w):
        if(S[x][y]=="."):
            que1.append((x,y,now[2],i))
            ans[x][y]= now[2]

while(que1):
    now = que1.popleft()
    for i in range(4):
        x = now[0] + to[i][0]
        y = now[1] + to[i][1]
        if(0<=x<h) and (0<=y<w):
            if(S[x][y]=="."):
                if(now[3]==i):
                    if(ans[x][y]>=now[2]):
                        que1.appendleft((x,y,now[2],i))
                        ans[x][y]= now[2]
                else:
                    if(ans[x][y]>=now[2]+1):
                        que1.append((x,y,now[2]+1,i))
                        ans[x][y]=now[2]+1

print(ans[t[0]-1][t[1]-1])
