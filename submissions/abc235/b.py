"""
" author : kaneshige
" created : 15.01.2022 20:57:48
"""

import sys
import itertools
from collections import deque


def main():
    n = int(readline())
    h = list(map(int,readline().split()))
    
    now = h[0]
    
    for i in range(1,n):
        if h[i] > now:
            now = h[i]
        else:
            break
            
    print(now)
        
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
