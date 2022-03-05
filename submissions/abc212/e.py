"""
" author : kaneshige
" created : 26.02.2022 18:57:09
"""

import sys
import itertools
from collections import deque


def main():
    n,m,k = map(int,readline().split())
    g = [set() for _ in range(n)]
    e = []
    for i in range(m):
        u,v = map(int,readline().split())
        g[u-1].add(v)
        g[v-1].add(u)
        e.append([u-1,v-1])

    dp = [[0]*n for _ in range(k+1)]
    dp[0][0] = 1
    for i in range(1,k+1):
        pl = sum(dp[i-1])
        for j in range(n):
            dp[i][j] += pl-dp[i-1][j]
            dp[i][j] %= MOD
        for l,r in e:
            dp[i][r] -= dp[i-1][l]
            dp[i][r] %= MOD
            dp[i][l] -= dp[i-1][r]
            dp[i][l] %= MOD

    print(dp[k][0])

if __name__ == "__main__":
    "----------Constants------------"
    INF = (1 << 62) - 1
    # MOD = 10 ** 9 + 7
    MOD = 998244353
    # sys.setrecursionlimit(10**6)
    true_ceil = lambda x, y: (x + y - 1) // y
    "----------Input------------"
    readline = sys.stdin.readline
    "----------Run------------"
    main()
