"""
" author : kaneshige
" created : 26.02.2022 20:57:53
"""

import sys
import itertools
from collections import deque


def main():
    n,m = map(int,readline().split())
    a = list(map(int,readline().split()))
    b = list(map(int,readline().split()))
    
    d = {}
    for i in a:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
            
    ans = True
    for i in b:
        if i not in d:
            ans = False
        elif d[i] == 0:
            ans = False
        else:
            d[i] -= 1
            
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
