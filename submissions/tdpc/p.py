n,k = map(int,input().split())


dp = [[0,0] for i in  range(n+1)]
dp[0] = [1,1]
dp[1][1] = 1
mod = 1000000007

for i in range(2,n+1):
    dp[i][0] = dp[i-1][0]+dp[i-1][1]
    dp[i][1] = dp[i-1][0]+dp[i-1][1]
    if i >= k:
        dp[i][1] -= dp[i-k][0]
    dp[i][0] %= mod
    dp[i][1] %= mod

print(dp[n][1])
#print(dp)
