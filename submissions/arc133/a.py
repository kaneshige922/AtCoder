"""
" author : kaneshige
" created : 22.01.2022 20:43:25
"""

import sys
import itertools
from collections import deque


def main():
    n = int(readline())
    a = list(map(int,readline().split()))

    e = a[-1]

    for i in range(n-1):
        if a[i] > a[i+1]:
            e = a[i]
            break

    ans = []
    for i in a:
        if i != e:
            ans.append(i)

    print(*ans)



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
