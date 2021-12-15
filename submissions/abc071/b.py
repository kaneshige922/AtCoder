n = int(input())
s = [input() for i in range(2)]

dp = [[float("inf") for i in range(n)] for j in range(2)]
if n == 1:
    print(3)
    exit()

if s[0][0] == s[0][1]:
    dp[0][0] = 6
    dp[0][1] = 6
    dp[1][0] = 6
    dp[1][1] = 6
else:
    dp[0][0] = 3
    dp[1][0] = 3



mod = 1000000007 
for i in range(1,n):
    if s[0][i] == s[1][i]:
        if s[0][i-1] != s[1][i-1]:
            dp[0][i] = dp[0][i-1]
            dp[1][i] = dp[0][i]
        else:
            dp[0][i] = 2*dp[0][i-1]
            dp[1][i] = dp[0][i]
    else:
        if s[0][i] == s[0][i-1]:
            dp[0][i] = dp[0][i-1]
            dp[1][i] = dp[0][i]
        else:
            if s[0][i-1] != s[1][i-1]:
                dp[0][i] = 3*dp[0][i-1]
                dp[1][i] = dp[0][i]
            else:
                dp[0][i] = 2*dp[0][i-1]
                dp[1][i] = dp[0][i]


print(dp[1][n-1]%mod)


