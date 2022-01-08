"""
" author : kaneshige
" created : 08.01.2022 20:52:02
"""

import sys
import itertools
from collections import deque


def main():
    k = int(readline())
    ans = ""

    cnt = 2

    while k != 0:
        if k % cnt //(cnt//2) == 1:
            ans += "2"
            k -= cnt//2
        else:
            ans += "0"

        cnt *= 2

    ans = list(reversed(ans))

    print("".join(ans))


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
