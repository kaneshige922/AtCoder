"""
" author : kaneshige
" created : 05.03.2022 20:49:00
"""

import sys
import itertools
from collections import deque


def main():
    s = list(readline().rstrip())
    s = [ord(i) for i in s]
    s.sort()
    s = [chr(i) for i in s]
    print("".join(s))

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
