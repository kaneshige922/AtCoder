import sys
sys.setrecursionlimit(100000)

n,m = map(int,input().split())

g = [[] for i in range(n)]

for i in range(m):
    a,b = map(int,input().split())
    g[a-1].append(b-1)

dp = [-1 for i in range(n)]

def saiki(x):
    if dp[x] != -1:
        return dp[x]
    else:
        if len(g[x]) == 0:
            dp[x] = 0
        else:
            c = -1
            for i in g[x]:
                c = max(saiki(i)+1,c)
            dp[x] = c
        return dp[x]

ans = -1
for i in range(n):
    ans = max(ans,saiki(i))


print(ans)
