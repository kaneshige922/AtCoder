"""
" author : kaneshige
" created : 05.03.2022 20:49:15
"""

import sys
import itertools
from collections import deque


def main():
    t = int(readline())
    for i in range(t):
        n = int(readline())
        s = list(readline().rstrip())
        sb = s[:(n//2)]
        sb2 = reversed(sb)
        dp = [[1,0] for _ in range(n//2+1)]
        for j in range(1,n//2+1):
            dp[j][0] = dp[j-1][0]
            dp[j][1] = dp[j-1][1]*26+dp[j-1][0]*(ord(s[j-1])-ord("A"))
            dp[j][0] %= MOD
            dp[j][1] %= MOD
        ans = 0
        if n % 2 == 0:
            ans += dp[n // 2][1]
            st = "".join(sb)+"".join(sb2)
            if st <= "".join(s):
                ans += 1
        else:
            #print(ord(s[n//2]),ord("A"),ans)
            ans += dp[n//2][1]*26
            ans %= MOD
            ans += (ord(s[n//2])-ord("A"))
            st = "".join(sb)+s[n//2]+"".join(sb2)
            if st <= "".join(s):
                ans += 1
        #print(dp)
        print(ans%MOD)

if __name__ == "__main__":
    "----------Constants------------"
    INF = (1 << 62) - 1
    #MOD = 10 ** 9 + 7
    MOD = 998244353
    # sys.setrecursionlimit(10**6)
    true_ceil = lambda x, y: (x + y - 1) // y
    "----------Input------------"
    readline = sys.stdin.readline
    "----------Run------------"
    main()
