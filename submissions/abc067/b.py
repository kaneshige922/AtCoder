from collections import deque

def myceil(a,b):
    return a//b + (a%b!=0)

n = int(input())
g = [[] for i in range(n)]
for i in range(n-1):
    a,b = map(int,input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)


#mark = [set() for i in range(n)]

def bfs(s):
    queue = deque([s])
    v  = set([s])
    dist = [float("inf") for i in range(n)]
    dist[s] = 0
    while queue:
        h = queue.popleft()
        for i in g[h]:
            if i not in v:
                queue.append(i)
                v.add(i)
                dist[i] = dist[h] + 1
                #mark[i].add(s)
    return dist

dist0 = bfs(0)
distn = bfs(n-1)

cnt0 = 0
cntn = 0

for i in range(n):
    if dist0[i] <= distn[i]:
        cnt0 += 1
    else:
        cntn += 1


if cnt0 <= cntn:
    print("Snuke")
else:
    print("Fennec")
