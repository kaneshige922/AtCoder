"""
" author : kaneshige
" created : 30.01.2022 20:57:05
"""

import sys
import itertools
from collections import deque


def main():
    n = int(readline())
    s = readline().rstrip()
    s = reversed(s)

    ans = deque()
    ans.append(n)
    n -= 1

    for i in s:
        if i == "R":
            ans.appendleft(n)
        else:
            ans.append(n)
        n -= 1

    print(*list(ans))



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
