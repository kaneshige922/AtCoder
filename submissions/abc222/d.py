
import sys
sys.setrecursionlimit(10**6)

mod = 10 ** 9 + 7
mod2 = 998244353

n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
mb = max(b)+1
dp = [[0]*mb for i in  range(n)]
dp2 = [[0]*mb for i in range(n)]

import itertools 
def ruisekiwa(a):
    return list(itertools.accumulate(a))


for i in range(n):
    if i == 0:
        for j in range(mb):
            if a[i] <= j <= b[i]:
                dp[i][j] = 1
        dp[i] = ruisekiwa(dp[i])
    else:
        for j in range(mb):
            if a[i] <= j <= b[i]:
                if j == 0:
                    dp[i][0] = dp[i-1][0]
                else:
                    dp[i][j] = (dp[i][j-1] + dp[i-1][j])%mod2
            else:
                if j != 0:
                    dp[i][j] = dp[i][j-1]



print(dp[n-1][-1]%mod2)
        
        


