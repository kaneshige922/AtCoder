"""
" author : kaneshige
" created : 22.12.2021 02:15:09
"""

import sys
import itertools
from collections import deque


def main():
    h,w,k = map(int,readline().split())
    s = [list(readline().rstrip()) for _ in range(h)]

    stb = []

    for i in range(h):
        for j in range(w):
            if s[i][j] == "#":
                stb.append([i,j])
    ans = [[0]*w for _ in range(h)]

    max_x = stb[-1][0]

    x1 = -1

    for i in range(k):
        if i == 0:
            x1 = 0
            y1 = 0
        else:
            if stb[i-1][0] == stb[i][0]:
                y1 = stb[i-1][1] + 1
            else:
                y1 = 0

        if i == k-1:
            y2 = w-1
        else:
            if stb[i][0] == stb[i+1][0]:
                y2 = stb[i][1]
            else:
                y2 = w-1

        if stb[i][0] == max_x:
            x2 = h-1
        else:
            x2 = stb[i][0]

        #print(x1,y1)
        #print(x2,y2)
        for x in range(x1,x2+1):
            for y in range(y1,y2+1):
                ans[x][y] = i+1

        if i == k-1:
            continue
        if stb[i][0] != stb[i + 1][0]:
            x1 = stb[i][0]+1

    for i in ans:
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
