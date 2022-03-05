"""
" author : kaneshige
" created : 05.03.2022 20:48:56
"""

import sys
import itertools
from collections import deque


def main():
    a,b,c,x = map(int,readline().split())

    if x <= a:
        print(1)
    elif b < x:
        print(0)
    else:
        print(c/(b-a))





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
