from collections import deque

n,x,y = map(int,input().split())

path = [set() for i in range(n)]
for i in range(n-1):
    path[i].add(i+1)
    path[i+1].add(i)
path[x-1].add(y-1)
path[y-1].add(x-1)

ans = [0]*(n-1)

for i in range(n):
    kyo = [0]*n
    q = deque([i])
    v = set([i])
    while q:
        h = q.popleft()
        for j in path[h]:
            if j not in v:
                q.append(j)
                v.add(j)
                kyo[j] = kyo[h]+1
                ans[kyo[j]-1] += 1

for i in ans:
    print(i//2)

