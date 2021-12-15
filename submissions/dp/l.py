import sys
sys.setrecursionlimit(10000000)

n = int(input())
a = list(map(int,input().split()))

dp = [[0 for i in range(n)] for j in range(n)]
flag = [[0 for i in range(n)] for j in range(n)]

"""""
def saiki(i,j):
    if flag[i][j]:
        return dp[i][j]
    flag[i][j] = 1
    if i==j:
        dp[i][j] = a[i]
    else:
        dp[i][j] = max(a[i]-saiki(i+1,j),a[j]-saiki(i,j-1))
    return dp[i][j]

print(saiki(0,n-1))
"""
for i in range(n):
    for j in range(n-i):
        if i == 0:
            dp[j][j] = a[j]
        else:
            dp[j][j+i] = max(a[j]-dp[j+1][j+i],a[j+i]-dp[j][j+i-1])

print(dp[0][n-1])
