n,l = map(int,input().split())

dp = [0 for i in range(n+1)]
dp[0] = 1
mod = 1000000007

for i in range(1,n+1):
    dp[i] = (dp[i]+dp[i-1])%mod
    if(i-l>=0):
        dp[i] = (dp[i]+dp[i-l])%mod

print(dp[n])
