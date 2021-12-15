n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
dif = [b[i]-a[i] for i in range(n)]

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

for i in range(m):
    c,d = map(int,input().split())
    unite(c-1,d-1)


dic = {}
for i in range(n):
    dic[i] = 0

for i in range(n):
    dic[find(i)] += dif[i]

ans = True
for i in range(n):
    if dic[i] != 0:
        ans = False
        break

if ans:
    print("Yes")
else:
    print("No")
