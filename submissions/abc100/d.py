"""
" author : kaneshige
" created : 03.03.2022 01:06:18
"""

import sys
import itertools
from collections import deque


def main():
    n,m = map(int,readline().split())
    xyz = [list(map(int,readline().split())) for _ in range(n)]

    ans = -INF
    cost = [-1,1]
    for i in cost:
        for j in cost:
            for k in cost:
                L = []
                for x,y,z in xyz:
                    L.append(i*x+j*y+k*z)
                L.sort(reverse=True)
                a = sum(L[:m])
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
