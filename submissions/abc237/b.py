"""
" author : kaneshige
" created : 30.01.2022 20:57:05
"""

import sys
import itertools
from collections import deque


def main():
    h,w = map(int,readline().split())
    a = [list(map(int,readline().split())) for _ in range(h)]
    b = [[0]*h for _ in range(w)]

    for i in range(w):
        for j in range(h):
            b[i][j] = a[j][i]

    for i in b:
        print(*i)



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
