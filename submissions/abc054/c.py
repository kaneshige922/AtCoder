from itertools import permutations

n,m = map(int,input().split())

g = [set() for i in range(n)]
for i in range(m):
    a,b = map(int,input().split())
    g[a-1].add(b-1)
    g[b-1].add(a-1)

num = [i for i in range(1,n)]

p = permutations(num)

ans = 0

for i in p:
    t = True
    for j in range(n-1):
        if j == 0:
            if i[j] not in g[0]:
                t = False
        else:
            if i[j] not in g[i[j-1]]:
                t = False
    if t:
        ans += 1

print(ans)

