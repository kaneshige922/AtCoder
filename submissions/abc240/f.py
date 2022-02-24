"""
" author : kaneshige
" created : 20.02.2022 20:56:02
"""

import sys
import itertools
from collections import deque


def main():
    t = int(readline())
    for i in range(t):
        n,m = map(int,readline().split())
        a = [0]
        h = 0
        for i in range(n):
            x,y = map(int,readline().split())
            if h > 0:
                if x >= 0:
                    a.append(a[-1]+(1+y)*y//2*x+h*y)
                    h += x*y
                elif h + x*y < 0:
                    a.append(a[-1]+((1+h//(-x))*(h//(-x)))//2*x+(h//(-x))*h)
                    a.append(a[-2]+(1+y)*y//2*x+h*y)
                    h += x*y
                else:
                    a.append(a[-1]+x+h)
                    a.append(a[-2]+(1+y)*y//2*x+h*y)
                    h += x*y
            else:
                a.append(a[-1]+x+h)
                a.append(a[-2]+(1+y)*y//2*x+h*y)
                h += x*y


            
        #print(a)
        print(max(a[1:]))



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
