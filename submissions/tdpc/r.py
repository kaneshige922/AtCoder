d = int(input())
n = int(input())
ns = list(str(n))
ns = [int(i) for i in ns]
nlen = len(str(n))

dp = [[[0,0] for i in range(d)] for j in range(nlen+1)]

for i in range(10):
    if int(ns[0]) > i:
        dp[1][i%d][0] += 1
    elif int(ns[0]) == i:
        dp[1][i%d][1] += 1

for i in range(2,nlen+1):
    for j in range(10):
        for k in range(d):
            to = (j+k)%d
            if ns[i-1] > j:
                dp[i][to][0] += dp[i-1][k][0]+dp[i-1][k][1]
            elif ns[i-1] == j:
                dp[i][to][0] += dp[i-1][k][0]
                dp[i][to][1] += dp[i-1][k][1]
            else:
                dp[i][to][0] += dp[i-1][k][0]
            dp[i][to][0] %= 1000000007
            dp[i][to][1] %= 1000000007

print((dp[nlen][0][0]+dp[nlen][0][1]-1)%1000000007)

