"""
" author : kaneshige
" created : 30.12.2021 01:52:51
"""

import sys
import itertools
from collections import deque


def main():
    h, w = map(int, readline().split())
    "######"
    "------"
    "######"
    "------"
    "######"

    ans = INF

    if h != 2:
        if h % 3 == 0:
            ans = 0
        else:
            ans = w

    if w != 2:
        if w % 3 == 0:
            ans = 0
        else:
            ans = min(ans, h)

    "###|##"
    "###|##"
    "---|##"
    "###|##"
    "###|##"

    for i in range(1, w):
        c = h * (w - i)
        a = i * (h // 2)
        b = i * true_ceil(h, 2)
        ans = min(ans, max(a, b, c) - min(a, b, c))

    for i in range(1, h):
        c = w * (h - i)
        a = i * (w // 2)
        b = i * true_ceil(w, 2)
        ans = min(ans, max(a, b, c) - min(a, b, c))

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
