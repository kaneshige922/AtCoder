from collections import deque


n,m = map(int,input().split())
ab = [set() for i in range(n)]
for i in range(m):
    a,b = map(int,input().split())
    ab[a-1].add(b-1)
    ab[b-1].add(a-1)

r = [0]*n

q = deque()
v = set()
ans = [0]*n
q.append(0)
v.add(0)
while q:
    h = q.popleft()
    for i in ab[h]:
        if i not in v:
            q.append(i)
            v.add(i)
            r[i] = h+1

print("Yes")
for i in range(1,n):
    print(r[i])
