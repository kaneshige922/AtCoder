n = int(input())
t = list(map(int,input().split()))
su = sum(t)

dp = [[0 for i in range(10**5+1)] for j in range(n+1)]

dp[0][0] = 1

for i in range(n):
    for j in range(10**5+1):
        if dp[i][j] == 1:
            dp[i+1][j] = 1
            dp[i+1][j+t[i]] = 1

ans = 1000000
for i in range(10**5+1):
    if dp[n][i] == 1:
        if abs(2*ans-su) >= abs(2*i-su):
            ans = i

print(ans)
