h,w = map(int,input().split())

a = [input() for i in range(h)]
mod = 1000000007

dp = [[0 for i in range(w+1)] for j in range(h+1)]
dp[1][1] = 1
for i in range(1,h+1):
    for j in range(1,w+1):
        if a[i-1][j-1] == ".":
            dp[i][j] += dp[i-1][j] + dp[i][j-1]

print(dp[h][w]%mod)
