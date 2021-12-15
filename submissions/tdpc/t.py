K = int(input())
r = [0 for i in range(2**K)]
for i in range(2**K):
    r[i] = int(input())

dp = [[0 for i in range(K+1)] for j in range(2**K)]

for i in range(2**K):
    dp[i][0] = 1

for i in range(1,K+1):
    for j in range(2**K):
        dp[j][i] = 0
        half = (j//(2**i)+1)*(2**i)-2**(i-1)
        if half > j:
            for k in range(half,half+2**(i-1)):
                dp[j][i] += dp[k][i-1]/(1+10**((r[k]-r[j])/400))
        else:
            for k in range(half-2**(i-1),half):
                dp[j][i] += dp[k][i-1]/(1+10**((r[k]-r[j])/400))
        dp[j][i] *= dp[j][i-1]

for i in range(2**K):
    print('{:.10f}'.format(dp[i][K]))
            
