s = list(input())
s.reverse()
slen = len(s)
MOD = 1000000007


dp = [[0]*13 for i in range(slen+1)]
if s[0] == "?":
    for j in range(10):
        dp[1][j] = 1
else:
    dp[1][int(s[0])] = 1




for i in range(2,slen+1):
    if s[i-1] == "?":
        for j in range(10):
            mod = j*(pow(10,i-1,13))%13
            for k in range(13):
                mod2 = (k+mod)%13
                dp[i][mod2] += dp[i-1][k]
                dp[i][mod2] %= MOD
    else:
        mod = int(s[i-1])*(pow(10,i-1,13))%13
        for k in range(13):
            mod2 = (k+mod)%13
            dp[i][mod2] += dp[i-1][k]
            dp[i][mod2] %= MOD

print(dp[slen][5])


