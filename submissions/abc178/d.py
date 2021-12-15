s = int(input())


keta = 1
dp = [[0]*(s+1) for i in range(s//3)]

for i in range(3,s+1):
    dp[0][i] = 1


for i in range(1,s//3):
    for j in range(3,s+1):
        dp[i][j] = dp[i][j-1]+dp[i-1][j-3]

ans = 0
mod = 10**9+7
for i in range(s//3):
    ans += dp[i][s]

print(ans % mod) 
