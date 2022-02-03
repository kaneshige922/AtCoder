"""
" author : kaneshige
" created : 15.01.2022 20:58:13
"""

import sys
import itertools
from collections import deque


def main():
    a,n = map(int,readline().split())

    dp = {1: 0}

    qu = deque()
    v = set()
    qu.append(1)
    v.add(1)

    while qu:
        h = qu.popleft()

        if h >= 10 and h % 10 != 0:
            s = str(h)
            s = int(s[-1]+s[:-1])
            if s not in v:
                dp[s] = dp[h] + 1
                qu.append(s)
                v.add(s)
        if h*a not in v and len(str(h*a)) <= len(str(n)):
            qu.append(h*a)
            v.add(h*a)
            dp[h*a] = dp[h] + 1

    if n not in dp:
        print(-1)
    else:
        print(dp[n])










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
