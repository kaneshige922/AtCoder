n,k = map(int,input().split())
a = list(map(int,input().split()))
mod = 1000000007

dp = [[0 for i in range(k+1)] for j in range(n+1)]
dp[0][0] = 1

for i in range(1,n+1):
    for j in range(k+1):
        dp[i][j] += dp[i-1][j]
        if j+a[i-1]+1 <= k:
            dp[i][j+a[i-1]+1] -= dp[i-1][j]
    for j in range(1,k+1):
        dp[i][j] = dp[i][j-1] + dp[i][j]
    dp[i] = [j%mod for j in dp[i]]

#for i in range(n+1):
#    print(dp[i])
print(dp[n][k]%mod)
