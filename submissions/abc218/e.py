n,m = map(int,input().split())


path = [list(map(int,input().split())) for i in range(m)]

path = sorted(path,key = lambda x:x[2])


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


ans = 0

for i in path:
    if same(i[0]-1,i[1]-1):
        if i[2] >= 0:
            ans += i[2]
    else:
        unite(i[0]-1,i[1]-1)
        
print(ans)
