n = int(input())
a = [list(map(int,input().split())) for i in range(n)]

dp = [0 for i in range(2**n)]
dp[0] = 1

for j in range(2**n-1):
    k = bin(j).count("1")
    for i in range(n):
        if a[k][i] == 1 and not(j >> i&1):
            dp[j+2**i] += dp[j]
            dp[j+2**i] %= 1000000007
print(dp[2**n-1]) 



