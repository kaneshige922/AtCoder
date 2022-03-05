"""
" author : kaneshige
" created : 03.03.2022 19:14:35
"""

import sys
import itertools
from collections import deque


def main():
    n,m,k = map(int,readline().split())

    ans = 0
    if n == 1 and m == 1:
        print(k)
        exit()
    elif n == 1:
        for i in range(1,k+1):
            ans += pow(k-i+1,m,MOD)-pow(k-i,m,MOD)
            ans %= MOD
        print(ans)
        exit()
    elif m == 1:
        for i in range(1,k+1):
            ans += pow(k-i+1,n,MOD)-pow(k-i,n,MOD)
            ans %= MOD
        print(ans)
        exit()

    for i in range(1,k+1):
        p1 = (pow(i,n,MOD)-pow(i-1,n,MOD))%MOD
        p2 = pow(k-i+1,m,MOD)
        ans += p1*p2
        ans %= MOD
        #print(p1,p2,ans)

    print(ans)


if __name__ == "__main__":
    "----------Constants------------"
    INF = (1 << 62) - 1
    #MOD = 10 ** 9 + 7
    MOD = 998244353
    # sys.setrecursionlimit(10**6)
    true_ceil = lambda x, y: (x + y - 1) // y
    "----------Input------------"
    readline = sys.stdin.readline
    "----------Run------------"
    main()
