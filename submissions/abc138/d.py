from collections import deque


n,q = map(int,input().split())
graph = [[] for i in range(n)]
for i in range(n-1):
    a,b = map(int,input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

cost = [0]*n

for i in range(q):
    p,x = map(int,input().split())
    cost[p-1] += x


qu = deque([0])
v = set([0])

while(qu):
    h = qu.popleft()
    for i in graph[h]:
        if i not in v:
            cost[i] += cost[h]
            qu.append(i)
            v.add(i)

print(*cost)
