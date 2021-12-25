"""
" author : kaneshige
" created : 25.12.2021 20:44:35
"""

import sys
import itertools
from collections import deque


def main():
    x,y = map(int,readline().split())

    if x >= y:
        print(0)
    else:
        print((y-x)//10 + ((y-x)%10 != 0))

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
