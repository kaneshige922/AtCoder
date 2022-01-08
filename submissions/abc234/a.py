"""
" author : kaneshige
" created : 08.01.2022 20:51:50
"""

import sys
import itertools
from collections import deque


def main():

    def f(x):
        return x**2+2*x+3

    t = int(readline())

    print(f(f(f(t)+t)+f(f(t))))

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
