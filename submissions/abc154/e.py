n = input()
kk = int(input())

if len(n) < kk:
    print(0)
    exit()

dp = [[[0,0]for j in range(len(n)-kk+1)] for i in range(len(n)+1)]
dp[0][0][0] = 1

for i in range(1,len(n)+1):
    for j in range(10):
        for k in range(len(n)-kk+1):
            if j == 0:
                if k != len(n)-kk:
                    if int(n[i-1]) == 0:
                        dp[i][k+1][0] += dp[i-1][k][0]
                        dp[i][k+1][1] += dp[i-1][k][1]
                    else:
                        dp[i][k+1][1] += dp[i-1][k][0] + dp[i-1][k][1]
            else:
                if int(n[i-1]) > j:
                    dp[i][k][1] += dp[i-1][k][0] + dp[i-1][k][1]
                elif int(n[i-1]) == j:
                    dp[i][k][0] += dp[i-1][k][0]
                    dp[i][k][1] += dp[i-1][k][1]
                else:
                    dp[i][k][1] += dp[i-1][k][1]

#print(dp)
print(sum(dp[len(n)][len(n)-kk]))

            


