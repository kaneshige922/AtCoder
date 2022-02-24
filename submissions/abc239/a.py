"""
" author : kaneshige
" created : 19.02.2022 20:56:01
"""

import sys
import itertools
from collections import deque
from math import sqrt


def main():
    h = int(readline())
    print(sqrt(h*(12800000+h)))

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
