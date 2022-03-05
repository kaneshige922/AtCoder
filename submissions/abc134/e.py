"""
" author : kaneshige
" created : 04.03.2022 20:02:16
"""

import sys
import itertools
from collections import deque
from heapq import heappop,heappush
from bisect import bisect_left

def main():
    n = int(readline())
    a = [int(readline()) for _ in range(n)]
    col = deque()
    cnt = 0

    for i in range(n):
        if i == 0:
            col.append(a[i])
            cnt += 1
        else:
            if a[i] <= col[0]:
                col.appendleft(a[i])
                cnt += 1
            else:
                l = 0
                r = len(col)
                m = (l+r)//2
                while r-l > 1:
                    if col[m] < a[i]:
                        l = m
                    else:
                        r = m
                    m = (l+r)//2
                col[m] = a[i]

    print(cnt)


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
