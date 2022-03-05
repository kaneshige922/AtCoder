"""
" author : kaneshige
" created : 25.02.2022 21:18:13
"""

import sys
import itertools
from collections import deque


def main():
    x = int(readline())

    cnt = 0
    b = 100
    while b < x:
        b += b//100
        cnt += 1

    print(cnt)

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
