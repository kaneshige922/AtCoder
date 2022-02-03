"""
" author : kaneshige
" created : 23.01.2022 20:56:47
"""

import sys
import itertools
from collections import deque


def main():
    n,m = map(int,readline().split())
    s = list(readline().split())
    t = list(readline().split())

    d = {}
    for i in s:
        d[i] = 0
    for i in t:
        d[i] = 1

    for i in s:
        if d[i]:
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
