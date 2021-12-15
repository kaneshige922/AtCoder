n = int(input())
p = list(map(float,input().split()))
half = n//2 +1

dp = [[0 for i in range(half+1)] for j in range(n+1)]
dp[0][0] = 1

for i in range(1,n+1):
    for j in range(half+1):
        if j != half:
            dp[i][j] += dp[i-1][j]*(1-p[i-1])
        else:
            dp[i][j] += dp[i-1][j]
        if j != 0:
            dp[i][j] += dp[i-1][j-1]*p[i-1]

print(dp[n][half])
