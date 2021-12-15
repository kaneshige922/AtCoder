from pprint import pprint


s = input()
t = input()

dp = [[0 for j in range(len(s)+1)] for i in range(len(t)+1)]


for i in range(len(t)):
    for j in range(len(s)):
        if t[i] == s[j]:
            dp[i+1][j+1]= dp[i][j] + 1
        else:
            dp[i+1][j+1] = max(dp[i][j+1],dp[i+1][j])
 
#•œŒ³
ans = ""
i = len(t)
j = len(s)
while i > 0 and j >0:
    if dp[i][j] == dp[i][j-1]:
        j -= 1
    elif dp[i][j] == dp[i-1][j]:
        i -= 1
    else:
        ans = t[i-1] + ans
        i -= 1
        j -= 1


print(ans)




