import sys
sys.setrecursionlimit(1000000)


n = int(input())

path = [[] for i in range(n)]

for i in range(n-1):
    a,b = map(int,input().split())
    path[a-1].append(b-1)
    path[b-1].append(a-1)

dp = [[0,0] for i in range(n)]

v = set()
mod = 1000000007
def saiki(x):
    if dp[x] != [0,0]:
        return dp[x]
    else:
        v.add(x)
        c = [1,1]
        for i in range(len(path[x])):
            if path[x][i] not in v:
                z = saiki(path[x][i])
                c[0] *= (z[0]+z[1])%mod
                c[1] *= z[0]%mod
        dp[x] = c
        return dp[x]

print(sum(saiki(0))%mod)

