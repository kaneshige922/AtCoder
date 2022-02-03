"""
" author : kaneshige
" created : 29.01.2022 20:59:03
"""

import sys
import itertools
from collections import deque


def main():
    n,l,w = map(int,readline().split())
    a = list(map(int,readline().split()))

    x = []
    r = 0
    for i in a:
        if i > r:
            x.append([r,i])
            r =  i + w
        else:
            r = i + w
    if r < l:
        x.append([r,l])
    ans = 0
    r = 0
    for c,d in x:
        ans += true_ceil(d-c,w)

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
