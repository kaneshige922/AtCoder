"""
" author : kaneshige
" created : 19.02.2022 20:56:10
"""

import sys
import itertools
from collections import deque


def main():
    dx = [2,-2,1,-1]
    dy = [1,2,-1,-2]
    
    x1,y1,x2,y2 = map(int,readline().split())
    ans = False

    for i in dx:
        for j in dy:
            if i**2 + j**2 != 5:
                continue
            if (x1+i-x2)**2 + (y1+j-y2)**2 == 5:
                ans = True
                
    if ans:
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
