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

dic = {}
for i in range(n):
    dic[i] = []

for i in range(m):
    a,b = map(int,input().split())
    dic[a-1].append(b-1)

#print(dic)
ans = [0]

v = set()
cnt = 0

for i in range(n):
    h = n-1-i
    for j in dic[h]:
        if find(j) != find(h):
            unite(j,h)
            cnt += 1
            v.add(min(j,h))
    #print(cnt)
    ans.append(i+1-cnt)

ans.reverse()

for i in ans[1:]:
    print(i)
