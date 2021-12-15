
n,m = map(int,input().split())
ab = [list(map(int,input().split())) for i in range(m)]
ab.reverse()

cost = [n*(n-1)//2]

#n = 100#—v‘f”n‚ğéŒ¾
par = [-1 for i in range(n)]
rank = [0 for i in range(n)]
size = [1 for i in range(n)]
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
            size[y] += size[x]
        else:
            par[y] = x
            size[x] += size[y]
            if rank[x] == rank[y]:
                rank[x] += 1
def same(x,y):
    if find(x) == find(y):
        return True
    else:
        return False

def nC2 (r):
    return r*(r-1)//2



for a,b in ab:
    a -= 1
    b -= 1
    if find(a) != find(b):
        s = 0
        s -= nC2(size[find(a)])+nC2(size[find(b)])
        unite(a,b)
        s +=  nC2(size[find(a)])
        cost.append(cost[-1]-s)
    else:
        cost.append(cost[-1])


cost.reverse()

for i in cost[1:]:
    print(i)
