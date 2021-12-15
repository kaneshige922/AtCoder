from bisect import bisect_left

n = int(input())

s = [int(input()) for i in range(n)]

dp = [float("inf") for i in range(n+1)]
dp[0] = 0

for i in s:
    p = bisect_left(dp,i)
    dp[p] = i

ans = n - (bisect_left(dp,float("inf"))-1)

print(ans,sep="\n")
