
n,m,k = map(int,input().split())
ab = [list(map(int,input().split())) for i in range(m)]
cd = [list(map(int,input().split())) for i in range(k)]

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
cnt = {}

for i in ab:
    unite(i[0]-1,i[1]-1)


for i in range(n):
    j = find(i)
    if j  not in dic:
        dic[j] = set([i])
        cnt[j] = 1
    else:
        dic[j].add(i)
        cnt[j] += 1

ans = [0]*n

for i in range(n):
    ans[i] += cnt[find(i)]-1
for i in ab:
    if find(i[0]-1) == find(i[1]-1):
        ans[i[0]-1] -= 1
        ans[i[1]-1] -= 1
for i in cd:
    if find(i[0]-1) == find(i[1]-1):
        ans[i[0]-1] -= 1
        ans[i[1]-1] -= 1

print(*ans)
