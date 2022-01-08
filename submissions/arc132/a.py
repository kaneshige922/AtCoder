"""
" author : kaneshige
" created : 26.12.2021 20:54:54
"""

import sys
import itertools
from collections import deque
from heapq import heappop,heappush


def main():
    n = int(readline())
    r = list(map(int,readline().split()))
    c = list(map(int,readline().split()))


    ans = []

    q = int(readline())
    for i in range(q):
        ri,ci = map(int,readline().split())
        if n - r[ri-1] < c[ci-1]:
            ans.append("#")
        else:
            ans.append(".")

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
