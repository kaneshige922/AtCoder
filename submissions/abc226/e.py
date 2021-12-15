
n,m = map(int,input().split())

g = [[] for i in range(n)]

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

Ms = []
for i in range(m):
    a,b = map(int,input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)
    unite(a-1,b-1)
    Ms.append(a-1)

if n != m:
    print(0)
    exit()
for i in range(n):
    if len(g[i]) == 0:
        print(0)
        exit()
    elif len(g[i]) == 1:
        if len(g[g[i][0]]) <= 1:
            print(0)
            exit()


s = set()
dic1 = {}
dic2 = {}

for i in range(n):
    dic1[i] = 0
    dic2[i] = 0
for i in range(n):
    s.add(find(i))
    dic1[find(i)] += 1
        

for i in Ms:
    dic2[find(i)] += 1

for i in range(n):
    if dic1[i] != dic2[i]:
        print(0)
        exit()

print(pow(2,len(list(s)),998244353))
