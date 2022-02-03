"""
" author : kaneshige
" created : 23.01.2022 20:56:38
"""

import sys
import itertools
from collections import deque


def main():
    S = list(readline().rstrip())
    a,b = map(int,readline().split())
    S[a-1],S[b-1] = S[b-1],S[a-1]
    
    print("".join(S))
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
