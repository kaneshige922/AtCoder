"""
" author : kaneshige
" created : 26.02.2022 20:57:48
"""

import sys
import itertools
from collections import deque


def main():
    a = list(map(int,readline().split()))
    h = 0
    h = a[h]
    h = a[h]
    h = a[h]

    print(h)

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
