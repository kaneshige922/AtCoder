n,m = map(int,input().split())
wv = [list(map(int,input().split())) for i in range(n)]
wv.sort()

dp = [[0]*(m+1) for i in range(n)]

dp[0][wv[0][0]] = wv[0][1]
for i in range(1,n):
    dp[i][wv[i][0]] = max(dp[i-1][wv[i][0]],wv[i][1])
    for j in range(m+1):
        if dp[i-1][j] > 0:
            dp[i][j] = max(dp[i-1][j],dp[i][j])
            if j + wv[i][0] <= m:
                dp[i][j+wv[i][0]] = max(dp[i-1][j+wv[i][0]],dp[i-1][j] + wv[i][1])


print(max(dp[n-1]))
