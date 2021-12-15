from collections import deque

n,m = map(int,input().split())

path = [set() for i in range(n)]

for i in range(m):
    a,b = map(int,input().split())
    path[a-1].add(b-1)
    path[b-1].add(a-1)

q = deque()
v = set()
ans = 0

for i in range(n):
    if i not in v:
        q.append(i)
        v.add(i)
        t = True
        while q:
            h = q.popleft()
            for j in path[h]:
                if j not in v:
                    for k in path[j]:
                        if k in (v-set([h])):
                            t = False  
                    q.append(j)
                    v.add(j)
        if t:
            ans += 1

print(ans)


