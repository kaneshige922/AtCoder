n,m,x = map(int,input().split())
c = []
for i in range(n):
    c.append(list(map(int,input().split())))

ans = False
mincost = 12*10**6

for i in range(2**n):
    bin(i)
    xlis = [0]*m
    cost = 0
    for j in range(n):
        if (i >> j) & 1:
            xlis = [xlis[k]+c[j][k+1] for k in range(m)]
            cost += c[j][0]
    if min(xlis) >= x and mincost > cost:
        ans = True
        mincost = cost

if ans:
    print(mincost)
else:
    print(-1)
