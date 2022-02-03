"""
" author : kaneshige
" created : 15.01.2022 20:57:57
"""

import sys
import itertools
from collections import deque


def main():
    x  = readline().rstrip()

    ans = 0
    ans += int(x)
    ans += int(x[1:] + x[0])
    ans += int(x[2] + x[:2])

    print(ans)




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
