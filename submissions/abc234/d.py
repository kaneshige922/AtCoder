"""
" author : kaneshige
" created : 08.01.2022 20:52:07
"""

import sys
import itertools
from collections import deque
from heapq import heappop,heappush


def main():
    n,k = map(int,readline().split())
    p = list(map(int,readline().split()))

    qu = []

    ans = []

    for i in range(n):
        if i < k:
            heappush(qu,p[i])
            if i == k-1:
                a = heappop(qu)
                ans.append(a)
                heappush(qu,a)
        else:
            heappush(qu, p[i])
            heappop(qu)
            a = heappop(qu)
            ans.append(a)
            heappush(qu, a)

    for i in ans:
        print(i)

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
