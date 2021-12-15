
n = int(input())

dp = [i for i in range(n+1)]


num = 6

while(num <= n):
    for i in range(n+1):
        if i+num <= n:
            dp[i+num] = min(dp[i]+1,dp[i+num])
    num *= 6

num = 9
while(num <= n):
    for i in range(n+1):
        if i+num <= n:
            dp[i+num] = min(dp[i]+1,dp[i+num])
    num *= 9

print(dp[n])
