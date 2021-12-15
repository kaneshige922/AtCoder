from heapq import heappop,heappush
from itertools import permutations

n,m,r = map(int,input().split())
R = list(map(int,input().split()))
R = [i-1 for i in R]

g = [[] for i in range(n)]

for i in range(m):
    a,b,c = map(int,input().split())
    g[a-1].append((b-1,c))
    g[b-1].append((a-1,c))

Dist = [[float("inf") for i in range(r)] for i in range(r)]


for i in range(r):
    s = R[i]
    dist = [float("inf")]*n
    parents = [-1]*n
    dist[s] = 0

    queue = [(0,s)]

    while queue:
        path_len,v = heappop(queue)
        for w,edge_len in g[v]:
            if edge_len+path_len < dist[w]:
                dist[w] = edge_len+path_len
                parents[w] = v
                heappush(queue,(edge_len+path_len,w))
    
    for j in range(r):
        Dist[i][j] = dist[R[j]]

p = [i for i in range(r)]
P = permutations(p)

ans = float("inf")


for i in P:
    cost = 0
    for j in range(1,r):
        cost += Dist[i[j-1]][i[j]]
    ans = min(ans,cost)

print(ans)

