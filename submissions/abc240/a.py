"""
" author : kaneshige
" created : 20.02.2022 20:55:34
"""

import sys
import itertools
from collections import deque


def main():
    a,b = map(int,readline().split())
    if abs(a-b) == 1 or (a==1 and b==10) or (b==1 and a==10):
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
