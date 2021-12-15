n,w = map(int,input().split())
v = [list(map(int,input().split())) for i in range(n)]
v.sort(key = lambda x:x[1])



dp = [[float("inf")]*(10**5+1) for i in range(n)]
dp[0][v[0][1]] = v[0][0]

for i in range(1,n):
    dp[i][v[i][1]] = min(dp[i-1][v[i][1]],v[i][0])
    for j in range(10**5+1):
        if dp[i-1][j] <= w:
            dp[i][j] = min(dp[i-1][j],dp[i][j])
            if dp[i-1][j] + v[i][0] <= w:
                dp[i][j+v[i][1]] = min(dp[i][j+v[i][1]],dp[i-1][j]+v[i][0])

ans = 0
for i in range(10**5+1):
    if dp[n-1][i] <= w:
        ans = i

print(ans)
