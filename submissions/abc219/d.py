
n = int(input())
x,y = map(int,input().split())

dp = [[[10000 for i in range(y+1)] for j in range(x+1)] for k in range(n+1)]
dp[0][0][0] = 0

for i in range(0,n):
    a,b = map(int,input().split())
    for j in range(x+1):
        for k in range(y+1):
            if dp[i][j][k] != 10000:
                dp[i+1][j][k] = min(dp[i][j][k],dp[i+1][j][k])
                mi = min(j+a,x)
                ma = min(k+b,y)
                dp[i+1][mi][ma] = min(dp[i][j][k]+1,dp[i+1][mi][ma])

if dp[n][x][y] != 10000:
    print(dp[n][x][y])
else:
    print(-1)
