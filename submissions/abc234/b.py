"""
" author : kaneshige
" created : 08.01.2022 20:51:57
"""

import sys
import itertools
from collections import deque


def main():
    n = int(readline())
    xy = [list(map(int,readline().split())) for _ in range(n)]

    ans = 0
    for i in range(n-1):
        for j in range(i+1,n):
            ans = max(ans,((xy[i][0]-xy[j][0])**2+(xy[i][1]-xy[j][1])**2)**0.5)


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
