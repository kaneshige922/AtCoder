"""
" author : kaneshige
" created : 19.02.2022 20:56:05
"""

import sys
import itertools
from collections import deque


def main():
    x = int(readline())

    if x >= 10:
        print(str(x)[:-1])
    elif 0<= x < 10:
        print(0)
    elif -10 < x < 0:
        print(-1)
    else:
        if str(x)[-1] == "0":
            print(str(x)[:-1])
        else:
            print(int(str(x)[:-1])-1)

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
