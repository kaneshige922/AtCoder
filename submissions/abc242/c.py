"""
" author : kaneshige
" created : 05.03.2022 20:49:05
"""

import sys
import itertools
from collections import deque


def main():
    n = int(readline())

    dp = [[0]*10 for _ in range(n+1)]
    for i in range(1,10):
        dp[1][i] = 1

    for i in range(2,n+1):
        for j in range(1,10):
            dp[i][j] += dp[i-1][j]
            if j != 1:
                dp[i][j] += dp[i-1][j-1]
            if j != 9:
                dp[i][j] += dp[i-1][j+1]
            dp[i][j] %= MOD

    print(sum(dp[n])%MOD)




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
