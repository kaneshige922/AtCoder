"""
" author : kaneshige
" created : 13.02.2022 20:56:19
"""

import sys
import itertools
from collections import deque


def saiki(x):
    if x in d:
        return d[x]
    if x % 2 == 0:
        a = saiki(x//2)
        d[x] = [2*a[0],2*a[1]]
        return d[x]
    else:
        a = saiki(x//2)
        b = saiki(x // 2 + 1)
        d[x] = [a[0]+b[0],a[1]+b[1]]
        return d[x]


def main():
    x = int(readline())
    ans = saiki(x)
    
    fa = pow(2,ans[0],MOD)*pow(3,ans[1],MOD)%MOD
    print(fa)




if __name__ == "__main__":
    "----------Constants------------"
    INF = (1 << 62) - 1
    # MOD = 10 ** 9 + 7
    MOD = 998244353
    # sys.setrecursionlimit(10**6)
    true_ceil = lambda x, y: (x + y - 1) // y
    "----------Input------------"
    readline = sys.stdin.readline
    "----------Run------------"
    d = {}
    d[1] = [0,0]
    d[2] = [1,0]
    d[3] = [0,1]
    main()
