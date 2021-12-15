n,m = map(int,input().split())

ab = [list(map(int,input().split())) for i in range(m)]

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

ans = 0

for i in range(m):
    par = [-1 for i in range(n)]
    rank = [0 for i in range(n)]
    for j in range(m):
        if i != j:
            unite(ab[j][0]-1,ab[j][1]-1)
    if find(ab[i][0]-1) != find(ab[i][1]-1):
        ans += 1

print(ans)
