n,m = map(int,input().split())
g = [[]for i in range(n)]

for i in range(m):
    a,b,c = map(int,input().split())
    g[a-1].append((b-1,c))
    g[b-1].append((a-1,c))

V = set()

#ダイクストラ
from heapq import heappop,heappush

for i in range(n):
    dist = [float("inf")]*n
    parents = [-1]*n
    dist[i] = 0

    queue = [(0,i)]

    while queue:
        path_len,v = heappop(queue)
        for w,edge_len in g[v]:
            if edge_len+path_len < dist[w]:
                dist[w] = edge_len+path_len
                parents[w] = v
                heappush(queue,(edge_len+path_len,w))

    for j in range(n):
        if i != j:
            V.add(tuple(sorted([j,parents[j]])))

ans = m - len(list(V))

print(ans)
