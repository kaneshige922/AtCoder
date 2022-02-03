"""
" author : kaneshige
" created : 30.01.2022 20:57:01
"""

import sys
import itertools
from collections import deque


def main():
    n = int(readline())
    if -pow(2,31) <= n < pow(2,31):
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
