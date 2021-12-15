n,k = map(int,input().split())
h = list(map(int,input().split()))

dp = [0 for i in range(n)]

for i in range(1,n):
    dp[i] = 10**9
    for j in range(1,k+1):
        if i - j < 0:
            break
        dp[i] = min(dp[i],dp[i-j]+abs(h[i]-h[i-j]))

print(dp[n-1])
