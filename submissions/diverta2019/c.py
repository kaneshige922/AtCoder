from collections import deque


n = int(input())
L = [list(input()) for _ in range(n)]

#n = 100#—v‘f”n‚ğéŒ¾
par = [-1 for i in range(n)]
rank = [0 for i in range(n)]
def find(x):
    if par[x] == -1:
        return x
    else:
        return find(par[x])
def unite(x,y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    else:
        if rank[x] < rank[y]:
            par[x] = y
        else:
            par[y] = x
            if rank[x] == rank[y]:
                rank[x] += 1
def same(x,y):
    if find(x) == find(y):
        return True
    else:
        return False






a = deque()
b = deque()

ans = 0

for i in range(n):
    l = L[i]
    if l[0] == "B":
        b.append(i)
    if l[-1] == "A":
        a.append(i)
    for j in range(len(l)-1):
        if l[j] == "A" and l[j+1] == "B":
            ans += 1
    
while a and b:
    x = a.popleft()
    y = b.popleft()
    if not(same(x,y)):
        unite(x,y)
        ans += 1
    else:
        if b:
            b.append(y)
            y = b.popleft()
            unite(x,y)
            ans += 1
        else:
            b.append(y)

print(ans)
