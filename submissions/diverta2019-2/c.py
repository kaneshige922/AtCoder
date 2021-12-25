"""
" author : kaneshige
" created : 25.12.2021 02:13:38
"""

import sys
import itertools
from collections import deque
from heapq import heappop,heappush


def main():
    n = int(readline())
    a = list(map(int,readline().split()))
    a.sort()
    qu = []
    heap = [a[0],a[n-1]]
    for i in range(1,n-1):
        if a[i] < 0:
            qu.append([heap[-1],a[i]])
            heap[-1] -= a[i]
        else:
            qu.append([heap[0],a[i]])
            heap[0] -= a[i]

    qu.append([heap[-1],heap[0]])
    heap[-1] -= heap[0]

    print(heap[-1])
    for i in qu:
        print(*i)


if __name__ == "__main__":
    "----------Constants------------"
    INF = (1 << 62) - 1
    MOD = 10 ** 9 + 7
    # MOD = 998244353
    # sys.setrecursionlimit(10**6)
    "----------Input------------"
    readline = sys.stdin.readline
    "----------Run------------"
    main()
