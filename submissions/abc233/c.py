"""
" author : kaneshige
" created : 25.12.2021 20:44:58
"""

import sys
import itertools
from collections import deque

ans = 0
def main():
    global ans
    n,x = map(int,readline().split())
    L = [list(map(int,readline().split())) for _ in range(n)]


    def saiki(r, h):
        global ans
        if r == n:
            if h == x:
                ans += 1
            return
        for i in range(1,L[r][0]+1):
            saiki(r+1,h*L[r][i])

    saiki(0,1)

    print(ans)





if __name__ == "__main__":
    "----------Constants------------"
    INF = (1 << 62) - 1
    MOD = 10 ** 9 + 7
    # MOD = 998244353
    sys.setrecursionlimit(10**6)
    "----------Input------------"
    readline = sys.stdin.readline
    "----------Run------------"
    main()
