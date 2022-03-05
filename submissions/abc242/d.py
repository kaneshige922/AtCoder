"""
" author : kaneshige
" created : 05.03.2022 20:49:10
"""

import sys
import itertools
from collections import deque


def main():
    s = readline().rstrip()
    q = int(readline())
    sl = len(s)


    def sol(t,k):
        if t == 0:
            return s[k-1]
        if t > 60:
            c = sol(60,k)
            d = {"A":0,"B":1,"C":2}
            r = ["A","B","C"]
            return r[(d[c]+t-60)%3]
        if k % 2 == 0:
            c = sol(t-1,k//2)
            if c == "A":
                return "C"
            elif c == "B":
                return "A"
            else:
                return "B"
        else:
            c = sol(t-1,true_ceil(k,2))
            if c == "A":
                return "B"
            elif c == "B":
                return "C"
            else:
                return "A"




    for i in range(q):
        t,k = map(int,readline().split())
        print(sol(t,k))




if __name__ == "__main__":
    "----------Constants------------"
    INF = (1 << 62) - 1
    MOD = 10 ** 9 + 7
    # MOD = 998244353
    sys.setrecursionlimit(10**6)
    true_ceil = lambda x, y: (x + y - 1) // y
    "----------Input------------"
    readline = sys.stdin.readline
    "----------Run------------"
    main()
