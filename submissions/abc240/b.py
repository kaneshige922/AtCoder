"""
" author : kaneshige
" created : 20.02.2022 20:55:39
"""

import sys
import itertools
from collections import deque


def main():
    n = int(readline())
    a = list(set(list(map(int,readline().split()))))
    print(len(a))

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
