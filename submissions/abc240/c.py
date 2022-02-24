"""
" author : kaneshige
" created : 20.02.2022 20:55:44
"""

import sys
import itertools
from collections import deque


def main():
    n,x = map(int,readline().split())
    dp = [[0]*(x+1) for i in range(n+1)]
    dp[0][0] = 1

    for i in range(1,n+1):
        a,b = map(int,readline().split())
        for j in range(x+1):
            if dp[i-1][j] == 1:
                if j+a <= x:
                    dp[i][j+a] = 1
                if j+b <= x:
                    dp[i][j+b] = 1

    if dp[n][x]:
        print("Yes")
    else:
        print("No")


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
    main()
