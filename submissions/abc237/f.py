"""
" author : kaneshige
" created : 30.01.2022 21:40:04
"""

import sys
import itertools
from collections import deque


def main():
    n, m = map(int, readline().split())
    dp = [[[[0 for _ in range(m+1)]for _ in range(m+1)]for _ in range(m+1)] for _ in range(n + 1)]

    for i in range(m):
        dp[1][i][m][m] = 1
    #print(dp[0])

    for i in range(2, n + 1):
        for a in range(m+1):
            for b in range(m+1):
                for c in range(m+1):
                    for t in range(m):
                        ta = a
                        tb = b
                        tc = c
                        if c < t:
                            continue
                        elif b < t:
                            tc = t
                        elif a < t:
                            tb = t
                        else:
                            ta = t
                        dp[i][ta][tb][tc] += dp[i-1][a][b][c]
                        dp[i][ta][tb][tc] %= MOD

    ans = 0
    for a in range(m+1):
        for b in range(m+1):
            for c in range(m):
                ans += dp[n][a][b][c]
                ans %= MOD


    print(ans)


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
