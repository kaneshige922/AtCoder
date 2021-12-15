n,k = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
mi = min(a)

dp = [-1 for i in range(k+1)]

for i in range(mi+1):
    dp[i] = 0

for i in range(k+1):
    for j in a:
        if i+j > k: 
            continue
        if dp[i+j] == -1:
            dp[i+j] = not(dp[i])
        elif dp[i+j] == 0:
            dp[i+j] = not(dp[i])

if dp[k]:
    print("First")
else:
    print("Second")

