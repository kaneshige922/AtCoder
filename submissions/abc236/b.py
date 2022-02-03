"""
" author : kaneshige
" created : 23.01.2022 20:56:42
"""

import sys
import itertools
from collections import deque


def main():
    n = int(readline())
    a = list(map(int,readline().split()))

    l = [0]*(n+1)

    for i in a:
        l[i] += 1

    for i in range(1,n+1):
        if l[i] != 4:
            print(i)
            exit()

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
