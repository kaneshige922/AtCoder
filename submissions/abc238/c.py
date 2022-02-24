"""
" author : kaneshige
" created : 05.02.2022 20:58:55
"""

import sys
import itertools
from collections import deque


def main():
    n = int(readline())
    ans = 0
    for i in range(1,19):
        if pow(10,i) <= n:
            ans += 9*pow(10,i-1)*(9*pow(10,i-1)+1)//2
            ans %= MOD
        else:
            k = n - pow(10,i-1) + 1
            ans += k * (k+1)//2
            ans %= MOD
            break
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
