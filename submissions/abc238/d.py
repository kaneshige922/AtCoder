"""
" author : kaneshige
" created : 05.02.2022 20:59:00
"""

import sys
import itertools
from collections import deque


def main():
    t = int(readline())
    for i in range(t):
        a,s = map(int,readline().split())
        k = 0
        x = 0
        y = 0
        for j in range(60):
            if a >> j & 1:
                x += pow(2,j)
                y += pow(2,j)
                k = 1
            else:
                if s >> j & 1:
                    if k:
                        k = 0
                    else:
                        x += pow(2,j)
                else:
                    if k:
                        x += pow(2,j)
        #print(x,y)
        if x & y == a and x + y == s:
            print("Yes")
        else:
            print("No")




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
