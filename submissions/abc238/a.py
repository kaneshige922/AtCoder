"""
" author : kaneshige
" created : 05.02.2022 20:59:11
"""

import sys
import itertools
from collections import deque
import math


def main():
    n = int(readline())
    if n > 2*math.log2(n):
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
