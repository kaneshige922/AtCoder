
n = int(input())
abc = [list(map(int,input().split())) for i in range(n)]

dp = [[0]*3 for i in range(n)]

dp[0] = abc[0]

for i in range(1,n):
    for j in range(3):
        if j == 0:
            dp[i][0] = abc[i][0] + max(dp[i-1][1],dp[i-1][2])
        elif j == 1:
            dp[i][1] = abc[i][1] + max(dp[i-1][0],dp[i-1][2])
        else:
            dp[i][2] = abc[i][2] + max(dp[i-1][0],dp[i-1][1])

print(max(dp[n-1]))
