"""
" author : kaneshige
" created : 22.12.2021 00:17:41
"""

import sys
import itertools
from collections import deque


def main():
    n,k = map(int,readline().split())
    LR = [list(map(int,readline().split())) for _ in range(k)]

    dp1 = [0]*n 
    dp2 = [0]*n #Ç¢Ç‡Ç∑ñ@ÇÃä«óù
    dp1[0] = 1
    
    for i in range(0,n):
        if i != 0:
            dp2[i] += dp2[i-1]
            dp1[i] += dp2[i]
            dp1[i] %= MOD
            
        for l,r in LR:
            if i + l <= n-1:
                dp2[i+l] += dp1[i]
                dp2[i+l] %= MOD
            if i + r + 1 <= n-1:
                dp2[i+r+1] -= dp1[i]
                dp2[i+r-1] %= MOD

    print(dp1[n-1]%MOD)


if __name__ == "__main__":
    "----------Constants------------"
    INF = (1 << 62) - 1
    #MOD = 10 ** 9 + 7
    MOD = 998244353
    # sys.setrecursionlimit(10**6)
    "----------Input------------"
    readline = sys.stdin.readline
    "----------Run------------"
    main()
