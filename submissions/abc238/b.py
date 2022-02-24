"""
" author : kaneshige
" created : 05.02.2022 20:58:50
"""

import sys
import itertools
from collections import deque
from heapq import heappop,heappush


def main():
    n = int(readline())
    a = list(map(int,readline().split()))
    hq = []
    heappush(hq,0)
    h = 0
    for i in a:
        h += i
        h %= 360
        heappush(hq, h)

    heappush(hq,360)
    t = heappop(hq)

    ans = -1
    while len(hq) != 0:
        ne = heappop(hq)
        ans = max(ne-t,ans)
        t = ne

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
