"""
" author : kaneshige
" created : 25.12.2021 20:44:47
"""

import sys
import itertools
from collections import deque


def main():
    l,r = map(int,readline().split())
    s = list(readline().rstrip())
    l -= 1
    r -= 1

    while r > l:
        s[r],s[l] = s[l],s[r]
        l += 1
        r -= 1

    print("".join(s))


if __name__ == "__main__":
    "----------Constants------------"
    INF = (1 << 62) - 1
    MOD = 10 ** 9 + 7
    # MOD = 998244353
    # sys.setrecursionlimit(10**6)
    "----------Input------------"
    readline = sys.stdin.readline
    "----------Run------------"
    main()
