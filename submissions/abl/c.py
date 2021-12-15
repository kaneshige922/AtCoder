
n,m = map(int,input().split())

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


unit = n

for i in range(m):
    a,b = map(int,input().split())
    if same(a-1,b-1):
        continue
    else:
        unite(a-1,b-1)
        unit -= 1

print(unit-1)
