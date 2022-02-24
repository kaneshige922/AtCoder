"""
" author : kaneshige
" created : 06.02.2022 02:43:42
"""

import sys
import itertools
from collections import deque
from math import gcd

def main():
    n = int(readline())
    a = list(map(int,readline().split()))
    g = 1
    ans = 0
    for i in a:
        g1 = g//gcd(g,i)*i
        ans *= g1//g
        ans %= MOD
        ans += g1//i
        ans %= MOD
        g = g1
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
