"""
" author : kaneshige
" created : 01.03.2022 23:33:04
"""

import sys
import itertools
from collections import deque

def sol(col,md):
    cnt = 0
    for x in range(n):
        for y in range(n):
            if (x + y) % 3 == md:
                cnt += d[c[x][y] - 1][col]
    return cnt


def main():
    ans = INF

    dp = [[0]*C for _ in range(3)]

    for i in range(C):
        dp[0][i] = sol(i,0)
        dp[1][i] = sol(i,1)
        dp[2][i] = sol(i,2)

    for i in range(C):
        for j in range(C):
            for k in range(C):
                if i == j or j == k or k == i:
                    continue
                ans = min(ans,dp[0][i]+dp[1][j]+dp[2][k])

    print(ans)
if __name__ == "__main__":
    "----------Constants------------"
    INF = (1 << 62) - 1
    MOD = 10 ** 9 + 7
    # MOD = 998244353
    # sys.setrecursionlimit(10**6)
    true_ceil = lambda x, y: (x + y - 1) // y
    "----------Input------------"
    readline = sys.stdin.readline
    "----------Run------------"
    n, C = map(int, readline().split())
    d = [list(map(int, readline().split())) for _ in range(C)]
    c = [list(map(int, readline().split())) for _ in range(n)]
    main()
