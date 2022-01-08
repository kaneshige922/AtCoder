"""
" author : kaneshige
" created : 30.12.2021 01:35:52
"""

import sys
import itertools
from collections import deque


def main():
    n = int(readline())
    xl = [list(map(int,readline().split())) for _ in range(n)]
    wid = [[a[0]-a[1],a[0]+a[1]] for a in xl]

    wid.sort(key=lambda x:x[1])

    R = -INF
    ans = 0
    for a in wid:
        if a[0] >= R:
            ans += 1
            R = a[1]

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
    main()
