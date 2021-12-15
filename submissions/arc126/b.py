from bisect import bisect_left


n,m = map(int,input().split())
ab = [list(map(int,input().split())) for i in range(m)]

ab.sort(key=lambda x:(x[0],-x[1]))

ans = 1
dp = [float("inf") for i in range(m+1)]

for i in range(m):
    p = bisect_left(dp,ab[i][1])
    dp[p] = ab[i][1]

print(bisect_left(dp,float("inf")))
