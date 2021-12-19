"""
" author : kaneshige
" created : 19.12.2021 20:49:34
"""

import sys
import itertools
from collections import deque


def main():
    h,w,k = map(int,readline().split())
    x1,y1,x2,y2 = map(int,readline().split())

    dp = [[0,0,0,0] for _ in range(k+1)]

    if x1 == x2:
        if y1 == y2:
            dp[0][0] = 1
        else:
            dp[0][1] = 1
    else:
        if y1 == y2:
            dp[0][2] = 1
        else:
            dp[0][3] = 1


    for i in range(1,k+1):
        dp[i][0] = (dp[i-1][1] + dp[i-1][2])%MOD
        dp[i][1] = ((w-1)*dp[i-1][0] + (w-2)*dp[i-1][1] + dp[i-1][3]) %MOD
        dp[i][2] = ((h-1)*dp[i-1][0] + (h-2)*dp[i-1][2] + dp[i-1][3])%MOD
        dp[i][3] = ((h-1)*dp[i-1][1] + (w-1)*dp[i-1][2] + (h+w-4)*dp[i-1][3])%MOD

    #rint(dp)
    print(dp[k][0]%MOD)


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
