n = int(input())
a = list(map(int,input().split()))

ans = 0

dp = [[[0,float("inf")] for i in range(n)] for j in range(n)]

for i in range(0,n):
    for j in range(n-i):
        if i == 0:
            dp[j][j+i][0] = a[j]
            dp[j][j+i][1] = 0
        elif i == 1:
            dp[j][j+i][0] = a[j]+a[j+i]
            dp[j][j+i][1] = a[j]+a[j+i]
        else:
            #dp[j][j+i][0] = min(a[j]+dp[j+1][j+i][0],a[j+i]+dp[j][j+i-1][0])
            #dp[j][j+i][1] = min(a[j]+dp[j+1][j+i][0]+dp[j+1][j+i][1],a[j+i]+dp[j][j+i-1][0]+dp[j][j+i-1][1])
            """""
            if a[j]+dp[j+1][j+i][0]+dp[j+1][j+i][1] >= a[j+i]+dp[j][j+i-1][0]+dp[j][j+i-1][1]:
                dp[j][j+i][0] = a[j+i]+dp[j][j+i-1][0]
                dp[j][j+i][1] = a[j+i]+dp[j][j+i-1][0]+dp[j][j+i-1][1]
            else:
                dp[j][j+i][0] = a[j]+dp[j+1][j+i][0]
                dp[j][j+i][1] = a[j]+dp[j+1][j+i][0]+dp[j+1][j+i][1]
            """
            dp[j][j+i][0] = a[j]+dp[j+1][j+i][0]
            for k in range(j,j+i):
                dp[j][j+i][1]  = min(dp[j][j+i][1],dp[j][k][0]+dp[j][k][1]+dp[k+1][j+i][0]+dp[k+1][j+i][1])







#print(dp)
print(dp[0][n-1][1])


