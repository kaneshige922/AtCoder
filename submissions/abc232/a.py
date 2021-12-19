"""
" author : kaneshige
" created : 19.12.2021 20:49:37
"""

import sys
import itertools
from collections import deque


def main():
    s = readline().rstrip()
    print(int(s[0])*int(s[2]))

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
