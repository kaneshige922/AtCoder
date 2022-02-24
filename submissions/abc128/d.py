"""
" author : kaneshige
" created : 05.02.2022 18:01:38
"""

import sys
import itertools
from collections import deque
from heapq import heappop,heappush


def main():
    n,k = map(int,readline().split())
    v = list(map(int,readline().split()))

    ans = 0

    for i in range(min(k+1,n+1)):
        for j in range(min(k+1,n+1)-i):
            t = k - i - j
            hq = []
            a = 0
            for l in range(i):
                if v[l] < 0:
                    heappush(hq,v[l])
                a += v[l]
            for r in range(j):
                if v[-(r+1)] < 0:
                    heappush(hq,v[-(r+1)])
                a += v[-(r+1)]
            while t != 0 and len(hq) != 0:
                a -= heappop(hq)
                t -= 1
            ans = max(ans,a)

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
