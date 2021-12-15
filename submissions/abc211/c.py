#DP‚Å‰ð‚­
S = input()
T = len(S)
SS = "chokudai"
N = len(SS)
mod = 10**9 +7
dp = [[0]*T for i in range(N)]
for i in range(N):
    for j in range(i,T):
        if i == 0:
            if j == 0: 
                if SS[i] == S[j]:
                    dp[i][j] += 1
            elif  SS[i] == S[j]:
                dp[i][j] = dp[i][j-1] + 1
            else:
                dp[i][j] = dp[i][j-1]
        else:
            if  SS[i] == S[j]:
                dp[i][j] = (dp[i][j-1] + dp[i-1][j-1]) % mod
            else:
                dp[i][j] = dp[i][j-1]
print(dp[7][T-1])
